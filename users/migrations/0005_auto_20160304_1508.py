# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160211_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
