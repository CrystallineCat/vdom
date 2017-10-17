import scrapy
import scrapy.crawler

from .spider import HTMLIndex


def save_code(kind, x):
    with open('vdom/%s.py' % kind, 'w', encoding='utf-8') as file:
        print(x, file=file)
        print(x)


class MDNDataSpider(scrapy.Spider):
    name = 'mdndata'
    custom_settings = {
        'HTTPCACHE_ENABLED': True,
        'HTTPCACHE_POLICY': 'scrapy.extensions.httpcache.DummyPolicy',
    }

    def start_requests(self):
        yield scrapy.Request(HTMLIndex.url, callback=HTMLIndex.parse)


items = []


def scraped(item, response, spider):
    if item.url is not ...:
        items.append(item)


process = scrapy.crawler.CrawlerProcess()
process.crawl(MDNDataSpider)

crawler = next(iter(process.crawlers))
crawler.signals.connect(scraped, signal=scrapy.signals.item_scraped)
process.start()

for x in items:
    save_code('html', x)

#save_code('svg', url % 'SVG', svg_index | svg_index_layout)
