# -*- coding: utf-8 -*-
import json
import string
import urllib
from urllib2 import Request

import re
import scrapy
import torndb
from scrapy import Selector

from tutorial.spiders.emailtool import send_mail


class DmozSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["dmoz.org"]
    productid = '3527963'
    mailto_list = ['364756388@qq.com']
    start_urls = [
        "https://item.jd.com/1447319.html",
        "https://item.jd.com/2195401.html"
     ]


    def parse(self, response):
        db = torndb.Connection('localhost', 'smzdm', 'root', '')

        mainurl = response.url
        productid = mainurl[20:27] # 暂时截取 回来用正则

        #获取价格
        priceUrl = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + productid + "&origin=2"
        priceData = urllib.urlopen(priceUrl).read().decode("utf-8", "ignore")
        patt = r'"p":"(\d+\.\d+)"'
        price = re.findall(patt, priceData)[0]

        sql = 'SELECT * FROM goods WHERE id = %s'
        data = db.get(sql, productid)
        if data:
            price = price.encode("utf-8")
            price = float(price)
            print price
            # print data['price_set']
            print price < data['price_set']
            if price < data['price_set'] and 不等于当前价格:
                send_mail(['364756388@qq.com'], productid, "new price is"+str(price).encode("utf-8"))
		#更新当前价格
            else:
                print "价格没有降!"
        else:
            sql = "INSERT INTO goods (id, price_set ,price_ ,price_) VALUES (%s, %s)"
            db.insert(sql, productid, price, price ,price)



