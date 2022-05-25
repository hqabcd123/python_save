# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3 
class ScrapyLihkgPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('lihkg_v2.sqlite')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS lihkg (
           title text, msg text, user_nickname text, thread_id text, post_id text, quote_post_id text, msg_num text, 
           page text)''')
        #pass
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        pass
    def process_item(self, item, spider):
        col = ','.join(item.keys())
        placeholder = ','.join(len(item) * '?')
        sql = "INSERT INTO lihkg ({}) VALUES({})"
        print(sql.format(col, placeholder))
        self.cursor.execute(sql.format(col, placeholder), list(item.values()))
        return item
