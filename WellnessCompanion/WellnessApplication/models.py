from django.db import models
import datetime
from django.utils import timezone
import uuid

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name

class Activity(models.Model):
    date = models.DateTimeField("publish date")
    CATEGORIES = [
        ('SWB', 'Social Wellbeing'),
        ('M', 'Mindfulness'),
        ('SM', 'Stress Managment'),
        ('PH', 'Physical Health'),
        ('N', 'Nutrition'),
    ]
    activity_catergory = models.CharField(max_length=40,choices=CATEGORIES)
    activity_type = models.CharField(max_length=200)
    personID = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.activity_type