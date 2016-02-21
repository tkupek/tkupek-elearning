from __future__ import unicode_literals

import hashlib
import os

from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=100, null=True)
    footer = models.TextField(null=True)
    message_welcome_user = models.TextField(null=True)
    message_access_denied = models.TextField(null=True)
    message_already_answered = models.TextField(null=True)
    button_solution = models.CharField(max_length=100, null=True)
    logo = models.CharField(max_length=256, null=False)
    active = models.BooleanField(unique=True, default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    explanation = models.TextField(null=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    text = models.CharField(max_length=100, null=True)
    correct = models.BooleanField(null=False, default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text


def gen_token():
    return hashlib.sha1(os.urandom(128)).hexdigest()


class User(models.Model):

    token = models.CharField(max_length=40, null=True, default=gen_token)
    name = models.CharField(max_length=100, null=False)
    last_seen = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    correct = models.NullBooleanField(null=True)

    def __str__(self):
        return str(self.user) + " - " + str(self.question)

    class Meta:
        unique_together = (('user', 'question'),)


class UserAnswerOptions(models.Model):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE, null=False)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = (('user_answer', 'option'),)
