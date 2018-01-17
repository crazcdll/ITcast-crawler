# -*- coding: utf-8 -*-
import scrapy


class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['http://www.tianqihoubao.com']
    start_urls = ['http://www.tianqihoubao.com/weather/top/beijing.html']

    def parse(self, response):
        print(response.body)
