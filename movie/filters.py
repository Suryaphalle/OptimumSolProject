import django_filters
from .models import Movies, Genre
from django import forms

class MoviesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title to search'})
    )
    released = django_filters.ModelChoiceFilter(
        field_name='released__year',
        empty_label='All',
        widget=forms.Select(attrs={'placeholder': 'Select Year','class': 'form-control'}),
        queryset=Movies.objects.values_list('released__year',flat=True).order_by('-year').distinct(),
    )
    genres = django_filters.ModelChoiceFilter(
        queryset=Genre.objects.all(),
        empty_label="Genre",
        widget=forms.Select(attrs={'placeholder': 'Select Genre','class': 'form-control'}),
        field_name='genres'
    )

    class Meta:
        model = Movies
        fields = ['title', 'released', 'genres']