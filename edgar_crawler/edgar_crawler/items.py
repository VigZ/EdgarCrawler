# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EdgarCrawlerItem(scrapy.Item):
    issuer = scrapy.Field()
    class_title = scrapy.Field()
    cusip = scrapy.Field()
    value = scrapy.Field()
    shrs_prn_amt = scrapy.Field()
    shrs_prn_type = scrapy.Field()
    put_call = scrapy.Field()
    investment_discretion = scrapy.Field()
    other_manager = scrapy.Field()
    vote_auth_sole = scrapy.Field()
    vote_auth_shared = scrapy.Field()
    vote_auth_none = scrapy.Field()
