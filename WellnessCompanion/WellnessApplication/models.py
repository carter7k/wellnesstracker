from django.db import models
import datetime
from django.utils import timezone
import uuid

# Create your models here.


class Activity(models.Model):
    date = models.DateTimeField("publish date")
    CATEGORIES = [
        
        ('Mindfulness and Stress Managment', 'Mindfulness and Stress Managment'),
        ('Physical Health', 'Physical Health'),
        ('Nutrition', 'Nutrition'),
    ]
    activity_catergory = models.CharField(max_length=40,choices=CATEGORIES, default="Mindfulness and Stress Managment")
    activity_type = models.CharField(max_length=200)
    time_spent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.activity_type