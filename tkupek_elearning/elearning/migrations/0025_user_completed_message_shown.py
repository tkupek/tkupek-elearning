# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0024_auto_20160305_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='completed_message_shown',
            field=models.BooleanField(default=False),
        ),
    ]
