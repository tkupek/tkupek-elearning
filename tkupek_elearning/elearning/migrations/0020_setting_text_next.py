# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0019_auto_20160221_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='text_next',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
