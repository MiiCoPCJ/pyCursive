import requests
from urllib.parse import urlencode
from time import sleep
from spider.wf.created_session.created_session import *
from spider.wf.get_time import get_time

coin_type = ['btc', 'eth','bcd', 'elf',
             'ink', 'trx', 'aidoc', 'pst',
             'ddd', 'eko', 'pra', 'uc',
             'bch', 'bcx', 'etc', 'ltc',
             'sbtc', 'qtum', 'neo', 'nem',
             'hsr', 'xrp', 'dash', 'xmr',
             'eos', 'omg', 'iota', 'zec',
             'waves', 'btg', 'bts', 'xlm',
             'lsk']
base_url = 'https://api.jinse.com/v4/market/web/list?'
params = {
        'type': '1',
        'currency_type': '',
        'currency': ''
    }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}


def get_base_market():
    session = DBSession()
    url = base_url + urlencode(params)
    respone_cny = requests.get(url=url, headers=headers)
    data_json = respone_cny.json()
    for dt in data_json:
        exchange_name = dt.get('exchange_name')
        exchange_code = dt.get('exchange_code')
        currency_name = dt.get('currency_name')
        exchange_icon_url = dt.get('logo')
        domain = dt.get('domain')

        if session.query(Wf_Exchange).filter_by(code=exchange_code).first() is None:
            print('交易所不存在')
            pass
        else:
            exchange_id = session.query(Wf_Exchange).filter_by(code=exchange_code).first().id

            if session.query(Wf_Detail).filter_by(abbreviation=currency_name).first() is None:
                print('币种不存在')
                pass
            else:
                detail_id = session.query(Wf_Detail).filter_by(abbreviation=currency_name).first().id

                if session.query(Wf_Market).filter_by(exchange_id=exchange_id).filter_by(detail_id=detail_id).first() is None:
                    session.add(Wf_Market(exchange_id=exchange_id, detail_id=detail_id,
                                          exchange_icon_url=exchange_icon_url))
                    session.commit()
    session.close()

    print('------------------------------------------------------------------------------------------')


def get_time_market():
    try:
        for coin in coin_type:
            params['currency_type'] = coin
            last_update_time = get_time()
            session = DBSession()
            params['currency'] = 'CNY'
            url = base_url + urlencode(params)
            respone_cny = requests.get(url=url, headers=headers)
            params['currency']='USD'
            url = base_url + urlencode(params)
            respone_usd = requests.get(url=url, headers=headers)
            data_json_cny = respone_cny.json()
            data_json_usd = respone_usd.json()
            for dt_cny, dt_usd in zip(data_json_cny, data_json_usd):
                currency_name = dt_cny.get('currency_name')
                exchange_code = dt_cny.get('exchange_code')
                prices_cny = dt_cny.get('last')
                hight_cny = dt_cny.get('high')
                low_cny = dt_cny.get('low')
                degree = dt_cny.get('degree')
                volume = dt_cny.get('vol')
                line_cny = dt_cny.get('line')

                prices_usd = dt_usd.get('last')
                hight_usd = dt_usd.get('high')
                low_usd = dt_usd.get('low')
                line_usd = dt_usd.get('line')

                if session.query(Wf_Detail).filter_by(abbreviation=currency_name).first() is None:
                    print('币种不存在')
                    pass
                else:
                    detail_id = session.query(Wf_Detail).filter_by(abbreviation=currency_name).first().id

                    if session.query(Wf_Exchange).filter_by(code=exchange_code).first() is None:
                        print('交易所不存在')
                        pass
                    else:
                        exchange_id = session.query(Wf_Exchange).filter_by(code=exchange_code).first().id

                        data_line = session.query(Wf_Market).filter_by(exchange_id=exchange_id).filter_by(detail_id=detail_id).first()

                        data_line.prices_cny = prices_cny
                        data_line.hight_cny = hight_cny
                        data_line.low_cny = low_cny
                        data_line.hight_usd = hight_usd
                        data_line.low_usd = low_usd
                        data_line.degree = degree
                        data_line.volume = volume
                        data_line.prices_usd = prices_usd
                        data_line.last_update_time = last_update_time

                        mar_kline = Wf_Mar_Kline()
                        mar_kline.exchange_id = exchange_id
                        mar_kline.detail_id = detail_id
                        mar_kline.prices_cny = prices_cny
                        mar_kline.prices_usd = prices_usd
                        mar_kline.datetimes = last_update_time
                        session.add(mar_kline)

                        session.commit()
                        print('*************************************************************')

            session.close()
    except requests.ConnectionError as e:
        sleep(60)
        pass


if __name__ == '__main__':
    get_time_market()


