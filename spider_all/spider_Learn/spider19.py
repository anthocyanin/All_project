#!/usr/bin/python
# -*- coding:UTF-8 -*-

import json
import codecs
import sys
import os
import requests
import time
import shutil
import xlwt

# 搜索关键字文件
keywords_file = './keyworlds.txt'


# 读取文件内容
def read_file(filePath):
    fileContents = ''
    with codecs.open(filePath, 'rU', 'utf-8') as f:
        fileContents = f.read()
    return fileContents


# 向文件中写入内容
def write_file(filePath, fileContent):
    with codecs.open(filePath, 'w', 'utf-8') as f:
        f.write(fileContent)


# 入口函数
def main():
    # 读取keyworlds文件

    # 读取文件所有内容到内存
    # keyworldsFileContent = read_file()
    # keyworldsArray = keyworldsFileContent.split('\n')
    # print 'keyworlds array', keyworldsArray, 'keyworlds array length:', len(keyworldsArray), '\n'
    # for keyworld in keyworldsArray:
    #    if len(keyworld.strip()) <= 0:
    #        continue
    #    grab_data(keyworld.strip())

    # 读取文件所有内容到内存，占用内存大，速度快
    # with codecs.open(keywords_file, 'rU', 'utf-8') as f:
    #    lines = f.readlines()
    #    for line in lines:
    #        if len(line.strip()) <= 0:
    #            continue
    #        grab_data(line.strip())

    # 按行读取文件，占用内存小，速度慢
    with codecs.open(keywords_file, 'rU', 'utf-8') as f:
        line = f.readline()
        while line:
            if len(line.strip()) <= 0:
                continue
            grab_data(line.strip())
            line = f.readline()


# 抓取数据
def grab_data(keyworld):
    requestUrlArray = [
        'http://apiv3.yangkeduo.com/search?q=' + keyworld + '&page=1&size=50&sort=default',
        'http://apiv3.yangkeduo.com/search?q=' + keyworld + '&page=1&size=50&sort=_sales',
        'http://apiv3.yangkeduo.com/search?q=' + keyworld + '&page=1&size=50&sort=_credit'
    ]
    # print 'grab data urls:', requestUrlArray, '\n'
    requestUrlNames = [u'综合', u'销量', u'评分']
    # print 'grab data url name:', requestUrlNames, '\n'
    for index, url in enumerate(requestUrlArray):
        request_and_save_data(url, requestUrlNames[index], keyworld)


# 请求接口抓取数据，并存储数据
def request_and_save_data(url, urlName, keyworld):
    # 创建存储的目录
    parentPath = './output/' + time.strftime("%Y-%m-%d", time.localtime()) + '/' + keyworld + '/'
    if not os.path.exists(parentPath):
        os.makedirs(parentPath)
    # else:
    #    shutil.rmtree(parentPath)

    # 保存json到文件
    jsonFilePath = parentPath + urlName + '.json'

    if os.path.exists(jsonFilePath):
        print
        jsonFilePath, 'file already exists'
        return
    # 请求返回数据
    responseText = request_data(url)
    print
    'request [' + url + '] response text:', responseText, '\n'
    if len(responseText) <= 0:
        return
    write_file(jsonFilePath, responseText)
    # 解析json
    responseJson = json.loads(responseText)
    # 生成Excell文件
    excellFilePath = parentPath + urlName + '.xls'
    save_data_to_excell(excellFilePath, responseJson)


# 存数据到excell表中
def save_data_to_excell(excellFilePath, responseJson):
    excellTitleArray = [u'商品名称', u'销售量', u'价格', u'图片链接', u'商品链接']
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)
    # excell表头
    for index, excellTitle in enumerate(excellTitleArray):
        ws.write(0, index, excellTitle)
    # 写数据
    for index, item in enumerate(responseJson['items']):
        index = index + 1
        ws.write(index, 0, item['goods_name'])
        ws.write(index, 1, item['sales'])
        ws.write(index, 2, float(item['price']) / 100)
        ws.write(index, 3, xlwt.Formula('HYPERLINK("' + item['image_url'] + '";"' + item['image_url'] + '")'))
        good_link = 'http://mobile.yangkeduo.com/goods.html?goods_id=' + str(item['goods_id'])
        ws.write(index, 4, xlwt.Formula('HYPERLINK("' + good_link + '";"' + good_link + '")'))
    wb.save(excellFilePath)


# 请求数据
def request_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 ===  iOS/11.2.5 Model/iPhone9,1 BundleID/com.xunmeng.pinduoduo AppVersion/3.58.0 AppBuild/1802061511 cURL/7.47.0'
    }
    response = requests.get(url, headers=headers)
    return response.text


# 写数据

if __name__ == '__main__':
    main()