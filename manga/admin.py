from django.contrib import admin
from manga import models

admin.site.register(models.Manga)
admin.site.register(models.Genre)
admin.site.register(models.Type)
