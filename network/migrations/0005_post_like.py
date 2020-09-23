# Generated by Django 3.0.7 on 2020-09-17 18:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='liked_user', to=settings.AUTH_USER_MODEL),
        ),
    ]