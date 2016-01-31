from __future__ import unicode_literals

from django.db import models

class question(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    options = models.TextField()
    answer = models.IntegerField()
    explanation = models.TextField()