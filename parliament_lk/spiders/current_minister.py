# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from parliament_lk.items import CurrentMinister
import json


class CurrentMinisterSpider(scrapy.Spider):
    name = 'current_minister'
    allowed_domains = ['parliament.lk']
    start_urls = ['http://parliament.lk/members-of-parliament/directory-of-members/index2.php?option=com_members&task=all&tmpl=component&letter=A&wordfilter=&search_district=']

    def parse(self,response):
		jsonresponse = json.loads(response.body_as_unicode())
		for r in jsonresponse:
			yield scrapy.Request("http://parliament.lk/en/members-of-parliament/directory-of-members/viewMember/%s" %r['mem_intranet_id'], callback=self.parse_minister)
		for i in range(65,91):
			yield scrapy.Request('http://parliament.lk/members-of-parliament/directory-of-members/index2.php?option=com_members&task=all&tmpl=component&letter=%s&wordfilter=&search_district='%chr(i))
    
    def parse_minister(self, response):
		l = ItemLoader(item=CurrentMinister(), response=response)
		l.add_xpath('name', '//div[@class="components-wrapper"]/h2/text()')
		l.add_xpath('party', '//div[@class="top-mp-detail-1"]//div[@class="right-details"]//table[@class="mem_profile"]//tr/td//div[contains(.//text(),"Party")]/following-sibling::a/text()')
		l.add_xpath('dob', '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Birth")]/text()')
		l.add_xpath('civil_status', '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Civil")]/text()')
		l.add_xpath('religion', '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Religion")]/text()') 
		l.add_xpath('occupation', '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Occupation")]/text()')
		l.add_xpath('mobile', '//div[@class="top-mp-detail-2"]//div[@class="right-wrap"]//table[@class="mem_profile"]//tr[1]//td[1]//td[@width="93%"]/text()')
		l.add_xpath('h_address', '//div[@class="top-mp-detail-2"]//div[@class="right-wrap"]//table[@class="mem_profile"]//tr[1]//td[1]//tr//td//img[@src="/images/address.png"]/parent::td/following-sibling::td/text()') 
		l.add_xpath('email', '//a[@class="link7"]/text()')
		l.add_xpath('o_phone', '//div[@class="top-mp-detail-2"]//div[@class="right-wrap"]//table[@class="mem_profile"]//tr[1]//td[2]//tr//td//img[@src="/images/phone_ico.png"]/parent::td/following-sibling::td/text()') 
		l.add_xpath('o_address', '//div[@class="top-mp-detail-2"]//div[@class="right-wrap"]//table[@class="mem_profile"]//tr[1]//td[2]//tr//td//img[@src="/images/address.png"]/parent::td/following-sibling::td/text()') 
		l.add_xpath('district', '//div[@class="top-mp-detail-1"]//div[@class="right-details"]//table[@class="mem_profile"]//tr/td[contains(.//div, "District")]/text()') 
		l.add_xpath('portfolio', '//div[@class="top-mp-detail-1"]//div[@class="right-details"]//table[@class="mem_profile"]//tr/td[contains(.//div, "Portfolio")]/text()') 
		l.add_xpath('image_urls', '//img[@style="width:106px;"]/@src')
		yield l.load_item()
		