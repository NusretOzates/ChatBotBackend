# Generated by Django 3.0.5 on 2020-05-21 19:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intent', models.TextField(blank=True, max_length=500)),
                ('response', models.TextField(blank=True, max_length=500)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('vergessenesElement', models.TextField(blank=True, max_length=500)),
                ('zustand', models.TextField(blank=True, max_length=500)),
                ('objekt', models.TextField(blank=True, max_length=500)),
                ('application', models.TextField(blank=True, max_length=500)),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]