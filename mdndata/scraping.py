import urllib

import lxml.html
import requests
import requests_cache

requests_cache.install_cache('.scraping.cache')


class Content:

    def __init__(self, elements):
        self.elements = [x.primitive if isinstance(x, Element) else x for x in elements]

    def until(self, *selectors, inclusive=False):
        selector = ', '.join(selectors)
        until = []

        for element in self.elements:
            if element.cssselect(selector):
                if inclusive:
                    until.append(element)
                break

            until.append(element)
        else:
            if inclusive:
                until.append(None)

        return Content(until)

    def after(self, *selectors):
        selector = ', '.join(selectors)
        after = None

        for element in self.elements:
            if after is None:
                if element.cssselect(selector):
                    after = []
            else:
                after.append(element)

        return Content([] if after is None else after)

    def every(self, *selectors):
        selector = ', '.join(selectors)
        every = []

        for element in self.elements:
            every += element.cssselect(selector)

        return Content(every)

    def first(self, *selectors):
        selector = ', '.join(selectors)

        for element in self.elements:
            for match in element.cssselect(selector):
                return Element(match)

        return Element(None)

    def split(self, *selectors, is_header=False):
        selector = ', '.join(selectors)
        chunks = [[]]

        for element in self.elements:
            if element.cssselect(selector):
                chunks.append([])

            chunks[-1].append(element)

        if is_header:
            return [(Element(header), Content(content)) for header, *content in chunks[1:]]
        else:
            return [Content(content) for content in chunks]

    def __iter__(self):
        return iter([Element(x) for x in self.elements])

    def __repr__(self):
        return ''.join(map(repr, self))


class Element(Content):

    def __init__(self, primitive):
        self.primitive = primitive
        super().__init__([] if primitive is None else primitive)

    def __getattr__(self, name):
        return None if self.primitive is None else self.primitive.get(name)

    def __str__(self):
        return '' if self.primitive is None else self.primitive.text_content().strip()

    def __repr__(self):
        return '' if self.primitive is None else lxml.html.tostring(self.primitive).decode('utf-8')


class Page(Content):

    def __init__(self, url, base_url=None, selector='html'):
        if base_url:
            url = urllib.parse.urljoin(base_url, url)

        self.url = url
        self.request = requests.get(url)

        if self.request.status_code == 200:
            self.tree = lxml.html.fromstring(self.request.content)
            self.content = self.tree.cssselect(selector)[0]
            super().__init__(self.content)
        else:
            self.tree = None
            self.content = None
            super().__init__([])

    def navigate(self, element):
        return type(self)(element.href or element.src, self.url)

    @property
    def exists(self):
        return self.content is not None
