from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)  # False means incomplete, True means complete

    def __str__(self):
        return self.title
