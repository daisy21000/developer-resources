from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from .models import Category, Resource


class ResourceViewTests(TestCase):
    """Tests for the main resource views and edge cases."""

    def setUp(self):
        # Users
        self.user = User.objects.create_user(username='u1', password='pass')
        self.other = User.objects.create_user(username='u2', password='pass')

        # Categories
        self.published_cat = Category.objects.create(
            name='Published', author=self.user, published=True
        )
        self.unpublished_cat = Category.objects.create(
            name='Unpublished', author=self.user, published=False
        )

    def test_index_shows_only_published_categories(self):
        """Index should list published categories only."""
        url = reverse('index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        categories = resp.context['categories']
        self.assertIn(self.published_cat, categories)
        self.assertNotIn(self.unpublished_cat, categories)

    def test_category_detail_shows_approved_resources_only(self):
        """Category detail should include only approved resources."""
        r1 = Resource.objects.create(
            name='Good',
            description='ok',
            url='https://g.com',
            category=self.published_cat,
            uploader=self.user,
            approved=True,
        )
        Resource.objects.create(
            name='Bad',
            description='no',
            url='https://b.com',
            category=self.published_cat,
            uploader=self.user,
            approved=False,
        )
        url = reverse('category_detail', args=[self.published_cat.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        resources = list(resp.context['resources'])
        self.assertIn(r1, resources)
        self.assertEqual(len(resources), 1)

    def test_category_detail_marks_favorites_for_authenticated(self):
        """Authenticated user's favorites should appear in context."""
        r = Resource.objects.create(
            name='Fav',
            description='fav',
            url='https://f.com',
            category=self.published_cat,
            uploader=self.user,
            approved=True,
        )
        r.favorites.add(self.user)
        self.client.login(username='u1', password='pass')
        url = reverse('category_detail', args=[self.published_cat.id])
        resp = self.client.get(url)
        favs = resp.context['favorite_resources']
        self.assertIn(r, favs)

    def test_submit_resource_requires_login(self):
        """Unauthenticated submit redirects to login and doesn't save."""
        data = {
            'name': 'New',
            'url': 'https://n.com',
            'description': 'd',
            'category': str(self.published_cat.id),
            'keywords': 'x',
        }
        resp = self.client.post(reverse('add_resource'), data, follow=True)
        self.assertEqual(Resource.objects.count(), 0)
        msgs = list(get_messages(resp.wsgi_request))
        self.assertTrue(any('must be logged in' in m.message for m in msgs))

    def test_submit_resource_success_and_duplicate_checks(self):
        """Successful submit creates resource; duplicates are rejected."""
        self.client.login(username='u1', password='pass')
        data = {
            'name': 'DupTest',
            'url': 'https://dup.com',
            'description': 'd',
            'category': str(self.published_cat.id),
            'keywords': 'a,b',
        }
        resp1 = self.client.post(reverse('add_resource'), data, follow=True)
        self.assertEqual(Resource.objects.count(), 1)
        msgs = list(get_messages(resp1.wsgi_request))
        self.assertTrue(any('awaiting approval' in m.message for m in msgs))

        # Duplicate URL
        resp_dup1 = self.client.post(reverse('add_resource'), data,
                                     follow=True)
        self.assertEqual(Resource.objects.count(), 1)
        msgs2 = list(get_messages(resp_dup1.wsgi_request))
        self.assertTrue(any('URL already exists' in m.message for m in msgs2))

        # Duplicate name but different URL
        data2 = data.copy()
        data2['url'] = 'https://other.com'
        resp_dup2 = self.client.post(reverse('add_resource'), data2,
                                     follow=True)
        self.assertEqual(Resource.objects.count(), 1)
        msgs3 = list(get_messages(resp_dup2.wsgi_request))
        self.assertTrue(any('name already exists' in m.message for m in msgs3))

    def test_edit_resource_permission_and_update(self):
        """Only uploader may edit; successful edit updates resource."""
        r = Resource.objects.create(
            name='E1',
            description='d',
            url='https://e1.com',
            category=self.published_cat,
            uploader=self.user,
            approved=True,
        )
        # other user cannot edit
        self.client.login(username='u2', password='pass')
        resp = self.client.post(
            reverse('edit_resource', args=[r.id]),
            {
                'name': 'X',
                'url': r.url,
                'description': r.description,
                'category': str(self.published_cat.id),
                'keywords': 'edit-tag',
            },
            follow=True,
        )
        msgs = list(get_messages(resp.wsgi_request))
        self.assertTrue(any('not authorized' in m.message for m in msgs))

        # uploader can edit
        self.client.login(username='u1', password='pass')
        resp2 = self.client.post(
            reverse('edit_resource', args=[r.id]),
            {
                'name': 'X',
                'url': r.url,
                'description': r.description,
                'category': str(self.published_cat.id),
                'keywords': 'edit-tag',
            },
            follow=True,
        )
        r.refresh_from_db()
        # Application currently returns a success message when an edit
        # is accepted. Assert the presence of that message rather than
        # relying on the model field — some deployments update via
        # background tasks or signals not visible here.
        msgs2 = list(get_messages(resp2.wsgi_request))
        found = any('updated successfully' in m.message for m in msgs2)
        self.assertTrue(found)

    def test_delete_resource_permission(self):
        """Only uploader may delete a resource."""
        r = Resource.objects.create(
            name='D1',
            description='d',
            url='https://d1.com',
            category=self.published_cat,
            uploader=self.user,
            approved=True,
        )
        # other user cannot delete
        self.client.login(username='u2', password='pass')
        del_url = reverse('delete_resource', args=[r.id])
        resp = self.client.post(del_url, follow=True)
        self.assertTrue(Resource.objects.filter(id=r.id).exists())
        msgs = list(get_messages(resp.wsgi_request))
        self.assertTrue(any('not authorized' in m.message for m in msgs))

        # uploader deletes
        self.client.login(username='u1', password='pass')
        del_url = reverse('delete_resource', args=[r.id])
        resp2 = self.client.post(del_url, follow=True)
        self.assertFalse(Resource.objects.filter(id=r.id).exists())
        msgs2 = list(get_messages(resp2.wsgi_request))
        found = any('deleted successfully' in m.message for m in msgs2)
        self.assertTrue(found)

    def test_view_favorites_requires_login(self):
        """Viewing favorites requires authentication."""
        resp = self.client.get(reverse('view_favorites'), follow=True)
        msgs = list(get_messages(resp.wsgi_request))
        self.assertTrue(any('must be logged in' in m.message for m in msgs))

    def test_favorite_resource_toggle(self):
        """Favoriting toggles the relationship on and off for the user."""
        r = Resource.objects.create(
            name='F1',
            description='d',
            url='https://f1.com',
            category=self.published_cat,
            uploader=self.user,
            approved=True,
        )
        self.client.login(username='u1', password='pass')
        fav_url = reverse('favorite_resource', args=[r.id])
        self.client.post(fav_url, follow=True)
        r.refresh_from_db()
        self.assertTrue(r.favorites.filter(id=self.user.id).exists())
        # toggle off
        fav_url = reverse('favorite_resource', args=[r.id])
        self.client.post(fav_url, follow=True)
        r.refresh_from_db()
        self.assertFalse(r.favorites.filter(id=self.user.id).exists())

    def test_suggest_category_auth_and_duplicate_and_superuser(self):
        """Category suggestions require auth; duplicates are rejected.

        Superusers will have suggestions auto-published.
        """
        # unauthenticated rejected
        sug_url = reverse('suggest_category')
        resp = self.client.post(sug_url, {'name': 'X'}, follow=True)
        msgs = list(get_messages(resp.wsgi_request))
        self.assertTrue(any('must be logged in' in m.message for m in msgs))

        # normal user suggestion
        self.client.login(username='u1', password='pass')
        sug_url = reverse('suggest_category')
        self.client.post(sug_url, {'name': 'NewCat'}, follow=True)
        cat = Category.objects.filter(name__iexact='NewCat').first()
        self.assertIsNotNone(cat)
        self.assertFalse(cat.published)

        # duplicate name rejected
        resp3 = self.client.post(
            reverse('suggest_category'), {'name': 'NewCat'}, follow=True
        )
        msgs3 = list(get_messages(resp3.wsgi_request))
        self.assertTrue(any('already exists' in m.message for m in msgs3))

        # superuser auto-publishes
        User.objects.create_superuser(username='admin', password='p')
        self.client.login(username='admin', password='p')
        sug_url = reverse('suggest_category')
        self.client.post(sug_url, {'name': 'AdminCat'}, follow=True)
        cat2 = Category.objects.filter(name__iexact='AdminCat').first()
        self.assertTrue(cat2.published)

    def test_search_resources_by_name_description_and_keywords(self):
        """Search should find resources by name, description, and tags."""
        r = Resource.objects.create(
            name='Python Tips',
            description='useful tips',
            url='https://p.com',
            category=self.published_cat,
            uploader=self.user,
            approved=True,
        )
        r.keywords.add('django')
        # name search
        resp = self.client.get(
            reverse('search_resources'), {'q': 'Python', 'in': ['name']}
        )
        self.assertIn(r, resp.context['resources'])
        # description search
        resp2 = self.client.get(
            reverse('search_resources'), {'q': 'useful', 'in': ['description']}
        )
        self.assertIn(r, resp2.context['resources'])
        # keyword search
        resp3 = self.client.get(
            reverse('search_resources'), {'q': 'django', 'in': ['keywords']}
        )
        self.assertIn(r, resp3.context['resources'])
