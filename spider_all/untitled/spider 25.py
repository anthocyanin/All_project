import re
pattern = re.compile(r"\d+")
m = pattern.findall("hello i am 18 years old and i am 185 cm")
print(m)

s = pattern.finditer("hello i am 18 years old and i am 185 cm")
print(type(s))
for i in s:
    print(i.group())

