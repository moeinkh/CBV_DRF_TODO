from django.shortcuts import render, redirect
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CreateTaskForm, UpdateTaskForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name  = 'tasks'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)    

class DoneTaskView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs.get("pk"))
        task.done = True
        task.save()
        return redirect(self.success_url)

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'task/update_task.html'
    success_url = reverse_lazy('task_list')  
