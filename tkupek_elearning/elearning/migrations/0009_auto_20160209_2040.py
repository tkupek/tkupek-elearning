# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0008_auto_20160209_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='questionId',
            new_name='question',
        ),
        migrations.AddField(
            model_name='user',
            name='userAnswer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elearning.UserAnswer'),
        ),
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
    ]