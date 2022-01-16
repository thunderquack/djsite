"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Post(models.Model):
    header = models.CharField(max_length=256)
    post = models.TextField()
    date = models.DateTimeField()
    tags = models.ManyToManyField('Tag', blank=True)

class Tag(models.Model):
    text = models.CharField(max_length=128)
    posts = models.ManyToManyField('Post', blank=True, through=Post.tags.through)