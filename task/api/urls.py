from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.TodoListView.as_view(), name='task_list'),
    path('task-details/<int:pk>/', views.TodoDetailsView.as_view(), name='task_details'),
]