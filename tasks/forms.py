from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(required=False, widget=forms.SelectDateWidget())
    class Meta:
        model = Task
        fields = ('text', 'priority', 'deadline')
        widgets = {
            'text': forms.Textarea(attrs={'autofocus': True, 'class': 'form-control'}),
            'priority': forms.Select(choices=Task.PRIORITY)
        }
        labels = {
            'text': 'Enter your task here',
            'priority':'Priority',
            'deadline':'Deadline'
        }
