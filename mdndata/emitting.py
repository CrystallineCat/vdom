import textwrap
import html2text

from yapf.yapflib.yapf_api import FormatCode

from .layout import Layout


class Text(str):
    @classmethod
    def parse(cls, context, request=None):
        yield cls(''.join(context.xpath('.//text()').extract()).strip())

    def wrap(self, n):
        return type(self)(textwrap.fill(self, n))

    def map_lines(self, pattern):
        return '\n'.join(pattern % line for line in self.splitlines())

    def __str__(self):
        return self.wrap(80).strip()

    def __repr__(self):
        if '\n' not in self:
            return str.__repr__(self)

        return '"""\n        %s\n    """' % self.replace('\n', '\n        ')


class HTML(Text):
    @classmethod
    def parse(cls, context, request=None):
        yield cls(''.join(
            html2text.html2text(element)
            for element in context.extract()
        ))


class Emitter(Layout):
    emit = property(lambda self: dict.values(self))

    def __str__(self):
        self.preprocess()
        return '\n\n'.join(filter(bool, map(self.postprocess, self.emit)))

    def preprocess(self):
        pass

    def postprocess(self, emitted):
        return str(emitted)


class CodeEmitter(Emitter):
    def postprocess(self, emitted):
        try:
            return FormatCode(str(emitted), style_config='pep8')[0]
        except SyntaxError as e:
            return Text(f'FIXME: {e}\n{emitted}').map_lines('# %s')
