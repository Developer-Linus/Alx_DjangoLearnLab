book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

The expected output is the creation of a Book instance, book, that will be stored in the database. The shell should move to the next line if the operation is successfull.

Book.objects.all()

The output should give a query set showing the title of book, author's name, and the year of publication.
<QuerySet [<Book: 1984 by George Orwell 1949>]>

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

The object returned and stored in book is the created object with an id of 1. The title is changed using dot notation to access it and a new value assigned. Finally, the changed title is saved.
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell 1949>]>

book = Book.objects.get(id=1)
book.delete()

These commands should delete the object instane and return number of objects deleted.

(1, {'bookshelf.Book': 1})
