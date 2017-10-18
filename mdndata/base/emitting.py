from yapf.yapflib.yapf_api import FormatCode
from keyword import kwlist as keywords

import builtins

from .layout import Layout
from .text import Text


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
    taken_names = set(keywords) | vars(builtins).keys()

    def postprocess(self, emitted):
        try:
            return FormatCode(str(emitted), style_config='pep8')[0]
        except SyntaxError as e:
            return Text(f'FIXME: {e}\n{emitted}').map_lines('# %s')
