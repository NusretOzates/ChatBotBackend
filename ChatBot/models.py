from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intent = models.TextField(max_length=500, blank=True)
    response = models.TextField(max_length=500, blank=True)
    message = models.TextField(max_length=500, blank=True)

    vergessenesElement = models.TextField(max_length=500, blank=True)
    zustand = models.TextField(max_length=500, blank=True)
    objekt = models.TextField(max_length=500, blank=True)
