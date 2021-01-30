from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Movie(models.Model):
    title = models.CharField(_("title"), max_length=150)
    actors = models.ManyToManyField("actors.Actor", verbose_name=_(
        "actors"), blank=True)
    created = DateTimeField(_("created on"), auto_now=True)

    class Meta:
        abstract = True


class Film(Movie):
    length = models.CharField(_("length"), max_length=200)

    def __str__(self):
        return self.title


class Commercial(Movie):
    company = models.CharField(_("company"), max_length=200)

    def __str__(self):
        return self.title
