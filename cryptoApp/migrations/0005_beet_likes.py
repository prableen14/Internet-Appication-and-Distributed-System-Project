# Generated by Django 4.2.7 on 2023-11-27 22:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoApp', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='beet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='beet_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
