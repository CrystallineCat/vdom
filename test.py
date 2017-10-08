from vdom import html, svg
from IPython.display import display, HTML

for key in dir(svg):
    if key.startswith('_'):
        continue

    element = getattr(svg, key)

    if not hasattr(element, 'examples'):
        continue

    display(html.h1(key))

    for example in element.examples:
        display(HTML(example))
