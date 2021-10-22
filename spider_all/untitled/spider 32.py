from lxml import etree
html = etree.parse("/Users/gonghuidepro/PycharmProjects/untitled/111.html")
rst = etree.tostring(html, pretty_print=True)
print(rst)
