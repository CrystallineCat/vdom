from yapf.yapflib.yapf_api import FormatCode
from keyword import kwlist as keywords

import builtins
import re

from .layout import Layout
from .text import Text


class Comment(Text):
    def __str__(self):
        return str(self.map_lines('# %s'))


class Name(str):
    taken_names = set(keywords) | vars(builtins).keys()

    @staticmethod
    def __new__(cls, name):
        name = re.sub('\{.+\}', '',name).replace('-', '_')
        name = name + ('_' if name in cls.taken_names else '')
        return super().__new__(cls, name)


class Call:
    def __init__(self, target, args, kwds):
        self.target = target
        self.args = tuple(args)
        self.kwds = dict(kwds)

    def __repr__(self):
        kwds = tuple(f'{k}={v!r}' for k, v in self.kwds.items())
        args = ', '.join(tuple(map(repr, self.args)) + kwds)
        return f'{self.target}({args})'


class Code(str):
    @staticmethod
    def __new__(cls, *code):
        code = ''.join(map(str, code))

        try:
            code = FormatCode(code, style_config='pep8')[0]
        except SyntaxError as e:
            code = Comment(f'FIXME: {e}\n{code}')

        return super().__new__(cls, code)
