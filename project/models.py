from django.db import models

# Create your models here.

class Task(models.Model):

    task_name = models.CharField(max_length=50)

    task_description = models.CharField(max_length=100)

    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name,self.task_description

