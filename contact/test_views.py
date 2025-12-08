from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from .forms import ContactForm
from .models import Request


class ContactViewTests(TestCase):

    def test_get_contact_renders_form(self):
        """GET request returns the contact form template."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        # Form should be present and not bound
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertIsInstance(form, ContactForm)
        self.assertFalse(form.is_bound)

    def test_post_valid_saves_and_shows_success(self):
        """A valid POST should save a Request and show a success msg."""
        data = {
            'name': 'Alice',
            'email': 'alice@example.com',
            'message': 'Hello there',
        }
        before = Request.objects.count()
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(Request.objects.count(), before + 1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        msgs = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any('Thank you for contacting us' in m.message for m in msgs)
        )
        # After success the form in context should be unbound (reset)
        form = response.context.get('form')
        self.assertIsInstance(form, ContactForm)
        self.assertFalse(form.is_bound)

    def test_post_invalid_shows_error_and_not_saved(self):
        """An invalid POST should not save and should show an error."""
        data = {'name': '', 'email': 'bad', 'message': ''}
        before = Request.objects.count()
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(Request.objects.count(), before)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        msgs = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any(
                'There was an error with your submission' in m.message
                for m in msgs
            )
        )

    def test_saved_fields_match_submission(self):
        """After a valid submission the model fields match the data."""
        data = {
            'name': 'Bob Builder',
            'email': 'bob@build.com',
            'message': 'Can you help with a build?',
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        req = Request.objects.first()
        self.assertIsNotNone(req)
        self.assertEqual(req.name, data['name'])
        self.assertEqual(req.email, data['email'])
        self.assertEqual(req.message, data['message'])

    def test_whitespace_only_fields_are_invalid(self):
        """Fields with only whitespace should be considered invalid."""
        data = {'name': '   ', 'email': '   ', 'message': '   '}
        before = Request.objects.count()
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(Request.objects.count(), before)
        self.assertEqual(response.status_code, 200)
        # The form in context should be bound and invalid
        form = response.context.get('form')
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_long_name_and_message_save_successfully(self):
        """Long name (200 chars) and large message should be accepted."""
        long_name = 'N' * 200
        long_msg = 'M' * 5000
        data = {
            'name': long_name,
            'email': 'long@msg.com',
            'message': long_msg,
        }
        before = Request.objects.count()
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(Request.objects.count(), before + 1)
        self.assertEqual(response.status_code, 200)
        req = Request.objects.first()
        self.assertEqual(req.name, long_name)
        self.assertEqual(req.message, long_msg)

    def test_multiple_identical_submissions_allowed(self):
        """Submitting the same data more than once creates separate objects."""
        data = {'name': 'Repeat', 'email': 'r@e.com', 'message': 'Repeat msg'}
        self.client.post(reverse('contact'), data)
        self.client.post(reverse('contact'), data)
        self.assertEqual(Request.objects.filter(name='Repeat').count(), 2)

    def test_various_invalid_email_formats(self):
        """Common invalid email formats should be rejected by the form."""
        invalid_emails = ['plainaddress', 'missing@domain', '@no-local.com']
        for email in invalid_emails:
            data = {'name': 'Test', 'email': email, 'message': 'Hi'}
            before = Request.objects.count()
            response = self.client.post(reverse('contact'), data)
            self.assertEqual(Request.objects.count(), before)
            # Ensure error message is present or form is invalid
            form = response.context.get('form')
            self.assertTrue(form is not None and not form.is_valid())
