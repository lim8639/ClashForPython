
import yaml
import requests



def getNode():
    url = "https://ikmom.cc/api/v1/client/subscribe?token=f22056c1a908b711b3521c513ed1eaed"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ClashforWindows/0.13.6 Chrome/85.0.4183.93 Electron/10.1.1 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return '0'
ystr = getNode();
aa = yaml.load(ystr, Loader=yaml.FullLoader)
print(aa['proxies'])
file = open('v2.yaml','w')

yaml.safe_dump(aa, file, default_flow_style=False)