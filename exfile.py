from bs4 import BeautifulSoup
import requests
from time import sleep
from spider.wf.created_session.created_session import *
from spider.wf.detail.coin_info import page_url_handler
import os

result_list = ['https://www.jinse.com/exchange/bitfinex', 'https://www.jinse.com/exchange/okex', 'https://www.jinse.com/exchange/binance', 'https://www.jinse.com/exchange/huobipro', 'https://www.jinse.com/exchange/bitflyer', 'https://www.jinse.com/exchange/gdax', 'https://www.jinse.com/exchange/bitstamp', 'https://www.jinse.com/exchange/quoine', 'https://www.jinse.com/exchange/bithumb', 'https://www.jinse.com/exchange/upbit', 'https://www.jinse.com/exchange/kraken', 'https://www.jinse.com/exchange/zaif', 'https://www.jinse.com/exchange/fisco', 'https://www.jinse.com/exchange/gemini', 'https://www.jinse.com/exchange/btcbox', 'https://www.jinse.com/exchange/btcc', 'https://www.jinse.com/exchange/hitbtc', 'https://www.jinse.com/exchange/lbank', 'https://www.jinse.com/exchange/bittrex', 'https://www.jinse.com/exchange/itbit', 'https://www.jinse.com/exchange/bit-z', 'https://www.jinse.com/exchange/poloniex', 'https://www.jinse.com/exchange/coinbene', 'https://www.jinse.com/exchange/coinone', 'https://www.jinse.com/exchange/zb-com', 'https://www.jinse.com/exchange/bitbank', 'https://www.jinse.com/exchange/korbit', 'https://www.jinse.com/exchange/coinegg', 'https://www.jinse.com/exchange/cex-io', 'https://www.jinse.com/exchange/coinsbank', 'https://www.jinse.com/exchange/exx', 'https://www.jinse.com/exchange/livecoin', 'https://www.jinse.com/exchange/wex', 'https://www.jinse.com/exchange/exmo', 'https://www.jinse.com/exchange/bitbay', 'https://www.jinse.com/exchange/lakebtc', 'https://www.jinse.com/exchange/paribu', 'https://www.jinse.com/exchange/gopax', 'https://www.jinse.com/exchange/tidex', 'https://www.jinse.com/exchange/gate-io', 'https://www.jinse.com/exchange/bibox', 'https://www.jinse.com/exchange/bitinka', 'https://www.jinse.com/exchange/yobit', 'https://www.jinse.com/exchange/luno', 'https://www.jinse.com/exchange/coolcoin', 'https://www.jinse.com/exchange/btc-markets', 'https://www.jinse.com/exchange/bitcoin-indonesia', 'https://www.jinse.com/exchange/btcturk', 'https://www.jinse.com/exchange/getbtc', 'https://www.jinse.com/exchange/quadrigacx', 'https://www.jinse.com/exchange/exrates', 'https://www.jinse.com/exchange/negocie-coins', 'https://www.jinse.com/exchange/kucoin', 'https://www.jinse.com/exchange/xbtce', 'https://www.jinse.com/exchange/bcc-exchange', 'https://www.jinse.com/exchange/coinfloor', 'https://www.jinse.com/exchange/bl3p', 'https://www.jinse.com/exchange/bitgrail', 'https://www.jinse.com/exchange/bx-thailand', 'https://www.jinse.com/exchange/qryptos', 'https://www.jinse.com/exchange/bitonic', 'https://www.jinse.com/exchange/coinsquare', 'https://www.jinse.com/exchange/oex', 'https://www.jinse.com/exchange/liqui', 'https://www.jinse.com/exchange/dsx', 'https://www.jinse.com/exchange/btctrade-im', 'https://www.jinse.com/exchange/bitmarket', 'https://www.jinse.com/exchange/cryptopia', 'https://www.jinse.com/exchange/rightbtc', 'https://www.jinse.com/exchange/topbtc', 'https://www.jinse.com/exchange/bcex', 'https://www.jinse.com/exchange/foxbit', 'https://www.jinse.com/exchange/bitso', 'https://www.jinse.com/exchange/btc-alpha', 'https://www.jinse.com/exchange/aex', 'https://www.jinse.com/exchange/mercado-bitcoin', 'https://www.jinse.com/exchange/okcoin-intl', 'https://www.jinse.com/exchange/bitmex', 'https://www.jinse.com/exchange/neraexpro', 'https://www.jinse.com/exchange/cointiger', 'https://www.jinse.com/exchange/trade-by-trade', 'https://www.jinse.com/exchange/zebpay', 'https://www.jinse.com/exchange/simex', 'https://www.jinse.com/exchange/c2cx', 'https://www.jinse.com/exchange/omicrex', 'https://www.jinse.com/exchange/fatbtc', 'https://www.jinse.com/exchange/mbaex', 'https://www.jinse.com/exchange/coinexchange', 'https://www.jinse.com/exchange/bithesap', 'https://www.jinse.com/exchange/octaex', 'https://www.jinse.com/exchange/coinroom', 'https://www.jinse.com/exchange/otcbtc', 'https://www.jinse.com/exchange/ooobtc', 'https://www.jinse.com/exchange/tidebit', 'https://www.jinse.com/exchange/etherdelta', 'https://www.jinse.com/exchange/bancor-network', 'https://www.jinse.com/exchange/coss', 'https://www.jinse.com/exchange/coinut', 'https://www.jinse.com/exchange/bigone', 'https://www.jinse.com/exchange/oasisdex', 'https://www.jinse.com/exchange/coinfalcon', 'https://www.jinse.com/exchange/independent-reserve', 'https://www.jinse.com/exchange/mercatox', 'https://www.jinse.com/exchange/chaoex', 'https://www.jinse.com/exchange/koinex', 'https://www.jinse.com/exchange/allcoin', 'https://www.jinse.com/exchange/idex', 'https://www.jinse.com/exchange/therocktrading', 'https://www.jinse.com/exchange/coinnest', 'https://www.jinse.com/exchange/koineks', 'https://www.jinse.com/exchange/litebit', 'https://www.jinse.com/exchange/cobinhood', 'https://www.jinse.com/exchange/vebitcoin', 'https://www.jinse.com/exchange/cryptonex', 'https://www.jinse.com/exchange/unocoin', 'https://www.jinse.com/exchange/bitbns', 'https://www.jinse.com/exchange/ripplefox', 'https://www.jinse.com/exchange/gatehub', 'https://www.jinse.com/exchange/ripple-china', 'https://www.jinse.com/exchange/mr-exchange', 'https://www.jinse.com/exchange/bitsane', 'https://www.jinse.com/exchange/altcoin-trader', 'https://www.jinse.com/exchange/triple-dice-exchange', 'https://www.jinse.com/exchange/bits-blockchain', 'https://www.jinse.com/exchange/coinrail', 'https://www.jinse.com/exchange/cryptomate', 'https://www.jinse.com/exchange/bitflip', 'https://www.jinse.com/exchange/rippex', 'https://www.jinse.com/exchange/abucoins', 'https://www.jinse.com/exchange/stellar-decentralized-exchange', 'https://www.jinse.com/exchange/sistemkoin', 'https://www.jinse.com/exchange/ovis', 'https://www.jinse.com/exchange/kuna', 'https://www.jinse.com/exchange/stellarport', 'https://www.jinse.com/exchange/coinbe', 'https://www.jinse.com/exchange/bitlish', 'https://www.jinse.com/exchange/surbtc', 'https://www.jinse.com/exchange/braziliex', 'https://www.jinse.com/exchange/bit2c', 'https://www.jinse.com/exchange/cryptobridge', 'https://www.jinse.com/exchange/trade-satoshi', 'https://www.jinse.com/exchange/acx', 'https://www.jinse.com/exchange/bittylicious', 'https://www.jinse.com/exchange/stocks-exchange', 'https://www.jinse.com/exchange/southxchange', 'https://www.jinse.com/exchange/gatecoin', 'https://www.jinse.com/exchange/qbtc', 'https://www.jinse.com/exchange/bitholic', 'https://www.jinse.com/exchange/crex24', 'https://www.jinse.com/exchange/btc-trade-ua', 'https://www.jinse.com/exchange/koinim', 'https://www.jinse.com/exchange/localtrade', 'https://www.jinse.com/exchange/waves-dex', 'https://www.jinse.com/exchange/c-cex', 'https://www.jinse.com/exchange/okcoin-cn', 'https://www.jinse.com/exchange/bleutrade', 'https://www.jinse.com/exchange/openledger', 'https://www.jinse.com/exchange/coingi', 'https://www.jinse.com/exchange/bitmaszyna', 'https://www.jinse.com/exchange/bitkonan', 'https://www.jinse.com/exchange/tdax', 'https://www.jinse.com/exchange/cryptox', 'https://www.jinse.com/exchange/coinsmarkets', 'https://www.jinse.com/exchange/nix-e', 'https://www.jinse.com/exchange/dgtmarket', 'https://www.jinse.com/exchange/freiexchange', 'https://www.jinse.com/exchange/tux-exchange', 'https://www.jinse.com/exchange/tradebytrade', 'https://www.jinse.com/exchange/lykke-exchange', 'https://www.jinse.com/exchange/nanex', 'https://www.jinse.com/exchange/iquant', 'https://www.jinse.com/exchange/tradeogre', 'https://www.jinse.com/exchange/crxzone', 'https://www.jinse.com/exchange/cryptohub', 'https://www.jinse.com/exchange/c-patex', 'https://www.jinse.com/exchange/cfinex', 'https://www.jinse.com/exchange/latoken', 'https://www.jinse.com/exchange/rfinex', 'https://www.jinse.com/exchange/forkdelta', 'https://www.jinse.com/exchange/idax', 'https://www.jinse.com/exchange/ddex', 'https://www.jinse.com/exchange/paradex', 'https://www.jinse.com/exchange/cryptomarket', 'https://www.jinse.com/exchange/stronghold', 'https://www.jinse.com/exchange/bisq', 'https://www.jinse.com/exchange/token-store', 'https://www.jinse.com/exchange/coinlink', 'https://www.jinse.com/exchange/rudex', 'https://www.jinse.com/exchange/bitshares-asset-exchange', 'https://www.jinse.com/exchange/alcurex', 'https://www.jinse.com/exchange/dc-ex', 'https://www.jinse.com/exchange/heat-wallet', 'https://www.jinse.com/exchange/cryptoderivatives', 'https://www.jinse.com/exchange/nxt-asset-exchange', 'https://www.jinse.com/exchange/omni-dex', 'https://www.jinse.com/exchange/nocks', 'https://www.jinse.com/exchange/guldentrader', 'https://www.jinse.com/exchange/counterparty-dex', 'https://www.jinse.com/exchange/burst-asset-exchange', 'https://www.jinse.com/exchange/leoxchange', 'https://www.jinse.com/exchange/isx', 'https://www.jinse.com/exchange/tcc-exchange', 'https://www.jinse.com/exchange/excambriorex', 'https://www.jinse.com/exchange/ore-bz', 'https://www.jinse.com/exchange/virtacoinworld', 'https://www.jinse.com/exchange/aidos-market', 'https://www.jinse.com/exchange/fargobase', 'https://www.jinse.com/exchange/coinrate', 'https://www.jinse.com/exchange/infinitycoin-exchange']
error_list = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
img_dir = r'C:\Users\Administrator\PycharmProjects\untitled\spider\wf\wf_img\exchange_img'


def find_exchange(base_url):
    respone = requests.get(url=base_url, headers=headers)
    soup = BeautifulSoup(respone.text, 'lxml')
    url_list = soup.select('div[class="link"]')[0].find_all('a')
    for dt in url_list:
        exchange_url = dt['href']
        print(dt['href'])
        if exchange_url not in result_list:
            result_list.append(exchange_url)


def exchange_info_handler(url):
    social_link = ''
    website = ''
    information = ''
    respone = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(respone.text, 'lxml')
    info = soup.select('div[class="name font24 center left"]')[0]
    print(info.find('img')['src'].split('/')[-1])
    print(info.find('img').attrs)
    logo_url = info.img['src'][:-1]
    logo_name = logo_url.split('/')[-1]
    os.chdir(img_dir)
    files = []
    for root, sub_dirs, files in os.walk(img_dir):
        files = files
    exit()
    if logo_name not in files:
        respone_img = requests.get(logo_url)
        img = respone_img.content
        with open(logo_name, 'wb') as f:
            f.write(img)
    else:
        print('图标已经存在')


    title = info.img['alt']
    link = soup.select('div[class="list right font16"]')[0]
    social = soup.select('li[class="social"]')[0].find_all('a')
    content = soup.select('div[class="font12 line26"]')[0]

    for dt in content.stripped_strings:
        information = information+dt
    if '隐藏更多' in information:
        information = information.replace('隐藏更多', '')

    for dt in link:
        if '官网' in str(dt):
            website = dt.a['href']
        elif '国家' in str(dt):
            nation = dt.string.split('：')[-1]
        elif '交易对' in str(dt):
            numtrading = dt.string.split('：')[-1]
        elif '交易模式' in str(dt):
            pattern = dt.string.split('：')[-1].strip('')

    for dt in social:
        link = dt['href']
        if social_link == '':
            social_link = link
        else:
            social_link = social_link+','+link

    print(title)
    print(logo_name)
    print(social_link)
    print(website)
    print(nation)
    print(numtrading)
    print(pattern)
    print(information)
    result = {'title':title, 'logo': logo_name, 'social_link':social_link,
              'website':website, 'nation':nation, 'numtrading':numtrading,
              'pattern':pattern, 'information':information}
    return result

def exchange_price_handler(url):
    respone = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(respone.text, 'lxml')
    price = soup.select('div["class=dey"]')[0].stripped_strings
    for dt in price:
        if 'BTC' in dt:
            transaction = dt
        elif '¥' in dt:
            business = dt

    print(transaction)
    print(business)
    result = {'transaction':transaction, 'business':business}
    return result


def main():
    session = DBSession()
    #
    # try:
    #     for i in range(1, 14):
    #         exchange_url_list, exchange_url_list_403 = page_url_handler(page_num=i)
    #         for base_url in exchange_url_list:
    #             find_exchange(base_url=base_url)
    #             sleep(0.1)
    # except requests.ConnectionError as e:
    #     error_list.append(e)
    # print(result_list)
    # print(len(result_list))
    # print(error_list)

    os.chdir(r'C:\Users\Administrator\PycharmProjects\untitled\spider\wf\exchange')
    with open('exchange_221.txt', 'r') as f:
        exchange_url_list = f.read().split(',')
    for url in result_list:
        url = url.replace('\'', '')
        try:
            exchange_info = exchange_info_handler(url)
            exchange_price = exchange_price_handler(url)
            sleep(0.15)
            code = url.split('/')[-1]
            if session.query(Wf_Exchange).filter_by(title=exchange_info['title']).first() is None:
                session.add(Wf_Exchange(title=exchange_info['title'], code=code, logo=exchange_info['logo'],
                                        transaction=exchange_price['transaction'], business=exchange_price['business'],
                                        website=exchange_info['website'], social_link=exchange_info['social_link'],
                                        nation=exchange_info['nation'],
                                        pattern=exchange_info['pattern'],
                                        numtrading=exchange_info['numtrading'], information=exchange_info['information']))
                session.commit()
        except requests.ConnectionError as e:
            error_list.append(e)

    print(error_list)
    session.close()


if __name__ == '__main__':
    main()