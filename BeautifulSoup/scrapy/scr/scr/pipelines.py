# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ScrPipeline(object):
#     def open_spider(self, spider):
#         self.conn = sqlite3.connect('scr.sqlite')
#         self.cur = self.conn.cursor()
#         self.cur.execute('create a table if not exist scr(title varchar(100), content text, time varchar(50));')
#         #pass
#     def close_spider(self, spider):
#         self.conn.commit()
#         self.conn.close()
#         pass
    def process_item(self, item, spider):
        # col = ','.join(item.key())
        # placeholder = ','.join(len(item))
        # sql = 'insert in scr ({}) value({})'
        # self.cur.execute(sql.format(col, placeholder), item.value())
        return item
