from django.contrib import admin
from . models import GenreBooks, Books, BooksInstance, Language, Author

# Register your models here.

class BooksInstanceInline(admin.TabularInline):

	"""
	Inline editing for Books Records
	"""

	model = BooksInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

	"""
	Displaying list of Author Models
	"""

	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):

	"""
	Displaying list of Books Models
	"""

	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]


@admin.register(BooksInstance)
class BooksInstanceAdmin(admin.ModelAdmin):

	"""
	Displaying list of Books Instance
	"""

	list_display = ('book', 'printed', 'date_back')
	list_filter = ('status', 'date_back')

	fieldsets = (
		(None, {
			'fields' : ('book', 'printed', 'id')
		}),
		('Availability', {
			'fields' : ('status', 'date_back')
		})
	)


@admin.register(GenreBooks)
class GenreBooksAdmin(admin.ModelAdmin):
	pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	pass


