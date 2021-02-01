from django.urls import path
from .views import index,  AddMovieFormView, MovieSelectFormView

app_name = 'movies'

urlpatterns = [
    path('index/', index, name='index'),
    path('', MovieSelectFormView.as_view(), name='select_movie'),
    path('add/', AddMovieFormView.as_view(), name='add_movies'),
]
