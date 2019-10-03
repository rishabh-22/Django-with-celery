from django.http import HttpResponse
from .tasks import send_email_task


def send_email(request):
    send_email_task.delay()
    return HttpResponse("<h1>Done!</h1><br><h2>The Email has been sent.</h2>")
