from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('published','Published'),)
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,related_name='blog_post')
    slug=models.SlugField(unique_for_date='publish')
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title


