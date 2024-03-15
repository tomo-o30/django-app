from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from todoapp.models import Task


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    
class TaskList(DetailView):
    model= Task
    