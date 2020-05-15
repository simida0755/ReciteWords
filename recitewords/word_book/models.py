from django.db.models import ForeignKey

from recitewords.base.model import Base
from django.db import models

from recitewords.word.models import Word


class WordBook(Base):
    name = models.CharField('名称', max_length=10)
    word = models.ManyToManyField(Word, default=models.CASCADE, related_name='B_word')

