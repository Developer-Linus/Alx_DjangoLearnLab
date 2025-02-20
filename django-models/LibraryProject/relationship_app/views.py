from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView

def book_list(request):
    books = Book.objects.all()
    context = {'book_title': books.title,
               'book_author' : books.author}
    return render(request, 'relationship_app/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

