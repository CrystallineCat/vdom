from mdndata.base import *
from mdndata.vdom import *
from yapf.yapflib.yapf_api import FormatCode

import re


class Call:
    def __init__(self, target, args, kwds):
        self.target = target
        self.args = tuple(args)
        self.kwds = dict(kwds)

    def __repr__(self):
        kwds = tuple(f'{k}={v!r}' for k, v in self.kwds.items())
        args = ', '.join(tuple(map(repr, self.args)) + kwds)
        return f'{self.target}({args})'


class ElementPage(Emitter):
    url = ...  # Filled in by the spider

    # TODO: Emit link to page
    # TODO: Fix relative urls
    # TODO: Handle 404s
    overview: ReST = XPath('id("wikiArticle")/*[1]').until('table', 'h2')
    notes: ReST = XPath('(id("Note")|id("Notes"))/following-sibling::*[1]').until('aside', 'h2') >> (XPath('.') - 'self::table')
    examples: HTML = XPath('(id("Example")|id("Examples"))[1]').until('h2') >> 'self::pre[@class="brush: html"]'

    @property
    def emit(self):
        if self.overview:
            yield self.overview

        if self.notes:
            yield 'Notes:'
            yield self.notes.map_lines('    %s')

        def transform(x):
            if not isinstance(x.tag, str):
                return Text(x.text).wrap(78).map_lines('# %s')

            args = [x.text] + [e for c in x for e in (transform(c), c.tail) if e is not None]

            if tuple(map(type, args)) == (str, str):
                args = [''.join(args)]

            def clean_whitespace(x, n, size):
                x = re.sub('\s+', ' ', x)

                if len(x) > 2 and x[0] == x[-1] == ' ' and n == 0:
                    x = x.strip()
                elif x == ' ': # and n in {0, size - 1}:
                    x = ''

                return x


            args = [clean_whitespace(arg, n, len(args)) if isinstance(arg, str) else arg for n, arg in enumerate(args)]
            args = [arg for arg in args if arg != '']

            tag = re.sub('\{.+\}', '', x.tag).replace('-', '_')
            tag += '_' if tag in CodeEmitter.taken_names else ''

            attrs = {re.sub('\{.+\}', '', k).replace('-', '_') + ('_' if k in CodeEmitter.taken_names else ''): v for k, v in x.attrib.items()}

            return Call(tag, [arg for arg in args if arg is not None], attrs)

        if self.examples:
            yield 'Examples::'

            for n, example in enumerate(self.examples):
                code = repr(transform(example))

                if n > 0:
                    yield '::'

                try:
                    yield Text(FormatCode(str(code), style_config='pep8')[0]).map_lines('    %s')
                except SyntaxError as e:
                    yield Text(f'FIXME: {e}\n{code}').map_lines('    # %s')


class ElementLink(ComponentEmitter, Layout):
    tag: Text = XPath('.')
    content: ElementPage = XPath('.')


class HTMLIndexPage(ModuleEmitter, Layout):
    file_name = 'vdom/html.py'
    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'

    class HTMLCategory(CategoryEmitter, Layout):
        name: Text = XPath('.')
        docs: ReST = XPath('following-sibling::*[1]').until('table')
        components: [ElementLink] = XPath('following-sibling::table[1]/tbody/tr/td[1]/a')

    categories: [HTMLCategory] = XPath('id("wikiArticle")/h2')


class SVGIndexPage(ModuleEmitter, Layout):
    file_name = 'vdom/svg.py'
    url = 'https://developer.mozilla.org/en-US/docs/Web/SVG/Element'

    class SVGCategory(CategoryEmitter, Layout):
        name: Text = XPath('.')
        docs: ReST = ReST()  # No category docs on the SVG page :(
        components: [ElementLink] = XPath('following-sibling::p[1]/a')

    categories: [SVGCategory] = XPath('id("SVG_elements_by_category")/following-sibling::h3')
