from .base import *
from .mdn import IndexPage, IndexCategory


class HTMLIndexPage(IndexPage):
    file_name = 'vdom/html.py'
    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'

    class HTMLCategory(IndexCategory):
        docs: ReST = XPath('following-sibling::*[1]').until('table')
        components = XPath('following-sibling::table[1]/tbody/tr/td[1]/a')

    categories: [HTMLCategory] = XPath('id("wikiArticle")/h2')
