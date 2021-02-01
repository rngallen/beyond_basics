from django import forms
from .models import Film, Commercial
from actors.models import Actor


MOVIE_CHOICES = (
    ('FILM', 'Film'),
    ('COMMERCIAL', 'Commercial')
)


class MovieSelectFormView(forms.Form):
    movie = forms.ChoiceField(choices=MOVIE_CHOICES, label='Select Movie Type',
                              widget=forms.RadioSelect(attrs={"class": "radio_1"}))


class CommercialModelForm(forms.ModelForm):
    actors = forms.ModelMultipleChoiceField(label='Select Actors', widget=forms.CheckboxSelectMultiple(
        attrs={"class": 'checkbox_1'}), queryset=Actor.objects.filter(is_star=False))

    class Meta:
        model = Commercial
        fields = "__all__"


class FilmModelForm(forms.ModelForm):
    actors = forms.ModelMultipleChoiceField(label='Select Actors', widget=forms.CheckboxSelectMultiple(
        attrs={"class": "checkbox_1"}), queryset=Actor.objects.filter(is_star=True))

    class Meta:
        model = Film
        fields = "__all__"
