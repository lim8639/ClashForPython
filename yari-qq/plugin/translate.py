import requests
import hashlib
import time
import asyncio

def translateEtoC(q):
    url = "http://dict.youdao.com/suggest"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 YaBrowser/19.7.0.1635 Yowser/2.5 Safari/537.36',
    }
    payload = {'q': q, 'num': 10, 'doctype': 'json'}
    r = requests.post(url=url, headers=headers, data=payload)
    res = ''
    if r.status_code == requests.codes.ok:
        content = r.json()
        for item in content['data']['entries']:
            res = res + item['entry'] + '  :  ' + item['explain'] + '\n'
    else:
        res = '查询失败'
    return res


def translateWord(q):
    url = "http://dict.youdao.com/suggest"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 YaBrowser/19.7.0.1635 Yowser/2.5 Safari/537.36',
    }
    payload = {'q': q, 'num': 10, 'doctype': 'json'}
    r = requests.post(url=url, headers=headers, data=payload)
    res = ''
    if r.status_code == requests.codes.ok:
        content = r.json()

        for item in content['data']['entries']:
            res = res + item['entry'] + '  :  ' + item['explain'] + '\n'
    else:
        res = '查询失败'
    return res


def baiduTranslate(q):
    url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
    hl = hashlib.md5()
    appid = '20220111001053227'
    salt = str(time.time())
    key = 'oFw4IG1fDLpg69O9aKEb'
    md5code = appid + q + salt + key
    hl.update(md5code.encode(encoding='utf-8'))
    sign = hl.hexdigest()
    payload = {'from': 'auto', 'to': 'en', 'q': q, 'appid': '20220111001053227', 'salt': salt, 'sign': sign}
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return '0'
