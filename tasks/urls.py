from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.TaskListView.as_view(), name='tasks_list'),
    path('tasks/new',
         views.TaskCreateView.as_view(),
         name='tasks_create'),
    path('tasks/<int:pk>/edit',
         views.TaskUpdateView.as_view(),
         name='tasks_update'),
    path('tasks/<int:pk>/delete',
         views.TaskDeleteView.as_view(),
         name='tasks_delete'),
]
