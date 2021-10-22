import sqlite3
import time

con = sqlite3.connect('sqliteTest.db')
cur = con.cursor()
# cur.execute('create table person(id integer primary key,name varchar(20),age integer)')
# time.sleep(3)
# cur.executemany('insert into person values (?,?,?)', [(0, 'qiye', 20), (1, 'mary', 22), (2, 'jack', 25)])
# con.commit()
# time.sleep(4)
cur.execute('select * from person')
res1 = cur.fetchone()  # 返回元组
res2 = cur.fetchall()  # 返回列表
#
# for line in res:
#     print(line)
print(type(res1))
print(type(res2))

