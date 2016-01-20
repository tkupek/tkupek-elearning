from __future__ import unicode_literals

from django.db import models

# Create your models here.

class questions(models.Model):

    questionId = models.IntegerField()
    questionTitle = models.CharField(max_length=100)
    questionText = models.TextField()
    questionAnswer = models.TextField()


