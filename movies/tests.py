import unittest
from django.test import TestCase
from django.contrib.auth.models import User

from movies.models import Movie, Genre
from movies.serializers import MovieSerializer, GenreSerializer
# Create your tests here.

#Testing the Genre Model
class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name="Cartoon")
        Genre.objects.create(name="Drama")

    def test_genre_exist(self):
        cartoon = Genre.objects.get(name="Cartoon")
        drama = Genre.objects.get(name="Drama")
        self.assertEqual(cartoon.name, 'Cartoon')
        self.assertEqual(drama.name, 'Drama')