import requests
from pyquery import PyQuery as pq

def getInfo():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    data = {
        'email': '863978160@qq.com',
        'passwd': '863978160',
    }
    url = 'https://user.ppypro.xyz/auth/login'
    session = requests.Session()
    session.post(url, headers=headers, data=data)
    # 登录后，我们需要获取另一个网页中的内容
    response = session.get('https://user.ppypro.xyz/user', headers=headers)
    msg = {}
    if response.status_code == 200:
        doc = pq(response.text)
        msg['code'] = 1
        msg['time'] = doc(
            '#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(1) > div > div.card-stats > div > nav > ol > li').text()
        msg['device'] = doc(
            '#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(3) > div > div.card-wrap > div.card-body > span').text()+" 台"  # 传入CSS选择器
        msg['transfer'] = doc(
            '#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(2) > div > div.card-wrap > div.card-body > span').text() + "GB"  # 传入CSS选择器
        msg['money'] = doc(
            '#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(4) > div > div.card-wrap > '
            'div.card-body > span').text()+"元"  # 传入CSS选择器
        msg['today_transfer'] = doc(
            '#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(2) > div > div.card-wrap > '
            'div.card-stats > div > nav > ol > li').text()  # 传入CSS选择器
    else:
        msg['code'] = 0
    return msg