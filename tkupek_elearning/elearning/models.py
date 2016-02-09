from __future__ import unicode_literals

import uuid

from django.db import models
from django.db.models.signals import post_init, pre_init


class Setting(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    footer = models.TextField(null=True)
    button_solution = models.CharField(max_length=100, null=True)
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


class User(models.Model):
    token = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    answers = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user) + " - " + str(self.questionId)

    class Meta:
        unique_together = (('user', 'questionId'),)