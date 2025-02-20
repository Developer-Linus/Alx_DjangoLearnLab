author = Author.objects.get(name='James Smith')
books = author.books.all()

library = Library.objects.get(name='Machakos University')
books = library.libraries.all()

library = Library.objects.get(name='Machakos University')
librarian = library.librarian.get(name="Jack")