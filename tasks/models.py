from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY = [
        (0, None),
        (1, 'Very low'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'High'),
        (5, 'Very high')
    ]
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    priority = models.SmallIntegerField(default=0, choices=PRIORITY)
    deadline = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
