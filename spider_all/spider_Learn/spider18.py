# coding: utf-8

import json
import time
import pymysql
import requests
import os

'''
说明:

'''

# ============ header中及时不加sign也可以通过(亲测) ============ #
header = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI NOTE LTE MIUI/V8.5.1.0.MXECNED)/1.10.0;100000',
    'hgUid': '232096',
    'hgSystemVersion': '6.0.1',
    'hgId': 'ffffffff-f382-a5d9-ffff-ffffa2a6d3ae',
    'hgDeviceName': 'MI+NOTE+LTE',
    'hgAppNetwork': '4',
    'hgUtm': '100000',
    'hgAppVersion': '1.10.0',
    'hgScreen': '1080x1920',
    'hgPlatform': 'Android',
    'Host': 'api.huiguo.net',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}


# ============ 获取请求内容, 写入mysql ============ #
def get_values_to_db(module, urls):
    skadi_conn = pymysql.connect(host='10.30.24.103',
                                         port=3306,
                                         user='root',
                                         password='chuchujiedata',
                                         database='skadi')
    skadi_cur = skadi_conn.cursor()

    insert = """
        INSERT INTO huiguo_goods_daily (goods_id, title, brand_name, flag_extend, main_pic, pic, original_price, sale_price, sales, date_sign, module, modify_time)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        goods_id=VALUES (goods_id),
        title=VALUES (title),
        brand_name=VALUES (brand_name),
        flag_extend=VALUES (flag_extend),
        main_pic=VALUES (main_pic),
        pic=VALUES (pic),
        original_price=VALUES (original_price),
        sale_price=VALUES (sale_price),
        sales=VALUES (sales),
        date_sign=VALUES (date_sign),
        module=VALUES (module),
        modify_time=VALUES (modify_time)
    """

    date_sign = time.strftime("%Y-%m-%d", time.localtime())
    modify_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    try:
        for url in urls:
            response = requests.get(url, headers=header, verify=False)
            time.sleep(1)
            data = json.loads(response.text)
            print(url)
            for goods in data['data']['goods']:
                if ('goods_id' not in goods) or ('sale_txt' not in goods) or ('title' not in goods):  # 这三个字段必须存在
                    continue
                brand_name = goods.get('brand_name', '')
                flag_extend = goods.get('flag_extend', [])
                flag_extend = [flag['text'] for flag in flag_extend if 'text' in flag]
                flag_extend = ','.join(flag_extend)
                goods_id = goods['goods_id']
                main_pic = goods.get('main_pic', '')
                pic = goods.get('pic', '')
                original_price = goods.get('original_price', 0.0000)
                sale_price = goods.get('sale_price', 0.0000)
                sales = goods['sale_txt'].replace('人已买', '')
                title = goods['title']

                all_data = (goods_id, title, brand_name, flag_extend, main_pic, pic, original_price, sale_price, sales, date_sign, module, modify_time)
                # print(all_data)
                skadi_cur.execute(insert, all_data)
        skadi_conn.commit()
    finally:
        skadi_cur.close()
        skadi_conn.close()


def get_static_urls(url_path):
    urls = []
    with open(url_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = line.split(' ')
            urls.append(arr[6].replace("\"", ""))
    return urls


def get_dynamic_urls(url_path):
    files = os.listdir(url_path)
    urls = []
    for file in files:
        if not os.path.isdir(file):
            with open(url_path + file, 'r') as f:
                lines = f.readlines()
                full_url = 'http://api.huiguo.net' + lines[0].replace('\n', '').split(' ')[1]
                print(full_url)
                urls.append(full_url)
    return urls


if __name__ == '__main__':

    static_url_base_path = "F:\\Git_repository\\skadi\\data\\huiguo_static_urls\\"
    recommend_url_path = static_url_base_path + "recommend_url_14.bat"
    subject_url_path = static_url_base_path + "subject_url.bat"
    house_url_path = static_url_base_path + "house_url.bat"
    fruits_url_path = static_url_base_path + "fruits_url.bat"
    food_url_path = static_url_base_path + "food_url.bat"
    beauty_url_path = static_url_base_path + "beauty_url.bat"
    mom_url_path = static_url_base_path + "mom_url.bat"
    digital_url_path = static_url_base_path + "digital_url.bat"
    costume_url_path = static_url_base_path + "costume_url.bat"

    # ============ 固定的url ============ #
    recommend_urls = get_static_urls(recommend_url_path)
    subject_urls = get_static_urls(subject_url_path)
    house_urls = get_static_urls(house_url_path)
    fruits_urls = get_static_urls(fruits_url_path)
    food_urls = get_static_urls(food_url_path)
    beauty_urls = get_static_urls(beauty_url_path)
    mom_urls = get_static_urls(mom_url_path)
    digital_urls = get_static_urls(digital_url_path)
    costume_urls = get_static_urls(costume_url_path)

    # ============ 动态的url ============ #
    # date = time.strftime("%Y-%m-%d ", time.localtime())
    # dynamic_url_path = "F:\\Git_repository\\skadi\\data\\huiguo_dynamic_urls\\" + date + "\\"
    # recommend_urls = get_dynamic_urls(dynamic_url_path)

    # ============ 获取数据 ============ #
    get_values_to_db('今日推荐', recommend_urls)
    get_values_to_db('subject', subject_urls)
    # get_values_to_db('居家', house_urls)
    # get_values_to_db('水果', fruits_urls)
    # get_values_to_db('美食', food_urls)
    # get_values_to_db('美妆', beauty_urls)
    # get_values_to_db('母婴', mom_urls)
    # get_values_to_db('家电数码', digital_urls)
    # get_values_to_db('服饰箱包', costume_urls)