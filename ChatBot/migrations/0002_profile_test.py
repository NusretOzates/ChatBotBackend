# Generated by Django 3.0.5 on 2020-05-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ChatBot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
