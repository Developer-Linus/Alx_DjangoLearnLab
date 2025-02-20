author = Author.objects.get(name='author_name')
books = author.books.all()

library = Library.objects.get(name='library_name')
books = library.libraries.all()

library = Library.objects.get(name='library_name')
librarian = library.librarian.get(name="librarian_name")