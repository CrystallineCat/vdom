from .base import *


def example_to_vdom(x):
    if not isinstance(x.tag, str):
        return Comment(x.text)

    args = [x.text] + [e for c in x for e in (transform(c), c.tail) if e is not None]

    if tuple(map(type, args)) == (str, str):
        args = [''.join(args)]

    def clean_whitespace(x):
        x = re.sub('\s+', ' ', x)
        return x.strip() if x[0] == x[-1] == ' ' else x

    args = [clean_whitespace(arg) if isinstance(arg, str) else arg for arg in args]
    args = [arg for arg in args if arg != '']

    attrs = {Name(k): v for k, v in x.attrib.items()}

    return Call(Name(x.tag), [arg for arg in args if arg is not None], attrs)


def to_doc_string(content):
    if content.overview:
        yield Text(content.overview)

    if content.examples:
        yield 'Examples::'
        yield Text(content.examples[0]).map_lines('    %s')

    if content.notes:
        yield 'Notes:'
        yield Text(content.notes).map_lines('    %s')


def to_python(index):
    def parts():
        yield Comment('-*- coding: utf-8 -*-')
        yield Code('from vdom.core import Component')
        yield Comment(f'From {index.url}')
        yield Code()

        seen = {}

        for category in index.categories:
            yield Comment(f'== {category.name} ==')

            if category.docs:
                yield Comment(category.docs).wrap(78)

            for component in category.components:
                if component.tag_name in seen:
                    yield Comment(f'{component.tag_name}: see above under "{seen[component.tag_name]}"')
                    continue

                seen[component.tag_name] = category.name

                yield Code(
                    f'class {component.name}(Component):',
                    repr(Text('\n\n'.join(to_doc_string(component.content)))),
                    f'    tag_name = {component.tag_name!r}' if component.tag_name != component.name else '',
                )

            yield Code()

        yield Code(f'__all__ = {list(seen.keys())!r}')

    return '\n'.join(filter(bool, map(str, parts())))
