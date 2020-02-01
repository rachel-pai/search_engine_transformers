# -*- coding: utf-8 -*-
# ============================================
# get the main page and substract the sublinks
# ============================================
import json
import os
from pathlib import Path

dire_list = []
url_list = []
with open('links.json') as json_file:
    ill_list = json.load(json_file)
    for illness in ill_list:
        temp = [x for x in illness['sublinklist'].split("/") if x]
        dire_list.append(temp[3])
        url_list.append(illness['sublinklist'])

ill_dire_list = list(set(dire_list))

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'obesity'
    start_urls = url_list

    def parse(self, response):
        temp = [x for x in response.url.split("/") if x]

        if not os.path.exists('./'+temp[2]+'/'+ temp[3]):
            os.makedirs('./'+temp[2]+'/'+ temp[3])
        filename = './'+temp[2]+'/'+temp[3] +"/" +"_".join(temp[3:]).split(".")[0]+ '.txt'
        if Path(filename).exists():
            pass
        else:
            content_list  = response.css('div.col-md-12').xpath('.//text()').extract()
            with open(filename, 'a+') as f:
                 _ = [f.write(ele+'\n') for ele in content_list]

