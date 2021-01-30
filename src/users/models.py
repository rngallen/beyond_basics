from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class CustomUser(AbstractUser):
    is_director = models.BooleanField(_("Is director"), default=False)
    is_producer = models.BooleanField(_("Is producer"), default=True)
