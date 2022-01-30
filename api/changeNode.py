import json

import requests

headers = {
    "content-type": "application/json",
}
data = {
    "timeout": "5000",
    "url": 'https://youtube.com',
}


def trafficShow():
    url = 'http://localhost:8090/proxies/Proxy'
    r = requests.put(url=url, data=json.dumps({'name': '🇭🇰 标准|香港03解锁|P22'}), headers=headers)
    print(r.status_code)
    print(r.content)
    print(r.request.url)


trafficShow()


def trafficShow2():
    data = {
        "timeout": "5000",
        "url": 'https://youtube.com',
    }

    url = 'http://localhost:8090/proxies/GLOBAL'
    r = requests.request("put", url, data=data, headers=headers)
    print(r.status_code)
    print(r.content)
    print(r.request.url)


