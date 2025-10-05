from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField()
    
    def __str__(self):
        return self.title