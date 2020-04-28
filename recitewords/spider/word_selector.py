# _*_ coding: utf-8 _*_
__author__ = 'john'


def find_phrases(soup):
    phrases =  soup.select('#wordGroup2 > p')
    phrases_list = [word.get_text() for word in phrases]
    return phrases_list

def find_centences(soup):
    centences = soup.select('#bilingual > ul > li')
    centences_list = [word.get_text() for word in centences]
    return centences_list
