# 数字比较
from math import floor, ceil
from decimal import Decimal

# decimal.Decimal
_decimal = Decimal(2645593613.4653)

# float格式
#_decimal = 2645593613.4653

print(_decimal)
print(type(_decimal))
print(_decimal > 1000000000)
print(_decimal > 3000000000)
# 向下取整
print(floor(_decimal/1000000000))
# 取n位小数 round是四舍五入
print(round(_decimal / 1000000000, 4))

print('-----------------------')

#format转变格式
print(type(1.0231212121))
print(type(format(1.0231212121)))

print("{:.2f}".format(1.0231212121))

print('########################################')


# 日期
import time

# time.time() float类型,返回值是小数 1527651680.1122005
print(time.time())

print(time.localtime(time.time()))
print(time.localtime(2011))

print(time.strftime('%Y-%m format %d %H:%M:%S',time.localtime()))
# 返回time.struct_time(tm_year=2018, tm_mon=5, tm_mday=30, tm_hour=16, tm_min=0, tm_sec=14, tm_wday=2, tm_yday=150, tm_isdst=-1)
# 根据fmt的格式把一个时间字符串解析为时间元组
print("返回元祖: ",time.strptime('23 Oct2017','%d %b%Y'))
# TypeError: Tuple or struct_time argument required
# print("time: ", time.strftime('%Y-%m format %d %H:%M:%S',time.time()))
print(type(time.strptime('23 Oct 2017','%d %b %Y')))

print("gmtime :", time.gmtime())

print('########################################')


# 日历
import calendar
# str类型
cal = calendar.month(2017,10)
print(cal)


print('########################################')


from datetime import date,datetime,timedelta
# datetime函数
print(datetime.strptime("2018-0212", "%Y-%m%d"))
# return 2018-05-30 16:54:00
print("datetime.strptime: ",datetime.strptime(time.strftime('%Y%m%d%H%M',time.localtime()), "%Y%m%d%H%M"))

# return 2018-05-30
today = date.today()
print(date.today())
print(type(date.today()))
print(today.year)

next = timedelta(days=0, hours=0, minutes=3, seconds=10)
pre =timedelta(days=0, hours=0, minutes=1, seconds=0)
print(next-pre)

# return 2018-05-30 16:19:46.182000
print(datetime.now())


print('fromtimestamp: ', date.fromtimestamp(time.time()))
print("timetuple: ", datetime.now().timetuple())
