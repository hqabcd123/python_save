import scrapy
from bs4 import BeautifulSoup
#from scr.items import ScrItem
import json
import requests
import time
import sys
from scrapy_lihkg.items import ScrapyLihkgItem 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

base = 'https://lihkg.com'

class lihkg_crawler(CrawlSpider):
    name = 'lihkg'
    base = 'https://lihkg.com'
    api = '/api_v2/thread/{}/page/{}?order=reply_time'

    def start_requests(self):
        i = 1
        while i <= 1:
            try:
                yield scrapy.Request(url = base + self.api.format(i, 1), callback=self.parse_list, errback=self.after_404)
                i += 1
            except KeyError:
                raise scrapy.exceptions.CloseSpider('thread {} is out of range'.format(i))
    def parse_list(self, response):
        #print(response.body)
        datas = json.loads(response.body)
        #print(datas)
        thread_id = int(datas['response']['thread_id'])
        pages = int(datas['response']['total_page'])
        yield scrapy.Request(url = base + self.api.format(1, 1), callback=self.self_parse, errback=self.after_404)
        # try:
        #     for page in range(pages):
        #         #print(data)
        #         yield scrapy.Request(url = base + self.api.format(thread_id, page+1), callback=self.self_parse, errback=self.after_404)
        # except KeyError:
        #     print(KeyError)
        #     raise scrapy.exceptions.CloseSpider('thread {} is out of range'.format(thread_id))
    
    def self_parse(self, response):
        datas = json.loads(response.body)
        lihkg_item = ScrapyLihkgItem()
        #print(datas)
        for data in datas['response']['item_data']:
            #print(data['user_nickname'], ': ', data['msg'], ', msg number: ', data['msg_num'])
            lihkg_item['title'] = datas['response']['title']
            lihkg_item['user_nickname'] = data['user_nickname']
            lihkg_item['msg'] = data['msg']
            lihkg_item['thread_id'] = data['thread_id']
            lihkg_item['post_id'] = data['post_id']
            lihkg_item['quote_post_id'] = data['quote_post_id']
            lihkg_item['msg_num'] = data['msg_num']
            lihkg_item['page'] = data['page']
            yield lihkg_item

    def after_404(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)