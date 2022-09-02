from django.urls import path, include
from . import views


urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.CreateTaskView.as_view(), name='task_create'),
    path('tasks/delete/<int:pk>/', views.DeleteTaskView.as_view(), name='task_delete'),
    path('tasks/done/<int:pk>/', views.DoneTaskView.as_view(), name='task_done'),
    path('tasks/update/<int:pk>/', views.UpdateTaskView.as_view(), name='task_update'),
    path('api/', include('task.api.urls')),
]