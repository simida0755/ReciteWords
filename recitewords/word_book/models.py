from django.contrib.auth import get_user_model
from django.db.models import ForeignKey

from recitewords.base.model import Base
from django.db import models

from recitewords.word.models import Word


class WordBook(Base):
    name = models.CharField('名称', max_length=10)
    word = models.ManyToManyField(Word, related_name='B_word')
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='O_user')


class WordOrder(Base):

    order_choices = (
        (1, '顺序'),
        (2, '随机'),
    )
    sort_choices = (
        (1, '使用频率'),
        (2, '出现频率'),
    )

    name = models.CharField('名称', max_length=10)
    order = models.IntegerField('顺序', default=1, choices=order_choices)
    isupload = models.BooleanField('是否为上传', default=1)
    sort = models.BooleanField('是否频率', default=1)
    last_word = models.CharField('单词', default='', max_length=50)

