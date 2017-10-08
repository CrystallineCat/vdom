from .emitting import *
from .scraping import *

from collections import OrderedDict


class MDNPage(Page):

    def __init__(self, *args, **kwds):
        super().__init__(selector='article#wikiArticle', *args, *kwds)


def save_code(kind, it):
    with open('vdom/%s.py' % kind, 'w', encoding='utf-8') as file:
        for x in it:
            print(str(x) + '\n', file=file)
            print(str(x) + '\n')


def scrape_page(index, categories, docs, links, tags=lambda tag: [tag]):
    yield '# -*- coding: utf-8 -*-'
    yield 'from .core import createComponent'
    yield '# From %s' % index.url

    done = {}

    for header, content in categories(index):
        yield Section(header, docs(header, content))

        for link in links(header, content):
            tag = str(link)[1:-1]

            if tag in done:
                yield '# %s: see under `%s` above\n' % (tag, done[tag])
                continue

            done[tag] = str(header).title()
            page = index.navigate(link)
            kwds = scrape_element(page)

            for tag in tags(tag):
                yield Component(tag, kwds)


def scrape_element(page):
    if not page.exists:
        return OrderedDict(
            (
                ('url', repr(page.url)),
                ('notes', repr('FIXME: http response had status %s' % page.request.status_code)),
            )
        )

    docs = page.until('table', 'h2')
    examples = page.after('h2#Example', 'h2#Examples').until('h2').every('pre.html')
    # ^ NB: SVG examples also seem to use the html class
    notes = page.after('h2#Notes').until('h2')

    return OrderedDict(
        (
            ('url', repr(page.url)),
            ('docs', triple_literal(docs)),
            ('notes', triple_literal(notes)),
            ('examples', list_literal(examples)),
        )
    )


save_code(
    'html',
    scrape_page(
        MDNPage('http://developer.mozilla.org/en-US/docs/Web/HTML/Element'),
        categories=lambda article: article.split('h2', is_header=True),
        docs=lambda header, content: content.until('table'),
        links=lambda header, content: content.first('table').every('tbody tr td:first-child a'),
        tags=lambda tag: ['h%d' % (i + 1) for i in range(6)] if tag.startswith('h1') else [tag],
    ),
)
save_code(
    'svg',
    scrape_page(
        MDNPage('http://developer.mozilla.org/en-US/docs/Web/SVG/Element'),
        categories=lambda article: article.after('h2#SVG_elements_by_category').until('h2').split('h3', is_header=True),
        docs=lambda header, content: Content([]),
        links=lambda header, content: content.every('p a'),
    ),
)
