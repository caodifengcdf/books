# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class BooksPipeline(object):
    def process_item(self, item, spider):
        price  = round(float(item['price'][1:]) * 8.7395,2)
        if price:
            item['price'] = '￥%.2f' %price
            return item
