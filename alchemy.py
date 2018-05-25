import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, Enum, DATE
from sqlalchemy.orm import mapper, sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:root@localhost/pywf", encoding='utf-8', \
                       echo=True)

#第一种方法

Base = declarative_base()

class User(Base):
    __tablename__ = 'al_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    def __repr__(self):
        return "[%s name: %s]" %(self.id,self.name)

#Base.metadata.create_all(engine)

#第二种方法

metadata = MetaData()

al_user_2 = Table('al_user_2', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )

class Al_User_2(object):
    def __init__(self,id, name, fullname, password):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(Al_User_2, al_user_2)
metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

# user_obj = User(name='zend',password='123')
# print(user_obj.name,user_obj)
#
# Session.add(user_obj)
# print(user_obj.id, user_obj.name)
#
# Session.commit()

#多值添加
# data01 = User(name='per', password='zer')
# data02 = User(name='good', password='east')
# data03 = User(name='zun', password='yang')
#
# Session.add_all([data01,data02,data03])
# Session.commit()

#查询
# my_user = Session.query(User).filter_by(name='zend').first()
# print(my_user.id,my_user.password)

# search_more = Session.query(User).filter(User.id>=2).filter(User.id<5).all()
# print(search_more[0].id)

#修改
# user_one = Session.query(User).filter_by(id=1).first()
# user_one.name = 'update one'
# user_one.password = 'pass one'
# Session.commit()

#多表
# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     stu_id = Column(Integer)
#     age = Column(Integer)
#     gender = Column(Enum('M', 'F'), nullable=False)
#     def __repr__(self):
#         return "[%s stu_id:%s sex:%s]" %(self.stu_id,self.age,self.gender)

# stu01 = Student(stu_id=1,age=20,gender='M')
# stu02 = Student(stu_id=2,age=30,gender='F')
# stu03 = Student(stu_id=3,age=40,gender='M')
# stu04 = Student(stu_id=4,age=50,gender='M')
#
#用来创建表
# Base.metadata.create_all(engine)
#
# Session.add_all([stu01,stu02,stu03,stu04])
# Session.commit();



# line_table = Session.query(User,Student).filter(User.id==Student.stu_id).all()
# print(line_table[0][1].gender)



# class Stu2(Base):
#     __tablename__ = "stu2"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32),nullable=False)
#     register_date = Column(DATE,nullable=False)
#     def __repr__(self):
#         return "<%s name:%s>" % (self.id, self.name)
#
# class StudyRecord(Base):
#     __tablename__ = "study_record"
#     id = Column(Integer, primary_key=True)
#     day = Column(Integer,nullable=False)
#     status = Column(String(32),nullable=False)
#     stu_id = Column(Integer,ForeignKey("stu2.id"))
#     stu2 = relationship("Stu2", backref="my_study_record")
#     def __repr__(self):
#         return "<%s day:%s status:%s>" % (self.stu2.name, self.day,self.status)
#
#
# stu_obj = Session.query(Stu2).filter(Stu2.name=="a").first()
# print(stu_obj.my_study_record)