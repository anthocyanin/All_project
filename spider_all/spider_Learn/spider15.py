"""
拼多多app爬虫(ios)

[映射结构]
    底部TAB: 首页,新品,_,_,_

    0. item -> meta

    1. 首页  -> [items]
            -> TODO: [modules]

    2. 新品  -> [items]
            -> 邻里团      -> [items]
            -> [主题团]    -> 主题团      -> [items]
"""

import requests
import json
from .common.persist import now_ts, persist2mysql_simple
from .common.time_sign import *
from .common.pinduoduo_URL import *


# Handle goods list
def goods_list_handler(goods_list, cnt, info):
    res = dict()
    item_id_list = list()
    for item in goods_list:
        res['item_id'] = item.get('goods_id', 0)
        res['item_name'] = item.get('goods_name', "")
        res['item_short_name'] = item.get('short_name', "")
        res['thumb_img_url'] = item.get('thumb_url', "")
        res['hd_thumb_img_url'] = item.get('hd_thumb_url', "")
        res['img_url'] = item.get('image_url', "")
        res['allowed_region'] = item.get('allowed_region', "")
        res['limited_region'] = item.get('region_limit', "")
        res['item_mode'] = item.get('p_rec', {}).get('m', "")
        res['item_type'] = item.get('p_rec', {}).get('t', "")
        res['customer_cnt'] = item.get('group', {}).get('customer_num', 0)
        res['sales_cnt'] = item.get('cnt', 0)
        res['price'] = item.get('group', {}).get('price', 0.) / 100.
        res['market_price'] = item.get('market_price', 0.) / 100.
        res['normal_price'] = item.get('normal_price', 0.) / 100.
        res['event_type'] = item.get('event_type', 0)
        cnt += 1

        print("[{}] {} {}".format(cnt, res['item_id'], res['item_name']))

        item_id_list.append(res['item_id'])

        persist2mysql_simple(table='pinduoduo_item', data=res)
        snap_res = dict((k, res[k]) for k in ['item_id', 'sales_cnt', 'price'])
        snap_res['date_sign'] = DATE_SIGN
        snap_res['channel'] = info
        persist2mysql_simple(table='pinduoduo_item_snap', data=snap_res)
    return cnt, item_id_list


# Get front page items
def get_front_page_items(info="", *args, **kwargs):
    try:
        req = requests.get(FRONT_PAGE_ITEM, params=kwargs, headers=headers)
        print("======= Query front page items =======")
        req_dict = json.loads(req.text)
        print(req.request.url)
        print(req_dict)

        # handle page
        page_size = kwargs['size']
        total_size = req_dict['total_size']
        page = kwargs['page']
        max_page = int((total_size - 1) / page_size) + 1

        # handle data
        cnt = 0
        while page < max_page:
            page += 1
            print("---- page {} ----".format(page))
            kwargs['page'] = page
            req = requests.get(FRONT_PAGE_ITEM, params=kwargs, headers=headers)
            print(req.request.url)
            req_dict = json.loads(req.text)
            print(req_dict)
            cnt, _ = goods_list_handler(req_dict['goods_list'], cnt, info)
        return 0, None
    except Exception as e:
        print("[Get front page error]" + str(e))
        raise e


# Get new items
def get_new_items(info="", *args, **kwargs):
    try:
        req = requests.get(NEW_ITEM, params=kwargs, headers=headers)
        print("======= Query new items =======")
        print(req.request.url)
        req_dict = json.loads(req.text)

        # handle page
        goods_list_size = len(req_dict['goods_list'])

        # handle data
        cnt = 0
        while goods_list_size > 0:
            print("---- page {} ----".format(kwargs['page']))
            print(req.request.url)
            req_dict = json.loads(req.text)
            cnt, _ = goods_list_handler(req_dict['good_list'], cnt, info)
            kwargs['page'] += 1
            req = requests.get(NEW_ITEM, params=kwargs, headers=headers)
            req_dict = json.loads(req.text)
            goods_list_size = len(req_dict['goods_list'])
        return 0, None
    except Exception as e:
        print("[Get new error]" + str(e))


# Get rank items
def get_rank_items(info="", *args, **kwargs):
    try:
        req = requests.get(RANK_ITEM, params=kwargs, headers=headers)
        print("======= Query rank items =======")
        print(req.request.url)
        req_dict = json.loads(req.text)

        # handle page
        goods_list_size = len(req_dict['goods_list'])

        # handle data
        cnt = 0
        while goods_list_size > 0:
            print("---- page {} ----".format(kwargs['page']))
            print(req.request.url)
            req_dict = json.loads(req.text)
            cnt, _ = goods_list_handler(req_dict['goods_list'], cnt, info)
            kwargs['page'] += 1
            req = requests.get(RANK_ITEM, params=kwargs, headers=headers)
            req_dict = json.loads(req.text)
            goods_list_size = len(req_dict['goods_list'])
        return 0, None
    except Exception as e:
        print("[Get rank error]" + str(e))


# Get subject items
def get_subject_items(info="", *args, **kwargs):
    try:
        req = requests.get(SUBJECT, params=kwargs, headers=headers)
        print("======= Query subjects =======")
        req_dict = json.loads(req.text)

        # handle page
        subject_list_size = len(req_dict)

        # handle data
        s_cnt = 0
        i_cnt = 0
        while subject_list_size > 0:
            print("---- page {} ----".format(kwargs['page']))
            print(req.request.url)
            req_dict = json.loads(req.text)
            for one_subject in req_dict:
                s_cnt += 1
                s_dict = dict()
                s_dict['subject_id'] = one_subject.get('subject_id', 0)
                s_dict['subject_name'] = one_subject.get('subject', '')
                s_dict['subject_describe'] = one_subject.get('desc', '')
                s_dict['banner_img_url'] = one_subject.get('home_banner', '')
                s_dict['banner_img_url_2'] = one_subject.get('home_banner2', '')
                s_dict['item_cnt'] = one_subject.get('goods_num', 0)
                s_dict['sales_cnt'] = one_subject.get('sales', 0)
                s_dict['start_time'] = one_subject.get('start_time', 0)
                s_dict['end_time'] = one_subject.get('end_time', 0)

                print("--- subject[{}] {} ---".format(s_cnt, s_dict['subject_id']))

                # get items in subject
                item_kwargs = {"size": 20, "page": 1}
                i_req = requests.get(SUBJECT_ITEM.format(subject_id=s_dict['subject_id']), params=item_kwargs, headers=headers)
                i_req_dict = json.loads(i_req.text)
                s_i_list_size = len(i_req_dict['goods_list'])

                while s_i_list_size > 0:
                    print("--- page {} ---".format(item_kwargs['page']))
                    print(i_req.request.url)
                    i_cnt, i_list = goods_list_handler(i_req_dict['goods_list'], i_cnt, info)

                    item_kwargs['page'] += 1
                    i_req = requests.get(SUBJECT_ITEM.format(subject_id=s_dict['subject_id']), params=item_kwargs, headers=headers)
                    i_req_dict = json.loads(i_req.text)
                    s_i_list_size = len(i_req_dict['goods_list'])

                    s_dict['goods_list'] = ",".join(list(map(lambda x: str(x), i_list)))

                persist2mysql_simple("pinduoduo_subject", s_dict)

            kwargs['page'] += 1
            req = requests.get(SUBJECT, params=kwargs, headers=headers)
            req_dict = json.loads(req.text)
            subject_list_size = len(req_dict)
        return 0, None
    except Exception as e:
        print("[Get rank error]" + str(e))


if __name__ == '__main__':
    # req = requests.get("http://apiv4.yangkeduo.com/v5/goods?size=60&assist_allowed=1&list_id=0&page=1&column=1&platform=3", headers=headers)
    # print(req.text)
    # exit(0)
    get_front_page_items(info='front_page_top', size=60, assist_allowed=1, list_id=0, page=0, column=1, platform=3)
    get_front_page_items(info='front_page_bottom', size=40, list_id=0, page=0, column=2, platform=3)
    get_new_items(info='new_list', size=50, page=1)
    get_rank_items(info='rank_list', size=50, page=1)
    get_subject_items(info='subject', size=30, page=1)