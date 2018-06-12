# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Minister(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    party = scrapy.Field()
    dob = scrapy.Field()
    civil_status = scrapy.Field()
    religion = scrapy.Field()
    occupation = scrapy.Field()
    political_carrer = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

class CurrentMinister(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    party = scrapy.Field()
    dob = scrapy.Field()
    civil_status = scrapy.Field()
    religion = scrapy.Field()
    occupation = scrapy.Field()
    district = scrapy.Field()
    portfolio = scrapy.Field()
    mobile = scrapy.Field()
    h_address = scrapy.Field()
    email = scrapy.Field()
    o_phone = scrapy.Field()
    o_address = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pass
