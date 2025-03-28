author = Author.objects.get(name=author_name)
books = author.Book.objects.filter(author=author)

library = Library.objects.get(name=library_name)
books = library.books.all()

library = Library.objects.get(name=library_name)
librarian = library.Librarian.objects.get(library=library_name)