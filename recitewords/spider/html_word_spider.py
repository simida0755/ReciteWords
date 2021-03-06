# _*_ coding: utf-8 _*_
import json

__author__ = 'john'

import requests
from bs4 import BeautifulSoup

api_url = 'http://www.youdao.com/w/eng/{}/#keyfrom=dict2.index'
#单词selector语法
WORD_SELECTOR='#wordGroup2 > p > span > a'

#词组单词selector语法语法
WORD_PHRASE_SELECTOR='#wordGroup2 > p'

#双语例句单词selector语法语法
WORD_CENTENCES_SELECTOR='#bilingual > ul > li'

#额外的（比较级)selector语法语法
WORD_ADDITIONAL_SELECTOR='#phrsListTab > .trans-container > p'

#html_url
YOUDAO_HTML_URL='http://www.youdao.com/w/eng/{}/#keyfrom=dict2.index'

#api_url
YOUDAO_URL='https://openapi.youdao.com/api'
APP_KEY='7bb52fcc9ffa80ca'
APP_SECRET='az7qP5kpdTVRWj3Uk2ZaQCa9pskWQrmQ'

#error-typo error-note

class SpiderWord:
    # 类有职责自己去完成一次请求

    def __init__(self, word):
        self.word = 'lj:{}'.format(word)
        self.youdao_html_url = YOUDAO_HTML_URL

        self.html = ''
        self.status_code = 0
        self.status = False
        self.soup = ''

        self.phrases = []
        self.centences = []

        self.spider_word()
        self.parse()

    def spider_word(self):
        url = self.youdao_html_url.format(self.word)
        result = requests.get(url)

        self.status_code = result.status_code
        self.html = result.text


    def parse(self):
        self.soup = BeautifulSoup(self.html, "lxml")
        self.verify_html()
        if self.status_code == 200 and self.status:
            self.find_phrases()
            self.find_centences()

    def verify_html(self):
        if self.status_code==200:
            verify_soup = self.soup.select('.error-note')
            if not verify_soup:
                self.status = True

    def find_phrases(self):
        phrases_soup = self.soup.select('#wordGroup2 > p')
        clutter_phrases = [word.get_text() for word in phrases_soup]

        self.phrases = SpiderWord.clean_phrases(clutter_phrases)


    def find_centences(self):
        centences_soup = self.soup.select('#bilingual > ul > li')
        clutter_centences = [word.get_text() for word in centences_soup]

        self.centences = SpiderWord.clean_centences(clutter_centences)

    @staticmethod
    def clean_phrases(clutter_phrases):
        '''格式化词组成列表'''
        list = []
        for word in clutter_phrases:
            word = word.replace('\n', '').replace('\r', '')
            word = [i.strip() for i in word.split('  ') if i]
            list.append(word)
        return list

    @staticmethod
    def clean_centences(clutter_centences):
        '''格式化双语例句成列表'''
        list = []
        for word in clutter_centences:
            word = [i.strip() for i in word.split('\n') if i]
            list.append(word)
        return list



if __name__=='__main__':

    spider = SpiderWord('try')
    for centence in spider.centences:
        print(len(centence[1]),'-------',centence[1])
