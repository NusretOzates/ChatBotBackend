# Register your models here.
from django.contrib import admin

from .models import Profile, Ticket

admin.site.register(Profile)
admin.site.register(Ticket)
