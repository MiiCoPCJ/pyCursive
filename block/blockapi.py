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
from urllib import request,parse
import json

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
    volume_usd = Column(Float(12.9))
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
req = request.Request(url=url,method="GET")
response = request.urlopen(req)

# 获取API的状态
# print(response.status)

symbol_json = json.loads(response.read().decode('utf-8'))

symbol_data = symbol_json['data']


for lt in symbol_data:
    name = lt['name']
    symbol = lt['symbol']
    volume_usd = lt['volume_usd']
    alias = lt['alias']
    status = lt['status']
    if status == 'enable':
        status = 1;
    # 查询是否已存在
    result = Session.query(Symbols).filter_by(name=name).first()
    # 判断结果
    if result is None:
        Session.add(Symbols(name=name, symbol=symbol, volume_usd=volume_usd, \
                            alias=alias, status=status))
        Session.commit()
        print('%s insert database')
        print('-----------------------------------')



# if response.status == 200:

