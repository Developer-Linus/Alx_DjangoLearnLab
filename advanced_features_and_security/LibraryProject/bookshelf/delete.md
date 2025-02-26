from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()

These commands should delete the object instane and return number of objects deleted.

(1, {'bookshelf.Book': 1})
