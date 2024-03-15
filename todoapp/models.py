from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.Textfield(null=True,blank=True)
    completed = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ["completed"]