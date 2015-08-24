# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from RSpider.items import TestLoader


class BaseSpider(CrawlSpider):
    name = 'Base'
    allowed_domains = ['dmoz.org']
    start_urls = ['http://www.dmoz.org/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@id="catalogs"]')),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="directory dir-col"]'), callback='parse_directory', follow=True)
    )

    def parse_directory(self, response):
        for li in response.css('ul.directory-url > li'):
            tl = TestLoader(selector=li)
            tl.add_css('name', 'a::text')
            tl.add_css('description', '::text')
            tl.add_css('link', 'a::attr(href)')
            tl.add_value('url', response.url)
            yield tl.load_item()
