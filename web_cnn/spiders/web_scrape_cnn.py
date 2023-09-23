import scrapy
from .. items import NewsItem

class WebScrapeCnnSpider(scrapy.Spider):
    name = "web_scrape_cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/"]

    def parse(self, response):

        newss = response.css('div.card.container__item.container__item--type-section.container_lead-plus-headlines__item.container_lead-plus-headlines__item--type-section')

        for news in newss:
            news_url = news.css('div.card.container__item.container__item--type-section.container_lead-plus-headlines__item.container_lead-plus-headlines__item--type-section a::attr(href)').get()
            yield response.follow(news_url, callback=self.parse_news_page)

    def parse_news_page(self, response):

        news_item = NewsItem()
        
        news_item['headline'] = response.css('div.headline__wrapper h1[id="maincontent"]::text').get(),
        news_item['timestamp'] = response.css('div.timestamp::text').get(),
        news_item['image_link'] = response.css('picture.image__picture img ::attr(src)').get(),
        news_item['local_image'] = ''

        yield news_item
