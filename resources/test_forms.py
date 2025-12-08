from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category
from .forms import ResourceForm, CategoryForm

# Create your tests here.


class ResourceFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )

        # create a Category instance directly to avoid form validation issues
        self.category_instance = Category(
            name='Web Development',
            author=self.user,
            published=True,
        )
        self.category_instance.save()

    def test_resource_form_valid_data(self):
        """Valid input produces a clean, valid form."""
        form_data = {
            'name': 'Django Tutorial',
            'url': 'https://www.djangoproject.com/start/',
            'description': 'A comprehensive guide to Django.',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_missing_data(self):
        """Missing required fields make the form invalid and report errors."""
        form_data = {
            'name': '',
            'url': '',
            'description': '',
            'category': '',
            'keywords': '',
        }
        form = ResourceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('url', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('category', form.errors)

    def test_resource_form_invalid_url(self):
        """An invalid URL should cause the form to be invalid."""
        form_data = {
            'name': 'Invalid URL Resource',
            'url': 'not-a-valid-url',
            'description': 'This resource has an invalid URL.',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('url', form.errors)

    def test_resource_form_long_title(self):
        """Very long titles should still validate if within limits."""
        form_data = {
            'name': 'T' * 200,
            'url': 'https://www.example.com/resource',
            'description': 'Resource with a very long title.',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_special_characters(self):
        """Special characters in fields should not break validation."""
        form_data = {
            'name': 'Resource!@#$',
            'url': 'https://www.example.com/resource',
            'description': 'Resource with special characters !@#$%^&*()',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_whitespace(self):
        """Whitespace-only input for required fields is invalid."""
        form_data = {
            'name': '   ',
            'url': '   ',
            'description': '   ',
            'category': '',
            'keywords': '   ',
        }
        form = ResourceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('url', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('category', form.errors)

    def test_resource_form_no_keywords(self):
        """At least one keyword should be required."""
        form_data = {
            'name': 'No Keywords Resource',
            'url': 'https://www.example.com/resource',
            'description': 'This resource has no keywords.',
            'category': self.category_instance,
            'keywords': '',
        }
        form = ResourceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('keywords', form.errors)

    def test_resource_form_many_keywords(self):
        """A high number of comma-separated keywords should be allowed."""
        form_data = {
            'name': 'Many Keywords Resource',
            'url': 'https://www.example.com/resource',
            'description': 'This resource has many keywords.',
            'category': self.category_instance,
            'keywords': (
                'django,web,framework,python,development,tutorial,guide,'
                'programming,code,software'
            ),
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_extreme_url(self):
        """Single-label domains exceeding DNS limits should be rejected."""
        form_data = {
            'name': 'Extreme URL Resource',
            # A single DNS label longer than 63 characters is invalid per
            # domain name rules; Django's URL validator will reject it.
            'url': 'https://www.' + 'a' * 150 + '.com',
            'description': 'This resource has an extremely long URL.',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        # This should be invalid because the domain label exceeds 63 chars
        self.assertFalse(form.is_valid())
        self.assertIn('url', form.errors)

    def test_resource_form_long_but_valid_url(self):
        """Construct a long URL using multiple labels (<=63 chars each).

        This keeps each DNS label within limits while producing a long
        overall URL string that should pass Django's URL validator.
        """
        # Build three labels of length 63, 63 and 24 -> total 150 chars
        labels = ['a' * 63, 'b' * 63, 'c' * 24]
        domain = '.'.join(labels)
        long_valid_url = f'https://{domain}.com'
        form_data = {
            'name': 'Long Valid URL Resource',
            'url': long_valid_url,
            'description': 'This resource has a long but valid URL.',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_xss_attempt(self):
        """Script-like input should validate; templates escape on render.

        Forms accept the text input; eventual HTML escaping happens when
        templates render the data.
        """
        form_data = {
            'name': '<script>alert("XSS")</script>',
            'url': 'https://www.example.com/resource',
            'description': '<img src=x onerror=alert("XSS") />',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_sql_injection_attempt(self):
        """Malicious-looking strings should be accepted as data.

        The form should validate the text; database layers prevent execution.
        """
        form_data = {
            'name': "Resource'); DROP TABLE resources;--",
            'url': 'https://www.example.com/resource',
            'description': (
                "This resource attempts SQL injection: '; DROP TABLE users;--"
            ),
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_boundary_description_length(self):
        """Very large descriptions should be accepted if allowed by model.

        This ensures the form does not impose a smaller limit than the model.
        """
        form_data = {
            'name': 'Boundary Description Resource',
            'url': 'https://www.example.com/resource',
            'description': 'D' * 10000,
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_unicode_characters(self):
        """Unicode characters should be accepted in all text fields."""
        form_data = {
            'name': 'Rësöürcé Nämé',
            'url': 'https://www.example.com/resource',
            'description': 'Thïs rësöürcé häš üñïcødë chäräctërs.',
            'category': self.category_instance,
            'keywords': 'djàñgö,wéþ,främëwörk',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_resource_form_partial_data(self):
        """Omitting required fields (e.g. URL) should make the form invalid."""
        form_data = {
            'name': 'Partial Data Resource',
            'url': '',
            'description': 'This resource is missing the URL.',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('url', form.errors)

    def test_resource_form_html_injection(self):
        """HTML-like input should validate; templates escape at render time."""
        form_data = {
            'name': '<b>Bold Resource Name</b>',
            'url': 'https://www.example.com/resource',
            'description': '<i>This description is italicized.</i>',
            'category': self.category_instance,
            'keywords': 'django,web,framework',
        }
        form = ResourceForm(data=form_data)
        self.assertTrue(form.is_valid())


class CategoryFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )

    def test_category_form_valid_data(self):
        """Valid input produces a clean, valid form."""
        form_data = {
            'name': 'Data Science',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_missing_name(self):
        """Missing name field makes the form invalid and reports error."""
        form_data = {
            'name': '',
        }
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_category_form_long_name(self):
        """Very long names should still validate if within limits."""
        form_data = {
            'name': 'N' * 100,
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_special_characters(self):
        """Special characters in name should not break validation."""
        form_data = {
            'name': 'Category!@#$',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_whitespace(self):
        """Whitespace-only input for name is invalid."""
        form_data = {
            'name': '   ',
        }
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_category_form_xss_attempt(self):
        """Script-like input should validate; templates escape on render."""
        form_data = {
            'name': '<script>alert("XSS")</script>',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_sql_injection_attempt(self):
        """Malicious-looking strings should be accepted as data.

        The form should validate the text; database layers prevent execution.
        """
        form_data = {
            'name': "Category'); DROP TABLE categories;--",
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_unicode_characters(self):
        """Unicode characters should be accepted in the name field."""
        form_data = {
            'name': 'Cätégöry Nämé',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_html_injection(self):
        """HTML-like input should validate; templates escape at render time."""
        form_data = {
            'name': '<b>Bold Category Name</b>',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())
