from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='tasks_created', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks_assigned', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

