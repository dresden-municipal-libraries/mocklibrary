import uuid
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class GenreBooks(models.Model):

	"""
	Representing Models of Book Genre
	"""

	name = models.CharField(max_length=150, help_text='Enter a Book Genre(e.g. Fiction)')

	def __str__(self):
		return self.name

class Books(models.Model):

	"""
	Representing Models of Books Params =
		:title:
		:author:
		:summary:
		:printed:
		:isbn:
		:return genre:
		:return language:
	"""

	title = models.CharField(max_length=150)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(help_text='Enter a Brief Description of Books')
	isbn = models.CharField('ISBN', max_length=20, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(GenreBooks, help_text='Select a Genre for this Book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):

		"""
		Return the URL access a detail from book
		"""

		return reverse('book-detail', args=[str(self.id)])

	def display_genre(self):

		"""
		Return string for genre of books
		"""

		return ', '.join(genre.name for genre in self.genre.all()[:3])

	display_genre.short_description = 'Genre'


class BooksInstance(models.Model):

	"""
	Representing Specific Model for Borrowed Book
	"""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for every Books')
	book = models.ForeignKey('Books', on_delete=models.SET_NULL, null=True)
	printed = models.CharField(max_length=150)
	date_back = models.DateField(null=True, blank=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	@property
	def is_over(self):
		if self.date_back and date.today() > self.date_back:
			return True
		return False

	"""
	List of Loaned book status
	"""

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On Loan'),
		('a', 'Available'),
		('r', 'Reserved')
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book Availability'
	)

	class Meta:
		ordering = ['date_back']
		permissions = (('can_mark_returned', 'Set Books as Returned'),)

	def __str__(self):
		return f'{self.id}({self.book.title})'

class Author(models.Model):

	"""
	Representing Models for Author of Books Params =
	:first name:
	:last name:
	:date of birth:
	:date of death:
	"""

	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):

		"""
		Return the URL access a detail from author book
		"""

		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):

		"""
		Return Representing of Model Objects
		"""

		return f'{self.last_name}, {self.first_name}'

class Language(models.Model):

	"""
	Representing Model of Languages that used
	"""

	name = models.CharField(max_length=100, help_text='Book Languages(e.g. English, Arab, etc)')

	def __str__(self):
		return self.name
