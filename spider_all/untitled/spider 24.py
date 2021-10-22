import re
s = r"([a-z]+) ([a-z]+)"

partten = re.compile(s, re.I)
m = partten.match("hello world web ")

s = m.group(0)  # group(0)表示返回匹配成功的整个子串
print(s)

a = m.span(0)  # span(0)返回匹配成功的整个子串的跨度
print(a)

# group(1)表示返回的第一个分组匹配成功的子串
s = m.group(1)
print(s)

a = m.span(1)  # 返回匹配成功的第一个子串的跨度
print(a)

s = m.groups()  # 等价于m.group(1), m.group(2).......
print(s)
