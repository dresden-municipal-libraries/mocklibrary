import datetime
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from . models import GenreBooks, Books, Language, BooksInstance, Author
from . forms import RenewBookForm

# Create your views here.

def index(request):

	"""
	Function for rendering a library homepage
	:return detailed number of books:
	:return detailed instances of books:
	:return availability of boosk:
	:return list of authors of books:
	"""

	num_books = Books.objects.all().count()

	num_instances = BooksInstance.objects.all().count()

	num_instances_availability = BooksInstance.objects.filter(status__exact='a').count()

	num_authors = Author.objects.all()

	context = {
		'num_books' : num_books,
		'num_instances' : num_instances,
		'num_instances_availability' : num_instances_availability,
		'num_authors' : num_authors
	}

	return render(request, 'index.html', context=context)

class BookListView(generic.ListView):

	"""
	Class for representating and displaying list of Books
	"""

	model = Books
	paginate_by = 10

class BookDetailView(generic.DetailView):

	"""
	Class for representating and detailed list of Books
	"""

	model = Books

class AuthorListView(generic.ListView):

	"""
	Class for representating and displaying list of authors
	"""

	model = Author
	paginate_by = 10

class AuthorDetailView(generic.DetailView):

	"""
	Class for representating and detailed list of Authors
	"""

	model = Author

class LoanBookByUserListView(LoginRequiredMixin, generic.ListView):

	"""
	Class for representating and listing books on loaned by user
	"""

	model = BooksInstance
	template_name = 'loaned_book_by_user.html'
	paginate_by = 10

	def get_queryset(self):
		return BooksInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('date_back')

class AllLoanBookforUserListView(PermissionRequiredMixin, generic.ListView):

	"""
	Class for representating and listing all books that loaned by user
	Only user with permission can seen
	"""

	model = BooksInstance
	permission_required = 'catalog.can_mark_returned'
	template_name = 'all_loaned_books_by_user.html'
	paginate_by = 10

	def get_queryset(self):
		return BooksInstance.objects.filter(status__exact='o').order_by('date_back')

@permission_required('catalog.can_mark_returned')
def renew_book(request, pk):

	"""
	Function for renewing a specific book by Library Administrator
	"""

	if request.method == "POST":
		form = RenewBookForm(request.POST)

		if form.is_valid():
			book_instances.date_back = form.cleaned_data['renewal_date']
			book_instances.save()
			return HttpResponseRedirect(reverse('all-borrowed'))

	else:
		future_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
		form = RenewBookForm(initial={'renewal_date' : future_renewal_date})

	context = {
		'form' : form,
		'book_instances' : book_instance
	}
	return render(request, 'renew_book.html', context)

class AuthorCreate(PermissionRequiredMixin, CreateView):

	"""
	Class for representating forms by Author
	"""

	model = Author
	fields = '__all__'
	initial = {'date_of_death' : '01/01/2018'}
	permission_required = 'catalog.can_mark_returned'

class AuthorUpdate(PermissionRequiredMixin, UpdateView):

	model = Author
	fields = ['first_name', 'last_name', 'date_of_death', 'date_of_birth']
	permission_required = 'catalog.can_mark_returned'

class AuthorDelete(PermissionRequiredMixin, DeleteView):

	model = Author
	success_url = reverse_lazy('authors')
	permission_required = 'catalog.can_mark_returned'

class BookCreate(PermissionRequiredMixin, CreateView):

	"""
	Class for representating forms by Books
	"""

	model = Books
	fields = '__all__'
	permission_required = 'catalog.can_mark_returned'

class BookUpdate(PermissionRequiredMixin, UpdateView):

	model = Books
	fields = '__all__'
	permission_required = 'catalog.can_mark_returned'

class BookDelete(PermissionRequiredMixin, DeleteView):

	model = Books
	success_url = reverse_lazy('books')
	permission_required = 'catalog,can_mark_returned'
