# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo

from itemadapter import ItemAdapter
from .connection import password

class MongodbPipeline:
    collection_name = "climatempo_dados"


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(f"mongodb+srv://admin:{password}@cluster0.tsc5b.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.db = self.client["climatempo"]

    def close_spider(self, spider):
        self.client.close()

    
    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
