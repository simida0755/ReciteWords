
from recitewords.base.model import Base
from django.db import models

class User(Base):
    name = models.CharField('单词', max_length=50)



class IPA(Base):
    """
    音标分类
    """
    CATEGORY_TYPE = (
        ('KK', "美式音标"),
        ('DJ', "英式音标"),

    )
    name = models.CharField('音标', max_length=50)
    type = models.CharField('音标类型', choices=CATEGORY_TYPE)
    link = models.CharField('链接',max_length=200)

class Trans(Base):
    name = models.CharField('释义', max_length=50)

class Trans(Base):
    name = models.CharField('释义', max_length=50)

class Additional(Base):
    name = models.CharField('额外的', max_length=50)


class Phrase(Base):
    name = models.CharField('词组', max_length=50)
    trans = models.CharField('释义', max_length=50)

