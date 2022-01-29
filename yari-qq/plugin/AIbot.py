from time import sleep

import requests

apiUrl = 'http://www.tuling123.com/openapi/api'

KEY1 = '988cc14521094fbca1f9c0115dbb6b60'
KEY2 = 'dc4312db600b4c41b4edaf381c23559a'
KEY3 = 'ae652fb5fc7d4ce9b78e8edb32ec6b5a'
KEY4 = '221cb1ac22f04de985a72c1cfbe7e73a'
KEY5 = '14d50167b71547349cd6e4456dab064e'


def get_response(msg):
    # 这里实现与图灵机器人的交互
    # 构造了要发送给服务器的数据
    data = {
        'key': KEY1,
        'info': msg,
        'userid': 'wechat-robot'
    }
    r1 = requests.post(apiUrl, data=data).json()
    if r1["code"] == 100000:
        res = r1["text"]
    else:
        data = {
            'key': KEY2,
            'info': msg,
            'userid': 'wechat-robot'
        }
        r2 = requests.post(apiUrl, data=data).json()
        if r2["code"] == 100000:
            res = r2.get('text')
        else:
            data = {
                'key': KEY3,
                'info': msg,
                'userid': 'wechat-robot'
            }
            r3 = requests.post(apiUrl, data=data).json()
            if r3["code"] == 100000:
                res = r3.get('text')
            else:
                data = {
                    'key': KEY4,
                    'info': msg,
                    'userid': 'wechat-robot'
                }
                r4 = requests.post(apiUrl, data=data).json()
                if r4["code"] == 100000:
                    res = r4.get('text')
                else:
                    data = {
                        'key': KEY5,
                        'info': msg,
                        'userid': 'wechat-robot'
                    }
                    r5 = requests.post(apiUrl, data=data).json()
                    if r5["code"] == 100000:
                        res = r5.get('text')
    return res
