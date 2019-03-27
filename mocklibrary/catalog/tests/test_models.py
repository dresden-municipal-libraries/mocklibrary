from catalog.models import Author
from django.test import TestCase

# Write test here for Models

class AuthorModelTest(TestCase):

    """
    Test Author models
    """

    @classmethod
    def setUp(self):
        Author.objects.create(first_name='Jane', last_name='Doe')
