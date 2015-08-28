# -*- coding: utf-8 -*-
import scrapy


class CompanyinfospiderSpider(scrapy.Spider):
    name = "CompanyInfoSpider"
    allowed_domains = ["http://cn.made-in-china.com/"]
    start_urls = (
        'http://www.http://cn.made-in-china.com//',
    )

    def parse(self, response):
        pass
