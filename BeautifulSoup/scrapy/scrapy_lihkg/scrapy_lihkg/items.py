# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLihkgItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    msg = scrapy.Field()
    user_nickname = scrapy.Field()
    thread_id = scrapy.Field()
    post_id = scrapy.Field()
    quote_post_id = scrapy.Field()
    msg_num = scrapy.Field()
    page = scrapy.Field()
    #pass
