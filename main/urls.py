from django.contrib import admin
from django.urls import path , include
from main.drf_yasg import urlpatterns as urlpatterns_swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('manga.urls'))
] + urlpatterns_swagger
