from django.urls import reverse_lazy
from django.views.generic import FormView
# from .models import Film, Commercial
from .forms import CommercialModelForm,  FilmModelForm, MovieSelectFormView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class MovieSelectFormView(LoginRequiredMixin,FormView):
    form_class = MovieSelectFormView
    template_name = 'movies/main.html'
    success_url = reverse_lazy('movies:add_movies')

    def post(self, *args, **kwargs):
        self.request.session['movie'] = self.request.POST.get('movie')
        return super().post(*args, **kwargs)


class AddMovieFormView(LoginRequiredMixin,FormView):
    template_name = 'movies/add.html'
    success_url = reverse_lazy('index')

    def get_form_class(self, *args, **kwargs):
        movie = self.request.session.get('movie')
        if movie == "FILM" :
            return FilmModelForm
        else:
            return CommercialModelForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
