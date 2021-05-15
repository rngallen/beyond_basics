from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Movie(models.Model):
    title = models.CharField(_("title"), max_length=60)
    actors = models.ManyToManyField(
        "actors.Actor", verbose_name=_("actors"), blank=True
    )
    created = models.DateField(_("created on"), auto_now=True)

    class Meta:
        abstract = True


class Film(Movie):
    length = models.CharField(_("length"), max_length=20)

    def __str__(self):
        return self.title


class Commercial(Movie):
    company = models.CharField(_("company"), max_length=60)

    def __str__(self):
        return self.title
