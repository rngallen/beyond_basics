from django.urls import path
from .views import AddMovieFormView, MovieSelectFormView

app_name = 'movies'

urlpatterns = [
    path('', MovieSelectFormView.as_view(), name='select_movie'),
    path('add/', AddMovieFormView.as_view(), name='add_movies'),
]
