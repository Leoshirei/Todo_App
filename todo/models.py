from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title