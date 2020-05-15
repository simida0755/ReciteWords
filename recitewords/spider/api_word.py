# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
import importlib

importlib.reload(sys)


YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '7bb52fcc9ffa80ca'
APP_SECRET = 'az7qP5kpdTVRWj3Uk2ZaQCa9pskWQrmQ'

class ApiWord():
    def __init__(self, word):
        self.word = word
        self.result = {}
        self.trans = []
        self.phonetic = []
        self.speech = []
        self.status = False
        self.connect()


    def connect(self):
        q = self.word

        data = {}
        data['from'] = 'en'
        data['to'] = 'zh-CHS'
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = APP_KEY + ApiWord.truncate(q) + salt + curtime + APP_SECRET
        sign = ApiWord.encrypt(signStr)
        data['appKey'] = APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign

        response = ApiWord.do_request(data)

        self.result = response.content.decode()
        import json
        j = json.loads(self.result)
        # j_obj = complex_dict_to_object(j)
        # if j_obj.basic.explains:
        #     self.trans = j_obj.basic.explains
        print(j)
        if j['errorCode'] == '0' and 'basic' in j.keys():
            self.status = True
            if 'explains' in j['basic']:
                self.trans = j["basic"]["explains"]

            if 'uk-speech' and 'uk-phonetic' in j['basic']:
                self.phonetic.append(['uk-speech', j['basic']['uk-speech']])

            if 'us-speech' and 'us-phonetic' in j['basic']:
                self.phonetic.append(['us-speech', j['basic']['us-speech']])
    @staticmethod
    def encrypt(signStr):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode('utf-8'))
        return hash_algorithm.hexdigest()

    @staticmethod
    def truncate(q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

    @staticmethod
    def verify_word(word):
        '''检测单词活词组不包含空格以外的数字或字符'''
        return word.replace(" ", "").isalpha()

    @staticmethod
    def do_request(data):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return requests.post(YOUDAO_URL, data=data, headers=headers)




if __name__ == '__main__':
    api = ApiWord('good')
    print(api.status)
    print(api.trans)
    print(api.phonetic)
