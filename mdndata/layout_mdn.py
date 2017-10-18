from .emitting_vdom import *
from .layout import XPath


class ElementPage(Emitter):
    url = ...

    class Docs(Emitter, Layout):
        overview: HTML = XPath(XPath.until('table', 'h2'))
        notes: HTML = XPath('id("Notes")')

    docs: Docs = XPath('id("wikiArticle")/*[1]')


class ComponentLayout(ComponentEmitter, Layout):
    tag: Text = XPath('.')
    content: ElementPage = XPath('.')


class HTMLIndexPage(ModuleEmitter, Layout):
    file_name = 'vdom/html.py'
    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'

    class HTMLCategoryLayout(CategoryEmitter, Layout):
        replacements = {lambda self: self.name.startswith('h1'), ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')}

        name: Text = XPath('.')
        docs: HTML = XPath('set:intersection(following-sibling::*, %s)' % XPath.until('table[1]'))
        components: [ComponentLayout] = XPath('following-sibling::table[1]/tbody/tr/td[1]/a')

    categories: [HTMLCategoryLayout] = XPath('id("wikiArticle")/h2')


class SVGIndexPage(ModuleEmitter, Layout):
    file_name = 'vdom/svg.py'
    url = 'https://developer.mozilla.org/en-US/docs/Web/SVG/Element'

    class SVGCategoryLayout(CategoryEmitter, Layout):
        name: Text = XPath('.')
        docs: HTML = HTML()
        components: [ComponentLayout] = XPath('following-sibling::p[1]/a')

    categories: [SVGCategoryLayout] = XPath('id("SVG_elements_by_category")/following-sibling::h3')
