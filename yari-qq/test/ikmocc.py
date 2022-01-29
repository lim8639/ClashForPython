from pyquery import PyQuery as pq
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
data = {
    'email': 'lim8639@qq.com',
    'password': '863978160',
}
url = 'https://ikmom.cc/api/v1/passport/auth/login'
session = requests.Session()
session.post(url, headers=headers, data=data)
# 登录后，我们需要获取另一个网页中的内容
response = session.get('https://ikmom.cc/api/v1/user/getSubscribe', headers=headers)
print(response.status_code)
print(response.json())

