import requests

url = 'https://ikmom.cc/api/v1/client/subscribe?token=f22056c1a908b711b3521c513ed1eaed'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/75.0.3770.100 YaBrowser/19.7.0.1635 Yowser/2.5 Safari/537.36',
}
rep = requests.request(url=url,params=headers)
data = rep.text

print(data)