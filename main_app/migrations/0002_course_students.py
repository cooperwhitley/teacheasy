# Generated by Django 4.2.5 on 2023-09-22 03:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_enrolled', to=settings.AUTH_USER_MODEL),
        ),
    ]