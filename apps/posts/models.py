from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    post = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)