from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class SavedRestaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    place_course = models.CharField(max_length=255, default='Unknown')
    place_latitude = models.FloatField(default=0.0)
    place_longitude = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name}"

