# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 11:58
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0022_auto_20160305_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]