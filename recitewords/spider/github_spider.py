# _*_ coding: utf-8 _*_
import re
import requests
from bs4 import BeautifulSoup

__author__ = 'john'



class SpiderGithub:

    def __init__(self, url):
        self.url = url
        self.status = 0
        self.words = {}
        self.parse()


    def parse(self):
        if len(self.url) < 11 or 'github.com/' not in self.url:
            return
        response = requests.get(self.url)
        self.status = response.status_code
        if self.status == 200:
            html = response.text
            soup = BeautifulSoup(html, "lxml")
            body = soup.select('.blob-code-inner')
            for i in body:
                for word in SpiderGithub.parse_line_word(i.get_text()):
                    word = word.lower()
                    if word in self.words.keys():
                        self.words[word] += 1
                    else:
                        self.words[word] = 1
            return self.words

    @staticmethod
    def parse_line_word(line):
        return re.compile(r'[a-zA-Z][a-z]+|[A-Z][A-Z]+').findall(line.replace('_', ' '))

if __name__=='__main__':
    url = 'https://github.com/simida0755/ReciteWords/blob/master/config/settings/base.py'
    sg = SpiderGithub(url)
    print(sg.words)
