from django import forms
from .models import Request


class ContactForm(forms.ModelForm):
    """
    Form for the contact request model.

    Fields:
    - name: The name of the person making the request.
    - email: The email address of the person making the request.
    - message: The message content of the request.
    """
    class Meta:
        # Specify the model and fields to include in the form
        model = Request
        fields = ['name', 'email', 'message']
