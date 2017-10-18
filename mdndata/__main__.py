from .base import Spider
from .mdn import HTMLIndexPage, SVGIndexPage

import sys


if 'cached' in sys.argv:
    Spider.use_cache(True)

scraped = Spider.scrape(HTMLIndexPage, SVGIndexPage)

for item in scraped:
    print(f'Writing {item.file_name}...')

    with open(item.file_name, 'w', encoding='utf-8') as file:
        print(item, file=file)
