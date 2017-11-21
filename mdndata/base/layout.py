import scrapy


class Layout(dict):
    @classmethod
    def parse(cls, context, request=None):
        obj = cls()

        if request is None:
            request = context
            obj = request.meta.get('object', obj)

        if isinstance(context, list):
            for x in context:
                yield from cls.parse(x, request)

        elif getattr(cls, 'url', None) is ... and context != request:
            # If we're not at top level and get a class that has its own unknown URL,
            # we hopefully are parsing a link and need to make a new request.
            # We also yield an object to get inserted in the right place in the tree
            # that will get filled with the data once the request is processed.
            yield obj
            yield request.follow(context, callback=cls.parse, meta={'object': obj})

        else:
            parsers = {}

            for supercls in reversed(cls.mro()):
                parsers.update(vars(supercls))

            obj.update(
                {
                    key: list(value.parse(context, request))
                    for key, value in parsers.items()
                    if not key.startswith('_') and hasattr(value, 'parse') and
                    not isinstance(value, (type, str, type(...)))
                }
            )

            # Bubble up all requests
            for key in obj:
                values = obj[key]

                for value in values.copy():
                    if isinstance(value, scrapy.Request):
                        yield value
                        values.remove(value)

                if not getattr(cls, key).plural:
                    obj[key] = values[0] if values else None

            if hasattr(obj, 'substitute_parse_results'):
                yield from obj.substitute_parse_results()
            else:
                yield obj


class AnnotatedDescriptor:
    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name

    @property
    def annotation(self):
        for cls in self.owner.mro():
            if self.name in cls.__annotations__:
                return cls.__annotations__[self.name]

    @property
    def cls(self):
        return self.annotation if not self.plural else self.annotation[0]

    @property
    def plural(self):
        return isinstance(self.annotation, list)

    def __get__(self, obj, owner=None):
        return obj.get(self.name, None) if obj is not None else self


class XPath(AnnotatedDescriptor):
    def __init__(self, *paths):
        self.paths = paths

    def parse(self, context, request=None):
        result = context

        for path in self.paths:
            result = result.xpath(path)

        yield from self.cls.parse(result, request)

    def __str__(self):
        return ', '.join(map(str, self.paths))

    def __repr__(self):
        paths = ', '.join(map(repr, self.paths))
        return f'{type(self).__qualname__}({paths})'

    def __rshift__(self, other):
        return type(self)(*(self.paths + (str(other),)))

    def __and__(self, other):
        return type(self)(f'set:intersection({self}, {other})')

    def __sub__(self, other):
        return type(self)(f'set:difference({self}, {other})')

    def until(self, *stoppers):
        mask = type(self)('.|following-sibling::*')

        for stopper in stoppers:
            exclusion = f'following-sibling::{stopper}[1]'
            mask -= f'{exclusion}|{exclusion}/following-sibling::*'

        return self >> mask
