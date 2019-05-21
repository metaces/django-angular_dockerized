from django.db import models

# Create your models here.
from datetime import date

class Task(models.Model):

    """STORES A TASK"""

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)

    created_on = models.DateField(default=date.today)

    due_date = models.DateField(default=date.today)

    class Meta:
        
        db_table = 'task'

        ordering = ['id']

    def __str__(self):
        return self.title