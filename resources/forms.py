from django import forms
from .models import Resource, Category


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'url', 'category', 'keywords']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
