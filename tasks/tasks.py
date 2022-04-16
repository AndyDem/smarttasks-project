from celery import shared_task
from datetime import date, timedelta
from .models import Task
from django.core.mail import send_mail


@shared_task
def send_deadline_notification():
    tasks = Task.objects.filter(deadline__lt=date.today() + timedelta(days=3))
    for task in tasks:
        days_left = (task.deadline - date.today()).days
        if days_left >= 0:
            send_mail(
                from_email='',
                subject='Deadline for task is coming',
                message=f'''You have set deadline for task {task.text} as of {task.deadline}.
                Only {days_left} {'day' if days_left==1 else 'days'} left!''',
                recipient_list=[task.user.email]
            )
    return 0
