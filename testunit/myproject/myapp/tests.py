from django.test import TestCase
from django.urls import reverse

class URLTestCase(TestCase):

    def test_book_list_url(self):
        # reverse('book_list') gives us the URL for the 'book_list' view
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)  # Check if the status code is 200 (OK)

from django.test import TestCase
from django.urls import reverse
from .models import Book

class ViewTestCase(TestCase):

    def test_book_list_view(self):
        # Create some sample books in the database
        Book.objects.create(title="The Great", author="Scott")
        Book.objects.create(title="1984", author="George ")

        # Make a GET request to the 'book_list' URL
        response = self.client.get(reverse('book_list'))

        # Check if the response contains the titles of the books
        self.assertContains(response, "The Great")
        self.assertContains(response, "1984")
        self.assertEqual(response.status_code, 200)  # The request should return 200 OK

from django.test import TestCase
from .models import Book

class ModelTestCase(TestCase):

    def test_book_model_str(self):
        book = Book.objects.create(title="Moby", author="Harman")
        
        # Check if the __str__ method returns the correct string
        self.assertEqual(str(book), "Moby")
