book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

The expected output is the creation of a Book instance, book, that will be stored in the database. The shell should move to the next line if the operation is successfull.
