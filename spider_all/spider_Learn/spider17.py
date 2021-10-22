# coding: utf-8

import json
import time
import mysql.connector
import requests
import os

header = {
    'User-Agent': 'beidian/2.5.0 (Android)',
    'Cache-Control': 'no-cache',
    'Host': 'api.beidian.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}


def get_urls(url_path):
    files = os.listdir(url_path)
    urls = []
    for file in files:
        if not os.path.isdir(file):
            with open(url_path + file, 'r') as f:
                lines = f.readlines()
                full_url = 'http://api.beidian.com' + lines[0].replace('\n', '').split(' ')[1]
                print(full_url)
                urls.append(full_url)
    return urls


def get_values_to_db(urls):
    skadi_conn = mysql.connector.connect(host='10.30.24.103',
                                         port=3306,
                                         user='root',
                                         password='chuchujiedata',
                                         database='skadi')
    skadi_cur = skadi_conn.cursor()

    insert = """
    INSERT INTO beidian_goods_daily (product_id,title,commission,descr,img,item_price,original_price,rect_img, 
    seller_count,stock, date_sign,modify_time)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE
    product_id=VALUES (product_id),
    title=VALUES (title),
    commission=VALUES (commission),
    descr=VALUES (descr),
    img=VALUES (img),
    item_price=VALUES (item_price),
    original_price=VALUES (original_price),
    rect_img=VALUES (rect_img),
    seller_count=VALUES (seller_count),
    stock=VALUES (stock),
    date_sign=VALUES (date_sign),
    modify_time=VALUES (modify_time)"""

    date_sign = time.strftime("%Y-%m-%d", time.localtime())
    modify_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    try:
        ss = set()
        for url in urls:
            response = requests.get(url, headers=header, verify=False)
            time.sleep(1)
            data = json.loads(response.text)
            for goods in data['items']:
                if ('product_id' not in goods) or ('title' not in goods) or ('commission' not in goods):
                    continue
                product_id = goods['product_id']
                title = goods['title']
                commission = float(goods['commission'].get('commission_value', 0.0000)) / 100.0
                desc = goods.get('desc', '')
                img = goods.get('img', '')
                item_price = float(goods.get('item_price', 0.0000)) / 100.0
                origin_price = float(goods.get('origin_price', 0.0000)) / 100.0
                rect_img = goods.get('rect_img', '')
                seller_count = goods.get('seller_count', '0').replace('已售', '').replace('件', '')
                stock = goods.get('stock', 0)

                ss.add(product_id)
                all_data = (product_id, title, commission, desc, img, item_price, origin_price, rect_img, seller_count, stock, date_sign, modify_time)
                # print(all_data)
                skadi_cur.execute(insert, all_data)

        skadi_conn.commit()
    finally:
        skadi_cur.close()
        skadi_conn.close()


if __name__ == "__main__":
    url_path = "D:\\urls\\"
    urls = get_urls(url_path)
    get_values_to_db(urls)
