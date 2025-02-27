from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Book
from .forms import ExampleForm  # Assuming you have a BookForm for editing

# Create your views here.

def book_list(request):
    # Get the search query from the request (if any)
    search_query = request.GET.get('q', '')

    # Use Django's ORM to filter books safely
    if search_query:
        books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__icontains=search_query)
    else:
        books = Book.objects.all()

    # Pass the books and search query to the template
    return render(request, 'bookshelf/book_list.html', {'books': books, 'search_query': search_query})
def home(request):
    return HttpResponse('Welcome to the bookshelf app.')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)  # Redirect to the book detail page
    else:
        form = ExampleForm(instance=book)

    return render(request, 'bookshelf/edit_view.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_view(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list page after deletion

    return render(request, 'bookshelf/confirm_delete.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', id=book.id)  # Redirect to the new book's detail page
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/create_view.html', {'form': form})