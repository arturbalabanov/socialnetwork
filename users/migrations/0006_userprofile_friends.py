# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 16:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160304_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='_userprofile_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
