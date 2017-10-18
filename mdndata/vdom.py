from .base import *

import itertools


class ModuleEmitter(CodeEmitter):
    categories: [...]
    components = property(lambda self: [component for category in self.categories for component in category.components])
    component_names = property(lambda self: sorted({component.name for component in self.components}))

    emit = property(lambda self: (
        '# -*- coding: utf-8 -*-',
        'from vdom.core import Component',
        f'# From {self.url}',
        *self.categories,
        f'__all__ = {self.component_names!r}',
    ))

    def preprocess(self):
        first_appearance = {}

        for category in self.categories:
            for component in category.components:
                if component.tag_name in first_appearance:
                    component.disable(first_appearance[component.tag_name])
                else:
                    first_appearance[component.tag_name] = category.name


class CategoryEmitter(CodeEmitter):
    name: ...
    docs: ...
    components: [...]

    emit = property(lambda self: (
        self.name.wrap(72).map_lines('# == %s =='),
        self.docs.wrap(78).map_lines('# %s'),
        *self.components,
    ))


class ComponentEmitter(CodeEmitter):
    tag: ...
    content: ...
    tag_name = property(lambda self: self.tag[1:-1])
    base_name = property(lambda self: self.tag_name.replace('-', '_'))
    name = property(lambda self: self.base_name + ('_' if self.base_name in self.taken_names else ''))

    @property
    def code(self):
        content = '' if self.tag_name == self.name else f'tag_name = {self.tag_name!r}'

        return f'class {self.name}(Component):\n    {Text(self.content)!r}\n\n    {content}'

    other_appearance = None

    def disable(self, other_appearance):
        self.other_appearance = other_appearance

    @property
    def emit(self):
        if self.other_appearance:
            yield f'# {self.tag_name}: see above under {self.other_appearance!r}'
        else:
            yield self.code

    @property
    def parse_results(self):
        if '\N{EN DASH}' not in self.tag_name:
            yield self
            return

        # h1-h6 (with en dash) needs to become (h1, h2, h3, h4, h5, h6)
        n0, n1 = self.tag_name.split('\N{EN DASH}')
        len_prefix = list(itertools.takewhile(lambda i: n0[i] == n1[i], range(min(len(n0), len(n1)))))[-1] + 1
        prefix = n0[:len_prefix]
        n0 = int(n0[len_prefix:])
        n1 = int(n1[len_prefix:])

        for n in range(n0, n1 + 1):
            yield type(self)(tag=f'<{prefix}{n}>', content=self.content)
