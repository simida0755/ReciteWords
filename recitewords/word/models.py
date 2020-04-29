from django.db.models import ForeignKey

from recitewords.base.model import Base
from django.db import models

from recitewords.spider.api_word import ApiWord
from recitewords.spider.html_word_spider import SpiderWord


class WordQuerySet(models.query.QuerySet):
    def get_word(self, word):
        '''返回查询单词'''
        if ApiWord.verify_word(word):
            html_spider = SpiderWord(word)
            api_spider = ApiWord(word)
            Word.get_or_spider(word)


            return self.filter(name = word)

class Trans(Base):
    name = models.CharField('释义', max_length=50)

class Word(Base):
    name = models.CharField('单词', max_length=50)
    trans = ForeignKey(Trans,on_delete=models.CASCADE,related_name='trans')

    objects = WordQuerySet.as_manager()

    def get_or_spider(self,word):
        w =  Word.objects.get(name = word)
        if w :
            return w
        else:
            html_spider = SpiderWord(word)
            api_spider = ApiWord(word)
            if



class IPA(Base):
    """
    音标分类
    """
    CATEGORY_TYPE = (
        ('US', "美式"),
        ('UK', "英式"),

    )
    name = models.CharField('音标', max_length=50)
    type = models.CharField('音标类型', choices=CATEGORY_TYPE)
    link = models.CharField('链接',max_length=200)



class Phrase(Base):
    name = models.CharField('词组', max_length=50)
    trans = models.CharField('释义', max_length=50)

class Centences(Base):
    name = models.CharField('例句', max_length=50)
    trans = models.CharField('释义', max_length=50)

class Additional(Base):
    name = models.CharField('额外的', max_length=50)



