# -*- coding: utf-8 -*-

from .core import create_component

# From https://developer.mozilla.org/en-US/docs/Web/HTML/Element

# == Main root ==

html = create_component(
    'html',
    docs="""
        The HTML <html> element represents the root (top-level element) of an HTML
        document, so it is also referred to as the root element. All other elements must
        be descendants of this element.
        
        
    """,
)


# == Document metadata ==
# Metadata contains information about the page. This includes information about
# styles, scripts and data to help software (search engines, browsers, etc.) use
# and render the page. Metadata for styles and scripts may be defined in the
# page or link to another file that has the information.
link = create_component(
    'link',
    docs="""
        The HTML <link> element specifies relationships between the current document and
        an external resource. Possible uses for this element include defining a
        relational framework for navigation. This element is most used to link to style
        sheets.
        
        Notes
    """,
)

meta = create_component(
    'meta',
    docs="""
        The HTML <meta> element represents metadata that cannot be represented by other
        HTML meta-related elements, like <base>, <link>, <script>, <style> or <title>.
        
        Notes
    """,
)

style = create_component(
    'style',
    docs="""
        The HTML <style> element contains style information for a document, or part of a
        document. By default, the style instructions written inside that element are
        expected to be CSS.
        
        
    """,
)


# == Sectioning root ==

body = create_component(
    'body',
    docs="""
        The HTML <body> Element represents the content of an HTML document. There can be
        only one <body> element in a document.
        
        
    """,
)


# == Content sectioning ==
# Content sectioning elements allow you to organize the document content into
# logical pieces. Use the sectioning elements to create a broad outline for your
# page content, including header and footer navigation, and heading elements to
# identify sections of content.
address = create_component(
    'address',
    docs="""
        The HTML <address> element supplies contact information for its nearest
        <article> or <body> ancestor; in the latter case, it applies to the whole
        document.
        
        
    """,
)

article = create_component(
    'article',
    docs="""
        The HTML <article> element represents a self-contained composition in a
        document, page, application, or site, which is intended to be independently
        distributable or reusable (e.g., in syndication). Examples include: a forum
        post, a magazine or newspaper article, or a blog entry.
        
        
    """,
)

aside = create_component(
    'aside',
    docs="""
        The HTML <aside> element represents a section of a document with content
        connected tangentially to the main content of the document (often presented as a
        sidebar).
        
        
    """,
)

footer = create_component(
    'footer',
    docs="""
        The HTML <footer> element represents a footer for its nearest sectioning content
        or sectioning root element. A footer typically contains information about the
        author of the section, copyright data or links to related documents.
        
        
    """,
)

# FIXME: invalid character in identifier (<unknown>, line 1)
# h1–h6 = create_component('h1–h6', docs = """
#         The HTML <h1>–<h6> elements represent six levels of section headings. <h1> is
#         the highest section level and <h6> is the lowest.
#         
#         
#     """,)
header = create_component(
    'header',
    docs="""
        The HTML <header> element represents introductory content, typically a group of
        introductory or navigational aids. It may contain some heading elements but also
        other elements like a logo, a search form, an author name, and so on.
        
        
    """,
)

hgroup = create_component(
    'hgroup',
    docs="""
        This is an experimental technologyBecause this technology's specification has
        not stabilized, check the compatibility table for usage in various browsers.
        Also note that the syntax and behavior of an experimental technology is subject
        to change in future versions of browsers as the specification changes. The HTML
        <hgroup> element represents a multi-level heading for a section of a document.
        It groups a set of <h1>–<h6> elements.
        
        
    """,
)

nav = create_component(
    'nav',
    docs="""
        The HTML <nav> element represents a section of a page whose purpose is to
        provide navigation links, either within the current document or to other
        documents. Common examples of navigation sections are menus, tables of contents,
        and indexes.
        
        
    """,
)

section = create_component(
    'section',
    docs="""
        The HTML <section> element represents a standalone section of functionality
        contained within an HTML document, typically with a heading, which doesn't have
        a more specific semantic element to represent it.As an example, a navigation
        menu should be wrapped in a <nav> element, but a list of search results and a
        map display and its controls don't have specific elements, and could be put
        inside a <section>.
        
        
    """,
)


# == Text content ==
# Use HTML text content elements to organize blocks or sections of content
# placed between the opening <body> and closing </body> tags. Important for
# accessibility and SEO, these elements identify the purpose or structure of
# that content.
blockquote = create_component(
    'blockquote',
    docs="""
        The HTML <blockquote> Element (or HTML Block Quotation Element) indicates that
        the enclosed text is an extended quotation. Usually, this is rendered visually
        by indentation (see Notes for how to change it). A URL for the source of the
        quotation may be given using the cite attribute, while a text representation of
        the source can be given using the <cite> element.
        
        Notes
    """,
)

dd = create_component(
    'dd',
    docs="""
        The HTML <dd> element indicates the description of a term in a description list
        (<dl>).
        
        
    """,
)

div = create_component(
    'div',
    docs="""
        The HTML <div> element is the generic container for flow content and does not
        inherently represent anything. Use it to group elements for purposes such as
        styling (using the class or id attributes), marking a section of a document in a
        different language (using the lang attribute), and so on.
        
        
    """,
)

dl = create_component(
    'dl',
    docs="""
        The HTML <dl> element represents a description list. The element encloses a list
        of groups of terms and descriptions. Common uses for this element are to
        implement a glossary or to display metadata (a list of key-value pairs).
        
        Notes
    """,
)

dt = create_component(
    'dt',
    docs="""
        The HTML <dt> element identifies a term in a description list. This element can
        occur only as a child element of a <dl>. It is usually followed by a <dd>
        element; however, multiple <dt> elements in a row indicate several terms that
        are all defined by the immediate next <dd> element.
        
        
    """,
)

figcaption = create_component(
    'figcaption',
    docs="""
        The HTML <figcaption> element represents a caption or a legend associated with a
        figure or an illustration described by the rest of the data of the <figure>
        element which is its immediate ancestor.
        
        
    """,
)

figure = create_component(
    'figure',
    docs="""
        The HTML <figure> element represents self-contained content, frequently with a
        caption (<figcaption>), and is typically referenced as a single unit.
        
        
    """,
)

hr = create_component(
    'hr',
    docs="""
        The HTML <hr> element represents a thematic break between paragraph-level
        elements (for example, a change of scene in a story, or a shift of topic with a
        section). In previous versions of HTML, it represented a horizontal rule. It may
        still be displayed as a horizontal rule in visual browsers, but is now defined
        in semantic terms, rather than presentational terms.
        
        
    """,
)

li = create_component(
    'li',
    docs="""
        The HTML <li> element is used to represent an item in a list. It must be
        contained in a parent element: an ordered list (<ol>), an unordered list (<ul>),
        or a menu (<menu>). In menus and unordered lists, list items are usually
        displayed using bullet points. In ordered lists, they are usually displayed with
        an ascending counter on the left, such as a number or letter.
        
        
    """,
)

main = create_component(
    'main',
    docs="""
        The HTML <main> element represents the main content of the <body> of a document,
        portion of a document, or application. The main content area consists of content
        that is directly related to, or expands upon the central topic of, a document or
        the central functionality of an application.You can use multiple <main> elements
        within the same page when it makes sense to do so. For instance, if you have a
        page presenting multiple articles (each inside an <article> element, each of
        which has some extra material within (such as toolbars for editing, ads, and so
        forth), it may make sense to include a <main> element within each article to
        identify the primary contents of that specific article.
        
        
    """,
)

ol = create_component(
    'ol',
    docs="""
        The HTML <ol> element represents an ordered list of items, typically rendered as
        a numbered list.
        
        
    """,
)

p = create_component(
    'p',
    docs="""
        The HTML <p> element represents a paragraph of text. Paragraphs are usually
        represented in visual media as blocks of text that are separated from adjacent
        blocks by vertical blank space and/or first-line indentation. Paragraphs are
        block-level elements.
        
        
    """,
)

pre = create_component(
    'pre',
    docs="""
        The HTML <pre> element represents preformatted text. Text within this element is
        typically displayed in a non-proportional ("monospace") font exactly as it is
        laid out in the file. Whitespace inside this element is displayed as typed.
        
        
    """,
)

ul = create_component(
    'ul',
    docs="""
        The HTML <ul> element represents an unordered list of items, typically rendered
        as a bulleted list.
        
        
    """,
)


# == Inline text semantics ==
# Use the HTML inline text semantic to define the meaning, structure, or style
# of a word, line, or any arbitrary piece of text.
a = create_component(
    'a',
    docs="""
        The HTML <a> element (or anchor element) creates a hyperlink to other web pages,
        files, locations within the same page, email addresses, or any other URL.
        
        Notes
    """,
)

abbr = create_component(
    'abbr',
    docs="""
        The HTML <abbr> element represents an abbreviation and optionally provides a
        full description for it. If present, the title attribute must contain this full
        description and nothing else.
        
        
    """,
)

b = create_component(
    'b',
    docs="""
        The HTML <b> element represents a span of text stylistically different from
        normal text, without conveying any special importance or relevance, and that is
        typically rendered in boldface.
        
        
    """,
)

bdi = create_component(
    'bdi',
    docs="""
        The HTML <bdi> element (bidirectional isolation) isolates a span of text that
        might be formatted in a different direction from other text outside it.This
        element is useful when embedding text with an unknown directionality, from a
        database for example, inside text with a fixed directionality.
        
        
    """,
)

bdo = create_component(
    'bdo',
    docs="""
        The HTML <bdo> element (bidirectional override) is used to override the current
        directionality of text. It causes the directionality of the characters to be
        ignored in favor of the specified directionality.
        
        Notes
    """,
)

br = create_component(
    'br',
    docs="""
        The HTML <br> element produces a line break in text (carriage-return). It is
        useful for writing a poem or an address, where the division of lines is
        significant.
        
        Notes
    """,
)

cite = create_component(
    'cite',
    docs="""
        The HTML <cite> element represents a reference to a creative work. It must
        include the title of a work or a URL reference, which may be in an abbreviated
        form according to the conventions used for the addition of citation metadata.
        
        
    """,
)

code = create_component(
    'code',
    docs="""
        The HTML <code> element represents a fragment of computer code. By default, it
        is displayed in the browser's default monospace font.
        
        
    """,
)

data = create_component(
    'data',
    docs="""
        The HTML <data> element links a given content with a machine-readable
        translation. If the content is time- or date-related, the <time> element must be
        used.
        
        
    """,
)

dfn = create_component(
    'dfn',
    docs="""
        The HTML <dfn> element represents the defining instance of a term.
        
        
    """,
)

em = create_component(
    'em',
    docs="""
        The HTML <em> element marks text that has stress emphasis. The <em> element can
        be nested, with each level of nesting indicating a greater degree of emphasis.
        
        
    """,
)

i = create_component(
    'i',
    docs="""
        The HTML <i> element represents a range of text that is set off from the normal
        text for some reason, for example, technical terms, foreign language phrases, or
        fictional character thoughts. It is typically displayed in italic type.
        
        Notes
    """,
)

kbd = create_component(
    'kbd',
    docs="""
        The HTML <kbd> element represents user input and produces an inline element
        displayed in the browser's default monospace font.
        
        
    """,
)

mark = create_component(
    'mark',
    docs="""
        The HTML <mark> element represents highlighted text, i.e., a run of text marked
        for reference purpose, due to its relevance in a particular context. For example
        it can be used in a page showing search results to highlight every instance of
        the searched-for word.
        
        
    """,
)

q = create_component(
    'q',
    docs="""
        The HTML <q> element  indicates that the enclosed text is a short inline
        quotation. This element is intended for short quotations that don't require
        paragraph breaks; for long quotations use the <blockquote> element.
        
        
    """,
)

rp = create_component(
    'rp',
    docs="""
        The HTML <rp> element is used to provide fall-back parentheses for browsers that
        do not support display of ruby annotations using the <ruby> element.
        
        
    """,
)

rt = create_component(
    'rt',
    docs="""
        The HTML <rt> element embraces pronunciation of characters presented in a ruby
        annotations, which are used to describe the pronunciation of East Asian
        characters. This element is always used inside a <ruby> element.
        
        
    """,
)

rtc = create_component(
    'rtc',
    docs="""
        The HTML <rtc> element embraces semantic annotations of characters presented in
        a ruby of <rb> elements used inside of <ruby> element. <rb> elements can have
        both pronunciation (<rt>) and semantic (<rtc>) annotations.
        
        
    """,
)

ruby = create_component(
    'ruby',
    docs="""
        The HTML <ruby> element represents a ruby annotation. Ruby annotations are for
        showing pronunciation of East Asian characters.
        
        
    """,
)

s = create_component(
    's',
    docs="""
        The HTML <s> element renders text with a strikethrough, or a line through it.
        Use the <s> element to represent things that are no longer relevant or no longer
        accurate. However, <s> is not appropriate when indicating document edits; for
        that, use the <del> and <ins> elements, as appropriate.
        
        
    """,
)

samp = create_component(
    'samp',
    docs="""
        The HTML <samp> element is an element intended to identify sample output from a
        computer program. It is usually displayed in the browser's default monotype font
        (such as Lucida Console).
        
        
    """,
)

small = create_component(
    'small',
    docs="""
        The HTML <small> element makes the text font size one size smaller (for example,
        from large to medium, or from small to x-small) down to the browser's minimum
        font size.  In HTML5, this element is repurposed to represent side-comments and
        small print, including copyright and legal text, independent of its styled
        presentation.
        
        Notes
    """,
)

span = create_component(
    'span',
    docs="""
        The HTML <span> element is a generic inline container for phrasing content,
        which does not inherently represent anything. It can be used to group elements
        for styling purposes (using the class or id attributes), or because they share
        attribute values, such as lang. It should be used only when no other semantic
        element is appropriate. <span> is very much like a <div> element, but <div> is a
        block-level element whereas a <span> is an inline element.
        
        
    """,
)

strong = create_component(
    'strong',
    docs="""
        The HTML <strong> element gives text strong importance, and is typically
        displayed in bold.
        
        
    """,
)

sub = create_component(
    'sub',
    docs="""
        The HTML <sub> element defines a span of text that should be displayed, for
        typographic reasons, lower, and often smaller, than the main span of text.
        
        
    """,
)

sup = create_component(
    'sup',
    docs="""
        The HTML <sup> element defines a span of text that should be displayed, for
        typographic reasons, higher, and often smaller, than the main span of text.
        
        
    """,
)

time = create_component(
    'time',
    docs="""
        The HTML <time> element represents either a time on a 24-hour clock or a precise
        date in the Gregorian calendar (with optional time and timezone information).
        
        
    """,
)

u = create_component(
    'u',
    docs="""
        The HTML <u> element renders text with an underline, a line under the baseline
        of its content. In HTML5, this element represents a span of text with an
        unarticulated, though explicitly rendered, non-textual annotation, such as
        labeling the text as being a proper name in Chinese text (a Chinese proper name
        mark), or labeling the text as being misspelled.
        
        
    """,
)

var = create_component(
    'var',
    docs="""
        The HTML <var> element represents a variable in a mathematical expression or a
        programming context.
        
        
    """,
)

wbr = create_component(
    'wbr',
    docs="""
        The HTML <wbr> element represents a word break opportunity—a position within
        text where the browser may optionally break a line, though its line-breaking
        rules would not otherwise create a break at that location.
        
        Notes
    """,
)


# == Image and multimedia ==
# HTML supports various multimedia resources such as images, audio, and video.
area = create_component(
    'area',
    docs="""
        The HTML <area> element defines a hot-spot region on an image, and optionally
        associates it with a hypertext link. This element is used only within a <map>
        element.
        
        Notes
    """,
)

audio = create_component(
    'audio',
    docs="""
        The HTML <audio> element is used to embed sound content in documents. It may
        contain one or more audio sources, represented using the src attribute or the
        <source> element: the browser will choose the most suitable one. It can also be
        the destination for streamed media, using a MediaStream.
        
        
    """,
)

img = create_component(
    'img',
    docs="""
        The HTML <img> element represents an image in the document.
        
        
    """,
)

map = create_component(
    'map',
    docs="""
        The HTML <map> element is used with <area> elements to define an image map (a
        clickable link area).
        
        
    """,
)

track = create_component(
    'track',
    docs="""
        The HTML <track> element is used as a child of the media elements <audio> and
        <video>. It lets you specify timed text tracks (or time-based data), for example
        to automatically handle subtitles. The tracks are formatted in WebVTT format
        (.vtt files) — Web Video Text Tracks.
        
        
    """,
)

video = create_component(
    'video',
    docs="""
        Use the HTML <video> element to embed video content in a document.
        
        
    """,
)


# == Embedded content ==
# In addition to regular multimedia content, HTML can include a variety of other
# content, even if it's not always easy to interact with.
embed = create_component(
    'embed',
    docs="""
        The HTML <embed> element represents an integration point for an external
        application or interactive content (in other words, a plug-in).Note: This topic
        documents only the element that is defined as part of HTML5. It does not address
        earlier, non-standardized implementation of the element.
        
        
    """,
)

object = create_component(
    'object',
    docs="""
        The HTML <object> element represents an external resource, which can be treated
        as an image, a nested browsing context, or a resource to be handled by a plugin.
        
        
    """,
)

param = create_component(
    'param',
    docs="""
        The HTML <param> element defines parameters for an <object> element.
        
        
    """,
)

source = create_component(
    'source',
    docs="""
        The HTML <source> element specifies multiple media resources for either the
        <picture>, the <audio> or the <video> element. It is an empty element. It is
        commonly used to serve the same media content in multiple formats supported by
        different browsers.
        
        
    """,
)


# == Scripting ==
# In order to create dynamic content and Web applications, HTML supports the use
# of scripting languages, most prominently JavaScript. Certain elements support
# this capability.
canvas = create_component(
    'canvas',
    docs="""
        Use the HTML <canvas> element with the canvas scripting API to draw graphics and
        animations.
        
        
    """,
)

noscript = create_component(
    'noscript',
    docs="""
        The HTML <noscript> element defines a section of HTML to be inserted if a script
        type on the page is unsupported or if scripting is currently turned off in the
        browser.
        
        
    """,
)

script = create_component(
    'script',
    docs="""
        The HTML <script> element is used to embed or reference an executable script.
        
        Notes
    """,
)


# == Demarcating edits ==
# These elements let you provide indications that specific parts of the text
# have been altered.
del_ = create_component(
    'del',
    docs="""
        The HTML <del> element represents a range of text that has been deleted from a
        document. This element is often (but need not be) rendered with strike-through
        text.
        
        
    """,
)

ins = create_component(
    'ins',
    docs="""
        The HTML <ins> element represents a range of text that has been added to a
        document.
        
        
    """,
)


# == Table content ==
# The elements here are used to create and handle tabular data.
caption = create_component(
    'caption',
    docs="""
        The HTML <caption> element represents the title of a table. Though it is always
        the first descendant of a <table>, its styling, using CSS, may place it
        elsewhere, relative to the table.
        
        
    """,
)

col = create_component(
    'col',
    docs="""
        The HTML <col> element defines a column within a table and is used for defining
        common semantics on all common cells. It is generally found within a <colgroup>
        element.This element allows styling columns using CSS, but only a few attributes
        will have an effect on the column (see the CSS 2.1 specification for a list).
        
        
    """,
)

colgroup = create_component(
    'colgroup',
    docs="""
        The HTML <colgroup> element defines a group of columns within a table.
        
        
    """,
)

table = create_component(
    'table',
    docs="""
        The HTML <table> element represents tabular data — that is, information
        expressed via a two-dimensional data table.
        
        
    """,
)

tbody = create_component(
    'tbody',
    docs="""
        The HTML <tbody> element groups one or more <tr> elements as the body of a
        <table> element.
        
        
    """,
)

td = create_component(
    'td',
    docs="""
        The HTML <td> element defines a cell of a table that contains data. It
        participates in the table model.
        
        
    """,
)

tfoot = create_component(
    'tfoot',
    docs="""
        The HTML <tfoot> element defines a set of rows summarizing the columns of the
        table.
        
        
    """,
)

th = create_component(
    'th',
    docs="""
        The HTML <th> element defines a cell as header of a group of table cells. The
        exact nature of this group is defined by the scope and headers attributes.
        
        
    """,
)

thead = create_component(
    'thead',
    docs="""
        The HTML <thead> element defines a set of rows defining the head of the columns
        of the table.
        
        
    """,
)

tr = create_component(
    'tr',
    docs="""
        The HTML <tr> element specifies that the markup contained inside the <tr> block
        comprises one row of a table, inside which the <th> and <td> elements create
        header and data cells, respectively, within the row. Each cell is placed into
        its own column; the user agent follows specific rules to determine how the cells
        in each row are placed into columns with those coming from other rows.To provide
        additional control over how cells fit into (or span across) columns, both <th>
        and <td> support the colspan attribute, which lets you specify how many columns
        wide the cell should be, with the default being 1. Similarly, you can use
        the rowspan attribute on cells to indicate they should span more than one table
        row.This can take a little practice to get right when building your tables. We
        have some examples below, but for more examples and an in-depth tutorial, see
        the HTML tables series in our Learn web development area, where you'll learn how
        to use the table elements and their attributes to get just the right layout and
        formatting for your tabular data.
        
        
    """,
)


# == Forms ==
# HTML provides a number of elements which can be used together to create forms
# which the user can fill out and submit to the Web site or application. There's
# a great deal of further information about this available in the HTML forms
# guide.
button = create_component(
    'button',
    docs="""
        The HTML <button> element represents a clickable button.
        
        Notes
    """,
)

datalist = create_component(
    'datalist',
    docs="""
        The HTML <datalist> element contains a set of <option> elements that represent
        the values available for other controls.
        
        
    """,
)

fieldset = create_component(
    'fieldset',
    docs="""
        The HTML <fieldset> element is used to group several controls as well as labels
        (<label>) within a web form.
        
        
    """,
)

form = create_component(
    'form',
    docs="""
        The HTML <form> element represents a document section that contains interactive
        controls to submit information to a web server.It is possible to use the :valid
        and :invalid CSS pseudo-classes to style a <form> element.
        
        
    """,
)

input = create_component(
    'input',
    docs="""
        The HTML <input> element is used to create interactive controls for web-based
        forms in order to accept data from the user.
        
        Notes
    """,
)

label = create_component(
    'label',
    docs="""
        The HTML <label> element represents a caption for an item in a user interface.
        
        
    """,
)

legend = create_component(
    'legend',
    docs="""
        The HTML <legend> element represents a caption for the content of its parent
        <fieldset>.
        
        
    """,
)

meter = create_component(
    'meter',
    docs="""
        The HTML <meter> element represents either a scalar value within a known range
        or a fractional value.
        
        
    """,
)

optgroup = create_component(
    'optgroup',
    docs="""
        The HTML <optgroup> element creates a grouping of options within a <select>
        element.
        
        
    """,
)

option = create_component(
    'option',
    docs="""
        The HTML <option> element is used to define an item contained in a <select>, an
        <optgroup>, or a <datalist> element. As such, <option> can represent menu items
        in popups and other lists of items in an HTML document.
        
        
    """,
)

output = create_component(
    'output',
    docs="""
        Introduced in HTML5 The HTML <output> element represents the result of a
        calculation or user action.
        
        
    """,
)

progress = create_component(
    'progress',
    docs="""
        Introduced in HTML5 The HTML <progress> element represents the completion
        progress of a task, typically displayed as a progress bar.
        
        
    """,
)

select = create_component(
    'select',
    docs="""
        The HTML <select> element represents a control that provides a menu of options:
        
        Notes
    """,
)

textarea = create_component(
    'textarea',
    docs="""
        The HTML <textarea> element represents a multi-line plain-text editing control.
        
        
    """,
)


# == Interactive elements ==
# HTML offers a selection of elements which help to create interactive user
# interface objects.
details = create_component(
    'details',
    docs="""
        The HTML <details> element is used as a disclosure widget from which the user
        can retrieve additional information.
        
        
    """,
)

dialog = create_component(
    'dialog',
    docs="""
        The HTML <dialog> element represents a dialog box or other interactive
        component, such as an inspector or window.
        
        
    """,
)

menu = create_component(
    'menu',
    docs="""
        This is an experimental technologyCheck the Browser compatibility table
        carefully before using this in production.  The HTML <menu> element represents a
        group of commands that a user can perform or activate. This includes both list
        menus, which might appear across the top of a screen, as well as context menus,
        such as those that might appear underneath a button after it has been clicked.
        
        
    """,
)

menuitem = create_component(
    'menuitem',
    docs="""
        This is an experimental technologyCheck the Browser compatibility table
        carefully before using this in production. The HTML <menuitem> element
        represents a command that a user is able to invoke through a popup menu. This
        includes context menus, as well as menus that might be attached to a menu
        button.A command can either be defined explicitly, with a textual label and
        optional icon to describe its appearance, or alternatively as an indirect
        command whose behavior is defined by a separate element. Commands can also
        optionally include a checkbox or be grouped to share radio buttons. (Menu items
        for indirect commands gain checkboxes or radio buttons when defined against
        elements <input type="checkbox"> and <input type="radio">.)
        
        
    """,
)

summary = create_component(
    'summary',
    docs="""
        The HTML <summary> element is used as a summary, caption, or legend for the
        content of a <details> element.
        
        
    """,
)


# == Web Components ==
# Web Components is an HTML-related technology which makes it possible to,
# essentially, create and use custom elements as if it were regular HTML. In
# addition, you can create custom versions of standard HTML elements.
content = create_component(
    'content',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.         The HTML <content> element—an obsolete part
        of the Web Components suite of technologies—was used inside of Shadow DOM as an
        insertion point, and wasn't meant to be used in ordinary HTML It has now been
        replaced by the <slot> element, which creates a point in the DOM at which a
        shadow DOM can be inserted. Note: Though present in early draft of the
        specifications and implemented in several browsers, this element has been
        removed in later versions of the spec.
        
        
    """,
)

element = create_component(
    'element',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.The HTML <element> element was part of Web Components; this element was
        intended to be used to define new custom DOM elements. It was removed in favor
        of a JavaScript-driven methodology for creating new custom elements; however,
        that technology is not mature and no browers fully implement it. Note: This
        element has been removed from the specification. See this for more information
        from the editor of the specification.
        
        
    """,
)

shadow = create_component(
    'shadow',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.The HTML <shadow> element—an obsolete part of the Web Components technology
        suite—was intended to be used as a shadow DOM insertion point. You might have
        used it if you have created multiple shadow roots under a shadow host. It is not
        useful in ordinary HTML.
        
        
    """,
)

slot = create_component(
    'slot',
    docs="""
        This is an experimental technologyCheck the Browser compatibility table
        carefully before using this in production. The HTML <slot> element—part of the
        Web Components technology suite—is a placeholder inside a web component that you
        can fill with your own markup, which lets you create separate DOM trees and
        present them together.
        
        
    """,
)

template = create_component(
    'template',
    docs="""
        The HTML <template> element is a mechanism for holding client-side content that
        is not to be rendered when a page is loaded but may subsequently be instantiated
        during runtime using JavaScript.Think of a template as a content fragment that
        is being stored for subsequent use in the document. While the parser does
        process the contents of the <template> element while loading the page, it does
        so only to ensure that those contents are valid; the element's contents are not
        rendered, however.
        
        
    """,
)


# == Obsolete and deprecated elements ==
# Warning: These are old HTML elements which are deprecated and should not be
# used. You should never use them in new projects, and should replace them in
# old projects as soon as you can. They are listed here for informational
# purposes only.
acronym = create_component(
    'acronym',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

applet = create_component(
    'applet',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.The HTML Applet Element (<applet>) identifies the inclusion of a Java applet.
        Note: The <applet> element was removed in Gecko 56 and Chrome in late 2015.
        Removal is being considered in WebKit and Edge.
        
        Notes
    """,
)

basefont = create_component(
    'basefont',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        Notes
    """,
)

big = create_component(
    'big',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

blink = create_component(
    'blink',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.            ObsoleteThis feature is obsolete. Although
        it may still work in some browsers, its use is discouraged since it could be
        removed at any time. Try to avoid using it.The HTML Blink Element (<blink>) is a
        non-standard element causing the enclosed text to flash slowly.Do not use this
        element as it is obsolete and bad design practice. Blinking text is frowned upon
        by several accessibility standards and the CSS specification allows browsers to
        ignore the blink value.
        
        
    """,
)

center = create_component(
    'center',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
        
        Note
    """,
)

command = create_component(
    'command',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it. Note: The command element has been removed from Gecko 24.0 in favor of the
        <menuitem> element. Firefox has never supported this command element, and the
        existing implementation of the HTMLCommandElement DOM interface has been dropped
        from Firefox 24.
        
        
    """,
)

content = create_component(
    'content',
    docs='',
)

dir = create_component(
    'dir',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

element = create_component(
    'element',
    docs='',
)

font = create_component(
    'font',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

frame = create_component(
    'frame',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
        
        
    """,
)

frameset = create_component(
    'frameset',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
        
        
    """,
)

image = create_component(
    'image',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.         Non-standard       This feature is non-standard and is not on a
        standards track. Do not use it on production sites facing the Web: it will not
        work for every user. There may also be large incompatibilities between
        implementations and the behavior may change in the future.       The HTML
        <image> element is an obsolete remnant of an ancient version of HTML lost in the
        mists of time; use the standard <img> element instead. Seriously, the
        specification even literally uses the words "Don't ask" when describing this
        element. Do not use this! In order to display images, use the standard <img>
        element. While browsers will attempt to automatically convert this into an <img>
        element, it won't always do so, and won't always succeed when it tries, due to
        the various ways this can happen. So just don't use it if you like your users.
        
        
    """,
)

isindex = create_component(
    'isindex',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

keygen = create_component(
    'keygen',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.         The HTML <keygen> element exists to
        facilitate generation of key material, and submission of the public key as part
        of an HTML form. This mechanism is designed for use with Web-based certificate
        management systems. It is expected that the <keygen> element will be used in an
        HTML form along with other information needed to construct a certificate
        request, and that the result of the process will be a signed certificate. There
        is currently discussion among Web browser makers whether to keep this feature or
        not. Until a decision is reached, it is better to continue to consider this
        feature as deprecated and going away.
        
        
    """,
)

listing = create_component(
    'listing',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

marquee = create_component(
    'marquee',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.The HTML <marquee> element is used to insert a scrolling area of text. You
        can control what happens when the text reaches the edges of its content area
        using its attributes. The <marquee> element is obsolete and must not be used.
        While some browsers still support it, it's not required.
        
        
    """,
)

multicol = create_component(
    'multicol',
    docs="""
        Non-standard       This feature is non-standard and is not on a standards track.
        Do not use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between implementations and the
        behavior may change in the future.         ObsoleteThis feature is obsolete.
        Although it may still work in some browsers, its use is discouraged since it
        could be removed at any time. Try to avoid using it.
        
        
    """,
)

nextid = create_component(
    'nextid',
    docs="""
        DeprecatedThis feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
        
        
    """,
)

noembed = create_component(
    'noembed',
    docs="""
        Non-standard       This feature is non-standard and is not on a standards track.
        Do not use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between implementations and the
        behavior may change in the future.                      DeprecatedThis feature
        has been removed from the Web standards. Though some browsers may still support
        it, it is in the process of being dropped. Avoid using it and update existing
        code if possible; see the compatibility table at the bottom of this page to
        guide your decision. Be aware that this feature may cease to work at any time.
        The <noembed> element is a deprecated and non-standard way to provide
        alternative, or "fallback", content for browsers that do not support the <embed>
        element or do not support embedded content an author wishes to use. This element
        was deprecated in HTML 4.01 and above in favor of  <object>. Fallback content
        should be inserted between the opening and closing <object> tags. While this
        element currently still works in many browsers, it has been deprecated and
        should not be used. Use <object> instead.
        
        
    """,
)

plaintext = create_component(
    'plaintext',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

shadow = create_component(
    'shadow',
    docs='',
)

spacer = create_component(
    'spacer',
    docs="""
        Non-standard       This feature is non-standard and is not on a standards track.
        Do not use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between implementations and the
        behavior may change in the future.         ObsoleteThis feature is obsolete.
        Although it may still work in some browsers, its use is discouraged since it
        could be removed at any time. Try to avoid using it.<spacer> is an obsolete HTML
        element which allowed insertion of empty spaces on pages. It was devised by
        Netscape to accomplish the same effect as a single-pixel layout image, which was
        something web designers used to use to add white spaces to web pages without
        actually using an image. However, <spacer> no longer supported by any major
        browser and the same effects can now be achieved using simple CSS. Firefox,
        which is the descendant of Netscape's browsers, removed support for <spacer> in
        version 4.
        
        
    """,
)

strike = create_component(
    'strike',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

tt = create_component(
    'tt',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        Notes
    """,
)

xmp = create_component(
    'xmp',
    docs="""
        ObsoleteThis feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to avoid using
        it.
        
        
    """,
)

