import requests
from pyquery import PyQuery as pq

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
if response.status_code == 200:
    doc = pq(response.text)      # 传入HTML字符串
    str = doc('#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(1) > div > div.card-stats > div > nav > ol > li')   # 传入CSS选择器
    print("到期时间",str.text())
    print("当前在线设备",doc('#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(3) > div > div.card-wrap > div.card-body > span').text())     # 传入CSS选择器
    print("流量剩余",doc('#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(2) > div > div.card-wrap > div.card-body > span').text(),"GB")     # 传入CSS选择器
    print("钱包余额",doc('#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(4) > div > div.card-wrap > div.card-body > span').text())     # 传入CSS选择器
    print(doc('#app > div > div.main-content > section > div:nth-child(2) > div:nth-child(2) > div > div.card-wrap > div.card-stats > div > nav > ol > li').text())     # 传入CSS选择器

