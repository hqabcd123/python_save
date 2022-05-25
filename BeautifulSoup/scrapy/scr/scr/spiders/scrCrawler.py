import scrapy
from bs4 import BeautifulSoup
from scr.items import ScrItem
import json
import requests
base = 'https://lihkg.com'

class scrCrawler(scrapy.Spider):
    name = 'scr'
    url = ''
    start_urls = 'https://lihkg.com/api_v2/thread/latest?cat_id=1&page=1&count=60&type=now'
    def parse(self, response):
        res = json.loads(response.body)
        print(res)
        # for str in res.select('.title a'):
        #     print(base + str['href'], str.text)
        #     yield scrapy.Request(base + str['href'], self.parse_detail)
        # for i in res.select('.action-bar a'):
        #     try:
        #         if i.text.find('上頁') != -1:
        #             front = i['href']
        #             print(front, i.text)
        #             yield scrapy.Request(base + front, self.parse)
        #     except KeyError:
        #         print(KeyError)


    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        scritem = ScrItem()
        scritem['title']  = res.select('#main-content .article-meta-value')[0].text
        scritem['content']  = res.select('#main-content')[0].text
        scritem['time']  = res.select('#main-content .article-meta-value')[0].text
        print(res.select('#main-content')[0].text)
        return scritem