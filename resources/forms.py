from django import forms
from .models import Resource, Category


class ResourceForm(forms.ModelForm):
    """
    Form for the resource model.

    Fields:
    - name: The name of the resource.
    - description: A brief description of the resource.
    - url: The URL of the resource.
    - category: The category to which the resource belongs.
    - keywords: Tags associated with the resource.
    """
    class Meta:
        model = Resource
        fields = ['name', 'description', 'url', 'category', 'keywords']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.fields:
            self.fields['category'].queryset = Category.objects.filter(published=True)


class CategoryForm(forms.ModelForm):
    """
    Form for the category model.

    Fields:
    - name: The name of the category.
    """
    class Meta:
        model = Category
        fields = ['name']
