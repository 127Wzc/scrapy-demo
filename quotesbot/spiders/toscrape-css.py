# -*- coding: utf-8 -*-
import json
import time

import scrapy
from scrapy import item


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        # 504 1-72页
        'https://vulncat.fortify.com/zh-cn/weakness?codelang=Java%2fJSP&po=',
        # 380 1-55页
        #java规则
        # 'https://vulncat.fortify.com/zh-cn/weakness?standard=OWASP+2021&codelang=Java%2fJSP&po='
        #全规则830 1-119
        # 'https://vulncat.fortify.com/zh-cn/weakness?po='
        # 'https://vulncat.fortify.com/zh-cn/weakness?standard=OWASP+2021&amp%3bcodelang=Java%2fJSP&amp%3bpo=0&po=2'
    ]

    def start_requests(self):
        for i in range(1, 74,1):
            yield scrapy.Request(url=self.start_urls[0] + str(i))

    def parse(self, response):
        for quote in response.css("div.detailcell"):
            yield {
                'title': quote.css("div.title a::text").extract_first(),
                'abstract': quote.css("div.body div.t").extract_first(),
                # 'tags': quote.css("div.tags > a.tag::text").extract()
            }

        # i = i + 1;
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
