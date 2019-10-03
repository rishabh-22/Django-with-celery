from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
              'This is proof the task worked!',
              'rbtherib2@gmail.com',
              ['rishabh.bhardwaj@tothenew.com', 'rishabh.bh22@gmail.com'])

    return "Task executed successfully!"
