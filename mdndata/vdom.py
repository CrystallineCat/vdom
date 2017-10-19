from .base import *

import collections


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


class CategoryEmitter(CodeEmitter):
    name: ...
    docs: ...
    components: [...]

    emit = property(lambda self: (
        self.name.wrap(72).map_lines('# == %s =='),
        self.docs.wrap(78).map_lines('# %s'),
        *self.components,
    ))

    def preprocess(self):
        for component in self.components:
            component.category = self
            component.categories_by_tag_name[component.tag_name].append(self)


class ComponentEmitter(CodeEmitter):
    tag: ...
    content: ...
    tag_name = property(lambda self: self.tag[1:-1])
    base_name = property(lambda self: self.tag_name.replace('-', '_'))
    name = property(lambda self: self.base_name + ('_' if self.base_name in self.taken_names else ''))

    categories_by_tag_name = collections.defaultdict(list)
    first_appearance = property(lambda self: self.categories_by_tag_name[self.tag_name][0])

    category = None

    @property
    def emit(self):
        if self.category.name != self.first_appearance.name:
            yield f'# {self.tag_name}: see above under {self.first_appearance.name!r}'
            return

        yield '\n'.join((
            f'class {self.name}(Component):',
            f'    {Text(self.content)!r}',
            f'    tag_name = {self.tag_name!r}' if self.tag_name != self.name else '',
        )).strip()

    def substitute_parse_results(self):
        if '\N{EN DASH}' in self.tag_name:
            # h1-h6 (with en dash) needs to become (h1, h2, h3, h4, h5, h6)
            for tag_name in Text(self.tag_name).split_into_range('\N{EN DASH}'):
                yield type(self)(tag=f'<{tag_name}>', content=self.content)
        else:
            yield self
