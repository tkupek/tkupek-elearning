# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0026_auto_20160305_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='popup_leave_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='footer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='setting',
            name='message_access_denied',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='message_already_answered',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='message_welcome_user',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='popup_completed_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='popup_completed_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='text_answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='text_next',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='text_solution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]