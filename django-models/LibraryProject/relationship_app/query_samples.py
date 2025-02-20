author = Author.objects.get(name='James Smith')
books = author.books.all()

book = Book.objects.get(title='12 Rules for Life')
books = book.libraries.all()

library = Library.objects.get(name="Machakos University")
librarian = library.librarian.get(name="Jack")