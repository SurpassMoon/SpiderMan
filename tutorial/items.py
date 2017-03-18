# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Taobao01Item(scrapy.Item):
    # define the fields for your item here like:
    #商品名称
    title = scrapy.Field()
    #商品链接
    link = scrapy.Field()
    #商品价格（原价）
    price = scrapy.Field()
    #促销价格
    price_now = scrapy.Field()
    #评论数
    comment = scrapy.Field()
