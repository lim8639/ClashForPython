import requests
import yaml


def getNode(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ClashforWindows/0.13.6 Chrome/85.0.4183.93 Electron/10.1.1 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == requests.codes.ok:
        return yaml.load(response.text, Loader=yaml.FullLoader)
    else:
        return False


def updateNodeConfig(filePath,nodelist):
    V2list = []
    V2NameList = []
    for url in nodelist:
        config = getNode(url)
        if config:
            V2list += config['proxies']
        else:
            return False
    for name in V2list:
        V2NameList.append(name['name'])
    file = open(filePath,encoding='utf-8')
    str = file.read()
    file.close()
    aa = yaml.load(str,Loader=yaml.FullLoader)
    aa['proxies'] = V2list
    SelectList = ['AutoSelect','DIRECT']
    SelectList += V2NameList
    aa['proxy-groups'][0]['proxies'] = SelectList
    aa['proxy-groups'][1]['proxies'] = V2NameList
    file2 = open(filePath,'w')
    yaml.safe_dump(aa, file2, default_flow_style=False)
    return True