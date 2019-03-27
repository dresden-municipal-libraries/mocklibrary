from catalog.models import Author
from django.test import TestCase

# Write test here for Models

class AuthorModelTest(TestCase):

    """
    Test Author models Params =
    :first name labels:
    :last name labels:
    :date of birth labels:
    :date of death labels:
    """

    @classmethod
    def setUp(self):
        Author.objects.create(first_name='Jane', last_name='Doe')

    def test_first_name_labels(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_labels(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_labels(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_labels(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')

    def test_first_name_max_length_fields(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 150)

    def test_last_name_max_length_fields(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 150)

    #this test will fail if url conf not setting in
    #def test_get_absolute_url(self):
    #    author = Author.objects.get(id=1)
    #    self.assertEquals(author.get_absolute_url(), '/catalog/author/')
