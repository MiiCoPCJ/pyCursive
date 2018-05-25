#import MySQLdb
#conn = MySQLdb.connect(host='localhost',poot='3306',user='root',password='root',db='pywf')
#cur = conn.cursor()

import pymysql

#cursorclass设置返回形式，默认返回时多维数组((),())，即tuple
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',cursorclass=pymysql.cursors.DictCursor)


# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'passwd': 'root',
#     'charset':'utf8',
#     'cursorclass':pymysql.cursors.DictCursor
# }
# conn = pymysql.connect(**config)
#conn.autocommit(1)
cursor = conn.cursor()

#选择表
conn.select_db('pywf')

#查询
# TABLE = 'wf_exchange'
count = cursor.execute("select * from %s" %('wf_exchange'))
# print('total records %s' %count)
# print('records row %s' %cursor.rowcount)

result = cursor.fetchall()
#数组对象[{},{}]
print(result[0].title)
# for row in result:
#     print('%s' %row)
#     print('##############')
#     print(row['id'])

#fet = cursor.fetchone()

#插入
# cursor.execute('insert into `wf_favorite`(`user_id`,`archive_id`) values(%s,%s)' %(3,2))
# conn.commit()

#更新
# title = 'update for py'
# cursor.execute('update `wf_exchange` set `title` = "%s" where `id` = %s ' %(title,223))
# conn.commit()
#换表查询
# conn.select_db('pywf2')
#
# cursor.execute('select * from `wf_exchange`')
#
# pyEX2 = cursor.fetchall()
# print(pyEX2)