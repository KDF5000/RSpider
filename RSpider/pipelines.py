# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import time

class BaseSpiderPipeline(object):
    def process_item(self, item, spider):
        item['crawled'] = time.time()
        item['spider'] = spider.name
        return item


class RspiderPipeline(object):
    def process_item(self, item, spider):
        return item
