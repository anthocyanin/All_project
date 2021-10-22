import re
s = r'\d+'
pattern = re.compile(s)
m = pattern.search("one12two34three56four78")
print(m.group())
m = pattern.search("one12two34three56four78five890", 8, 15)
print(m.group())