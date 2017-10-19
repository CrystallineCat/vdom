import creole
import itertools
import lxml.etree
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
        return self.wrap(80).strip()

    def __repr__(self):
        if '\n' not in self:
            return str.__repr__(self)

        return '"""\n        %s\n    """' % self.replace('\n', '\n        ')


class ReST(Text):

    @classmethod
    def parse(cls, context, request=None):
        yield cls('\n\n'.join(creole.html2rest(html) for html in context.extract()))


class HTML(list):

    @classmethod
    def parse(cls, context, request=None):
        for html in context.xpath('.//text()').extract():
            try:
                yield cls(lxml.etree.fromstring(f'<article>{html}</article>'))
            except lxml.etree.XMLSyntaxError:
                pass
