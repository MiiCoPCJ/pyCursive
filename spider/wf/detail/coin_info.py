from bs4 import BeautifulSoup
import requests
from spider.wf.created_session.created_session import *
from time import sleep
import os

coin_url_list = []
coin_url_list_403 = []
error_list = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
img_dir = 'F:\work\spider\wf\wf_img\coin_img'


def page_url_handler(page_num):
    result_list = []
    result_list_403 =[]
    base_url = 'http://www.jinse.com/coin?page='
    respone = requests.get(url=base_url+str(page_num), headers=headers)
    soup = BeautifulSoup(respone.text, 'lxml')
    url_list = soup.select('div[class="link"]')[0].find_all('a')
    for dt in url_list:
        url = 'http://www.jinse.com'+dt['data-source']
        respone_t = requests.get(url=url, headers=headers)
        if respone_t.status_code != 200:
            if url not in coin_url_list_403:
                coin_url_list_403.append(url)
                result_list_403.append(url)
        else:
            print(url)
            if url not in coin_url_list:
                coin_url_list.append(url)
                result_list.append(url)
    return result_list, result_list_403


def coin_info_handler(url):
    respone_1 = requests.get(url=url, headers=headers)
    soup_1 = BeautifulSoup(respone_1.text, 'lxml')
    respone_2 = requests.get(url=url+'/basic', headers=headers)
    soup_2 = BeautifulSoup(respone_2.text, 'lxml')

    icon_url = soup_1.select('div[class="name font20 fontw"]')[0].img['src'][:-1]
    icon_name = icon_url.split('/')[-1]
    os.chdir(img_dir)
    files = []
    for root, sub_dirs, files in os.walk(img_dir):
        files = files
    if icon_name not in files:
        respone_img = requests.get(icon_url)
        img = respone_img.content
        with open(icon_name, 'wb') as f:
            f.write(img)
    else:
        print('图标已经存在')

    website_url = ''
    browser_url = ''
    white_paper_url = ''
    content = ''
    info = soup_1.select('div[class="mar clearfix"]')[0].stripped_strings
    link = soup_1.select('div[class="pric right font16 line40"]')[0].find_all('li')
    post = soup_2.select('div[class="bgc padding font16 line36 brief"]')[0].stripped_strings

    for info_dt in info:
        if '中文' in info_dt:
            cn_name = info_dt.split('：')[-1]
        elif '英文' in info_dt:
            en_name = info_dt.split('：')[-1]
        elif '简称' in info_dt:
            abbreviation = info_dt.split('：')[-1]
        elif '流通数量' in info_dt:
            supply = info_dt.split('：')[-1]
        elif '发行总量' in info_dt:
            max_supply = info_dt.split('：')[-1]

    for link_dt in link:
        for i in link_dt.find_all('a'):
            if '官网' in str(i):
                if website_url is '':
                    website_url = i['href']
                else:
                    website_url = website_url+','+i['href']
            elif '浏览器' in str(i):
                if browser_url is'':
                    browser_url = i['href']
                else:
                    browser_url = browser_url+','+i['href']
            elif '点击进入' in str(i):
                white_paper_url = i['href']

    for content_dt in post:
        content = content+content_dt
    reslut = {'icon_url':icon_name, 'cn_name':cn_name, 'en_name':en_name, 'abbreviation':abbreviation, 'supply':supply,
              'max_supply':max_supply, 'website_url':website_url, 'browser_url':browser_url,
              'white_paper_url':white_paper_url, 'content':content}
    return reslut


def coin_price_handler(url):
    respone_CNY = requests.get(url=url+'?currency=CNY', headers=headers)
    soup_CNY = BeautifulSoup(respone_CNY.text, 'lxml')
    respone_USD = requests.get(url=url+'?currency=USD', headers=headers)
    soup_USD = BeautifulSoup(respone_USD.text, 'lxml')
    respone_BTC = requests.get(url=url+'?currency=BTC', headers=headers)
    soup_BTC = BeautifulSoup(respone_BTC.text, 'lxml')

    data_CNY = soup_CNY.select('div[class="pric left font16"]')
    data_USD = soup_USD.select('div[class="pric left font16"]')
    data_BTC = soup_BTC.select('div[class="pric left font16"]')

    for dt_CNY in data_CNY:
        for i in dt_CNY:
            if 'font36 fontw marb' in str(i):
                prices_cny = i.string
            elif 'font36 fontw green marb' in str(i):
                degree = i.string
            elif '市值' in str(i):
                market_cap_cny = i.string.split('：')[-1]
            elif '成交额' in str(i):
                volumn_cny = i.string.split('：')[-1]

    for dt_USD in data_USD:
        for i in dt_USD:
            if 'font36 fontw marb' in str(i):
                prices_usd = i.string
            elif '市值' in str(i):
                market_cap_usd = i.string.split('：')[-1]
            elif '成交额' in str(i):
                volumn_usd = i.string.split('：')[-1]

    for dt_BTC in data_BTC:
        for i in dt_BTC:
            if 'font36 fontw marb' in str(i):
                prices_btc = i.string
            elif '市值' in str(i):
                market_cap_btc = i.string.split('：')[-1]
            elif '成交额' in str(i):
                volumn_btc = i.string.split('：')[-1]

    result = {'prices_cny':str(prices_cny), 'prices_usd':str(prices_usd), 'prices_btc':str(prices_btc),
              'market_cap_cny':str(market_cap_cny), 'market_cap_usd':str(market_cap_usd), 'market_cap_btc':str(market_cap_btc),
              'volumn_cny':str(volumn_cny), 'volumn_usd':str(volumn_usd), 'volumn_btc':str(volumn_btc),
              'degree':str(degree)}
    return result

def main():
    session = DBSession()
    # try:
    #     for i in range(1, 14):
    #        page_url_handler(page_num=i)
    # except requests.ConnectionError as e:
    #     error_list.append(e.strerror)
    #
    # print(coin_url_list)
    # print(len(coin_url_list))
    # print(coin_url_list_403)
    # print(len(coin_url_list_403))
    # print(len(error_list))
    # print(error_list)

    os.chdir('F:\work\spider\wf\detail')
    with open('coin_1247.txt', 'r') as f:
        coin_url_list = f.read().split(',')
    for url in coin_url_list:
        url = url.replace('\'', '')
        try:
            coin_info = coin_info_handler(url)
            coin_price = coin_price_handler(url)
            sleep(0.5)
            session.add(Wf_Detail(icon_url=coin_info['icon_url'], cn_name=coin_info['cn_name'], en_name=coin_info['en_name'],
                                  abbreviation=coin_info['abbreviation'],
                                  prices_cny=coin_price['prices_cny'], prices_usd=coin_price['prices_usd'],
                                  prices_btc=coin_price['prices_btc'],
                                  degree=coin_price['degree'],
                                  market_cap_cny=coin_price['market_cap_cny'], market_cap_usd=coin_price['market_cap_usd'],
                                  market_cap_btc=coin_price['market_cap_btc'],
                                  volumn_cny=coin_price['volumn_cny'], volumn_usd=coin_price['volumn_usd'],
                                  volumn_btc=coin_price['volumn_btc'],
                                  supply_rate=None, supply=coin_info['supply'], max_supply=coin_info['max_supply'],
                                  website_url=coin_info['website_url'], browser_url=coin_info['browser_url'],
                                  white_paper_url=coin_info['white_paper_url'],
                                  content=coin_info['content']))
            session.commit()

            print(coin_info)
            print(coin_price)
        except requests.ConnectionError as e:
            error_list.append(e)

    print(error_list)
    session.close()


if __name__ == '__main__':
    main()