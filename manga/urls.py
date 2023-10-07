from django.urls import path
from manga import views

urlpatterns = [
    path('manga/', views.MangaApiView.as_view(), name='Manga'),
    path('type/', views.TypesApiView.as_view(), name='type list'),
    path('genre/', views.GenreApiView.as_view(), name='genere list'),
    path('manga/<slug:slug_manga>/', views.MangaDetailApiView.as_view(), name='manga detail'),
    path('type/<int:id>/', views.TypesDetailApiView.as_view(), name='types detail'),
    path('genre/<int:id>/', views.GenreDetailApiView.as_view(), name='genres detail'),

]
