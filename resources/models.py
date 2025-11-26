from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='resources')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keywords = TaggableManager()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
