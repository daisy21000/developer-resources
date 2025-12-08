from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact(request):
    """
    Handle contact form submissions.

    This view processes the contact form. If the request method is POST,
    it validates the form data and saves it if valid.
    It also provides user feedback through messages.

    :param request: The HTTP request object.

    **Context:**

    ``form``: An instance of `ContactForm`, either empty or populated with POST data.

    **Template:**

    :template:`contact/contact.html`
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
            form = ContactForm()  # Clear the form after successful submission
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
