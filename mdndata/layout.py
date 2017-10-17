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
            obj.update(
                {
                    key: list(value.parse(context, request))
                    for key, value in vars(cls).items()
                    if not key.startswith('_') and hasattr(value, 'parse') and
                    not isinstance(value, (type, str, type(...)))
                }
            )

            # Bubble up all requests; using dict.items since obj might overwrite items
            for key, values in dict.items(obj):
                for value in values.copy():
                    if isinstance(value, scrapy.Request):
                        yield value
                        values.remove(value)

                if not getattr(cls, key).plural:
                    obj[key] = values[0] if values else None

            yield obj


class XPath:

    def __init__(self, value):
        self.value = value

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name

    @property
    def cls(self):
        cls = self.owner.__annotations__[self.name]
        return cls if not isinstance(cls, list) else cls[0]

    @property
    def plural(self):
        cls = self.owner.__annotations__[self.name]
        return isinstance(cls, list)

    def parse(self, context, request=None):
        result = context.xpath(self.value)
        yield from self.cls.parse(result, request)

    def __repr__(self):
        if self.cls is None:
            return f'{type(self).__qualname__}({self.value!r})'
        else:
            return f'{type(self).__qualname__}({self.value!r}, {self.cls.__qualname__})'

    def __get__(self, obj, owner=None):
        return obj.get(self.name, None) if obj is not None else self

    @classmethod
    def until(cls, head, *tail):
        return 'set:difference(%s, following-sibling::%s|following-sibling::%s/following-sibling::*)' % (
            cls.until(*tail) if tail else '.|following-sibling::*',
            head,
            head,
        )
