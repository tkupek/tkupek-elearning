# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0011_setting_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='message',
            new_name='message_access_denied',
        ),
        migrations.AddField(
            model_name='setting',
            name='message_welcome_user',
            field=models.TextField(null=True),
        ),
    ]
