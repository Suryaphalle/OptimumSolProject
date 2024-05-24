from django.views.generic import ListView, DetailView, View
from django_filters.views import FilterView
from .models import Movies, Genre
from django.shortcuts import render
from .filters import MoviesFilter
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Count
from collections import defaultdict

class MovieListView(FilterView, ListView):
    model = Movies
    filterset_class = MoviesFilter
    template_name = 'movie_list.html'
    context_object_name = 'movie'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtering logic
        title = self.request.GET.get('title')
        released = self.request.GET.get('released')
        rating = self.request.GET.get('rating')
        genres = self.request.GET.get('genres')
        
        filter_args = {}
        if title:
            filter_args['title__icontains']=title
        if released:
            filter_args['released__year']=released
        if rating:
            filter_args['rating__gte']=rating
        if genres and genres != '':
            filter_args['genres__in']=genres
        queryset = queryset.filter(**filter_args).order_by('-year')

        return queryset

    def get_grouped_movies(self):
        queryset = self.get_queryset()

        # Group by release month and year
        grouped_movies = defaultdict(lambda: defaultdict(list))
        for movie in queryset:
            release_date = movie.released
            year = release_date.year
            month = release_date.strftime('%b')
            grouped_movies[year][month].append(movie)

        grouped_movies = {year: dict(months) for year, months in grouped_movies.items()}
        return grouped_movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['grouped_movies'] = self.get_grouped_movies()
        return context

class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movie_detail.html'
    context_object_name = 'movie'