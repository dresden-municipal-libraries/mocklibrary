from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from catalog.views import index, BookListView

# test for views

class SimpleViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Jane Doe', email='janedoe@mail.com', password='secret'
        )

    @classmethod
    def setUpAuthor(self):
        number_of_authors = 13
        for author_id in range(number_of_authors):
            Author.objects.create(first_name='Jane'.format(author_id),
                                  last_name='Doe'.format(author_id))

    def test_view_urls_does_exist(self):
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_urls_is_accessible(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 10)

    def test_lists_all_authors(self):

        """
        Get second page and confirm it has (exactly) remaining 3 items
        """

        response = self.client.get(reverse('authors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 3)
