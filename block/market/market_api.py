from urllib import request,parse,error
import json

# 导入
import block.market.market_model

url ='https://data.block.cc/api/v1/markets'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'
}

Session = block.market.market_model.Session
Markets = block.market.market_model.Markets



def get_market():
    name = ''
    display_name = ''
    home_url = ''
    volume = ''
    display_volume = ''
    status = ''
    ping = ''
    has_kline = ''
    timestamps = ''
    inflow_30m = ''
    outflow_30m = ''
    inflow_1h = ''
    outflow_1h = ''
    inflow_1d = ''
    outflow_1d = ''
    inflow_1w = ''
    outflow_1w = ''

    try:
        req = request.Request(url=url,method="GET")
        response = request.urlopen(req)
    except error.URLError as e:
        print(e.reason)
        exit()
    # 获取API的状态
    # print(response.status)

    if response.status == 200:
        symbol_json = json.loads(response.read().decode('utf-8'))

        symbol_data = symbol_json['data']

        # 存入txt中
        f = open("market.txt","w")
        for lt in symbol_data:
            # 转换为str
            f.write(str(lt)+"\n")
        f.close()

        # 逐行读取
        f = open("market.txt","r")
        line = f.readline()
        while line:
            # 转换为dict
            lt = eval(line)
            # 数据处理
            for key in lt:
                key = lt[key]

            # name = lt['name']
            # display_name = lt['display_name']
            # home_url = lt['home_url']
            # volume = lt['volume']
            # display_volume = lt['display_volume']
            # status = lt['status']
            # ping = lt['ping']
            # has_kline = lt['has_kline']
            # timestamps = lt['timestamps']
            # inflow_30m = lt['inflow_30m']
            # outflow_30m = lt['outflow_30m']
            # inflow_1h = lt['inflow_1h']
            # outflow_1h = lt['outflow_1h']
            # inflow_1d = lt['inflow_1d']
            # outflow_1d = lt['outflow_1d']
            # inflow_1w = lt['inflow_1w']
            # outflow_1w = lt['outflow_1w']


            if status is not None:
                if status == 'enable':
                    status = 1;
                else:
                    status = 0;
            print(status)
            exit()
            # 查询是否已存在
            result = Session.query(Markets).filter_by(name=name).first()
            # 判断结果
            if result is None:
                market = Markets(name=name, display_name=display_name,home_url=home_url, status=status,
                                    volume=volume,display_volume=display_volume,ping=ping,has_kline=has_kline,
                                    timestamps=timestamps,inflow_30m=inflow_30m,outflow_30m=outflow_30m,
                                    inflow_1h=inflow_1h,outflow_1h=outflow_1h,inflow_1d=inflow_1d,outflow_1d=outflow_1d,
                                    inflow_1w=inflow_1w,outflow_1w=outflow_1w)
                Session.add( market )
                Session.commit()
                print('%s insert database' %name)
                print('-----------------------------------')
            else:
                result.status = status
                result.volume = volume
                result.display_volume = display_volume
                result.ping = ping
                result.has_kline = has_kline
                result.timestamps = timestamps
                result.inflow_30m = inflow_30m
                result.outflow_30m = outflow_30m
                result.inflow_1h = inflow_1h
                result.outflow_1h = outflow_1h
                result.inflow_1d = inflow_1d
                result.outflow_1d = outflow_1d
                result.inflow_1w = inflow_1w
                result.outflow_1w = outflow_1w
                Session.commit()
                print('%s update' %name)
                print('-----------------------------------')
            line = f.readline()


        Session.close()
    else:
        print("response status %s" %response.status)
        exit()