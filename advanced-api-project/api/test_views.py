from django.urls import reverse # Generate URLs for API endpoints
from rest_framework import status # HTTP status codes for assertions
from rest_framework import APITestCase, APIClient #Tools for testing DRF APIs
from .models import Author, Book #Models in api app
from django.contrib.auth.models import User #User for authentication


# Create a class for Book views inheriting from APITestCase with tools for testing APIs
class BookTests(APITestCase):
    def setUp(self):
        '''
        set up data for tests.
        The function runs first before any test.
        '''

        #Create a user for authentication
        self.user = User.objects.create_user(username='test user', password='testpassword')

        #Create a test author(required for creating a book)
        self.author = Author.objects.create(name='test author')

        #Create some test books
        self.book1 = Book.objects.create(title='Book One', publication_year='2020-01-01', author = self.author)
        self.book2 = Book.objects.create(title='Book Two', publication_year='2021-01-01', author = self.author)

        #Authenticate the client for tests requiring authentication
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.client.login(user=self.user)

    # Write test to test BookListView - lists all the books and supports filtering, searching, and ordering
    def book_list_test(self):
        '''
        Test that a BookListView returns list of books with a status code of 200
        '''
        url = reverse('books') #Generate the URL for listing books based on the name of URL
        #Make a GET request to the endpoint
        response = self.client.get(url)
        #Check that the response status code is 200(OK)
        self.assertEqual(response.status.code, status.HTTP_200_OK)

        #Check that the response data contains the books we created
        self.assertEqual(len(response.data), 2)
        self.assertequal(response.data[0]['title'], 'Book One')
        self.assertequal(response.data[1]['title'], 'Book Two')
    # Write a test for BookCreateView to ensure it correctly creats a book
    def create_book_test(self):
        '''
        Test that BookCreateView creates a new book with status code 201
        '''
        #Generate URL for BookCreateView
        url = reverse('book-create')
        #Data for the new book
        data = {
            'title': 'New Book',
            'publication_year': '2022-01-01',
            'author': self.author.id # Use the ID of the test author
        }

        # Make a POST request to the endpoint
        response = self.client.post(url, data, format='json')

        # Check that the status response code is 201(created)
        self.assertEqual(response.status, status.HTTP_201_CREATED)

        # Check that the book was created in the databse
        self.asserEqual(Book.objects.count(), 3) #We started with 2 books
        self.assertEqual(Book.objects.get(id=3).title, 'New Book')


