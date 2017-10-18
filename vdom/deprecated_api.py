from warnings import warn

from .core import create_component, to_json


def toJSON(el, schema=None):
    """Convert an element to JSON

    WARNING: This call is deprecated in favor of to_json().

    If you wish to validate the JSON, pass in a schema via the schema keyword argument.
    If a schema is provided, this raises a ValidationError if JSON does not match the schema.
    """
    warn("toJSON is deprecated in favor of to_json")
    return to_json(el, schema)


def createElement(tagName):
    """Takes an HTML tag and creates a VDOM Component

    WARNING: This call is deprecated, as the name is the same as React.createElement
    while having an entirely different meaning.

    This is written more like a helper, similar to https://github.com/ohanhi/hyperscript-helpers
    allowing you to create code like

    div([
      p('hey')
    ])

    Instead of writing

    h('div', [
        h('p', 'hey')
    ])

    This should have been written more like React.createClass
    """
    warn("createElement is deprecated in favor of create_component")
    return create_component(tagName)


def createComponent(tagName):
    """Create a component for an HTML Tag

    WARNING: This call is deprecated in favor of create_component().

    Examples:
        >>> marquee = create_component('marquee')
        >>> marquee('woohoo')
        <marquee>woohoo</marquee>

    """
    warn("createComponent is deprecated in favor of create_component")
    return create_component(tagName)
