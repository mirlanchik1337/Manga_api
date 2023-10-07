from rest_framework import serializers
from slugify import slugify
from manga import models


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    genre_manga = serializers.SerializerMethodField()
    type_manga = serializers.SerializerMethodField()

    class Meta:
        model = models.Manga
        fields = '__all__'

    def create(self, validated_data):
        # Генерируем slug на основе заголовка (title)
        slug = slugify(validated_data['title'])
        validated_data['slug'] = slug

    def get_genre_manga(self, obj):
        return ', '.join(
            [f'name genre: ({genre.genre_name}) id genre : ({genre.pk}) |' for genre in obj.genre_manga.all()])

    def get_type_manga(self, obj):
        return ', '.join([f'name type :({type.type_name}) id type :({type.pk}) |' for type in obj.type_manga.all()])
