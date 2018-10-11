from urllib import request,parse,error
import json

url ='https://api.coinmarketcap.com/v1/ticker/?convert=CNY&limit=0'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'
}

try:
    req = request.Request(url=url, method="GET")
    response = request.urlopen(req)
except error.URLError as e:
    print(e.reason)
    exit()

api_json = json.loads(response.read().decode('utf-8'))

print(api_json)