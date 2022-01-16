"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Post(models.Model):
    header = models.CharField(max_length=256)
    post = models.TextField()
    date = models.DateTimeField()