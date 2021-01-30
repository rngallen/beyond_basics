from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Actor(models.Model):
    name = models.CharField(_("name"), max_length=200)
    # if is_star he/she will be directed to hollywoodelse directed to commercial
    is_star = models.BooleanField(_("is start"), default=False)

    def __str__(self):
        return self.name
    
