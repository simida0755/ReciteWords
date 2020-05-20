from django.db.models import ForeignKey
from django.http import Http404

from recitewords.base.model import Base
from django.db import models

from recitewords.spider.api_word import ApiWord
from recitewords.spider.html_word_spider import SpiderWord




class Word(Base):
    name = models.CharField('单词', max_length=50, db_index=True)
    additional = models.OneToOneField('Additional',null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "单词"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @staticmethod
    def get_or_spider(word):
        try:
            w =  Word.objects.get(name = word)
            return w
        except:
            return Word.spider_add_word(word)

    @staticmethod
    def spider_add_word(word):
        html_spider = SpiderWord(word)
        api_word = ApiWord(word)
        if api_word.status and html_spider.status:
            w = Word()
            w.name = word
            w.save()
            for tran in api_word.trans:
                t = Trans()
                t.name = tran
                t.word = w
                t.save()

            for ipa in api_word.phonetic:
                i = IPA()
                i.name = ipa[0]
                i.link = ipa[1]
                i.word = w
                i.save()

            for phrease in html_spider.phrases:
                p = Phrase()
                p.name = phrease[0]
                p.trans = phrease[1]
                p.word = w
                p.save()
            for centence in html_spider.centences:
                c = Centences()
                c.name = centence[0]
                c.trans = centence[1]
                c.link = centence[2]
                c.word = w
                c.save()

            w = Word.objects.get(name = word)
            return w
        Http404('No %s matches the given word.' % word)





class Trans(Base):
    word = models.ForeignKey(Word,on_delete=models.CASCADE, related_name='t_word')
    name = models.CharField('释义', max_length=50)

    class Meta:
        verbose_name = "释义"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class IPA(Base):

    word = models.ForeignKey(Word,on_delete=models.CASCADE, related_name='i_word')
    name = models.CharField('音标', max_length=50)
    link = models.CharField('链接',max_length=200)

    class Meta:
        verbose_name = "音标"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Phrase(Base):
    word = models.ForeignKey(Word,on_delete=models.CASCADE, related_name='p_word')
    name = models.CharField('词组', max_length=50)
    trans = models.CharField('释义', max_length=50)

    class Meta:
        verbose_name = "词组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Centences(Base):
    word = models.ForeignKey(Word,on_delete=models.CASCADE, related_name='c_word')
    name = models.CharField('例句', max_length=200)
    trans = models.CharField('释义', max_length=100)
    link = models.CharField('网址',max_length=50)

    class Meta:
        verbose_name = "例句"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Additional(Base):
    name = models.CharField('额外的', max_length=50)

    class Meta:
        verbose_name = "额外的"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





