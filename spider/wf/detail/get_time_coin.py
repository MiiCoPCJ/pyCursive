from bs4 import BeautifulSoup
import requests
from time import sleep
from spider.wf.created_session.created_session import *
from urllib.parse import urlencode
from spider.wf.get_time import get_time

base_url = 'https://www.jinse.com/coin?'
params = {
        'page': '1',
        'currency': ''
    }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}


def get_time_coin():
    try:
        time = get_time()
        session = DBSession()
        for i in range(1, 15):
            params['page'] = i
            params['currency'] = 'CNY'
            url = base_url + urlencode(params)
            respone_cny = requests.get(url=url, headers=headers)
            params['currency'] = 'USD'
            url = base_url + urlencode(params)
            respone_usd = requests.get(url=url, headers=headers)
            params['currency'] = 'BTC'
            url = base_url + urlencode(params)
            respone_btc = requests.get(url=url, headers=headers)
            sleep(0.2)

            soup = BeautifulSoup(respone_cny.text, 'lxml')
            ul_list_cny = soup.select('div[class="link"]')[0].find_all('ul')

            soup = BeautifulSoup(respone_usd.text, 'lxml')
            ul_list_usd = soup.select('div[class="link"]')[0].find_all('ul')

            soup = BeautifulSoup(respone_btc.text, 'lxml')
            ul_list_btc = soup.select('div[class="link"]')[0].find_all('ul')

            for ul_cny, ul_usd, ul_btc in zip(ul_list_cny, ul_list_usd, ul_list_btc):
                data_cny = list(ul_cny.strings)
                en_name = str(data_cny[3])
                prices_cny = str(data_cny[5])
                degree = str(data_cny[7])
                market_cap_cny = str(data_cny[11])
                volumn_cny = str(data_cny[9])
                supply_rate = str(data_cny[15])

                data_usd = list(ul_usd.strings)
                prices_usd = str(data_usd[5])
                market_cap_usd = str(data_usd[11])
                volumn_usd = str(data_usd[9])

                data_btc = list(ul_btc.strings)
                prices_btc = str(data_btc[5])
                market_cap_btc = str(data_btc[11])
                volumn_btc = str(data_btc[9])

                if session.query(Wf_Detail).filter_by(en_name=en_name).first() is not None:
                    data_line = session.query(Wf_Detail).filter_by(en_name=en_name).first()
                    detail_id = data_line.id
                    data_line.prices_cny = prices_cny
                    data_line.degree = degree
                    data_line.market_cap_cny = market_cap_cny
                    data_line.volumn_cny = volumn_cny
                    data_line.supply_rate = supply_rate

                    data_line.prices_usd = prices_usd
                    data_line.market_cap_usd = market_cap_usd
                    data_line.volumn_usd = volumn_usd

                    data_line.prices_btc = prices_btc
                    data_line.market_cap_btc = market_cap_btc
                    data_line.volumn_btc = volumn_btc

                    session.flush()
                    #------------------------------------------------------------------------
                    det_kline = Wf_Det_Kline()
                    det_kline.detail_id = detail_id
                    det_kline.prices_cny = prices_cny
                    det_kline.prices_usd = prices_usd
                    det_kline.price_btc = prices_btc
                    det_kline.datetimes = time
                    session.add(det_kline)
                    session.commit()

                else:
                    print('币种不存在')

                print(en_name)
                print(prices_cny)
                print(degree)
                print(market_cap_cny)
                print(volumn_cny)
                print(supply_rate)
                print('----------------')

        session.close()
    except requests.ConnectionError as e:
        sleep(60)
        pass

if __name__ == '__main__':
    get_time_coin()
