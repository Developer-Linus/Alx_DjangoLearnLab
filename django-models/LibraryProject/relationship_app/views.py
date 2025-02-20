from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def book_list(request):
    books = Book.objects.all()
    context = {'book_title': books.title,
               'book_author' : books.author}
    return render(request, 'books/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library/library_detail.html'

