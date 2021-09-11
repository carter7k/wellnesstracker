from django.db import models
import datetime
from django.utils import timezone
import uuid

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Activity(models.Model):
    date = models.DateTimeField("publish date")
    activity_type = "placeholder activity"
    personID = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.activity_type