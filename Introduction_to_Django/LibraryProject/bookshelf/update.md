book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

The object returned and stored in book is the created object with an id of 1. The title is changed using dot notation to access it and a new value assigned. Finally, the changed title is saved.
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell 1949>]>
