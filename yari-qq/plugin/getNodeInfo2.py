import requests


def getInfo():
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
    data = {}
    if response.status_code == 200:
        data = response.json().get('data')
        transfer_enable = data.get('transfer_enable') / (1024 * 1024 * 1024)
        transfer_d = data.get('d') / (1024 * 1024 * 1024)
        transfer_d = str(transfer_d)[0:4]
        msg = "第二机场：\n到期：" + str(data.get('reset_day')) \
              + "天后\n已用： " + transfer_d \
              + "GB\n总共： " + str(transfer_enable)+"GB"
        return msg

