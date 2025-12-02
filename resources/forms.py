from django import forms
from .models import Resource, Category


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'url', 'category', 'keywords']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.fields:
            self.fields['category'].queryset = Category.objects.filter(published=True)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
