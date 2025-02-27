from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Book
# from .forms import BookForm  # Assuming you have a BookForm for editing

# Create your views here.
def home(request):
    return HttpResponse('Welcome to the bookshelf app.')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)  # Redirect to the book detail page
    else:
        form = BookForm(instance=book)

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
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', id=book.id)  # Redirect to the new book's detail page
    else:
        form = BookForm()

    return render(request, 'bookshelf/create_view.html', {'form': form})