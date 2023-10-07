from django_filters import rest_framework as filter

from manga.models import Type, Genre, Manga


class MangaFilter(filter.FilterSet):
    type_manga = filter.ModelChoiceFilter(queryset=Type.objects.all())
    genre_manga = filter.ModelChoiceFilter(queryset=Genre.objects.all())

    class Meta:
        model = Manga
        fields = ['type_manga', 'genre_manga', ]
