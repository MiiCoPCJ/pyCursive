import requests
from bs4 import BeautifulSoup

url = r'https://stackoverflow.com/questions/17766725/how-to-re-install-lxml'

data = requests.get(url, stream=True)

print(data.cookies)