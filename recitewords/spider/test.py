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


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect():
    q = "good"

    data = {}
    data['from'] = 'en'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    # contentType = response.headers['Content-Type']
    # if contentType == "audio/mp3":
    #     millis = int(round(time.time() * 1000))
    #     filePath = r"E:/workSpace/webworld/app/MP3/" + str(millis) + ".mp3"
    #     fo = open(filePath, 'wb')
    #     fo.write(response.content)
    #     fo.close()
    # else:
    #     print(response.content.decode())
    print(response.content.decode())


if __name__ == '__main__':
    connect()
    # q = 'qwertyuiopasdfghjklzxcvbnm'
    # truncate = truncate(q)
    # print(truncate)
