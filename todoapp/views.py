from django.http import HttpResponse


# Create your views here.
def taskList(request):
    return HttpResponse("<h1>Hello django</h1>")