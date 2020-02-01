# -*- coding: utf-8 -*-
# =====================
# get all illness names
# =====================
import scrapy
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.cdc.gov/obesity/index.html'
    ]
    def parse(self, response):
        for links in response.css('li.nav-lvl1').xpath('.//a/@href').extract():
            if links[0] == '/':
                yield  {'sublinklist': "https://www.cdc.gov"+links}

# scrapy runspider webCrawler.py -o links.json
