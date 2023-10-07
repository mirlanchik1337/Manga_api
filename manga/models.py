import pytils
from autoslug import AutoSlugField
from django.core.validators import FileExtensionValidator
from django.db import models
from pytils import translit
from slugify import slugify


class Genre(models.Model):
    genre_name = models.CharField(
        max_length=30, blank=True, unique=True, verbose_name="Жанр"
    )

    def __str__(self):
        return self.genre_name

    class Meta:
        ordering = ("id",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Type(models.Model):
    type_name = models.CharField(
        max_length=20, blank=True, verbose_name="Тип"
    )

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ("id",)
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Manga(models.Model):
    title_manga = models.CharField(
        max_length=100, unique=True,
        db_index=True, verbose_name='title_manga')
    slug_manga = AutoSlugField(unique=True, populate_from='title_manga')
    genre_manga = models.ManyToManyField(
        Genre, related_name="genres",
        verbose_name="Genre Manga"
    )
    type_manga = models.ManyToManyField(
        Type, related_name="types",
        verbose_name="Type Manga"
    )
    manga_year = models.DateField(verbose_name="Year of Born", blank=True)
    manga_posted_date = models.DateField(
        auto_now_add=True, verbose_name="Created Date",
    )
    manga_synopsis = models.TextField(max_length=300, verbose_name="Краткое описание")
    manga_image = models.ImageField(upload_to='media/images', verbose_name='Icon for Manga',
                                    blank=True, default='',
                                    validators=[FileExtensionValidator(allowed_extensions=["png", "jpeg", "img"]), ])

    def __str__(self):
        return self.title_manga

    def get_genre_list(self):
        return ', '.join([genre.genre_name for genre in self.genre_manga.all()])

    def get_type_list(self):
        return ', '.join([type.type_name for type in self.type_manga.all()])

    def save(self, *args, **kwargs):
        self.mango_slug = pytils.translit.slugify(self.title_manga)
        super(Manga, self).save(*args, **kwargs)

    class Meta:
        ordering = ("slug_manga",)
        verbose_name = "Manga"
        verbose_name_plural = "Manga"
