

import requests

url = 'https://americansjewelry.com/libraries/monitored-object/lib/MonitorLed.js'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

r = requests.get(url, headers=headers)

print(r.text)
