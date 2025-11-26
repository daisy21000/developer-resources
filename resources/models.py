from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keywords = TaggableManager()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
