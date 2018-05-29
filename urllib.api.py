
block_cc_url = 'https://data.block.cc/api/v1/markets'


# requests 方法

# import requests,json
#
# data = json.dumps({})
# r = requests.get(block_cc_url)
#
# print(r)

# pycurl , json

# import pycurl, json
#
# c = pycurl.Curl()
# c.setopt(pycurl.URL, block_cc_url)
# c.perform()

# urllib, httplib2

# import urllib.request
# import urllib.parse
# #response = urllib.request.urlopen(block_cc_url)
#
# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
#
# print(response.read())
#print(response.read().decode("utf-8"))

from urllib import request,parse,error
import urllib
import json
url ='http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'
}
dict = { 'name':'Germey' }
try:
    data=bytes(parse.urlencode(dict),encoding='utf8')
    req = request.Request(url=block_cc_url,method="GET")
    response = request.urlopen(req)

    #print(type(response.read().decode('utf8')))
    print(json.loads(response.read().decode('utf-8'))['data'][0]['name'])
except error.URLError as e:
    print(e.reason)

# urllib2, urllib