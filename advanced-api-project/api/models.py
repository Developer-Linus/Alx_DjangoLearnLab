from django.db import models
#Create the Author model that will store data about authors in the system
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create Book model that stores data about book instances.
# Book model has one-to-many relationship with Author model in the field 'author'
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    

