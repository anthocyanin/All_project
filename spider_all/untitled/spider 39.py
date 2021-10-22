import scrapy

class ItcastItem(scrapy.item):
    name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
