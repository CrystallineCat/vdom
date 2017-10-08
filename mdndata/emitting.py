from keyword import iskeyword

from html2text import HTML2Text
from yapf.yapflib.yapf_api import FormatCode


class Section:

    def __init__(self, header, docs):
        self.header = header
        self.docs = docs

    def __str__(self):
        return '''
# == %s ==
# %s
'''.strip() % (str(self.header).title(), html.handle(repr(self.docs)).strip().replace('\n', '\n# '))


class Component:

    def __init__(self, tag, kwds):
        self.tag = tag
        self.kwds = kwds
        self.name = tag.replace('-', '_') + ('_' if iskeyword(tag) else '')

    def __str__(self):
        kwds = ', '.join('%s = %s' % (k, v) for k, v in self.kwds.items() if v is not None)
        code = '%s = createComponent(\'%s\', %s,)' % (self.name, self.tag, kwds)

        try:
            return FormatCode(code, style_config='pep8')[0]
        except SyntaxError as e:
            return '# FIXME: %s\n%s' % (e, code)


html = HTML2Text()
html.ignore_links = True


def triple_literal(content):
    text = html.handle(repr(content)).strip()

    if not text:
        return None

    if text.startswith('* '):
        text = '  ' + text

    return '"""\n        %s\n    """' % text.replace('\n', '\n        ')


def list_literal(iterable):
    obj = list(filter(lambda x: x is not None, map(str, iterable)))

    if not obj:
        return None

    return repr(obj)[:-1] + ',]'
