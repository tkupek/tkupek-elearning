from __future__ import unicode_literals

import hashlib
import os

from django.db import models


def gen_token():
    return hashlib.sha1(os.urandom(128)).hexdigest()


class Setting(models.Model):
    title = models.CharField(max_length=100, null=True)
    footer = models.TextField(null=True)
    message_welcome_user = models.TextField(null=True)
    message_access_denied = models.TextField(null=True)
    message_already_answered = models.TextField(null=True)
    text_answer = models.CharField(max_length=100, null=True)
    text_solution = models.CharField(max_length=100, null=True)
    text_next = models.CharField(max_length=100, null=True)
    logo = models.CharField(max_length=256, null=False)
    active = models.BooleanField(unique=True, default=False)
    token = models.CharField(max_length=40, null=True, default=gen_token)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    explanation = models.TextField(null=True)

    def __unicode__(self):
        return self.title


class Option(models.Model):
    text = models.CharField(max_length=256, null=True)
    correct = models.BooleanField(null=False, default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return self.text


class User(models.Model):

    token = models.CharField(max_length=40, null=True, default=gen_token)
    name = models.CharField(max_length=100, null=False)
    last_seen = models.DateTimeField(null=True)

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
