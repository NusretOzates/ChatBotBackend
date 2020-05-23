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
    application = models.TextField(max_length=500, blank=True)


class Ticket(models.Model):
    creator = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    user_id = models.TextField(max_length=500, blank=True)
    intent = models.TextField(max_length=500, blank=True)
    application = models.TextField(max_length=500, blank=True)
    requestedPermissions = models.TextField(max_length=500, blank=True)
    reasoning = models.TextField(max_length=500, blank=True)
    creationDate = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.user_id is None:
            self.user_id = self.creator.username
        super(Ticket, self).save(*args, **kwargs)
