"""
云集爬虫,基于ios的[云集微店app]

[映射结构]
    底部TAB: 选品,专柜,发现,店铺,我的

    0.item  ->  1. meta
                2. detail
                3. documents

    1.选品   -> TODO:banner
            -> activity -> [times] -> 1.group -> [items] -> item
                                      2.single -> item
"""

import requests
import json
import time
import random
import pymysql

# Connection
conn = pymysql.connect(
    host='10.30.24.103',
    port=3306,
    user='root',
    password='chuchujiedata',
    db='skadi',
    charset='utf8'
)


# Token
TICKETS = "ticket%7C4150362_d68d6fd682ca7e55bcd466774c08e24c"

#  Urls
# TODO:item
GET_ITEM_APP = "https://app.yunjiweidian.com/yunjiapp/app/queryItemBoV1.json"
GET_ITEM_M = "https://m.yunjiweidian.com/yunjibuyer/getItemInfo.json"
GET_ITEM_SELLER_COUNT = "https://m.yunjiweidian.com/yunjibuyer/getItemSellerCounts.json"
GET_ITEM_DETAIL = "https://m.yunjiweidian.com/yunjibuyer/getItemDetailInfo.json?itemId=5562"

# [banners]
GET_BANNER = "https://app.yunjiweidian.com/yunjiapp/app/sale/getNewSaleBanner.json?ticket=ticket%{0}".format(TICKETS)

# [activities]
GET_ACTIVITY_IDS = "https://app.yunjiweidian.com/yunjiapp/app/queryAllActivityTimesList.json"

# one activity -> [groups]
GET_ACTIVITY_GROUP = "https://app.yunjiweidian.com/yunjiapp/app/queryTimesBizListByTimesId.json"

# one activity -> group(brand) -> [items] (brandId and pageIndex can be modified)
GET_GROUP_SELLER_COUNT = "https://app.yunjiweidian.com/yunjiapp/app/getBrandSellerCounts.json"
GET_GROUP_ITEMS = "https://app.yunjiweidian.com/yunjiapp/app/getshopbranditemList.json"

# one activity -> group(subject) -> [items]
GET_SUBJECT_GROUP_ITEMS = "https://app.yunjiweidian.com/yunjiapp/app/subject/getSubject.json"

# one activity -> [items]
GET_ACTIVITY_ITEMS = "https://app.yunjiweidian.com/yunjiapp/app/queryItemListByTimesId.json"


# Help func
def r_sleep(func):
    def wrapper(*args, **kwargs):
        print('@' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        return func(*args, **kwargs)
    return wrapper


def now_ts():
    return int(time.time())


def get_ts_from_str(str_time, str_format="%Y-%m-%d %H:%M:%S"):
    array_time = time.strptime(str_time, str_format)
    ts = str(int(time.mktime(array_time)))
    return ts

# Time params
GMT_START_STR = time.strftime("%Y-%m-%d 00:00:00", time.localtime(time.time()))
GMT_END_STR = time.strftime("%Y-%m-%d 23:59:59", time.localtime(time.time()))
BIZ_START_STR = time.strftime("%Y-%m-%d 00:00:00", time.localtime(time.time() - 3600 * 24))
BIZ_END_STR = time.strftime("%Y-%m-%d 23:59:59", time.localtime(time.time() - 3600 * 24))
GMT_START_TS = get_ts_from_str(GMT_START_STR)
GMT_END_TS = get_ts_from_str(GMT_END_STR)
BIZ_START_TS = get_ts_from_str(BIZ_START_STR)
BIZ_END_TS = get_ts_from_str(BIZ_END_STR)
DATE_SIGN = time.strftime("%Y-%m-%d", time.localtime(time.time()))
LAST_DATE_SIGN = time.strftime("%Y-%m-%d", time.localtime(time.time() - 3600 * 24))


# activity -> [times]
def get_activity(*args, **kwargs):
    """Get time ids of all activities.

    Params:
        (http)ticket,version

    Returns:
        A list of dict of online activities.
        [{activity_id,alias,date_time,start_time,creator_id,creator_name}, ...]
    """
    try:
        activity = requests.get(GET_ACTIVITY_IDS, params=kwargs)
        print("\n====== Query activities ======")
        print(activity.request.url)
        return_dict = json.loads(activity.text)
        ins_activity = ("INSERT INTO yunji_activity "
                        "(activity_id,alias,activity_time,creator_id,modifier_id,start_ts,end_ts,date_sign,create_time,modify_time) "
                        "VALUES "
                        "({0},'{1}','{2}',{3},{4},'{5}','{6}','{7}','{8}','{9}') "
                        "ON DUPLICATE KEY UPDATE "
                        "alias='{1}',activity_time='{2}',creator_id={3},modifier_id={4},start_ts='{5}',end_ts='{6}',modify_time='{9}'")
        ins_op = ("INSERT INTO yunji_operator "
                  "(op_id,op_name,create_time,modify_time) "
                  "VALUES ({0},'{1}',{2},{3}) "
                  "ON DUPLICATE KEY UPDATE "
                  "op_name='{1}', modify_time={3}")
        cur = conn.cursor()
        if return_dict['errorCode'] == 0:
            cnt = 1
            for one_act in return_dict['activityTimesList']:
                print("[{0}] {1} : {2}@{3}".format(
                    cnt,
                    one_act['activityTimesId'],
                    one_act['alias'],
                    one_act['dateTime'])
                )
                cnt += 1
                activity_id = one_act.get('activityTimesId', 0)
                alias = one_act.get('alias', 0)
                activity_time = one_act.get('dateTime', 'unknown')
                creator_id = one_act.get('creatorId', 0)
                modifier_id = one_act.get('modifierId', 0)
                start_ts = one_act.get('startTime', 0)
                end_ts = one_act.get('endTime', 0)
                creator_name = one_act.get('creatorName', None)
                modifier_name = one_act.get('modifierName', None)

                cur.execute(ins_activity.format(
                    activity_id, alias, activity_time, creator_id, modifier_id, start_ts, end_ts, DATE_SIGN, now_ts(), now_ts()
                ))

                if creator_name:
                    cur.execute(ins_op.format(
                        creator_id, creator_name, now_ts(), now_ts()
                    ))
            cur.close()
            conn.commit()
            print("\nActivities persisted")
            return return_dict['activityTimesList']
        else:
            print('[Server error] {0}'.format(return_dict['errorMessage']))
    except Exception:
        print("[ERROR] - activity time ids")
        raise Exception


# activity -> [times] -> items
def get_activity_items(*args, **kwargs):
    """Get all single products in one activity.

        Params:
            (http)ticket,activityTimesId,version,*pageNo

        Returns:
            Item id list.
        """
    try:
        kwargs['pageNo'] = 0
        activity_items = requests.get(GET_ACTIVITY_ITEMS, params=kwargs)
        print("\n====== Query activity[{0}] -> [item ids] ======".format(kwargs['activityTimesId']))
        print(activity_items.request.url)
        return_dict = json.loads(activity_items.text)

        ins_item_id_list = ("INSERT INTO yunji_activity "
                            "(activity_id,item_id_list,date_sign) "
                            "VALUES ({0},'{1}','{2}') "
                            "ON DUPLICATE KEY UPDATE "
                            "activity_id={0},item_id_list='{1}',date_sign='{2}'")
        cur = conn.cursor()
        item_id_list = list()
        if return_dict['errorCode'] == 0:
            time.sleep(random.uniform(1, 2))
            item_data = return_dict['data']
            page_size = int(item_data['pageSize'])
            total_count = int(item_data['totalCount'])
            max_page = int((int(total_count) - 1) / page_size)
            print("total items: {0}\npage size: {1}\ntotal page: {2}".format(
                total_count, page_size, max_page
            ))
            print("-- page 0 --")
            this_page = 0
            for one_item in item_data['itemList']:
                item_id_list.append(one_item.get('itemId', 'unknown'))
            print("item cnt: {0}".format(len(item_id_list)))
            while this_page < max_page:
                this_page += 1
                print("-- page {0} --".format(this_page))
                kwargs['pageNo'] = this_page
                activity_items = requests.get(GET_ACTIVITY_ITEMS, params=kwargs)
                # print(activity_items.status_code)
                # print(activity_items.request.url)
                return_dict = json.loads(activity_items.text)
                item_data = return_dict['data']
                for one_item in item_data['itemList']:
                    item_id_list.append(one_item.get('itemId', 'unknown'))
                print("{0} items".format(len(item_id_list)))

            cur.execute(ins_item_id_list.format(
                kwargs['activityTimesId'], ",".join(list(map(lambda x: str(x), item_id_list))), DATE_SIGN
            ))
            conn.commit()
            print("\nActivities persisted")
            return item_id_list
        else:
            print('[Server error] {0}'.format(return_dict['errorMessage']))
    except Exception as e:
        print(str(e))


# activity -> [times] -> group
def get_activity_group(*args, **kwargs):
    """Get brand group in one activity.

    Params:
        (http)ticket,version,activityTimesId

    Returns:
        A list of dict of brand group in one activity.
        List[(biz_id, biz_type)]
    """
    try:
        activity_group = requests.get(GET_ACTIVITY_GROUP, params=kwargs)
        print("\n====== Query activity[{0}] -> [group ids] ======".format(kwargs['activityTimesId']))
        print(activity_group.request.url)
        return_dict = json.loads(activity_group.text)

        ins_group = ("INSERT INTO yunji_group "
                     "(group_id, group_name, small_img, list_img, item_cnt, group_type, create_time, modify_time) "
                     "VALUES "
                     "({0},'{1}','{2}','{3}',{4},{5},{6},{7}) "
                     "ON DUPLICATE KEY UPDATE "
                     "group_name='{1}',small_img='{2}',list_img='{3}',item_cnt={4},group_type={5},modify_time={7} ")
        cur = conn.cursor()
        group_id_list = list()
        if return_dict['errorCode'] == 0:
            for one_group in return_dict['data']:
                group_id = one_group.get('bizId', 0)
                group_name = one_group.get('bizName', 0).replace("'", r"\'")
                small_img = one_group.get('bizSmallImg', 0)
                list_img = one_group.get('bizListImg', 0)
                item_cnt = one_group.get('brandItemTotalCount', 0)
                group_type = one_group.get('bizType', 0)
                group_id_list.append((group_id, group_type))
                cur.execute(
                    ins_group.format(
                        group_id, group_name, small_img, list_img, item_cnt, group_type, now_ts(), now_ts()
                    )
                )
            conn.commit()
            print("\nGroup persisted!")
            return group_id_list
        else:
            print('[Server error] {0}'.format(return_dict['errorMessage']))
    except Exception:
        print("[ERROR] - activity brand group")
        raise Exception


# group(brand) -> [items]
def get_brand_group_items(*args, **kwargs):
    """Get items in a group.

    Params:
        (http)ticket,brandId,pageSize,pageIndex

    Return:
        Item id list.
    """
    try:
        group_items = requests.get(GET_GROUP_ITEMS, params=kwargs)
        group_cnt = requests.get(GET_GROUP_SELLER_COUNT, params={'ticket': kwargs['ticket'], 'brandIds': kwargs['brandId']})
        print("\n====== Query brand group[{0}] -> [items] ======".format(kwargs['brandId']))
        print("item: {0}".format(group_items.request.url))
        print("cnt: {0}".format(group_cnt.request.url))

        item_dict = json.loads(group_items.text)
        cnt_dict = json.loads(group_cnt.text)

        ins_cnt = ("INSERT INTO yunji_group "
                   "(group_id, seller_cnt, create_time, modify_time) "
                   "VALUES "
                   "({0}, {1}, {2}, {3}) "
                   "ON DUPLICATE KEY UPDATE "
                   "group_id={0},seller_cnt={1}, create_time={2}, modify_time={3}")
        ins_item = ("INSERT INTO yunji_group "
                    "(group_id, item_list, create_time, modify_time) "
                    "VALUES "
                    "({0}, '{1}', {2}, {3}) "
                    "ON DUPLICATE KEY UPDATE "
                    "group_id={0},item_list='{1}', create_time={2}, modify_time={3}")

        cur = conn.cursor()

        if cnt_dict['errorCode'] == 0:
            cnt = cnt_dict['data'][0]['count']
            cur.execute(ins_cnt.format(kwargs['brandId'], cnt, now_ts(), now_ts()))
            conn.commit()
            print("Group cnt persisted")
        else:
            print("Get group cnt error")

        item_id_list = list()
        if item_dict['errorCode'] == 0:
            for one_item in item_dict['itemList']:
                item_id_list.append(one_item.get('itemId', 0))
            item_id_list_str = ",".join(list(map(lambda x: str(x), item_id_list)))
            cur.execute(ins_item.format(kwargs['brandId'], item_id_list_str, now_ts(), now_ts()))
            conn.commit()
            print("Group item persisted")
            return item_id_list
        else:
            print('[Server error] {0}'.format(item_dict['errorMessage']))
    except Exception:
        print("[ERROR] - group items")
        raise Exception


# group(special) -> [items]
def get_subject_group_items(*args, **kwargs):
    """Get items in a group.

    Params:
        (http)ticket,subjectId

    Return:
        Item id list.
    """
    try:
        group_items = requests.get(GET_SUBJECT_GROUP_ITEMS, params=kwargs)
        print("\n====== Query group[{0}] -> [items] ======".format(kwargs['subjectId']))
        print(group_items.request.url)

        item_dict = json.loads(group_items.text)

        ins_item = ("INSERT INTO yunji_group "
                    "(group_id, item_list, create_time, modify_time) "
                    "VALUES "
                    "({0}, '{1}', {2}, {3}) "
                    "ON DUPLICATE KEY UPDATE "
                    "group_id={0},item_list='{1}', create_time={2}, modify_time={3}")

        cur = conn.cursor()

        item_id_list = list()
        if item_dict['errorCode'] == 0:
            for one_item in item_dict['data']['itemsString']:
                item_id_list.append(one_item)
            item_id_list_str = ",".join(list(map(lambda x: str(x), item_id_list)))
            cur.execute(ins_item.format(kwargs['subjectId'], item_id_list_str, now_ts(), now_ts()))
            conn.commit()
            print("Subject group items persisted")
            return item_id_list
        else:
            print('[Server error] {0}'.format(item_dict['errorMessage']))
    except Exception:
        print("[ERROR] - group items")
        raise Exception


# item
def get_item(*args, **kwargs):
    """Get item meta of one item.

    Params:
        (http)ticket,limitActivityId,itemId

    Return:
        Item meta data dict
    """
    try:
        item_meta = requests.get(GET_ITEM_M, params=kwargs)
        print("\n-- Query item[{0}] --".format(kwargs['itemId']))
        print("meta: {0}".format(item_meta.request.url))
        return_dict = json.loads(item_meta.text)

        item_cnt = requests.get(GET_ITEM_SELLER_COUNT, params={'itemIds': kwargs['itemId']})
        print("sales: {0}".format(item_cnt.request.url))
        cnt_dict = json.loads(item_cnt.text)

        ins_item = ("INSERT INTO yunji_item "
                    "(item_id,item_name,activity_name,activity_limit,big_img,fine_img,small_img,brand_id,brand_name,subtitle,cid,c1,c2,c3,stock,max_price,min_price,max_vip_price,min_vip_price,max_commission,min_commission,commission_rate,sales_cnt,online_time,release_time,create_time,modify_time) "
                    "VALUES "
                    "({item_id},'{item_name}','{activity_name}','{activity_limit}','{big_img}','{fine_img}','{small_img}',{brand_id},'{brand_name}','{subtitle}',{cid},{c1},{c2},{c3},{stock},{max_price},{min_price},{max_vip_price},{min_vip_price},{max_commission},{min_commission},{commission_rate},{sales_cnt},{online_time},{release_time},{create_time},{modify_time}) "
                    "ON DUPLICATE KEY UPDATE "
                    "item_name='{item_name}',activity_name='{activity_name}',activity_limit='{activity_limit}',big_img='{big_img}',fine_img='{fine_img}',small_img='{small_img}',brand_id={brand_id},brand_name='{brand_name}',subtitle='{subtitle}',cid={cid},c1={c1},c2={c2},c3={c3},stock={stock},max_price={max_price},min_price={min_price},max_vip_price={max_vip_price},min_vip_price={min_vip_price},max_commission={max_commission},min_commission={min_commission},commission_rate={commission_rate},sales_cnt={sales_cnt},online_time={online_time},release_time={release_time},modify_time={modify_time} ")
        cur = conn.cursor()

        res_dict = dict()
        if 'objItemBo' in return_dict:
            data = return_dict['objItemBo']
            res_dict['item_id'] = data.get('itemId', 0)
            res_dict['item_name'] = data.get('itemName', '').replace("'", r"\'")
            res_dict['activity_name'] = data.get('activityName', '').replace("'", r"\'")
            res_dict['activity_limit'] = data.get('activityDesc', '').replace("'", r"\'")
            res_dict['big_img'] = data.get('itemImgBig', '')
            res_dict['fine_img'] = data.get('fineImg', '')
            res_dict['small_img'] = data.get('itemImgSmall', '')
            res_dict['brand_id'] = data.get('itemBrand', 0)
            res_dict['brand_name'] = data.get('itemBrandName', '').replace("'", r"\'")
            res_dict['subtitle'] = data.get('subtitle', '').replace("'", r"\'")
            res_dict['cid'] = data.get('itemCategory', 0)
            res_dict['c1'] = data.get('itemCategoryLevel1', 0)
            res_dict['c2'] = data.get('itemCategoryLevel2', 0)
            res_dict['c3'] = data.get('itemCategoryLevel3', 0)
            res_dict['stock'] = data.get('stock', 0)
            res_dict['max_price'] = data.get('maxPrice', 0)
            res_dict['min_price'] = data.get('minPrice', 0)
            res_dict['max_vip_price'] = data.get('maxItemVipPrice', 0)
            res_dict['min_vip_price'] = data.get('minItemVipPrice', 0)
            res_dict['max_commission'] = data.get('maxCommission', 0)
            res_dict['min_commission'] = data.get('minCommission', 0)
            res_dict['commission_rate'] = data.get('commissionPoint', 0)
            res_dict['sales_cnt'] = cnt_dict.get('data', {'': ''}).get(str(kwargs['itemId']), 0)
            res_dict['online_time'] = data.get('onlineTime', 0)
            res_dict['release_time'] = data.get('releaseTime', 0)
            # print(ins_item.format(
            #         item_id=res_dict['item_id'],
            #         item_name=res_dict['item_name'],
            #         activity_name=res_dict['activity_name'],
            #         activity_limit=res_dict['activity_limit'],
            #         big_img=res_dict['big_img'],
            #         fine_img=res_dict['fine_img'],
            #         small_img=res_dict['small_img'],
            #         brand_id=res_dict['brand_id'],
            #         brand_name=res_dict['brand_name'],
            #         subtitle=res_dict['subtitle'],
            #         cid=res_dict['cid'],
            #         c1=res_dict['c1'],
            #         c2=res_dict['c2'],
            #         c3=res_dict['c3'],
            #         stock=res_dict['stock'],
            #         max_price=res_dict['max_price'],
            #         min_price=res_dict['min_price'],
            #         max_vip_price=res_dict['max_vip_price'],
            #         min_vip_price=res_dict['min_vip_price'],
            #         max_commission=res_dict['max_commission'],
            #         min_commission=res_dict['min_commission'],
            #         commission_rate=res_dict['commission_rate'],
            #         sales_cnt=res_dict['sales_cnt'],
            #         online_time=res_dict['online_time'],
            #         release_time=res_dict['release_time'],
            #         create_time=now_ts(),
            #         modify_time=now_ts()
            #     ))
            cur.execute(
                ins_item.format(
                    item_id=res_dict['item_id'],
                    item_name=res_dict['item_name'],
                    activity_name=res_dict['activity_name'],
                    activity_limit=res_dict['activity_limit'],
                    big_img=res_dict['big_img'],
                    fine_img=res_dict['fine_img'],
                    small_img=res_dict['small_img'],
                    brand_id=res_dict['brand_id'],
                    brand_name=res_dict['brand_name'],
                    subtitle=res_dict['subtitle'],
                    cid=res_dict['cid'],
                    c1=res_dict['c1'],
                    c2=res_dict['c2'],
                    c3=res_dict['c3'],
                    stock=res_dict['stock'],
                    max_price=res_dict['max_price'],
                    min_price=res_dict['min_price'],
                    max_vip_price=res_dict['max_vip_price'],
                    min_vip_price=res_dict['min_vip_price'],
                    max_commission=res_dict['max_commission'],
                    min_commission=res_dict['min_commission'],
                    commission_rate=res_dict['commission_rate'],
                    sales_cnt=res_dict['sales_cnt'],
                    online_time=res_dict['online_time'],
                    release_time=res_dict['release_time'],
                    create_time=now_ts(),
                    modify_time=now_ts()
                )
            )
            conn.commit()
            print("\nItem persisted")
        else:
            print("Invalid return json")
        return res_dict
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # print(get_activity(conn, ticket=TICKETS, version=2))
    # print(get_activity_group(ticket=TICKETS, version=1, activityTimesId=5500))
    # print(get_subject_group_items(ticket=TICKETS, subjectId=53313))
    # print(get_group_items(ticket=TICKETS, brandId=53321, pageSize=100, pageIndex=0))
    # print(get_item(limitActivityId=0, itemId=12910, appCont=1))
    # print(get_activity_items(ticket=TICKETS, activityTimesId=5473, version=1))

    # count
    activity_cnt = 0
    group_cnt = 0
    item_cnt = 0

    # activity_ids
    activities = get_activity(ticket=TICKETS, version=2)

    activity_list = list()
    for item in activities:
        time.sleep(random.uniform(0.3, 0.8))
        activity_list.append(item.get('activityTimesId', 0))
        activity_cnt += 1
    print(activity_list)

    # activity single items
    for one_activity in activity_list:
        item_list = get_activity_items(ticket=TICKETS, activityTimesId=one_activity, version=1)
        for item in item_list:
            item_cnt += 1
            time.sleep(random.uniform(0.1, 0.2))
            item_meta = get_item(ticket=TICKETS, limitActivityId=0, itemId=item)
            # print(item_meta)

    # activity group items
    for one_activity in activity_list:
        group_id_list = get_activity_group(ticket=TICKETS, version=1, activityTimesId=one_activity)
        for group_id, group_type in group_id_list:
            if group_type == 1:
                group_cnt += 1
                item_list = get_brand_group_items(ticket=TICKETS, brandId=group_id, pageSize=100, pageIndex=0)
                for item in item_list:
                    item_cnt += 1
                    time.sleep(random.uniform(0.1, 0.2))
                    item_meta = get_item(ticket=TICKETS, limitActivityId=0, itemId=item)
                    # print(item_meta)
            elif group_type == 2:
                group_cnt += 1
                item_list = get_subject_group_items(ticket=TICKETS, subjectId=group_id)
                for item in item_list:
                    item_cnt += 1
                    time.sleep(random.uniform(0.1, 0.2))
                    item_meta = get_item(ticket=TICKETS, limitActivityId=0, itemId=item)
                    # print(item_meta)
            else:
                print("Invalid group type {0}:{1}".format(group_type, group_id))

    conn.close()

