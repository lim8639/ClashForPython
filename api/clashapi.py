import json

import requests
data = {
    "timeout": "5000",
    "url": 'https://youtube.com',
}

class ClashApi:
    def trafficShow(self):
        url = 'http://localhost:8090/logs'
        r = requests.get(url, stream=True)
        for raw_rsvp in r.iter_lines():
            if raw_rsvp:
                rsvp = json.loads(raw_rsvp)
                print(rsvp.get('payload'))
api = ClashApi()
api.trafficShow()

