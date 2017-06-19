# -*- coding: utf-8 -*-
import scrapy
from scrapy_test.items import ScrapyTestItem
import sys


class Spider1Spider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E6%B8%B8%E6%88%8F&fr=search']

    def parse(self, response):
        for line in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            item = ScrapyTestItem()
            item['title'] = line.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()').extract()
            item['author'] = line.xpath('.//div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
            item['reply'] = line.xpath('.//div[contains(@class,"col2_left j_threadlist_li_left")]/span/text()').extract()
            yield item

