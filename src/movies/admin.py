from django.contrib import admin
from .models import Film, Commercial
from actors.models import Actor
# Register your models here.


# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ("title", "created")

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "length")

    def render_change_form(self, request, context, *args, **kwargs):
        context["adminform"].form.fields['actors'].queryset = Actor.objects.filter(is_star=True)
        return super().render_change_form(request, context, *args, **kwargs)


@admin.register(Commercial)
class CommercialAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "company")

    def render_change_form(self, request, context, *args, **kwargs):
        context["adminform"].form.fields['actors'].queryset = Actor.objects.filter(is_star=False)
        return super().render_change_form(request, context, *args, **kwargs)
