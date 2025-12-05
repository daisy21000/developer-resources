from django import forms
from .models import Request


class ContactForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'email', 'message']
