# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    question = scrapy.Field()
    num = scrapy.Field()
    content = scrapy.Field()
    status = scrapy.Field()
    time = scrapy.Field()
