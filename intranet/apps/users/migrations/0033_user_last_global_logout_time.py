# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-11 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_userdarkmodeproperties'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_global_logout_time',
            field=models.DateTimeField(null=True),
        ),
    ]
