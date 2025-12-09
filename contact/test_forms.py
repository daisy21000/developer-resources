from django.test import TestCase
from .forms import ContactForm

# Create your tests here.


class ContactFormTest(TestCase):
    def test_contact_form_valid_data(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_missing_data(self):
        form_data = {
            'name': '',
            'email': '',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)

    def test_contact_form_invalid_email(self):
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_contact_form_long_message(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'A' * 5000
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_special_characters(self):
        form_data = {
            'name': 'John Doe!@#$',
            'email': 'john.doe@example.com',
            'message': (
                'Hello, this is a test message with special characters '
                '!@#$%^&*()'
            )
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_whitespace(self):
        form_data = {
            'name': '   ',
            'email': '   ',
            'message': '   '
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)

    def test_contact_form_partial_data(self):
        form_data = {
            'name': 'John Doe',
            'email': '',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_contact_form_html_injection(self):
        form_data = {
            'name': '<script>alert("hack")</script>',
            'email': 'john.doe@example.com',
            'message': '<b>This is bold text</b>'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_unicode_characters(self):
        form_data = {
            'name': 'Jöhn Döe',
            'email': 'john.doe@example.com',
            'message': 'Hello, this is a test message with ünicode characters.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_empty_message(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)

    def test_contact_form_numeric_name(self):
        form_data = {
            'name': '123456',
            'email': 'john.doe@example.com',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_email_case_insensitivity(self):
        form_data = {
            'name': 'John Doe',
            'email': 'JOHN.DOE@EXAMPLE.COM',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
