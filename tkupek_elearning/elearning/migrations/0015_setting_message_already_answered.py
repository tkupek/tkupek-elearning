# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0014_auto_20160214_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='message_already_answered',
            field=models.TextField(null=True),
        ),
    ]