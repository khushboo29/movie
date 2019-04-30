from __future__ import unicode_literals
from django.db import models

class Genre(models.Model):
    """ Genre model: Model for the genre of the movie"""
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

class Movie(models.Model):
    """ Movie model: model for the movie """
    name = models.CharField(max_length=200)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name