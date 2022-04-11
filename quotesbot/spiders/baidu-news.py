# -*- coding: utf-8 -*-
import json
import os
import time

import scrapy
from scrapy import item


class ToScrapeCSSSpider(scrapy.Spider):
    name = "baidu-news"


    allowed_domains = ['baidu.com']
    start_urls = [
        'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&medium=0&x_bfe_rqs=03E80&x_bfe_tjscore=0.100000&tngroupname=organic_news&ne=&newVideo=12&goods_entry_switch=1&rsv_dl=news_b_pn&pn='
    ]


    def start_requests(self):
        #遍历所有页码
        for i in range(0, 5,1):
            yield scrapy.Request(url=self.start_urls[0] + str(i)+'0')

    def parse(self, response):
        #解析内容
        for quote in response.css("div.content_left div.result-op"):

            yield {
                'title': quote.css("h3 a::text").extract_first(),
                'time': quote.css(" div.c-span-last span.c-color-gray2::text").extract_first(),
                'source': quote.css("div.news-source_Xj4Dv a.source-link_Ft1ov span.c-color-gray::text").extract_first(),
                'abstract': quote.css("div.result-op div.c-span-last span.c-color-text::attr(aria-label)").extract_first()
            }

        # i = i + 1;
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
