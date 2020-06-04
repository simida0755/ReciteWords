# _*_ coding: utf-8 _*_
__author__ = 'john'


class Man:
    def __init__(self,age):
        self.age = age



list = []

for i in range(5):
    m = Man(i)
    list.append(m)

for i in list:
    print(i.age)
