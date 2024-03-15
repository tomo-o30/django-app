from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from todoapp.models import Task


class TaskList( LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model= Task
    context_object_name = "task"
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    
class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name="todoapp/login.html"
    
    def get_success_url(self):
        return reverse_lazy("tasks")