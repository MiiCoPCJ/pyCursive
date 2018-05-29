import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, Enum, DATE, Float, DECIMAL,Boolean,BigInteger
from sqlalchemy.orm import mapper, sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:root@localhost/pywf", encoding='utf-8', \
                       echo=True)

Base = declarative_base()
# 数据表
class Markets(Base):
    __tablename__ = 'markets'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    display_name = Column(String(32))
    home_url = Column(String(32))
    volume = Column(DECIMAL(21,9))
    display_volume = Column(DECIMAL(21,9))
    status = Column(Integer)
    ping = Column(DECIMAL(21,9))
    has_kline = Column(Boolean)
    timestamps = Column(BigInteger)
    inflow_30m = Column(DECIMAL(21,9))
    outflow_30m = Column(DECIMAL(21,9))
    inflow_1h = Column(DECIMAL(21,9))
    outflow_1h = Column(DECIMAL(21,9))
    inflow_1d = Column(DECIMAL(21, 9))
    outflow_1d = Column(DECIMAL(21, 9))
    inflow_1w = Column(DECIMAL(21,9))
    outflow_1w = Column(DECIMAL(21,9))
    def __repr__(self):
        return " name : %s ; display_name : %s " %(self.name, self.display_name)

# 初始化数据表，无的添加
Base.metadata.create_all(engine)
# 实例化，链接数据
Session_class = sessionmaker(bind=engine)
Session = Session_class()