from django.contrib.auth import get_user_model
from django.db.models import ForeignKey

from django.conf import settings
from recitewords.base.model import Base
from django.db import models

from recitewords.word.models import Word

# User = get_user_model()





class WordBook(Base):
    name = models.CharField('名称', max_length=10)
    isupload = models.BooleanField('是否记录次数', default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', related_name='O_user')

class WordCount(Base):
    word = models.ForeignKey(Word,on_delete=models.CASCADE, related_name='count_word')
    count = models.IntegerField(default=1 )
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, default='',on_delete=models.CASCADE)
    w_book = models.ForeignKey(WordBook, on_delete=models.CASCADE, default='',related_name='w_count')

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
    sort = models.BooleanField('是否频率', default=1)
    last_word = models.CharField('单词', default='', max_length=50)


