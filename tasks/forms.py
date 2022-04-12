from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'text': 'Enter your task here'
        }

