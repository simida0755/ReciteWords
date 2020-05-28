from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models

from recitewords.base.model import Base
from recitewords.word_book.models import WordBook, WordOrder


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    Wbook = models.ManyToManyField(WordBook, related_name='w_book')
    Worder = models.OneToOneField(WordOrder, null=True,on_delete=models.CASCADE, related_name='w_order')
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

# class UserProfiles(AbstractUser):
#     name = models.CharField('姓名', max_length=200)
#
#
#     def get_absolute_url(self):
#         return reverse("users:detail", kwargs={"username": self.username})
