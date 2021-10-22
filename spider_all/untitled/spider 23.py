import re
s = r"\d+"
pattern = re.compile(s)
m = pattern.match("one1two2three3")
print(type(m))
print(m)
d = pattern.match("one1two23n45three3", 7, 12)  # 匹配过程中只找一次，无论找到与否，都返回
print(type(d))
print(d)
print(d.group())
print(d.start(0))
print(d.end(0))
print(d.span(0))
