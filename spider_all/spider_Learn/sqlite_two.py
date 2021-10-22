import sqlite3
import time
conn = sqlite3.connect('sqliteTest.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
time.sleep(2)

cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

row = cursor.rowcount
print(row)
cursor.close()
conn.commit()
conn.close()
