import requests

headersIndex = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'https://jwc.ysu.edu.cn/'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

}

response = requests.get('http://202.206.243.62/', headers=headers)
url = 'https://user.ppypro.xyz/auth/login'
session = requests.Session()
session.post(url, headers=headers, data=data)
# 登录后，我们需要获取另一个网页中的内容
response = session.get('https://user.ppypro.xyz/user', headers=headers)