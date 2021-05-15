from django.urls import path
from .views import index

app_name = "actors"

urlpatterns = [
    path("actors", index, name="actors_home"),
]
