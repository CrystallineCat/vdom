from .layout_mdn import HTMLIndexPage, SVGIndexPage
from .spider import MDNDataSpider

import sys


if 'cached' in sys.argv:
    MDNDataSpider.use_cache(True)

scraped = MDNDataSpider.scrape(HTMLIndexPage, SVGIndexPage)

for item in scraped:
    print(f'Writing {item.file_name}...')

    with open(item.file_name, 'w', encoding='utf-8') as file:
        print(item, file=file)
