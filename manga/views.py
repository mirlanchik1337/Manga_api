from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from manga import models, serializers
from manga.filters import MangaFilter


class MangaApiView(generics.ListAPIView):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MangaFilter
    ordering_fields = ['manga_year', ]


class MangaDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangaSerializer
    lookup_field = 'slug_manga'


class TypesApiView(generics.ListAPIView):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


class TypesDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
    lookup_field = 'id'


class GenreApiView(generics.ListAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class GenreDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    lookup_field = 'id'
