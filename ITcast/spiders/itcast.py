# -*- coding: utf-8 -*-

import scrapy
from ITcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # items = []
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = ItcastItem()

            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # 返回提取到的每个 item 数据，给管道文件处理，同时返回回来，继续执行后面的代码（循环）
            yield item
            # items.append(item)
        # print(items)
        # return items
