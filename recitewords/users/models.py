from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models

from recitewords.base.model import Base
from recitewords.word_book.models import WordBook


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserProfiles(Base):
    name = models.CharField('例句', max_length=200)
    Wbook = models.ManyToManyField(WordBook, default=models.CASCADE, related_name='w_book')

