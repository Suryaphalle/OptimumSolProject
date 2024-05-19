import django_filters
from .models import Movies, Genre
from django import forms

class MoviesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    release_date = django_filters.NumberFilter(
        field_name='released__year',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    genres = django_filters.ModelChoiceFilter(
        queryset=Genre.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        field_name='genres'
    )

    class Meta:
        model = Movies
        fields = ['title', 'released', 'genres']