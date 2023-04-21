from django.http import HttpResponse
from mail.task import sendEmail

 

from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render

from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.
def send_mail_to_all(request):
    #sendEmail.delay()
    #sendEmail.delay()
    # tasks = [dummyAccountData,dummyLoanData]
    # chain(*tasks).apply_async()
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"6", task='mail.task.sendEmail')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")
   