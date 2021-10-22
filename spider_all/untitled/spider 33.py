from lxml import etree

html = etree.parse("/Users/gonghuidepro/PycharmProjects/untitled/111.html")
# print(type(html))

rst = html.xpath("//book")
# print(type(rst))
print(rst)

rst2 = html.xpath('//book[@category="sport"]/title[@lang="en"]/text()')
# print(type(rst2))
print(rst2)

rst3 = html.xpath('//book[@category="sport"]/year/text()')
# print(type(rst3))
print(rst3)

rst4 = html.xpath('//year/text()')
print(rst4)

rst5 = html.xpath('//title')
rst5 = rst5[0]
print(rst5.tag)
print(rst5.text)

