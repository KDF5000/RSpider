# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class TestItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    crawled = scrapy.Field()
    spider = scrapy.Field()
    url = scrapy.Field()


class TestLoader(ItemLoader):
    default_item_class = TestItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()


class RspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
