import scrapy
import scrapy.crawler


class MDNDataSpider(scrapy.Spider):
    name = 'mdndata'
    custom_settings = {
        'HTTPCACHE_ENABLED': False,
        'HTTPCACHE_POLICY': 'scrapy.extensions.httpcache.DummyPolicy',
    }

    def __init__(self, to_scrape, scraped):
        super().__init__()

        self.to_scrape = to_scrape
        self.scraped = scraped

    def start_requests(self):
        for cls in self.to_scrape:
            yield scrapy.Request(cls.url, meta={'class': cls})

    def parse(self, response):
        for item in response.meta['class'].parse(response):
            if isinstance(item, response.meta['class']):
                self.scraped.append(item)

            yield item

    @classmethod
    def use_cache(cls, use_cache):
        cls.custom_settings['HTTPCACHE_ENABLED'] = use_cache

    @classmethod
    def scrape(cls, *to_scrape):
        scraped = []

        process = scrapy.crawler.CrawlerProcess()
        process.crawl(cls, to_scrape=to_scrape, scraped=scraped)
        process.start()

        return scraped
