from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    
    # Important below is recommended at add in every model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # This task name to be displayed in admin panel
    def __str__(self):
        return self.task