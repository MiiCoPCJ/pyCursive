from bs4 import BeautifulSoup
import requests

# url = r'https://www.jinse.com/exchange/bitfinex'
#
# html = requests.get(url)
#
# soup = BeautifulSoup(html.text, 'html.parser')
#
# pret = soup.prettify()
#
# f = soup.li
#
# print(f)

# ul = soup.select('div[class="link"]')[0].find_all('ul')
#
# for lt in ul:
#      print(lt)
#      print('1')

#print(soup.select('div[class="link"]'))

soup = BeautifulSoup('<div class="good"><b class="boldest solid" tid="yam">Extremely bold</b></div>', 'lxml')
tag = soup.b
type(tag)
soup.b.string = 'change b content'
di = soup.div
bex = di.b.extract()
print(di)
print(bex)