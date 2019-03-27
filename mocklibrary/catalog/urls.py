from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('books/<int:pk>/', views.BookDetailView.as_view(), name='books_detail'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
	path('userbooks/', views.LoanBookByUserListView.as_view(), name='borrowed_book'),
	path('borrowed/', views.AllLoanBookforUserListView.as_view(), name='all_borrowed_book'),
	path('books/<uuid:pk>/renew/', views.renew_book, name='renew_book'),
	path('author/create/', views.AuthorCreate.as_view(), name='author_view'),
	path('author/<int:pk>/update/', views.AuthorDelete.as_view(), name='author_update'),
	path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
	path('book/create/', views.BookCreate.as_view(), name='book_view'),
	path('book/<int:pk>/update/', views.BookDelete.as_view(), name='book_update'),
	path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),

]
