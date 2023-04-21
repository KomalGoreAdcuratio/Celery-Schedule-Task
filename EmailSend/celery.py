import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailSend.settings')

app = Celery('EmailSend')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#Celery Beat Settings
app.conf.beat_schedule = {
    'new': {
        'task': 'mail.task.sendEmail',
        'schedule': crontab(hour=1,minute=20),
        #'args': (2,)
    }
    
}


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

