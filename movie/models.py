# Create your models here.
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    source = models.CharField(max_length=50)
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.source

class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=10)
    released = models.DateField(null=True)
    runtime = models.CharField(max_length=10)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.TextField()
    poster = models.URLField()
    meta_score = models.IntegerField()
    imdb_rating = models.FloatField()
    imdb_votes = models.CharField(max_length=20)
    imdb_id = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    dvd = models.DateField(null=True)
    box_office = models.CharField(max_length=20)
    production = models.CharField(max_length=100)
    website = models.URLField()
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    ratings = models.ManyToManyField(Rating)

    def __str__(self):
        return self.title
