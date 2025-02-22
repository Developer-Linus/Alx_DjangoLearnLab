from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.name
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

ROLE_CHOICES = {
    'Admin': 'Admin',
    'Librarian': 'Librarian',
    'MEMBER': 'MEMBER',
}
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.CharField(max_length=20, choices = ROLE_CHOICES, default='Member')
    def __str__(self):
        return f'{self.user.username} - {self.role}'


