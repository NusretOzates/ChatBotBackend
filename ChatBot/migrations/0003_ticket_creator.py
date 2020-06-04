# Generated by Django 3.0.6 on 2020-05-22 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChatBot', '0002_auto_20200523_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='creator',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
