from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class Wf_Detail(Base):
    __tablename__ = 'wf_detail'
    id = Column(Integer, primary_key=True)
    icon_url = Column(String(255))
    cn_name = Column(String(255))
    en_name = Column(String(32))
    abbreviation = Column(String(32))
    prices_cny = Column(String(50))
    prices_usd = Column(String(50))
    prices_btc = Column(String(50))
    degree = Column(String(50))
    market_cap_cny = Column(String(50))
    market_cap_usd = Column(String(50))
    market_cap_btc = Column(String(50))
    volumn_cny = Column(String(50))
    volumn_usd = Column(String(50))
    volumn_btc = Column(String(50))
    supply_rate = Column(String(50))
    supply = Column(String(50))
    max_supply = Column(String(50))
    website_url = Column(String(255))
    browser_url = Column(String(255))
    white_paper_url = Column(String(255))
    content = Column(Text)


class Wf_Exchange(Base):
    __tablename__ = 'wf_exchange'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    code = Column(String(64))
    logo = Column(String(255))
    transaction = Column(String(50))
    business = Column(String(50))
    website = Column(String(255))
    social_link = Column(String(255))
    nation = Column(String(50))
    numtrading = Column(String(50))
    information = Column(Text)
    pattern = Column(String(50))


class Wf_Market(Base):
    __tablename__ = 'wf_market'
    id = Column(Integer, primary_key=True)
    exchange_id = Column(Integer)
    detail_id = Column(Integer)
    prices_cny = Column(String(32))
    prices_usd = Column(String(32))
    prices_btc = Column(String(32))
    prices_total = Column(String(32))
    last_update_time = Column(String(32))
    exchange_icon_url = Column(String(255))
    degree =Column(String(255))
    volume = Column(String(255))
    hight_cny = Column(String(32))
    low_cny = Column(String(32))
    hight_usd = Column(String(32))
    low_usd = Column(String(32))


class Wf_Mar_List(Base):
    __tablename__ = 'wf_mar_list'
    id = Column(Integer, primary_key=True)
    exchange_id = Column(Integer)
    detail_id = Column(Integer)
    come_from = Column(String(64))
    to = Column(String(64))
    prices_cny = Column(String(64))
    prices_usd = Column(String(64))
    prices_btc = Column(String(64))
    last_update_time = Column(String(64))
    price_total_cny = Column(String(64))
    price_total_usd = Column(String(64))
    price_total_btc = Column(String(64))
    change = Column(String(64))
    exchange_icon_url = Column(String(64))


class Wf_Arc_Exchange(Base):
    __tablename__ = 'wf_arc_exchange'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    url = Column(String(255))
    description = Column(String(255))
    views = Column(Text)
    exchange_id = Column(Integer)
    created_at = Column(String(64))
    updated_at = Column(String(64))

class Wf_Det_Kline(Base):
    __tablename__ = 'wf_det_kline'
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    prices_cny = Column(String(32))
    prices_usd = Column(String(32))
    price_btc = Column(String(32))
    datetimes = Column(DateTime)


class Wf_Mar_Kline(Base):
    __tablename__ = 'wf_mar_kline'
    id = Column(Integer, primary_key=True)
    exchange_id = Column(Integer)
    detail_id = Column(Integer)
    prices_cny = Column(String(32))
    prices_usd = Column(String(32))
    price_btc = Column(String(32))
    datetimes = Column(DateTime)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/pywf')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
