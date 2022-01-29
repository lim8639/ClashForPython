import requests

def getWeatherInfo(city):
    url = "https://v2.alapi.cn/api/tianqi"
    payload = "token=KaFFgg59SceYx9KH&city="+city
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    data=payload.encode("utf-8").decode("latin1")
    response = requests.post(url=url, data=data, headers=headers)
    print(response.json())
    return response.json().get('data')