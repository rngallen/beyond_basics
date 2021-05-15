"""chiluba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from .views import index, login_view, logout_view

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/", include("users.urls")),
    path("movies/", include("movies.urls", namespace="movies")),
    # path('actors/', include("actors.urls", namespace="actors")),
]

admin.site.site_header = "Movies Administration"
admin.site.site_title = "Bongo Movie"
admin.site.index_title = "Manage Bongo Movies"
# admin.site.site_url = 'localhost:8000/movies/'
