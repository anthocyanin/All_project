import pymysql
import time
# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='gonghui21513049', db='test', charset='utf8')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

row = cursor.rowcount
print(row)

conn.commit()
cursor.close()

time.sleep(5)

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()

