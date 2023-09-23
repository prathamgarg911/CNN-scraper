# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebCnnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    headline = scrapy.Field()
    timestamp = scrapy.Field()
    image_link = scrapy.Field()
    local_image = scrapy.Field()