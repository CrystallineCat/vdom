#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
vdom.core
~~~~~~~~~

This module provides the core implementation for the VDOM (Virtual DOM).

"""

from jsonschema import validate, Draft4Validator, ValidationError


def to_json(el, schema=None):
    """Convert an element to JSON

    If you wish to validate the JSON, pass in a schema via the schema keyword argument.
    If a schema is provided, this raises a ValidationError if JSON does not match the schema.
    """
    if (type(el) is str):
        return el
    if (type(el) is list):
        return list(map(to_json, el))
    elif (type(el) is dict):
        assert 'tagName' in el
        json_el = el.copy()
        if 'attributes' not in el:
            json_el['attributes'] = {}
        if 'children' not in el:
            json_el['children'] = []
    elif (hasattr(el, 'tagName') and hasattr(el, 'attributes')):
        json_el = {'tagName': el.tagName, 'attributes': el.attributes, 'children': to_json(el.children)}
    else:
        json_el = el

    if schema:
        try:
            validate(instance=json_el, schema=schema, cls=Draft4Validator)
        except ValidationError as e:
            raise ValidationError("Your object didn't match the schema: {}. \n {}".format(schema, e))

    return json_el


class VDOM():
    """A basic virtual DOM class which allows you to write literal VDOM spec

    >>> VDOM({ 'tagName': 'h1', 'children': 'Hey', 'attributes': {}})

    It's probably better to use `vdom.h` or the helper functions:

    >>> from vdom import h
    >>> h('h1', 'Hey')
    <h1 />

    >>> from vdom.helpers import h1
    >>> h1('Hey')

    """

    def __init__(self, obj):
        self.obj = obj

    def _repr_mimebundle_(self, include, exclude, **kwargs):
        return {'application/vdom.v1+json': to_json(self.obj)}


def _flatten_children(*children, **kwargs):
    '''Flattens *args to allow children to be passed as an array or as
    positional arguments.

    >>> _flatten_children("a", "b", "c")
    ["a", "b", "c"]

    >>> _flatten_children(["a", "b"])
    ["a", "b"]

    >>> _flatten_children(children=["c", "d"])
    ["c", "d"]

    >>> _flatten_children()
    []

    '''
    # children as keyword argument takes precedence
    if ('children' in kwargs):
        children = kwargs['children']
    elif children is not None:
        if len(children) == 0:
            children = None
        elif len(children) == 1:
            # Flatten by default
            children = children[0]
        elif isinstance(children[0], list):
            # Only one level of flattening, just to match the old API
            children = children[0]
        else:
            children = list(children)
    else:
        # Empty list of children
        children = []
    return children


def create_component(tag_name, docs=None):
    """Create a component for an HTML Tag

    Examples:
        >>> marquee = create_component('marquee')
        >>> marquee('woohoo')
        <marquee>woohoo</marquee>
    """

    docs = docs or """
        A virtual DOM component for a {tag_name} tag

        >>> {tag_name}()
        <{tag_name} />
    """.format(tag_name=tag_name)

    return type(tag_name, (Component,), {
        '__doc__': docs or default_docs,
        'tag_name': tag_name,
    })


class Component():
    """A basic class for a virtual DOM Component"""

    def __init__(self, *children, **kwargs):
        self.children = _flatten_children(*children, **kwargs)
        self.attributes = kwargs

    @property
    def tag_name(self):
        return self.__name__

    def _repr_mimebundle_(self, include, exclude, **kwargs):
        return {
            'application/vdom.v1+json': to_json(self),
            'text/plain': '<{tag_name} />'.format(tag_name=self.tag_name),
        }


def h(tag_name, *children, **kwargs):
    """Takes an HTML Tag, children (string, array, or another element), and attributes

    Examples:

      >>> h('div', [h('p', 'hey')])
      <div><p>hey</p></div>

    """
    attrs = {}
    if 'attrs' in kwargs:
        attrs = kwargs.pop('attrs')

    attrs = attrs.copy()
    attrs.update(kwargs)

    el = create_component(tag_name)
    return el(children, **attrs)


# These are left for backwards compatibility, from here on out we should
# define these in vdom.helpers, just like hyperscript-helpers
h1 = create_component('h1')
p = create_component('p')
div = create_component('div')
img = create_component('img')
b = create_component('b')
