from rest_framework import generics

from manga import models, serializers


class MangaApiView(generics.ListAPIView):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangaSerializer


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
