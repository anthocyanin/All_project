# A small library of database routines to power a payments application.
import os
import pprint
import sqlite3
from collections import namedtuple


def open_database(path='bank.db'):
    new = not os.path.exists(path)  # 这个语句简洁有力,
    db = sqlite3.connect(path)
    if new:
        c = db.cursor()
        c.execute('CREATE TABLE payment (id INTEGER PRIMARY KEY, debit TEXT, credit TEXT, dollars INTEGER, memo TEXT)')
        add_payment(db, 'brandon', 'psf', 125, 'Registration for PyCon')
        add_payment(db, 'brandon', 'liz', 200, 'payments for writing that code')
        add_payment(db, 'sam', 'brandon', 25, 'Gas money-thanks for the ride')
        db.commit()
    return db


def add_payment(db, debit, credit, dollars, memo):
    db.cursor().execute('INSERT INTO payment (debit, credit, dollars, memo)'
                        ' VALUES (?, ?, ?, ?)', (debit, credit, dollars, memo))


def get_payment_of(db, account):
    c = db.cursor()
    c.execute('SELECT * FROM payment WHERE credit = ? or debit = ? '
              ' ORDER BY id', (account, account))

    # print(c.description)  # c.descript返回的是元素为元组的元组。
    # print(c.fetchall())  # c.fetchall返回元素为元组的列表。

    Row = namedtuple('Row', [tup[0] for tup in c.description])  # namedtuple这里需要注意下,Row是一个类
    # dd = [Row(*row) for row in c.fetchall()]
    # print(len(dd))
    # print(type(dd))
    # print(dd)
    # print('=='*12)
    return [Row(*row) for row in c.fetchall()]  # 还有这里用c.fetchall()的结果实例化Row类，构成列表。


if __name__ == '__main__':
    db = open_database()  # 打开数据库这一步,就完成了数据的生成
    pprint.pprint(get_payment_of(db, 'brandon'))
































