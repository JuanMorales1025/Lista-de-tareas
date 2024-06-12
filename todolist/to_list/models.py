from django.db import models # type: ignore
from django.utils import timezone # type: ignore

# Create your models here.

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

