from urllib import parse, request
import json

baseurl = "https://fanyi.baidu.com/"

data = {"kw": "girl"}
data = parse.urlencode(data).encode("utf-8")

# headers = {"Content-Length": len(data)}

rsp = request.urlopen(baseurl, data=data)
# html = rsp.read().decode('utf-8')
# print(type(html))
#
# json_data = json.loads(html)
# print(json_data)


json_data = rsp.read().decode('utf-8')
print(type(json_data))
# print(json_data)


# 把json字符串转化成字典
json_data = json.loads(json_data)
# print(type(json_data))
print(json_data)