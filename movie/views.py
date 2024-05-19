from django.views.generic import ListView, DetailView, View
from django_filters.views import FilterView
from .models import Movies
from django.shortcuts import render
from .filters import MoviesFilter

class MovieListView(FilterView, ListView):
    model = Movies
    filterset_class = MoviesFilter
    template_name = 'movie_list.html'
    context_object_name = 'movie'

class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movie_detail.html'
    context_object_name = 'movie'