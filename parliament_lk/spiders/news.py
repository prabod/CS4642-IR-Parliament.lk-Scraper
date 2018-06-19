# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from parliament_lk.items import News


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['parliament.lk']
    start_urls = ['http://parliament.lk/en/news-en?view=news&category=6']

    def parse(self, response):
        for news in response.xpath('//td[@width="82%"]/a/@href').extract():
        	yield scrapy.Request(response.urljoin(news),callback=self.parseNews)

        next_page_url = response.xpath('//li[@class="pagination-next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


    def parseNews(self, response):
    	l = ItemLoader(item=News(), response=response)
    	l.add_xpath('title', '//table[@class="newsheader"]//td//h2[1]/text()')
    	l.add_xpath('date', '//table[@class="newsheader"]//tr[1]/td[3]/text()')
    	l.add_xpath('content', '//div[@class="inner-div newsarea"]/div[1]/p[string-length(text()) > 3]/text()')
    	yield l.load_item()
