from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 5
    template_name = "tasks/tasks_list.html"
    login_url = '/login'

    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user) \
            .order_by('priority','deadline').reverse()
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