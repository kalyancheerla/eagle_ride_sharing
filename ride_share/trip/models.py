from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    driver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField("Ride start Time")
    end_time = models.DateTimeField("Estimated reach time")
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)


