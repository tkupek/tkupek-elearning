from __future__ import unicode_literals

import hashlib
import os

from django.db import models
from tinymce.models import HTMLField


def gen_token():
    return hashlib.sha1(os.urandom(128)).hexdigest()


class Setting(models.Model):
    title = models.CharField(max_length=100, null=True)
    footer = models.TextField(null=True, blank=True)
    message_welcome_user = models.TextField(null=True, blank=True)
    message_access_denied = models.TextField(null=True, blank=True)
    message_already_answered = models.TextField(null=True, blank=True)
    text_answer = models.CharField(max_length=100, null=True, blank=True)
    text_solution = models.CharField(max_length=100, null=True, blank=True)
    text_next = models.CharField(max_length=100, null=True, blank=True)
    popup_completed_title = models.CharField(max_length=100, null=True, blank=True)
    popup_completed_message = models.TextField(null=True, blank=True)
    popup_leave_message = models.TextField(null=True, blank=True)
    logo = models.CharField(max_length=256, null=False, blank=True)
    active = models.BooleanField(default=False)
    statistic_token = models.CharField(max_length=40, null=True, default=gen_token, unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = Setting.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except Setting.DoesNotExist:
                pass
        super(Setting, self).save(*args, **kwargs)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    text = HTMLField(null=True)
    explanation = HTMLField(null=True)

    def __unicode__(self):
        return self.title


class Option(models.Model):
    text = models.CharField(max_length=256, null=True)
    correct = models.BooleanField(null=False, default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return self.text


class User(models.Model):

    token = models.CharField(max_length=40, null=True, default=gen_token, unique=True)
    name = models.CharField(max_length=100, null=False)
    last_seen = models.DateTimeField(null=True, blank=True)
    completed_message_shown = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    correct = models.NullBooleanField(null=True)

    def __unicode__(self):
        return str(self.user) + " - " + str(self.question.id)

    class Meta:
        unique_together = (('user', 'question'),)


class UserAnswerOptions(models.Model):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE, null=False)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = (('user_answer', 'option'),)

    def __unicode__(self):
        return str(self.user_answer) + " - " + str(self.option)
