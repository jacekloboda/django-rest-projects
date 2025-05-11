from django.db import models
from datetime import date

# Create your models here.


class Todo(models.Model):

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
