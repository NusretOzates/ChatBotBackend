from django.db import models


# Create your models here.

class User(models.Model):
    id = models.CharField()
    name_surname = models.TextField()
    password = models.TextField()
