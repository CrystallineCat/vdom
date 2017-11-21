from .base import *
from .mdn import IndexPage, IndexCategory


class SVGCategory(IndexCategory):
    docs: ReST = None  # No category docs on the SVG page :(
    components = XPath('following-sibling::p[1]/a')


class SVGIndexPage(IndexPage):
    file_name = 'vdom/svg.py'
    url = 'https://developer.mozilla.org/en-US/docs/Web/SVG/Element'

    categories: [SVGCategory] = XPath('id("SVG_elements_by_category")/following-sibling::h3')
