from .layout import *

from keyword import iskeyword
import textwrap
from yapf.yapflib.yapf_api import FormatCode


def render_html(element):
    return lxml.html.tostring(element).decode('utf-8')


class Text(str):

    @classmethod
    def parse(cls, context, request=None):
        yield cls(''.join(context.xpath('.//text()').extract()).strip())

    def wrap(self, n):
        return type(self)(textwrap.fill(self, n))

    def map_lines(self, pattern):
        return type(self)('\n'.join(pattern % line for line in self.splitlines()))

    def __str__(self):
        return self.wrap(80)

    def __repr__(self):
        if '\n' not in self:
            return str.__repr__(self)

        text = self

        if text.startswith('* '):
            text = '  ' + text

        return '"""\n        %s\n    """' % text.replace('\n', '\n        ')


def component(tag, **kwds):
    name = tag.replace('-', '_') + ('_' if iskeyword(tag) else '')
    kwds = ', '.join(f'{k} = {v!r}' for k, v in kwds.items() if v is not None)
    code = f'{name} = create_component({tag!r}, {kwds},)'

    try:
        return Text(FormatCode(code, style_config='pep8')[0])

    except SyntaxError as e:
        return Text(f'FIXME: {e}\n{code}').map_lines('# %s')


class Element(Layout):
    url = ...

    class Docs(Layout):
        overview: Text = XPath(XPath.until('table', 'h2'))
        notes: Text = XPath('id("Notes")')

    docs: Docs = XPath('id("wikiArticle")/*[1]')


class HTMLIndex(Layout):
    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'

    class Category(Layout):

        class Item(Layout):
            tag: Text = XPath('.')
            content: Element = XPath('.')

        name: Text = XPath('.')
        docs: Text = XPath('set:intersection(following-sibling::*, %s)' % XPath.until('table[1]'))
        items: [Item] = XPath('following-sibling::table[1]/tbody/tr/td[1]/a')

    categories: [Category] = XPath('id("wikiArticle")/h2')

#svg_index_layout = (
#    Every('article#wikiArticle > *') | After('h2#SVG_elements_by_category') | Until('h2') | Subdivisions('h3') |
#    Collect(
#        category=First('h3') | Collect(render_text),
#        overview=(),
#        items=Every('p a') | Collect(
#            tag=Collect(render_text),
#            content=Collect(svg_index.navigate) | element_page_layout,
#        ),
#    )
#)


# Assigning __str__ methods below to keep parsing and emitting separated in code:
Layout.__str__ = lambda self: '\n\n'.join(map(str, dict.values(self)))
HTMLIndex.__str__ = lambda self: '\n\n'.join(
    (
        '# -*- coding: utf-8 -*-',
        'from .core import create_component',
        f'# From {self.url}',
    ) + tuple(map(str, self.categories))
)
HTMLIndex.Category.__str__ = lambda self: '\n'.join(
    (
        self.name.wrap(72).map_lines('# == %s =='),
        self.docs.wrap(78).map_lines('# %s'),
    ) + tuple(map(str, self.items))
)
HTMLIndex.Category.Item.__str__ = lambda self: component(self.tag[1:-1], docs=Text(self.content))
