from .base import *
from .vdom import *


class ElementPage(Layout):
    url = ...  # Filled in by the spider

    # TODO: Emit link to page
    # TODO: Fix relative urls
    # TODO: Handle 404s
    # TODO: Clean-up nested markup
    overview: ReST = XPath('id("wikiArticle")/*[1]').until('table', 'h2')
    notes: ReST = XPath('(id("Note")|id("Notes"))/following-sibling::*[1]').until('aside', 'h2') >> (XPath('.') - 'self::table')
    examples: [HTML] = XPath('(id("Example")|id("Examples"))[1]').until('h2') >> 'self::pre[@class="brush: html"]'


class LinkToElementPage(Layout):
    tag: Text = XPath('.')
    content: ElementPage = XPath('.')

    tag_name = property(lambda self: self.tag[1:-1])
    name = property(lambda self: Name(self.tag_name))

    def substitute_parse_results(self):
        if '\N{EN DASH}' not in self.tag_name:
            yield self
        else:
            # h1-h6 (with en dash) needs to become (h1, h2, h3, h4, h5, h6)
            for tag_name in Text(self.tag_name).split_into_range('\N{EN DASH}'):
                yield type(self)(tag=f'<{tag_name}>', content=self.content)


class IndexCategory(Layout):
    name: Text = XPath('.')
    docs: Text = ...
    components: [LinkToElementPage] = ...


class IndexPage(Layout):
    categories: [IndexCategory] = ...

    def __str__(self):
        return to_python(self)
