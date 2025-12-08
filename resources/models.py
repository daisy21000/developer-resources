from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Resource(models.Model):
    """
    Model for a developer resource related to :model:`Category` by :model:`auth.User`.

    Fields:
    - name: The name of the resource.
    - description: A brief description of the resource.
    - url: The URL of the resource.
    - category: The category to which the resource belongs.
    - created_at: The timestamp when the resource was created.
    - updated_at: The timestamp when the resource was last updated.
    - keywords: Tags associated with the resource.
    - uploader: The user who uploaded the resource.
    - approved: A boolean indicating whether the resource has been approved.
    - favorites: Many-to-many relationship with users who have favorited the resource.
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='resources')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keywords = TaggableManager()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    approved = models.BooleanField(default=False)
    favorites = models.ManyToManyField(User, related_name='favorite_resources', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Model for a resource category related to :model:`auth.User`.

    Fields:
    - name: The name of the category.
    - author: The user who created the category.
    - published: A boolean indicating whether the category is published.
    """
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
