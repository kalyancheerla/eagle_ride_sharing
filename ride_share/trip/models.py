from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=200)
    car_details = models.CharField(max_length=200)




class Trip(models.Model):
    # one user can have many Trips
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    # we do not delete users, we only soft delete, if we delete then we delete all user data so we cascade
    start_time = models.DateTimeField("Ride start Time")
    end_time = models.DateTimeField("Estimated reach time")
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    seats = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

