from celery import shared_task
from django.core.mail import BadHeaderError, send_mail

    
    
@shared_task()
#@shared_task(bind=True)
def sendEmail():
    subject='TEST'
    message="Great it's working"
    from_email="komal.gore.demo@adcuratio.com"
    try:
        send_mail(subject, message, from_email, ['gorekomal576@gmail.com'])
    except BadHeaderError:
        print("Invalid header found.")

    
    