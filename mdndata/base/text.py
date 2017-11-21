import creole
import itertools
import lxml.html
import lxml.html.builder
import textwrap


class Text(str):

    @classmethod
    def parse(cls, context, request=None):
        yield cls(''.join(context.xpath('.//text()').extract()).strip())

    def wrap(self, n):
        return type(self)('\n\n'.join(filter(bool, (textwrap.fill(para, n) for para in self.split('\n\n')))))

    def map_lines(self, pattern):
        return '\n'.join(pattern % line for line in self.splitlines())

    def split_into_range(self, delimiter='-'):
        n0, n1 = self.split(delimiter)
        len_prefix = list(itertools.takewhile(lambda i: n0[i] == n1[i], range(min(len(n0), len(n1)))))[-1] + 1
        prefix = n0[:len_prefix]
        n0 = int(n0[len_prefix:])
        n1 = int(n1[len_prefix:])

        return tuple(f'{prefix}{n}' for n in range(n0, n1 + 1))

    def __str__(self):
        return self

    def __repr__(self):
        if '\n' not in self:
            return str.__repr__(self)

        return '"""\n        %s\n    """' % self.replace('\n', '\n        ')


class Tree:
    def __init__(self, tree=None):
        self.tree = tree
        self.process_tree()

    def process_tree(self):
        pass

    @classmethod
    def parse(cls, context, request=None):
        yield cls(lxml.html.builder.E.article(*[element.root for element in context.xpath('.')]))

    def __repr__(self):
        return repr(Text(self))

    def __str__(self):
        return lxml.html.tostring(self.tree, pretty_print=True).decode('utf8')


class ReST(Tree):
    def process_tree(self):
        for path in (
            './/a',
            './/em//strong',
            './/em//code',
            './/strong//em',
            './/strong//code',
            './/code//em',
            './/code//strong',
        ):
            for element in self.tree.xpath(path):
                element.drop_tag()

    def __str__(self):
        html = super().__str__()
        rest = Text(creole.html2rest(html).replace('\\', '\n\n')).wrap(70)

        return rest


class HTML(Tree):
    @classmethod
    def parse(cls, context, request=None):
        html = ''.join(context.xpath('.//text()').extract())

        try:
            yield cls(lxml.html.fromstring(f'<article>{html}</article>'))
        except lxml.etree.XMLSyntaxError:
            yield cls(lxml.html.builder.E.pre(html))
