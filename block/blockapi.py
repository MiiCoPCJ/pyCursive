import time
# 队列
import sched
# 链接数据库
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, Enum, DATE, Float, DECIMAL
from sqlalchemy.orm import mapper, sessionmaker, relationship
# 获取API
from urllib import request,parse,error
import json
# 循环执行
import time
import sched

# 链接数据库
engine = create_engine("mysql+pymysql://root:root@localhost/pywf", encoding='utf-8', \
                       echo=True)

# 初始化
Base = declarative_base()
# 数据表
class Symbols(Base):
    __tablename__ = 'symbols'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    symbol = Column(String(10))
    volume_usd = Column(DECIMAL(21,9))
    alias = Column(String(250))
    status = Column(Integer)
    def __repr__(self):
        return " name : %s ; symbol : %s ; volume_usd : %s" %(self.name, self.symbol, self.volume_usd)

# 初始化数据表，无的添加
Base.metadata.create_all(engine)
# 实例化，链接数据
Session_class = sessionmaker(bind=engine)
Session = Session_class()


# API获取数据
url ='https://data.block.cc/api/v1/symbols'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'
}

# 获取symbol的函数
def get_symbol():
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
        f = open("symbol.txt","w")
        for lt in symbol_data:
            # 转换为str
            f.write(str(lt)+"\n")
        f.close()

        # 逐行读取
        f = open("symbol.txt","r")
        line = f.readline()
        while line:
            # 转换为dict
            lt = eval(line)
            # 数据处理
            name = lt['name']
            symbol = lt['symbol']
            volume_usd = lt['volume_usd']
            alias = ",".join(lt['alias'])
            status = lt['status']
            if status == 'enable':
                status = 1;
            else:
                status = 0;

            # 查询是否已存在
            result = Session.query(Symbols).filter_by(name=name).first()
            # 判断结果
            if result is None:
                Session.add(Symbols(name=name, symbol=symbol, volume_usd=volume_usd, \
                                    alias=alias, status=status))
                Session.commit()
                print('%s insert database' %name)
                print('-----------------------------------')
            else:
                result.volume_usd = volume_usd
                result.alias = alias
                result.status = status
                Session.commit()
                print('%s update' %name)
                print('-----------------------------------')
            line = f.readline()


        Session.close()
    else:
        print("response status %s" %response.status)
        exit()

# 间隔60s循环执行
schedule = sched.scheduler(time.time, time.sleep)

# 方法一
# def func(fun, inc):
#     schedule.enter(inc, 0, func, (inc,))
#     print("-----Start spider symbol API %s -----" %time.time())
#     fun()
#
# if __name__ == '__main__':
#     schedule.enter(10, 0, func, (get_symbol, 60))
#     schedule.run()

# 方法二
def perform_command(fun, inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (fun, inc))
    print("----- Start spider symbol API %s -----" % time.time())
    fun()


def timming_exe(fun, inc=60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (fun, inc))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

if __name__ == '__main__':
    get_symbol()
    # try:
    #     timming_exe(get_symbol, inc=10)
    # except KeyboardInterrupt as e:
    #     pass
