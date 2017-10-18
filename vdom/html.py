# -*- coding: utf-8 -*-

from vdom.core import create_component

# From https://developer.mozilla.org/en-US/docs/Web/HTML/Element

# == Main root ==

html = create_component(
    'html',
    """
        The **HTML`<html>` element** represents the root (top-level element) of an
        HTML document, so it is also referred to as the _root element_. All other
        elements must be descendants of this element.
    """,
)

# == Document metadata ==

# Metadata contains information about the page. This includes information about
# styles, scripts and data to help software ([search engines](/en-
# US/docs/Glossary/search_engine "search engines: A search engine is a software
# system that collects information from the World Wide Web and presents it to
# users who are looking for specific information."), [browsers](/en-
# US/docs/Glossary/Browser "browsers: A Web browser is a program that retrieves
# and displays pages from the Web, and lets users access further pages through
# hyperlinks."), etc.) use and render the page. Metadata for styles and scripts
# may be defined in the page or link to another file that has the information.

link = create_component(
    'link',
    """
        The **HTML`<link>` element** specifies relationships between the current
        document and an external resource. Possible uses for this element include
        defining a relational framework for navigation. This element is most used to
        link to [style sheets](/en-US/docs/Glossary/CSS "Cascading Style Sheets").

        ## Notes
    """,
)

meta = create_component(
    'meta',
    """
        The **HTML`<meta>` element** represents [metadata](/en-
        US/docs/Glossary/Metadata "metadata: Metadata is — in its very simplest
        definition — data that describes data. For example, an HTML document is data,
        but HTML can also contain metadata in its <head> element that describes the
        document — for example who wrote it, and its summary.") that cannot be
        represented by other HTML meta-related elements, like [`<base>`](/en-
        US/docs/Web/HTML/Element/base "The HTML <base> element specifies the base URL to
        use for all relative URLs contained within a document. There can be only one
        <base> element in a document."), [`<link>`](/en- US/docs/Web/HTML/Element/link
        "The HTML <link> element specifies relationships between the current document
        and an external resource. Possible uses for this element include defining a
        relational framework for navigation. This element is most used to link to style
        sheets."), [`<script>`](/en- US/docs/Web/HTML/Element/script "The HTML <script>
        element is used to embed or reference an executable script."), [`<style>`](/en-
        US/docs/Web/HTML/Element/style "The HTML <style> element contains style
        information for a document, or part of a document. By default, the style
        instructions written inside that element are expected to be CSS.") or
        [`<title>`](/en-US/docs/Web/HTML/Element/title "The HTML <title> element defines
        the title of the document, shown in a browser's title bar or on the page's tab.
        It can only contain text, and any contained tags are ignored.").

        ## Notes
    """,
)

style = create_component(
    'style',
    """
        The **HTML`<style>` element** contains style information for a document,
        or part of a document. By default, the style instructions written inside that
        element are expected to be [CSS](/en-US/docs/Web/CSS).
    """,
)

# == Sectioning root ==

body = create_component(
    'body',
    """
        The **HTML`<body>` Element** represents the content of an HTML document.
        There can be only one `<body>` element in a document.
    """,
)

# == Content sectioning ==

# Content sectioning elements allow you to organize the document content into
# logical pieces. Use the sectioning elements to create a broad outline for your
# page content, including header and footer navigation, and heading elements to
# identify sections of content.

address = create_component(
    'address',
    """
        The **HTML`<address>` element** supplies contact information for its nearest
        [`<article>`](/en-US/docs/Web/HTML/Element/article "The HTML <article> element
        represents a self-contained composition in a document, page, application, or
        site, which is intended to be independently distributable or reusable \(e.g., in
        syndication\). Examples include: a forum post, a magazine or newspaper article,
        or a blog entry.") or [`<body>`](/en-US/docs/Web/HTML/Element/body "The HTML
        <body> Element represents the content of an HTML document. There can be only one
        <body> element in a document.") ancestor; in the latter case, it applies to the
        whole document.
    """,
)

article = create_component(
    'article',
    """
        The **HTML`<article>` element** represents a self-contained composition in
        a document, page, application, or site, which is intended to be independently
        distributable or reusable (e.g., in syndication). Examples include: a forum
        post, a magazine or newspaper article, or a blog entry.
    """,
)

aside = create_component(
    'aside',
    """
        The **HTML`<aside>` element** represents a section of a document with content
        connected tangentially to the main content of the document (often presented as a
        sidebar).
    """,
)

footer = create_component(
    'footer',
    """
        The **HTML`<footer>` element** represents a footer for its nearest
        [sectioning content](/en- US/docs/Web/Guide/HTML/Sections_and_Outlines_of_an_HTM
        L5_document#Defining_Sections_in_HTML5) or [sectioning root](/en- US/docs/Web/Gu
        ide/HTML/Sections_and_Outlines_of_an_HTML5_document#Sectioning_root "Sections
        and Outlines of an HTML5 document#Sectioning root") element. A footer typically
        contains information about the author of the section, copyright data or links to
        related documents.
    """,
)

h1 = create_component(
    'h1',
    """
        The **HTML`<h1>`–`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
)

h2 = create_component(
    'h2',
    """
        The **HTML`<h1>`–`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
)

h3 = create_component(
    'h3',
    """
        The **HTML`<h1>`–`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
)

h4 = create_component(
    'h4',
    """
        The **HTML`<h1>`–`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
)

h5 = create_component(
    'h5',
    """
        The **HTML`<h1>`–`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
)

h6 = create_component(
    'h6',
    """
        The **HTML`<h1>`–`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
)

header = create_component(
    'header',
    """
        The **HTML`<header>` element** represents introductory content, typically a
        group of introductory or navigational aids. It may contain some heading elements
        but also other elements like a logo, a search form, an author name, and so on.
    """,
)

hgroup = create_component(
    'hgroup',
    """
        __ **This is an experimental technology**   Because this technology's
        specification has not stabilized, check the compatibility table for usage in
        various browsers. Also note that the syntax and behavior of an experimental
        technology is subject to change in future versions of browsers as the
        specification changes.  The **HTML`<hgroup>` element** represents a multi-level
        heading for a section of a document. It groups a set of `[<h1>–<h6>](/en-
        US/docs/Web/HTML/Element/Heading_Elements)` elements.
    """,
)

nav = create_component(
    'nav',
    """
        The **HTML`<nav>` element** represents a section of a page whose purpose is to
        provide navigation links, either within the current document or to other
        documents. Common examples of navigation sections are menus, tables of contents,
        and indexes.
    """,
)

section = create_component(
    'section',
    """
        The **HTML`<section>` element** represents a standalone section of
        functionality contained within an HTML document, typically with a heading, which
        doesn't have a more specific semantic element to represent it.  As an example, a
        navigation menu should be wrapped in a [`<nav>`](/en-
        US/docs/Web/HTML/Element/nav "The HTML <nav> element represents a section of a
        page whose purpose is to provide navigation links, either within the current
        document or to other documents. Common examples of navigation sections are
        menus, tables of contents, and indexes.") element, but a list of search results
        and a map display and its controls don't have specific elements, and could be
        put inside a `<section>`.
    """,
)

# == Text content ==

# Use HTML text content elements to organize blocks or sections of content
# placed between the opening [`<body>`](/en-US/docs/Web/HTML/Element/body "The
# HTML <body> Element represents the content of an HTML document. There can be
# only one <body> element in a document.") and closing `</body>` tags. Important
# for [accessibility](/en-US/docs/Glossary/accessibility "accessibility: Web
# Accessibility \(A11Y\) refers to best practices for keeping a website usable
# despite physical and technical restrictions. Web accessibility is formally
# defined and discussed at the W3C through the Web Accessibility Initiative
# \(WAI\).") and [SEO](/en-US/docs/Glossary/SEO "SEO: SEO \(Search Engine
# Optimization\) is the process of making a website more visible in search
# results, also termed improving search rankings."), these elements identify the
# purpose or structure of that content.

blockquote = create_component(
    'blockquote',
    """
        The **HTML`<blockquote>` Element** (or _HTML Block Quotation Element_ )
        indicates that the enclosed text is an extended quotation. Usually, this is
        rendered visually by indentation (see [Notes](/en-
        US/docs/HTML/Element/blockquote#Notes) for how to change it). A URL for the
        source of the quotation may be given using the **cite** attribute, while a text
        representation of the source can be given using the [`<cite>`](/en-
        US/docs/Web/HTML/Element/cite "The HTML <cite> element represents a reference to
        a creative work. It must include the title of a work or a URL reference, which
        may be in an abbreviated form according to the conventions used for the addition
        of citation metadata.") element.

        ## Notes
    """,
)

dd = create_component(
    'dd',
    """
        The **HTML`<dd>` element** indicates the description of a term in a
        description list ([`<dl>`](/en-US/docs/Web/HTML/Element/dl "The HTML
        <dl> element represents a description list. The element encloses a list of
        groups of terms and descriptions. Common uses for this element are to implement
        a glossary or to display metadata \(a list of key-value pairs\).")).
    """,
)

div = create_component(
    'div',
    """
        The **HTML`<div>` element** is the generic container for flow content and
        does not inherently represent anything. Use it to group elements for purposes
        such as styling (using the `[class](/en-US/docs/Web/HTML/Global_attributes#attr-
        class)` or `[id](/en-US/docs/Web/HTML/Global_attributes#attr-id)` attributes),
        marking a section of a document in a different language (using the `[lang](/en-
        US/docs/Web/HTML/Global_attributes#attr-lang)` attribute), and so on.
    """,
)

dl = create_component(
    'dl',
    """
        The **HTML`<dl>` ** element represents a description list. **** The element
        encloses a list of groups of terms and descriptions. Common uses for this
        element are to implement a glossary or to display metadata (a list of key- value
        pairs).

        ## Notes
    """,
)

dt = create_component(
    'dt',
    """
        The **HTML`<dt>` element** identifies a term in a description list. This
        element can occur only as a child element of a [`<dl>`](/en-
        US/docs/Web/HTML/Element/dl "The HTML <dl> element represents a description
        list. The element encloses a list of groups of terms and descriptions. Common
        uses for this element are to implement a glossary or to display metadata \(a
        list of key-value pairs\)."). It is usually followed by a [`<dd>`](/en-
        US/docs/Web/HTML/Element/dd "The HTML <dd> element indicates the description of
        a term in a description list \(<dl>\).") element; however, multiple `<dt>`
        elements in a row indicate several terms that are all defined by the immediate
        next [`<dd>`](/en-US/docs/Web/HTML/Element/dd "The HTML <dd> element indicates
        the description of a term in a description list \(<dl>\).") element.
    """,
)

figcaption = create_component(
    'figcaption',
    """
        The **HTML`<figcaption>` element** represents a caption or a legend
        associated with a figure or an illustration described by the rest of the data of
        the [`<figure>`](/en-US/docs/Web/HTML/Element/figure "The HTML <figure> element
        represents self-contained content, frequently with a caption \(<figcaption>\),
        and is typically referenced as a single unit.") element which is its immediate
        ancestor.
    """,
)

figure = create_component(
    'figure',
    """
        The **HTML`<figure>` element** represents self-contained content,
        frequently with a caption ([`<figcaption>`](/en-
        US/docs/Web/HTML/Element/figcaption "The HTML <figcaption> element represents a
        caption or a legend associated with a figure or an illustration described by the
        rest of the data of the <figure> element which is its immediate ancestor.")),
        and is typically referenced as a single unit.
    """,
)

hr = create_component(
    'hr',
    """
        The **HTML`<hr>` element** represents a thematic break between paragraph-
        level elements (for example, a change of scene in a story, or a shift of topic
        with a section). In previous versions of HTML, it represented a horizontal rule.
        It may still be displayed as a horizontal rule in visual browsers, but is now
        defined in semantic terms, rather than presentational terms.
    """,
)

li = create_component(
    'li',
    """
        The **HTML`<li>` element** is used to represent an item in a list. It must
        be contained in a parent element: an ordered list ([`<ol>`](/en-
        US/docs/Web/HTML/Element/ol "The HTML <ol> element represents an ordered list of
        items, typically rendered as a numbered list.")), an unordered list
        ([`<ul>`](/en-US/docs/Web/HTML/Element/ul "The HTML <ul> element represents an
        unordered list of items, typically rendered as a bulleted list.")), or a menu
        ([`<menu>`](/en-US/docs/Web/HTML/Element/menu "The HTML <menu> element
        represents a group of commands that a user can perform or activate. This
        includes both list menus, which might appear across the top of a screen, as well
        as context menus, such as those that might appear underneath a button after it
        has been clicked.")). In menus and unordered lists, list items are usually
        displayed using bullet points. In ordered lists, they are usually displayed with
        an ascending counter on the left, such as a number or letter.
    """,
)

main = create_component(
    'main',
    """
        The **HTML`<main>` element** represents the main content of the
        [`<body>`](/en-US/docs/Web/HTML/Element/body "The HTML <body> Element represents
        the content of an HTML document. There can be only one <body> element in a
        document.") of a document, portion of a document, or application. The main
        content area consists of content that is directly related to, or expands upon
        the central topic of, a document or the central functionality of an application.
        You can use multiple `<main>` elements within the same page when it makes sense
        to do so. For instance, if you have a page presenting multiple articles (each
        inside an [`<article>`](/en-US/docs/Web/HTML/Element/article "The HTML <article>
        element represents a self-contained composition in a document, page,
        application, or site, which is intended to be independently distributable or
        reusable \(e.g., in syndication\). Examples include: a forum post, a magazine or
        newspaper article, or a blog entry.") element, each of which has some extra
        material within (such as toolbars for editing, ads, and so forth), it may make
        sense to include a `<main>` element within each article to identify the primary
        contents of that specific article.
    """,
)

ol = create_component(
    'ol',
    """
        The **HTML`<ol>` element** represents an ordered list of items, typically
        rendered as a numbered list.
    """,
)

p = create_component(
    'p',
    """
        The **HTML`<p>` element** represents a paragraph of text. Paragraphs are
        usually represented in visual media as blocks of text that are separated from
        adjacent blocks by vertical blank space and/or first-line indentation.
        Paragraphs are [block-level elements](/en-US/docs/Web/HTML/Block-
        level_elements).
    """,
)

pre = create_component(
    'pre',
    """
        The **HTML`<pre>` element** represents preformatted text. Text within this
        element is typically displayed in a non-proportional ("[monospace](/en-
        US/docs/XUL/Style/monospace)") font exactly as it is laid out in the file.
        Whitespace inside this element is displayed as typed.
    """,
)

ul = create_component(
    'ul',
    """
        The **HTML`<ul>` element** represents an unordered list of items, typically
        rendered as a bulleted list.
    """,
)

# == Inline text semantics ==

# Use the HTML inline text semantic to define the meaning, structure, or style
# of a word, line, or any arbitrary piece of text.

a = create_component(
    'a',
    """
        The **HTML`<a>` element** (or _anchor_ element) creates a hyperlink to other web
        pages, files, locations within the same page, email addresses, or any other URL.

        ## Notes
    """,
)

abbr = create_component(
    'abbr',
    """
        The **HTML`<abbr>` element** represents an abbreviation and optionally
        provides a full description for it. If present, the `[title](/en-
        US/docs/Web/HTML/Global_attributes#attr-title)` attribute must contain this full
        description and nothing else.
    """,
)

b = create_component(
    'b',
    """
        The **HTML`<b>` element** represents a span of text stylistically different from
        normal text, without conveying any special importance or relevance, and that is
        typically rendered in boldface.
    """,
)

bdi = create_component(
    'bdi',
    """
        The **HTML`<bdi>` element** ( _bidirectional isolation_ ) isolates a span of
        text that might be formatted in a different direction from other text outside
        it.  This element is useful when embedding text with an unknown directionality,
        from a database for example, inside text with a fixed directionality.
    """,
)

bdo = create_component(
    'bdo',
    """
        The **HTML`<bdo>` element** ( _bidirectional override_ ) is used to override
        the current directionality of text. It causes the directionality of the
        characters to be ignored in favor of the specified directionality.

        ## Notes
    """,
)

br = create_component(
    'br',
    """
        The **HTML`<br>` element** produces a line break in text (carriage-return). It
        is useful for writing a poem or an address, where the division of lines is
        significant.

        ## Notes
    """,
)

cite = create_component(
    'cite',
    """
        The **HTML <cite> element** represents a reference to a creative work. It must
        include the title of a work or a URL reference, which may be in an abbreviated
        form according to the conventions used for the addition of citation metadata.
    """,
)

code = create_component(
    'code',
    """
        The **HTML`<code>` element** represents a fragment of computer code. By default,
        it is displayed in the browser's default monospace font.
    """,
)

data = create_component(
    'data',
    """
        The **HTML`<data>` element** links a given content with a machine-readable
        translation. If the content is time- or date-related, the [`<time>`](/en-
        US/docs/Web/HTML/Element/time "The HTML <time> element represents either a time
        on a 24-hour clock or a precise date in the Gregorian calendar \(with optional
        time and timezone information\).") element must be used.
    """,
)

dfn = create_component(
    'dfn',
    'The **HTML <dfn> element** represents the defining instance of a term.',
)

em = create_component(
    'em',
    """
        The **HTML`<em>` element** marks text that has stress emphasis. The `<em>`
        element can be nested, with each level of nesting indicating a greater degree of
        emphasis.
    """,
)

i = create_component(
    'i',
    """
        The **HTML`<i>` element** represents a range of text that is set off from the
        normal text for some reason, for example, technical terms, foreign language
        phrases, or fictional character thoughts. It is typically displayed in italic
        type.

        ## Notes
    """,
)

kbd = create_component(
    'kbd',
    """
        The **HTML`<kbd>` element** represents user input and produces an inline element
        displayed in the browser's default monospace font.
    """,
)

mark = create_component(
    'mark',
    """
        The **HTML`<mark>` element** represents highlighted text, i.e., a run of text
        marked for reference purpose, due to its _relevance_ in a particular context.
        For example it can be used in a page showing search results to highlight every
        instance of the searched-for word.
    """,
)

q = create_component(
    'q',
    """
        The **HTML`<q>` element ** indicates that the enclosed text is a short inline
        quotation. This element is intended for short quotations that don't require
        paragraph breaks; for long quotations use the [`<blockquote>`](/en-
        US/docs/Web/HTML/Element/blockquote "The HTML <blockquote> Element \(or HTML
        Block Quotation Element\) indicates that the enclosed text is an extended
        quotation. Usually, this is rendered visually by indentation \(see Notes for how
        to change it\). A URL for the source of the quotation may be given using the
        cite attribute, while a text representation of the source can be given using the
        <cite> element.") element.
    """,
)

rp = create_component(
    'rp',
    """
        The **HTML`<rp>` element** is used to provide fall-back parentheses for browsers
        that do not support display of ruby annotations using the [`<ruby>`](/en-
        US/docs/Web/HTML/Element/ruby "The HTML <ruby> element represents a ruby
        annotation. Ruby annotations are for showing pronunciation of East Asian
        characters.") element.
    """,
)

rt = create_component(
    'rt',
    """
        The **HTML`<rt>` element** embraces pronunciation of characters presented in a
        ruby annotations, which are used to describe the pronunciation of East Asian
        characters. This element is always used inside a [`<ruby>`](/en-
        US/docs/Web/HTML/Element/ruby "The HTML <ruby> element represents a ruby
        annotation. Ruby annotations are for showing pronunciation of East Asian
        characters.") element.
    """,
)

rtc = create_component(
    'rtc',
    """
        The **HTML`<rtc>` element** embraces semantic annotations of characters
        presented in a ruby of [`<rb>`](/en-US/docs/Web/HTML/Element/rb "The
        documentation about this has not yet been written; please consider
        contributing!") elements used inside of [`<ruby>`](/en-
        US/docs/Web/HTML/Element/ruby "The HTML <ruby> element represents a ruby
        annotation. Ruby annotations are for showing pronunciation of East Asian
        characters.") element. [`<rb>`](/en-US/docs/Web/HTML/Element/rb "The
        documentation about this has not yet been written; please consider
        contributing!") elements can have both pronunciation ([`<rt>`](/en-
        US/docs/Web/HTML/Element/rt "The HTML <rt> element embraces pronunciation of
        characters presented in a ruby annotations, which are used to describe the
        pronunciation of East Asian characters. This element is always used inside a
        <ruby> element.")) and semantic ([`<rtc>`](/en-US/docs/Web/HTML/Element/rtc "The
        HTML <rtc> element embraces semantic annotations of characters presented in a
        ruby of <rb> elements used inside of <ruby> element. <rb> elements can have both
        pronunciation \(<rt>\) and semantic \(<rtc>\) annotations.")) annotations.
    """,
)

ruby = create_component(
    'ruby',
    """
        The **HTML`<ruby>` element** represents a ruby annotation. Ruby annotations are
        for showing pronunciation of East Asian characters.
    """,
)

s = create_component(
    's',
    """
        The **HTML`<s>` element** renders text with a strikethrough, or a line through
        it. Use the `<s>` element to represent things that are no longer relevant or no
        longer accurate. However, `<s>` is not appropriate when indicating document
        edits; for that, use the [`<del>`](/en-US/docs/Web/HTML/Element/del "The HTML
        <del> element represents a range of text that has been deleted from a document.
        This element is often \(but need not be\) rendered with strike- through text.")
        and [`<ins>`](/en-US/docs/Web/HTML/Element/ins "The HTML <ins> element
        represents a range of text that has been added to a document.") elements, as
        appropriate.
    """,
)

samp = create_component(
    'samp',
    """
        The **HTML`<samp>` element** is an element intended to identify sample output
        from a computer program. It is usually displayed in the browser's default
        monotype font (such as Lucida Console).
    """,
)

small = create_component(
    'small',
    """
        The **HTML`<small>`** **element** makes the text _font size_ one size smaller
        (for example, from large to medium, or from small to x-small) down to the
        browser's minimum font size. In HTML5, this element is repurposed to represent
        side-comments and small print, including copyright and legal text, independent
        of its styled presentation.

        ## Notes
    """,
)

span = create_component(
    'span',
    """
        The **HTML`<span>` element** is a generic inline container for phrasing content,
        which does not inherently represent anything. It can be used to group elements
        for styling purposes (using the `class` or `id` attributes), or because they
        share attribute values, such as `lang`. It should be used only when no other
        semantic element is appropriate. `<span>` is very much like a [`<div>`](/en-
        US/docs/Web/HTML/Element/div "The HTML <div> element is the generic container
        for flow content and does not inherently represent anything. Use it to group
        elements for purposes such as styling \(using the class or id attributes\),
        marking a section of a document in a different language \(using the lang
        attribute\), and so on.") element, but [`<div>`](/en-
        US/docs/Web/HTML/Element/div "The HTML <div> element is the generic container
        for flow content and does not inherently represent anything. Use it to group
        elements for purposes such as styling \(using the class or id attributes\),
        marking a section of a document in a different language \(using the lang
        attribute\), and so on.") is a [block-level element](/en-US/docs/HTML/Block-
        level_elements) whereas a `<span>` is an[ inline element](/en-
        US/docs/HTML/Inline_elements).
    """,
)

strong = create_component(
    'strong',
    """
        The **HTML**` **< strong>**` **element** gives text strong importance, and is
        typically displayed in bold.
    """,
)

sub = create_component(
    'sub',
    """
        The **HTML`<sub>` element** defines a span of text that should be
        displayed, for typographic reasons, lower, and often smaller, than the main span
        of text.
    """,
)

sup = create_component(
    'sup',
    """
        The **HTML`<sup>` element** defines a span of text that should be displayed, for
        typographic reasons, higher, and often smaller, than the main span of text.
    """,
)

time = create_component(
    'time',
    """
        The **HTML`<time>` element** represents either a time on a 24-hour clock or a
        precise date in the [Gregorian
        calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) (with optional time
        and timezone information).
    """,
)

u = create_component(
    'u',
    """
        The **HTML`<u>` element** renders text with an underline, a line under the
        baseline of its content. In HTML5, this element represents a span of text with
        an unarticulated, though explicitly rendered, non-textual annotation, such as
        labeling the text as being a proper name in Chinese text (a Chinese proper name
        mark), or labeling the text as being misspelled.
    """,
)

var = create_component(
    'var',
    """
        The **HTML`<var>` element** represents a variable in a mathematical expression
        or a programming context.
    """,
)

wbr = create_component(
    'wbr',
    """
        The **HTML`<wbr>` element** represents a word break opportunity—a position
        within text where the browser may optionally break a line, though its line-
        breaking rules would not otherwise create a break at that location.

        ## Notes
    """,
)

# == Image and multimedia ==

# HTML supports various multimedia resources such as images, audio, and video.

area = create_component(
    'area',
    """
        The **HTML`<area>` element** defines a hot-spot region on an image, and
        optionally associates it with a [hypertext link](/en- US/docs/Glossary/Hyperlink
        "hypertext link: Hyperlinks connect webpages or data items to one another. In
        HTML, <a> elements define hyperlinks from a spot on a webpage \(like a text
        string or image\) to another spot on some other webpage \(or even on the same
        page\)."). This element is used only within a [`<map>`](/en-
        US/docs/Web/HTML/Element/map "The HTML <map> element is used with <area>
        elements to define an image map \(a clickable link area\).") element.

        ## Notes
    """,
)

audio = create_component(
    'audio',
    """
        The **HTML`<audio>` element** is used to embed sound content in documents. It
        may contain one or more audio sources, represented using the `src` attribute or
        the [`<source>`](/en-US/docs/Web/HTML/Element/source "The HTML <source> element
        specifies multiple media resources for either the <picture>, the <audio> or the
        <video> element. It is an empty element. It is commonly used to serve the same
        media content in multiple formats supported by different browsers.") element:
        the browser will choose the most suitable one. It can also be the destination
        for streamed media, using a [`MediaStream`](/en- US/docs/Web/API/MediaStream
        "The MediaStream interface represents a stream of media content. A stream
        consists of several tracks such as video or audio tracks. Each track is
        specified as an instance of MediaStreamTrack.").
    """,
)

img = create_component(
    'img',
    'The **HTML`<img>` element** represents an image in the document.',
)

map_ = create_component(
    'map',
    """
        The **HTML`<map>` element** is used with [`<area>`](/en-
        US/docs/Web/HTML/Element/area "The HTML <area> element defines a hot-spot region
        on an image, and optionally associates it with a hypertext link. This element is
        used only within a <map> element.") elements to define an image map (a clickable
        link area).
    """,
)

track = create_component(
    'track',
    """
        The **HTML`<track>` element** is used as a child of the media elements
        [`<audio>`](/en-US/docs/Web/HTML/Element/audio "The HTML <audio> element is used
        to embed sound content in documents. It may contain one or more audio sources,
        represented using the src attribute or the <source> element: the browser will
        choose the most suitable one. It can also be the destination for streamed media,
        using a MediaStream.") and [`<video>`](/en- US/docs/Web/HTML/Element/video "Use
        the HTML <video> element to embed video content in a document."). It lets you
        specify timed text tracks (or time-based data), for example to automatically
        handle subtitles. The tracks are formatted in [WebVTT format](/en-
        US/docs/Web/API/Web_Video_Text_Tracks_Format) (`.vtt` files) — Web Video Text
        Tracks.
    """,
)

video = create_component(
    'video',
    'Use the **HTML`<video>` element** to embed video content in a document.',
)

# == Embedded content ==

# In addition to regular multimedia content, HTML can include a variety of other
# content, even if it's not always easy to interact with.

embed = create_component(
    'embed',
    """
        The **HTML`<embed>` element** represents an integration point for an external
        application or interactive content (in other words, a plug-in).    **Note:**
        This topic documents only the element that is defined as part of HTML5. It does
        not address earlier, non-standardized implementation of the element.
    """,
)

object_ = create_component(
    'object',
    """
        The **HTML`<object>` element** represents an external resource, which can be
        treated as an image, a nested browsing context, or a resource to be handled by a
        plugin.
    """,
)

param = create_component(
    'param',
    """
        The **HTML`<param>` element** defines parameters for an [`<object>`](/en-
        US/docs/Web/HTML/Element/object "The HTML <object> element represents an
        external resource, which can be treated as an image, a nested browsing context,
        or a resource to be handled by a plugin.") element.
    """,
)

source = create_component(
    'source',
    """
        The **HTML`<source>` element** specifies multiple media resources for either the
        [`<picture>`](/en-US/docs/Web/HTML/Element/picture "The HTML <picture> element
        is a container used to specify multiple <source> elements for a specific <img>
        contained in it. The browser will choose the most suitable source according to
        the current layout of the page \(the constraints of the box the image will
        appear in\) and the device it will be displayed on \(e.g. a normal or hiDPI
        device.\)"), the [`<audio>`](/en- US/docs/Web/HTML/Element/audio "The HTML
        <audio> element is used to embed sound content in documents. It may contain one
        or more audio sources, represented using the src attribute or the <source>
        element: the browser will choose the most suitable one. It can also be the
        destination for streamed media, using a MediaStream.") or the [`<video>`](/en-
        US/docs/Web/HTML/Element/video "Use the HTML <video> element to embed video
        content in a document.") element. It is an empty element. It is commonly used to
        serve the same media content in [multiple formats supported by different
        browsers](/en- US/docs/Media_formats_supported_by_the_audio_and_video_elements).
    """,
)

# == Scripting ==

# In order to create dynamic content and Web applications, HTML supports the use
# of scripting languages, most prominently JavaScript. Certain elements support
# this capability.

canvas = create_component(
    'canvas',
    """
        Use the **HTML`<canvas>` element** with the [canvas scripting API ](/en-
        US/docs/Web/API/Canvas_API)to draw graphics and animations.
    """,
)

noscript = create_component(
    'noscript',
    """
        The **HTML`<noscript>` element** defines a section of HTML to be inserted if a
        script type on the page is unsupported or if scripting is currently turned off
        in the browser.
    """,
)

script = create_component(
    'script',
    """
        The **HTML`<script>` element** is used to embed or reference an executable
        script.

        ## Notes
    """,
)

# == Demarcating edits ==

# These elements let you provide indications that specific parts of the text
# have been altered.

del_ = create_component(
    'del',
    """
        The **HTML`<del>` element** represents a range of text that has been deleted
        from a document. This element is often (but need not be) rendered with strike-
        through text.
    """,
)

ins = create_component(
    'ins',
    """
        The **HTML`<ins>` element** represents a range of text that has been added to a
        document.
    """,
)

# == Table content ==

# The elements here are used to create and handle tabular data.

caption = create_component(
    'caption',
    """
        The **HTML`<caption>` element** represents the title of a table. Though it is
        always the first descendant of a [`<table>`](/en- US/docs/Web/HTML/Element/table
        "The HTML <table> element represents tabular data — that is, information
        expressed via a two-dimensional data table."), its styling, using CSS, may place
        it elsewhere, relative to the table.
    """,
)

col = create_component(
    'col',
    """
        The **HTML`<col>` element** defines a column within a table and is used for
        defining common semantics on all common cells. It is generally found within a
        [`<colgroup>`](/en-US/docs/Web/HTML/Element/colgroup "The HTML <colgroup>
        element defines a group of columns within a table.") element.  This element
        allows styling columns using CSS, but only a few attributes will have an effect
        on the column ([see the CSS 2.1
        specification](https://www.w3.org/TR/CSS21/tables.html#columns) for a list).
    """,
)

colgroup = create_component(
    'colgroup',
    'The **HTML`<colgroup>` element** defines a group of columns within a table.',
)

table = create_component(
    'table',
    """
        The **HTML`<table>` element** represents tabular data — that is, information
        expressed via a two-dimensional data table.
    """,
)

tbody = create_component(
    'tbody',
    """
        The **HTML`<tbody>` element** groups one or more [`<tr>`](/en-
        US/docs/Web/HTML/Element/tr "The HTML <tr> element defines a row of cells in a
        table. Those can be a mix of <td> and <th> elements.") elements as the body of a
        [`<table>`](/en-US/docs/Web/HTML/Element/table "The HTML <table> element
        represents tabular data — that is, information expressed via a two-dimensional
        data table.") element.
    """,
)

td = create_component(
    'td',
    """
        The **HTML`<td>` element** defines a cell of a table that contains data. It
        participates in the _table model_.
    """,
)

tfoot = create_component(
    'tfoot',
    """
        The **HTML`<tfoot>` element** defines a set of rows summarizing the columns of
        the table.
    """,
)

th = create_component(
    'th',
    """
        The **HTML`<th>` element** defines a cell as header of a group of table cells.
        The exact nature of this group is defined by the `[scope](/en-
        US/docs/Web/HTML/Element/th#attr-scope)` and `[headers](/en-
        US/docs/Web/HTML/Element/th#attr-headers)` attributes.
    """,
)

thead = create_component(
    'thead',
    """
        The **HTML`<thead>` element** defines a set of rows defining the head of the
        columns of the table.
    """,
)

tr = create_component(
    'tr',
    """
        The HTML **`<tr>`** element specifies that the markup contained inside the
        `<tr>` block comprises one row of a table, inside which the [`<th>`](/en-
        US/docs/Web/HTML/Element/th "The HTML <th> element defines a cell as header of a
        group of table cells. The exact nature of this group is defined by the scope and
        headers attributes.") and [`<td>`](/en-US/docs/Web/HTML/Element/td "The HTML
        <td> element defines a cell of a table that contains data. It participates in
        the table model.") elements create header and data cells, respectively, within
        the row. Each cell is placed into its own column; the [user agent](/en-
        US/docs/Glossary/user_agent "user agent: A user agent is a computer program
        representing a person, for example, a browser in a Web context.") follows
        specific rules to determine how the cells in each row are placed into columns
        with those coming from other rows.  To provide additional control over how cells
        fit into (or span across) columns, both `<th>` and `<td>` support the
        `[colspan](/en- US/docs/Web/HTML/Element/td#attr-colspan)` attribute, which lets
        you specify how many columns wide the cell should be, with the default being 1.
        Similarly, you can use the `[rowspan](/en-US/docs/Web/HTML/Element/td#attr-
        rowspan)` attribute on cells to indicate they should span more than one table
        row.  This can take a little practice to get right when building your tables. We
        have some examples below, but for more examples and an in-depth tutorial, see
        the [HTML tables](/en-US/docs/Learn/HTML/Tables) series in our [Learn web
        development](/en-US/docs/Learn) area, where you'll learn how to use the table
        elements and their attributes to get just the right layout and formatting for
        your tabular data.
    """,
)

# == Forms ==

# HTML provides a number of elements which can be used together to create forms
# which the user can fill out and submit to the Web site or application. There's
# a great deal of further information about this available in the [HTML forms
# guide](/en-US/docs/Web/Guide/HTML/Forms).

button = create_component(
    'button',
    """
        The **HTML`<button>` element** represents a clickable button.

        ## Notes
    """,
)

datalist = create_component(
    'datalist',
    """
        The **HTML`<datalist>` element** contains a set of [`<option>`](/en-
        US/docs/Web/HTML/Element/option "The HTML <option> element is used to define an
        item contained in a <select>, an <optgroup>, or a <datalist> element. As
        such, <option> can represent menu items in popups and other lists of items in an
        HTML document.") elements that represent the values available for other
        controls.
    """,
)

fieldset = create_component(
    'fieldset',
    """
        The **HTML`<fieldset>` element** is used to group several controls as well as
        labels ([`<label>`](/en-US/docs/Web/HTML/Element/label "The HTML <label> element
        represents a caption for an item in a user interface.")) within a web form.
    """,
)

form = create_component(
    'form',
    """
        The **HTML`<form>` element** represents a document section that contains
        interactive controls to submit information to a web server.  It is possible to
        use the [`:valid`](/en-US/docs/Web/CSS/:valid "The :valid CSS pseudo-class
        represents any <input> or <form> element whose content validates correctly
        according to the input's type setting. This allows to easily make valid fields
        adopt an appearance that helps the user confirm that their data is formatted
        properly.") and [`:invalid`](/en- US/docs/Web/CSS/:invalid "The :invalid CSS
        pseudo-class selects any <input> or <form> element whose content fails to
        validate according to the input's attribute settings. This allows you to easily
        have invalid fields adopt an appearance that helps the user identify and correct
        errors.") CSS pseudo- classes to style a `<form>` element.
    """,
)

input_ = create_component(
    'input',
    """
        The **HTML`<input>` element** is used to create interactive controls for web-
        based forms in order to accept data from the user.

        ## Notes
    """,
)

label = create_component(
    'label',
    """
        The **HTML`<label>` element** represents a caption for an item in a user
        interface.
    """,
)

legend = create_component(
    'legend',
    """
        The **HTML`<legend>` element** represents a caption for the content of its
        parent [`<fieldset>`](/en-US/docs/Web/HTML/Element/fieldset "The HTML <fieldset>
        element is used to group several controls as well as labels \(<label>\) within a
        web form.").
    """,
)

meter = create_component(
    'meter',
    """
        The **HTML`<meter>` element** represents either a scalar value within a known
        range or a fractional value.
    """,
)

optgroup = create_component(
    'optgroup',
    """
        The **HTML`<optgroup>` element** creates a grouping of options within a
        [`<select>`](/en-US/docs/Web/HTML/Element/select "The HTML <select> element
        represents a control that provides a menu of options:") element.
    """,
)

option = create_component(
    'option',
    """
        The **HTML`<option>` element** is used to define an item contained in a
        [`<select>`](/en-US/docs/Web/HTML/Element/select "The HTML <select> element
        represents a control that provides a menu of options:"), an [`<optgroup>`](/en-
        US/docs/Web/HTML/Element/optgroup "The HTML <optgroup> element creates a
        grouping of options within a <select> element."), or a [`<datalist>`](/en-
        US/docs/Web/HTML/Element/datalist "The HTML <datalist> element contains a set of
        <option> elements that represent the values available for other controls.")
        element. As such, `<option>` can represent menu items in popups and other lists
        of items in an HTML document.
    """,
)

output = create_component(
    'output',
    """
        Introduced in [HTML5](/en-US/docs/HTML/HTML5)  The **HTML`<output>` element**
        represents the result of a calculation or user action.
    """,
)

progress = create_component(
    'progress',
    """
        Introduced in [HTML5](/en-US/docs/HTML/HTML5)  The **HTML`<progress>` element**
        represents the completion progress of a task, typically displayed as a progress
        bar.
    """,
)

select = create_component(
    'select',
    """
        The **HTML`<select>` element** represents a control that provides a menu of
        options:

        ### Notes
    """,
)

textarea = create_component(
    'textarea',
    """
        The **HTML`<textarea>` element** represents a multi-line plain-text editing
        control.
    """,
)

# == Interactive elements ==

# HTML offers a selection of elements which help to create interactive user
# interface objects.

details = create_component(
    'details',
    """
        The **HTML`<details>` element** is used as a disclosure widget from which the
        user can retrieve additional information.
    """,
)

dialog = create_component(
    'dialog',
    """
        The **HTML`<dialog>` element** represents a dialog box or other interactive
        component, such as an inspector or window.
    """,
)

menu = create_component(
    'menu',
    """
        __ **This is an[experimental technology](/en-
        US/docs/MDN/Contribute/Guidelines/Conventions_definitions#Experimental)**
        Check the Browser compatibility table carefully before using this in production.
        The **HTML`<menu>` element** represents a group of commands that a user can
        perform or activate. This includes both list menus, which might appear across
        the top of a screen, as well as context menus, such as those that might appear
        underneath a button after it has been clicked.
    """,
)

menuitem = create_component(
    'menuitem',
    """
        __ **This is an[experimental technology](/en-
        US/docs/MDN/Contribute/Guidelines/Conventions_definitions#Experimental)**
        Check the Browser compatibility table carefully before using this in production.
        The **HTML`<menuitem>` element** represents a command that a user is able to
        invoke through a popup menu. This includes context menus, as well as menus that
        might be attached to a menu button.  A command can either be defined explicitly,
        with a textual label and optional icon to describe its appearance, or
        alternatively as an _indirect command_ whose behavior is defined by a separate
        element. Commands can also optionally include a checkbox or be grouped to share
        radio buttons. (Menu items for indirect commands gain checkboxes or radio
        buttons when defined against elements `<input type="checkbox">` and `<input
        type="radio">`.)
    """,
)

summary = create_component(
    'summary',
    """
        The **HTML`<summary>` element** is used as a summary, caption, or legend for
        the content of a [`<details>`](/en-US/docs/Web/HTML/Element/details "The HTML
        <details> element is used as a disclosure widget from which the user can
        retrieve additional information.") element.
    """,
)

# == Web Components ==

# Web Components is an HTML-related technology which makes it possible to,
# essentially, create and use custom elements as if it were regular HTML. In
# addition, you can create custom versions of standard HTML elements.

content = create_component(
    'content',
    """
        **__ Deprecated**   This feature has been removed from the Web standards.
        Though some browsers may still support it, it is in the process of being
        dropped. Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision. Be aware
        that this feature may cease to work at any time.    The **HTML`<content>`
        element** —an obsolete part of the [Web Components](/en-
        US/docs/Web/Web_Components) suite of technologies—was used inside of [Shadow
        DOM](/en-US/docs/Web/Web_Components/Shadow_DOM) as an [insertion point](/en-
        US/docs/Glossary/insertion_point "The definition of that term \(insertion
        point\) has not been written yet; please consider contributing it!"), and wasn't
        meant to be used in ordinary HTML It has now been replaced by the
        [`<slot>`](/en-US/docs/Web/HTML/Element/slot "The HTML <slot> element—part of
        the Web Components technology suite—is a placeholder inside a web component that
        you can fill with your own markup, which lets you create separate DOM trees and
        present them together.") element, which creates a point in the DOM at which a
        shadow DOM can be inserted.  **Note:** Though present in early draft of the
        specifications and implemented in several browsers, this element has been
        removed in later versions of the spec.
    """,
)

element = create_component(
    'element',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.    The **HTML`<element>` element** was part of [Web
        Components](/en- US/docs/Web/Web_Components); this element was intended to be
        used to define new custom DOM elements. It was removed in favor of a JavaScript-
        driven methodology for creating new custom elements; however, that technology is
        not mature and no browers fully implement it.  **Note:** This element has been
        removed from the specification. See
        [this](http://lists.w3.org/Archives/Public/public- webapps/2013JulSep/0287.html)
        for more information from the editor of the specification.
    """,
)

shadow = create_component(
    'shadow',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.    The **HTML`<shadow>` element** —an obsolete part of the [Web
        Components](/en- US/docs/Web/Web_Components) technology suite—was intended to be
        used as a shadow DOM [insertion point](/en-US/docs/Glossary/insertion_point "The
        definition of that term \(insertion point\) has not been written yet; please
        consider contributing it!"). You might have used it if you have created multiple
        shadow roots under a shadow host. It is not useful in ordinary HTML.
    """,
)

slot = create_component(
    'slot',
    """
        __ **This is an[experimental technology](/en-
        US/docs/MDN/Contribute/Guidelines/Conventions_definitions#Experimental)**
        Check the Browser compatibility table carefully before using this in production.
        The **HTML`<slot>` element** —part of the [Web Components](/en-
        US/docs/Web/Web_Components) technology suite—is a placeholder inside a web
        component that you can fill with your own markup, which lets you create separate
        DOM trees and present them together.
    """,
)

template = create_component(
    'template',
    """
        The **HTML`<template>` element** is a mechanism for holding client-side
        content that is not to be rendered when a page is loaded but may subsequently be
        instantiated during runtime using JavaScript.  Think of a template as a content
        fragment that is being stored for subsequent use in the document. While the
        parser does process the contents of the **`<template>` ** element while loading
        the page, it does so only to ensure that those contents are valid; the element's
        contents are not rendered, however.
    """,
)

# == Obsolete and deprecated elements ==

# **Warning:** These are old HTML elements which are deprecated and should not
# be used. **You should never use them in new projects, and should replace them
# in old projects as soon as you can.** They are listed here for informational
# purposes only.

acronym = create_component(
    'acronym',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

applet = create_component(
    'applet',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.  The HTML Applet Element (`<applet>`) identifies the inclusion
        of a Java applet.  **Note** : The [`<applet>`](/en-
        US/docs/Web/HTML/Element/applet "The HTML Applet Element \(<applet>\) identifies
        the inclusion of a Java applet.") element was removed in [Gecko
        56](https://bugzilla.mozilla.org/show_bug.cgi?id=1279218) and [Chrome in late
        2015](https://bugs.chromium.org/p/chromium/issues/detail?id=470301). Removal is
        being considered in [WebKit](https://bugs.webkit.org/show_bug.cgi?id=157926) and
        [Edge](https://developer.microsoft.com/en-us/microsoft-
        edge/platform/issues/11946645/).

        ## Notes
    """,
)

basefont = create_component(
    'basefont',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.

        ## Notes
    """,
)

big = create_component(
    'big',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

blink = create_component(
    'blink',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  **__ Obsolete**   This feature is obsolete. Although
        it may still work in some browsers, its use is discouraged since it could be
        removed at any time. Try to avoid using it.  The **HTML Blink Element**
        (`<blink>`) is a non-standard element causing the enclosed text to flash slowly.
        Do not use this element as it is **obsolete** and bad design practice. Blinking
        text is frowned upon by several accessibility standards and the CSS
        specification allows browsers to ignore the blink value.
    """,
)

center = create_component(
    'center',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.

        ## Note
    """,
)

command = create_component(
    'command',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.  **Note:** The `command` element has been removed from  Gecko
        24.0 in favor of the [`<menuitem>`](/en-US/docs/Web/HTML/Element/menuitem "The
        HTML <menuitem> element represents a command that a user is able to invoke
        through a popup menu. This includes context menus, as well as menus that might
        be attached to a menu button.") element. Firefox has never supported this
        `command` element, and the existing implementation of the
        [`HTMLCommandElement`](/en- US/docs/Web/API/HTMLCommandElement "The
        documentation about this has not yet been written; please consider
        contributing!") DOM interface has been dropped from [Firefox 24](/en-
        US/docs/Site_Compatibility_for_Firefox_24).
    """,
)

# content: see above under 'Web Components'

dir_ = create_component(
    'dir',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

# element: see above under 'Web Components'

font = create_component(
    'font',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

frame = create_component(
    'frame',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
    """,
)

frameset = create_component(
    'frameset',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
    """,
)

image = create_component(
    'image',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.  **__ Non-standard**   This feature is non-standard and is not
        on a standards track. Do not use it on production sites facing the Web: it will
        not work for every user. There may also be large incompatibilities between
        implementations and the behavior may change in the future.  The HTML `<image>`
        element is an obsolete remnant of an ancient version of HTML lost in the mists
        of time; use the standard [`<img>`](/en- US/docs/Web/HTML/Element/img "The HTML
        <img> element represents an image in the document.") element instead. Seriously,
        the specification even literally uses the words "Don't ask" when describing this
        element.  **Do not use this! __** In order to display images, use the standard
        [`<img>`](/en-US/docs/Web/HTML/Element/img "The HTML <img> element represents an
        image in the document.") element.  While browsers will attempt to automatically
        convert this into an [`<img>`](/en-US/docs/Web/HTML/Element/img "The HTML <img>
        element represents an image in the document.") element, it won't always do so,
        and won't always succeed when it tries, due to the various ways this can happen.
        So just don't use it if you like your users.
    """,
)

isindex = create_component(
    'isindex',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

keygen = create_component(
    'keygen',
    """
        **__ Deprecated**   This feature has been removed from the Web standards.
        Though some browsers may still support it, it is in the process of being
        dropped. Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision. Be aware
        that this feature may cease to work at any time.    The HTML `<keygen>` element
        exists to facilitate generation of key material, and submission of the public
        key as part of an [HTML form](/en- US/docs/Web/Guide/HTML/Forms). This mechanism
        is designed for use with Web- based certificate management systems. It is
        expected that the `<keygen>` element will be used in an HTML form along with
        other information needed to construct a certificate request, and that the result
        of the process will be a signed certificate.  There is currently discussion
        among Web browser makers whether to keep this feature or not. Until a decision
        is reached, it is better to continue to consider this feature as deprecated and
        going away.
    """,
)

listing = create_component(
    'listing',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

marquee = create_component(
    'marquee',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.  The HTML `<marquee>` element is used to insert a scrolling area
        of text. You can control what happens when the text reaches the edges of its
        content area using its attributes.  The `<marquee>` element is **obsolete** and
        must not be used. While some browsers still support it, it's not required.
    """,
)

multicol = create_component(
    'multicol',
    """
        **__ Non-standard**   This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.  **__ Obsolete**   This feature is
        obsolete. Although it may still work in some browsers, its use is discouraged
        since it could be removed at any time. Try to avoid using it.
    """,
)

nextid = create_component(
    'nextid',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.
    """,
)

noembed = create_component(
    'noembed',
    """
        **__ Non-standard**   This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.  **__ Deprecated**   This feature has
        been removed from the Web standards. Though some browsers may still support it,
        it is in the process of being dropped. Avoid using it and update existing code
        if possible; see the compatibility table at the bottom of this page to guide
        your decision. Be aware that this feature may cease to work at any time.  The
        `**< noembed>**` element is a deprecated and non-standard way to provide
        alternative, or "fallback", content for browsers that do not support the
        [`<embed>`](/en-US/docs/Web/HTML/Element/embed "The HTML <embed> element
        represents an integration point for an external application or interactive
        content \(in other words, a plug-in\).") element or do not support [embedded
        content](/en-US/docs/Web/Guide/HTML/Content_categories#Embedded_content) an
        author wishes to use. This element was deprecated in HTML 4.01 and above in
        favor of [`<object>`](/en-US/docs/Web/HTML/Element/object "The HTML <object>
        element represents an external resource, which can be treated as an image, a
        nested browsing context, or a resource to be handled by a plugin."). Fallback
        content should be inserted between the opening and closing [`<object>`](/en-
        US/docs/Web/HTML/Element/object "The HTML <object> element represents an
        external resource, which can be treated as an image, a nested browsing context,
        or a resource to be handled by a plugin.") tags.  While this element currently
        still works in many browsers, it has been deprecated and should not be used. Use
        [`<object>`](/en- US/docs/Web/HTML/Element/object "The HTML <object> element
        represents an external resource, which can be treated as an image, a nested
        browsing context, or a resource to be handled by a plugin.") instead.
    """,
)

plaintext = create_component(
    'plaintext',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

# shadow: see above under 'Web Components'

spacer = create_component(
    'spacer',
    """
        **__ Non-standard**   This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.  **__ Obsolete**   This feature is
        obsolete. Although it may still work in some browsers, its use is discouraged
        since it could be removed at any time. Try to avoid using it.  **`<spacer>`** is
        an obsolete HTML element which allowed insertion of empty spaces on pages. It
        was devised by Netscape to accomplish the same effect as a single-pixel layout
        image, which was something web designers used to use to add white spaces to web
        pages without actually using an image. However, `<spacer>` no longer supported
        by any major browser and the same effects can now be achieved using simple CSS.
        Firefox, which is the descendant of Netscape's browsers, removed support for
        `<spacer>` in version 4.
    """,
)

strike = create_component(
    'strike',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

tt = create_component(
    'tt',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.

        ## Notes
    """,
)

xmp = create_component(
    'xmp',
    """
        **__ Obsolete**   This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """,
)

__all__ = [
    'a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 'audio', 'b', 'basefont', 'bdi', 'bdo',
    'big', 'blink', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code', 'col',
    'colgroup', 'command', 'content', 'data', 'datalist', 'dd', 'del_', 'details', 'dfn', 'dialog', 'dir_', 'div', 'dl',
    'dt', 'element', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'font', 'footer', 'form', 'frame', 'frameset',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup', 'hr', 'html', 'i', 'image', 'img', 'input_', 'ins',
    'isindex', 'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'listing', 'main', 'map_', 'mark', 'marquee', 'menu',
    'menuitem', 'meta', 'meter', 'multicol', 'nav', 'nextid', 'noembed', 'noscript', 'object_', 'ol', 'optgroup',
    'option', 'output', 'p', 'param', 'plaintext', 'pre', 'progress', 'q', 'rp', 'rt', 'rtc', 'ruby', 's', 'samp',
    'script', 'section', 'select', 'shadow', 'slot', 'small', 'source', 'spacer', 'span', 'strike', 'strong', 'style',
    'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time', 'tr',
    'track', 'tt', 'u', 'ul', 'var', 'video', 'wbr', 'xmp'
]
