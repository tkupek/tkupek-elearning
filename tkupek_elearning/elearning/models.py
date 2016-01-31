from __future__ import unicode_literals

from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    footer = models.TextField(null=True)
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