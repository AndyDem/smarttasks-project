from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'
    login_url = '/login'

    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)
        return tasks


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/smart/tasks'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = '/smart/tasks'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/smart/tasks'
    template_name = 'tasks/tasks_delete.html'