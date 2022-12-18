from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
import json

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Email Sent")

def schedule_mail(request):
    schedule, created = IntervalSchedule.objects.get_or_create(every = 15,period=IntervalSchedule.SECONDS,)
    task = PeriodicTask.objects.create(interval=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Email Sent With Intervals")
