import sys
import io
from urllib import request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

cookie_str = r'lang=zh-cn;_ga=GA1.2.913294773.1641517786;_gid=GA1.2.380437300.1642333474; PHPSESSID=83vsph4j5navrdja4ke3na16l5; uid=30353; email=863978160%40qq.com; key=0cc8edae5cef1f6b30da7e1c5473b2cfdece2d3b980b2; ip=ed4dfed04e9da25904681cb518e997e0; expire_in=1642421790'
#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
url = 'https://user.ppypro.xyz/user'
print(cookies)
req = request.Request(url)
req.add_header('cookie', cookies)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

resp = request.urlopen(req)

print(resp.read().decode('utf-8'))