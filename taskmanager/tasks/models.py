from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    status_choices = [('Todo', 'Todo'),('In Progress', 'In Progress'),('Done', 'Done')]
    priority_choices = [('Low','Low'),('Medium','Medium'),('High','High')]
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=status_choices,default='Todo')
    priority = models.CharField(max_length=20,choices=priority_choices,default='Medium')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

