# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0009_auto_20160209_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userAnswer',
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='elearning.User'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together={('user', 'question')},
        ),
    ]