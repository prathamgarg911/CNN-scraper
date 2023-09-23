# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests
from urllib.request import urlretrieve
import os

count = 0

os.makedirs('./images', exist_ok = True)

class WebCnnPipeline:
    def download_image(self, value):
        global count
        count = count + 1
        output_path = f"./images/image{count}.jpg"
        urlretrieve(value[0], output_path)
        return output_path


    def process_item(self, item, spider):
    
        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == 'headline':
                value = adapter.get(field_name)
                if value[0]:
                    adapter[field_name] = value[0].strip()

            if field_name == 'timestamp':
                value = adapter.get(field_name)
                if value[0]:
                    adapter[field_name] = value[0].strip().split(',', 1)[1].strip()

            if field_name == 'image_link':
                value = adapter.get(field_name)
                local_path = self.download_image(value)
                adapter['local_image'] = local_path

        return item
