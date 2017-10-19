# -*- coding: utf-8 -*-


from vdom.core import Component


# From https://developer.mozilla.org/en-US/docs/Web/HTML/Element


# == Main root ==


class html(Component):
    """
        The **HTML ``<html>`` element** represents the root (top-level element) of an
        HTML document, so it is also referred to as the *root element*. All other
        elements must be descendants of this element.
    """


# == Document metadata ==

# Metadata contains information about the page. This includes information about
# styles, scripts and data to help software (`search engines </en-
# US/docs/Glossary/search_engine>`_, `browsers </en-US/docs/Glossary/Browser>`_,
# etc.) use and render the page. Metadata for styles and scripts may be defined
# in the page or link to another file that has the information.


class link(Component):
    """
        The **HTML ``<link>`` element** specifies relationships between the current
        document and an external resource. Possible uses for this element include
        defining a relational framework for navigation. This element is most used to
        link to `style sheets </en-US/docs/Glossary/CSS>`_.
        
        Notes:
        
            * A ``<link>`` tag can occur either in the head element or in the body element (or both), depending on whether it has a`link type <https://html.spec.whatwg.org/multipage/links.html#body-ok>`_that is **body-ok**. For example, the ``stylesheet`` link type is body-ok, and therefore a ``<link rel="stylesheet">`` is permitted in the body.
            
            * HTML 3.2 defines only the **href**, **rel**, **rev**, and **title** attributes for the link element.
            
            * HTML 2 defines the **href**, **methods**, **rel**, **rev**, **title**, and **urn** attributes for the ``<link>`` element. The **methods** and **urn** attributes were later removed from the specifications.
            
            * The HTML and XHTML specifications define event handlers for the ``<link>`` element, but it is unclear how they would be used.
            
            * Under XHTML 1.0, empty elements such as ``<link>`` require a trailing slash: ``<link />``.
    """


class meta(Component):
    """
        The **HTML ``<meta>`` element** represents `metadata </en-
        US/docs/Glossary/Metadata>`_ that cannot be represented by other HTML meta-
        related elements, like ```<base>`` </en-US/docs/Web/HTML/Element/base>`_,
        ```<link>`` </en-US/docs/Web/HTML/Element/link>`_, ```<script>`` </en-
        US/docs/Web/HTML/Element/script>`_, ```<style>`` </en-
        US/docs/Web/HTML/Element/style>`_ or ```<title>`` </en-
        US/docs/Web/HTML/Element/title>`_.
        
        Notes:
        
            Depending on the attributes set, the kind of metadata can be one of the following:
            
            * If ```name </en-US/docs/Web/HTML/Element/meta#attr-name>`_`` is set, it is *document-level* *metadata*, applying to the whole page.
            
            * If ```http-equiv </en-US/docs/Web/HTML/Element/meta#attr-http-equiv>`_`` is set, it is a *pragma directive* — information normally given by the web server about how the web page is served.
            
            * If ```charset </en-US/docs/Web/HTML/Element/meta#attr-charset>`_`` is set, it is a *charset declaration* — the character encoding used by the webpage.
            
            * If ```itemprop </en-US/docs/Web/HTML/Element/meta#attr-itemprop>`_`` is set, it is *user-defined metadata* — transparent for the user-agent as the semantics of the metadata is user-specific. **
    """


class style(Component):
    """
        The **HTML ``<style>`` element** contains style information for a document, or
        part of a document. By default, the style instructions written inside that
        element are expected to be `CSS </en-US/docs/Web/CSS>`_.
    """


# == Sectioning root ==


class body(Component):
    """
        The **HTML ``<body>`` Element** represents the content of an HTML document.
        There can be only one ``<body>`` element in a document.
        
        Examples::
        
            html(head(title('Document title')), body(p('This is a paragraph')))
    """


# == Content sectioning ==

# Content sectioning elements allow you to organize the document content into
# logical pieces. Use the sectioning elements to create a broad outline for your
# page content, including header and footer navigation, and heading elements to
# identify sections of content.


class address(Component):
    """
        The **HTML``<address>`` element** supplies contact information for its nearest
        ```<article>`` </en-US/docs/Web/HTML/Element/article>`_ or ```<body>`` </en-
        US/docs/Web/HTML/Element/body>`_ ancestor; in the latter case, it applies to the
        whole document.
    """


class article(Component):
    """
        The **HTML ``<article>`` element** represents a self-contained composition in a
        document, page, application, or site, which is intended to be independently
        distributable or reusable (e.g., in syndication). Examples include: a forum
        post, a magazine or newspaper article, or a blog entry.
        
        Examples::
        
            article(
                header(h2('Jurassic Park')),
                section(p('Dinos were great!'), class_='main_review'),
                section(
                    article(
                        p('Way too scary for me.'),
                        footer(
                            p('Posted on',
                              time('May 16', datetime='2015-05-16 19:00'), ' by Lisa. ')),
                        class_='user_review'),
                    article(
                        p('I agree, dinos are my favorite.'),
                        footer(
                            p('Posted on',
                              time('May 17', datetime='2015-05-17 19:00'), ' by Tom. ')),
                        class_='user_review'),
                    class_='user_reviews'),
                footer(
                    p('Posted on',
                      time('May 15', datetime='2015-05-15 19:00'), ' by Staff. ')),
                class_='film_review')
    """


class aside(Component):
    """
        The **HTML ``<aside>`` element** represents a section of a document with content
        connected tangentially to the main content of the document (often presented as a
        sidebar).
        
        Examples::
        
            article(
                p('The Disney movie',
                  cite('The Little Mermaid'), ' was first released to theatres in 1989. '),
                aside(p('The movie earned $87 million during its initial release.')),
                p('More info about the movie...'))
    """


class footer(Component):
    """
        The **HTML ``<footer>`` element** represents a footer for its nearest
        `sectioning content </en-US/docs/Web/Guide/HTML/Sections_and_Outlines_of_an_HTML
        5_document#Defining_Sections_in_HTML5>`_ or `sectioning root </en-US/docs/Web/Gu
        ide/HTML/Sections_and_Outlines_of_an_HTML5_document#Sectioning_root>`_ element.
        A footer typically contains information about the author of the section,
        copyright data or links to related documents.
        
        Examples::
        
            footer('Some copyright info or perhaps some author info for an <article>?')
    """


class h1(Component):
    """
        The **HTML ``<h1>``–``<h6>`` elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the lowest.
        
        Examples::
        
            h1('Heading level 1')
        
        ::
        
            h2('Heading level 2')
        
        ::
        
            h3('Heading level 3')
        
        ::
        
            h4('Heading level 4')
        
        ::
        
            h5('Heading level 5')
        
        ::
        
            h6('Heading level 6')
    """


class h2(Component):
    """
        The **HTML ``<h1>``–``<h6>`` elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the lowest.
        
        Examples::
        
            h1('Heading level 1')
        
        ::
        
            h2('Heading level 2')
        
        ::
        
            h3('Heading level 3')
        
        ::
        
            h4('Heading level 4')
        
        ::
        
            h5('Heading level 5')
        
        ::
        
            h6('Heading level 6')
    """


class h3(Component):
    """
        The **HTML ``<h1>``–``<h6>`` elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the lowest.
        
        Examples::
        
            h1('Heading level 1')
        
        ::
        
            h2('Heading level 2')
        
        ::
        
            h3('Heading level 3')
        
        ::
        
            h4('Heading level 4')
        
        ::
        
            h5('Heading level 5')
        
        ::
        
            h6('Heading level 6')
    """


class h4(Component):
    """
        The **HTML ``<h1>``–``<h6>`` elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the lowest.
        
        Examples::
        
            h1('Heading level 1')
        
        ::
        
            h2('Heading level 2')
        
        ::
        
            h3('Heading level 3')
        
        ::
        
            h4('Heading level 4')
        
        ::
        
            h5('Heading level 5')
        
        ::
        
            h6('Heading level 6')
    """


class h5(Component):
    """
        The **HTML ``<h1>``–``<h6>`` elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the lowest.
        
        Examples::
        
            h1('Heading level 1')
        
        ::
        
            h2('Heading level 2')
        
        ::
        
            h3('Heading level 3')
        
        ::
        
            h4('Heading level 4')
        
        ::
        
            h5('Heading level 5')
        
        ::
        
            h6('Heading level 6')
    """


class h6(Component):
    """
        The **HTML ``<h1>``–``<h6>`` elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the lowest.
        
        Examples::
        
            h1('Heading level 1')
        
        ::
        
            h2('Heading level 2')
        
        ::
        
            h3('Heading level 3')
        
        ::
        
            h4('Heading level 4')
        
        ::
        
            h5('Heading level 5')
        
        ::
        
            h6('Heading level 6')
    """


class header(Component):
    """
        The **HTML ``<header>`` element** represents introductory content, typically a
        group of introductory or navigational aids. It may contain some heading elements
        but also other elements like a logo, a search form, an author name, and so on.
    """


class hgroup(Component):
    """
        ** **This is an experimental technology**\\Because this technology's
        specification has not stabilized, check the `compatibility table
        <#Browser_compatibility>`_ for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **HTML ``<hgroup>`` element** represents a multi-level heading for a section
        of a document. It groups a set of ```<h1>–<h6> </en-
        US/docs/Web/HTML/Element/Heading_Elements>`_`` elements.
        
        Examples::
        
            hgroup(
                h1('HTML'),
                h2('Living Standard — Last Updated 12 August 2016'),
                id_='document-title')
    """


class nav(Component):
    """
        The **HTML ``<nav>`` element** represents a section of a page whose purpose is
        to provide navigation links, either within the current document or to other
        documents. Common examples of navigation sections are menus, tables of contents,
        and indexes.
        
        Examples::
        
            nav(ul(
                li(a('Home', href='#')),
                li(a('About', href='#')), li(a('Contact', href='#'))),
                class_='menu')
    """


class section(Component):
    """
        The **HTML ``<section>`` element** represents a standalone section of
        functionality contained within an HTML document, typically with a heading, which
        doesn't have a more specific semantic element to represent it.
        
        As an example, a navigation menu should be wrapped in a ```<nav>`` </en-
        US/docs/Web/HTML/Element/nav>`_ element, but a list of search results and a map
        display and its controls don't have specific elements, and could be put inside a
        ``<section>``.
    """


# == Text content ==

# Use HTML text content elements to organize blocks or sections of content
# placed between the opening ```<body>`` </en-US/docs/Web/HTML/Element/body>`_
# and closing ``</body>`` tags. Important for `accessibility </en-
# US/docs/Glossary/accessibility>`_ and `SEO </en-US/docs/Glossary/SEO>`_, these
# elements identify the purpose or structure of that content.


class blockquote(Component):
    """
        The **HTML ``<blockquote>`` Element** (or *HTML Block Quotation Element*)
        indicates that the enclosed text is an extended quotation. Usually, this is
        rendered visually by indentation (see `Notes </en-
        US/docs/HTML/Element/blockquote#Notes>`_ for how to change it). A URL for the
        source of the quotation may be given using the **cite** attribute, while a text
        representation of the source can be given using the ```<cite>`` </en-
        US/docs/Web/HTML/Element/cite>`_ element.
        
        Notes:
        
            To change ``<blockquote>`` indent, use `CSS </en-US/docs/CSS>`_ ```margin`` </en-US/docs/Web/CSS/margin>`_ property.
            
            For short quotes use the ```<q>`` </en-US/docs/Web/HTML/Element/q>`_ element.
        
        Examples::
        
            blockquote(
                p('This is a quotation taken from the Mozilla Developer Center.'),
                cite='http://developer.mozilla.org')
    """


class dd(Component):
    """
        The**HTML ``<dd>`` element** indicates the description of a term in a
        description list (```<dl>`` </en-US/docs/Web/HTML/Element/dl>`_).
    """


class div(Component):
    """
        The **HTML ``<div>`` element** is the generic container for flow content and
        does not inherently represent anything. Use it to group elements for purposes
        such as styling (using the ```class </en-
        US/docs/Web/HTML/Global_attributes#attr-class>`_`` or ```id </en-
        US/docs/Web/HTML/Global_attributes#attr-id>`_`` attributes), marking a section
        of a document in a different language (using the ```lang </en-
        US/docs/Web/HTML/Global_attributes#attr-lang>`_`` attribute), and so on.
        
        Examples::
        
            div(p('Any kind of content here. Such as <p>, <table>. You name it!'))
    """


class dl(Component):
    """
        The **HTML ``<dl>``**element represents a description list.****The element
        encloses a list of groups of terms and descriptions. Common uses for this
        element are to implement a glossary or to display metadata (a list of key-value
        pairs).
        
        Notes:
        
            Do not use this element (nor ```<ul>`` </en-US/docs/Web/HTML/Element/ul>`_ elements) to merely create indentation on a page. Although it works, this is a bad practice and obscures the meaning of description lists.
            
            To change the indentation of a description term, use the `CSS </en-US/docs/CSS>`_ ```margin`` </en-US/docs/Web/CSS/margin>`_ property.
        
        Examples::
        
            dl(
                dt('Firefox'),
                dd('A free, open source, cross-platform, graphical web browser developed by the Mozilla Corporation and hundreds of volunteers.'
                   ), '# Other terms and descriptions')
    """


class dt(Component):
    """
        The **HTML ``<dt>`` element** identifies a term in a description list. This
        element can occur only as a child element of a ```<dl>`` </en-
        US/docs/Web/HTML/Element/dl>`_. It is usually followed by a ```<dd>`` </en-
        US/docs/Web/HTML/Element/dd>`_ element; however, multiple ``<dt>`` elements in a
        row indicate several terms that are all defined by the immediate next
        ```<dd>```_ element.
    """


class figcaption(Component):
    """
        The **HTML ``<figcaption>`` element** represents a caption or a legend
        associated with a figure or an illustration described by the rest of the data of
        the ```<figure>`` </en-US/docs/Web/HTML/Element/figure>`_ element which is its
        immediate ancestor.
    """


class figure(Component):
    """
        The **HTML ``<figure>`` element** represents self-contained content, frequently
        with a caption (```<figcaption>`` </en-US/docs/Web/HTML/Element/figcaption>`_),
        and is typically referenced as a single unit.
        
        Examples::
        
            figure(
                figcaption('Get browser details using navigator'),
                pre('function NavigatorExample() { var txt; txt = "Browser CodeName: " + navigator.appCodeName; txt+= "Browser Name: " + navigator.appName; txt+= "Browser Version: " + navigator.appVersion ; txt+= "Cookies Enabled: " + navigator.cookieEnabled; txt+= "Platform: " + navigator.platform; txt+= "User-agent header: " + navigator.userAgent; }'
                    ))
    """


class hr(Component):
    """
        The **HTML ``<hr>`` element** represents a thematic break between paragraph-
        level elements (for example, a change of scene in a story, or a shift of topic
        with a section). In previous versions of HTML, it represented a horizontal rule.
        It may still be displayed as a horizontal rule in visual browsers, but is now
        defined in semantic terms, rather than presentational terms.
    """


class li(Component):
    """
        The **HTML ``<li>`` element** is used to represent an item in a list. It must be
        contained in a parent element: an ordered list (```<ol>`` </en-
        US/docs/Web/HTML/Element/ol>`_), an unordered list (```<ul>`` </en-
        US/docs/Web/HTML/Element/ul>`_), or a menu (```<menu>`` </en-
        US/docs/Web/HTML/Element/menu>`_). In menus and unordered lists, list items are
        usually displayed using bullet points. In ordered lists, they are usually
        displayed with an ascending counter on the left, such as a number or letter.
        
        Examples::
        
            ol(li('first item'), li('second item'), li('third item'))
    """


class main(Component):
    """
        The **HTML ``<main>`` element** represents the main content of the ```<body>``
        </en-US/docs/Web/HTML/Element/body>`_ of a document, portion of a document, or
        application. The main content area consists of content that is directly related
        to, or expands upon the central topic of, a document or the central
        functionality of an application.
        
        You can use multiple ``<main>`` elements within the same page when it makes
        sense to do so. For instance, if you have a page presenting multiple articles
        (each inside an ```<article>`` </en-US/docs/Web/HTML/Element/article>`_ element,
        each of which has some extra material within (such as toolbars for editing, ads,
        and so forth), it may make sense to include a ``<main>`` element within each
        article to identify the primary contents of that specific article.
        
        Examples::
        
            '#  other content'
        
        ::
        
            main(
                h1('Apples'),
                p('The apple is the pomaceous fruit of the apple tree.'),
                article(
                    h2('Red Delicious'),
                    p('These bright red apples are the most common found in many supermarkets.'
                      ), p('... '), p('... ')),
                article(
                    h2('Granny Smith'),
                    p('These juicy, green apples make a great filling for apple pies.'),
                    p('... '), p('... ')))
        
        ::
        
            '#  other content'
    """


class ol(Component):
    """
        The **HTML ``<ol>`` element** represents an ordered list of items, typically
        rendered as a numbered list.
        
        Examples::
        
            ol(li('first item'), li('second item'), li('third item'))
    """


class p(Component):
    """
        The **HTML ``<p>`` element** represents a paragraph of text. Paragraphs are
        usually represented in visual media as blocks of text that are separated from
        adjacent blocks by vertical blank space and/or first-line
        indentation. Paragraphs are `block-level elements </en-US/docs/Web/HTML/Block-
        level_elements>`_.
        
        Examples::
        
            p('This is the first paragraph of text. This is the first paragraph of text. This is the first paragraph of text. This is the first paragraph of text.'
              )
        
        ::
        
            p('This is the second paragraph. This is the second paragraph. This is the second paragraph. This is the second paragraph.'
              )
    """


class pre(Component):
    """
        The **HTML ``<pre>`` element** represents preformatted text. Text within this
        element is typically displayed in a non-proportional ("`monospace </en-
        US/docs/XUL/Style/monospace>`_") font exactly as it is laid out in the file.
        Whitespace inside this element is displayed as typed.
        
        Examples::
        
            '#  Some example CSS code'
        
        ::
        
            pre('body { color:red; }')
    """


class ul(Component):
    """
        The **HTML ``<ul>`` element** represents an unordered list of items, typically
        rendered as a bulleted list.
        
        Examples::
        
            ul(li('first item'), li('second item'), li('third item'))
    """


# == Inline text semantics ==

# Use the HTML inline text semantic to define the meaning, structure, or style
# of a word, line, or any arbitrary piece of text.


class a(Component):
    """
        The **HTML ``<a>`` element** (or *anchor* element) creates a hyperlink to other
        web pages, files, locations within the same page, email addresses, or any other
        URL.
        
        Notes:
        
            HTML 3.2 defines only the ``name``, ``href``, ``rel``, ``rev``, and ``title`` attributes.
            
            Accessibility recommendations
            =============================
            
            Anchor tags are often abused with the ``onclick`` event to create pseudo-buttons by setting**href**to ``"#"`` or ``"javascript:void(0)"``to prevent the page from refreshing. These values cause unexpected behavior when copying/dragging links, opening links in a new tabs/windows, bookmarking, and when JavaScript is still downloading, errors out, or is disabled. This also conveys incorrect semantics to assistive technologies (e.g., screen readers). In these cases, it is recommended to use a ```<button>`` </en-US/docs/Web/HTML/Element/button>`_ instead. In general you should only use an anchor for navigation using a proper URL.
            
            Clicking and focus
            ==================
            
            Whether clicking on an ```<a>`` </en-US/docs/Web/HTML/Element/a>`_ causes it to become focused varies by browser and OS.
        
        Examples::
        
            '#  anchor linking to external file'
        
        ::
        
            a('External Link', href='https://www.mozilla.com/')
    """


class abbr(Component):
    """
        The **HTML ``<abbr>`` element** represents an abbreviation and optionally
        provides a full description for it. If present, the ```title </en-
        US/docs/Web/HTML/Global_attributes#attr-title>`_`` attribute must contain this
        full description and nothing else.
        
        Examples::
        
            abbr('I18N', title='Internationalization')
    """


class b(Component):
    """
        The **HTML ``<b>`` element** represents a span of text stylistically different
        from normal text, without conveying any special importance or relevance, and
        that is typically rendered in boldface.
    """


class bdi(Component):
    """
        The **HTML ``<bdi>`` element** (*bidirectional isolation*) isolates a span of
        text that might be formatted in a different direction from other text outside
        it.
        
        This element is useful when embedding text with an unknown directionality, from
        a database for example, inside text with a fixed directionality.
        
        Examples::
        
            p('This arabic word ',
              bdi('ARABIC_PLACEHOLDER'),
              ' is automatically displayed right-to-left.',
              dir_='ltr')
    """


class bdo(Component):
    """
        The **HTML ``<bdo>`` element** (*bidirectional override*) is used to override
        the current directionality of text. It causes the directionality of the
        characters to be ignored in favor of the specified directionality.
        
        Notes:
        
            The HTML 4 specification did not specify events for this element; they were added in XHTML. This is most likely an oversight.
        
        Examples::
        
            '#  Switch text direction'
        
        ::
        
            p('This text will go left to right.')
        
        ::
        
            p(bdo('This text will go right to left.', dir_='rtl'))
    """


class br(Component):
    """
        The **HTML ``<br>`` element** produces a line break in text (carriage-return).
        It is useful for writing a poem or an address, where the division of lines is
        significant.
        
        Notes:
        
            Do not use ``<br>`` to increase the gap between lines of text; use the `CSS </en-US/docs/CSS>`_ ```margin`` </en-US/docs/Web/CSS/margin>`_ property or the ```<p>`` </en-US/docs/Web/HTML/Element/p>`_ element.
    """


class cite(Component):
    """
        The **HTML <cite> element** represents a reference to a creative work. It must
        include the title of a work or a URL reference, which may be in an abbreviated
        form according to the conventions used for the addition of citation metadata.
        
        Examples::
        
            cite('[ISO-0000]')
    """


class code(Component):
    """
        The **HTML ``<code>`` element** represents a fragment of computer code. By
        default, it is displayed in the browser's default monospace font.
        
        Notes:
        
            A CSS rule can be defined for the ``code`` selector to override the browser's default font face. Preferences set by the user might take precedence over the specified CSS.
        
        Examples::
        
            p('This is how we declare a Javascript variable:', br(), code('var i = 0;'))
    """


class data(Component):
    """
        The **HTML ``<data>`` element** links a given content with a machine-readable
        translation. If the content is time- or date-related, the ```<time>`` </en-
        US/docs/Web/HTML/Element/time>`_ element must be used.
        
        Examples::
        
            p('New Products')
        
        ::
        
            ul(
                li(data('Mini Ketchup', value='398')),
                li(data('Jumbo Ketchup', value='399')),
                li(data('Mega Jumbo Ketchup', value='400')))
    """


class dfn(Component):
    """
        The **HTML <dfn> element** represents the defining instance of a term.
        
        Examples::
        
            '#  Define "The Internet"'
        
        ::
        
            p(
                dfn('The Internet', id_='def-internet'),
                ' is a global system of interconnected networks that use the Internet Protocol Suite (TCP/IP) to serve billions of users worldwide.'
            )
    """


class em(Component):
    """
        The **HTML ``<em>`` element**marks text that has stress emphasis. The ``<em>``
        element can be nested, with each level of nesting indicating a greater degree of
        emphasis.
        
        Examples::
        
            p('In HTML 5, what was previously called',
              em('block-level'), ' content is now called ', em('flow'), ' content. ')
    """


class i(Component):
    """
        The **HTML ``<i>`` element** represents a range of text that is set off from the
        normal text for some reason, for example, technical terms, foreign language
        phrases, or fictional character thoughts. It is typically displayed in italic
        type.
        
        Notes:
        
            In earlier versions of the HTML specification, the ``<i>`` tag was merely a presentational element used to display text in italics, much like the ``<b>`` tag was used to display text in bold letters. This is no longer true, as these tags now define semantics rather than typographic appearance. The ``<i>`` tag should represent a range of text with a different semantic meaning whose typical typographic representation is italicized. This means a browser will typically still display its contents in italic type, but is, by definition, no longer required to.
            
            Use this element only when there is not a more appropriate semantic element. For example:
            
            * Use ```<em>`` </en-US/docs/Web/HTML/Element/em>`_ to indicate emphasis or stress.
            
            * Use ```<strong>`` </en-US/docs/Web/HTML/Element/strong>`_ to indicate importance.
            
            * Use ```<mark>`` </en-US/docs/Web/HTML/Element/mark>`_ to indicate relevance.
            
            * Use ```<cite>`` </en-US/docs/Web/HTML/Element/cite>`_ to mark the name of a work, such as a book, play, or song.
            
            * Use ```<dfn>`` </en-US/docs/Web/HTML/Element/dfn>`_ to mark the defining instance of a term.
            
            It is a good idea to use the **class** attribute to identify why the element is being used, so that if the presentation needs to change at a later date, it can be done selectively with style sheets.
        
        Examples::
        
            p('The Latin phrase ',
              i('Veni, vidi, vici', class_='latin'),
              ' is often mentioned in music, art, and literature.')
    """


class kbd(Component):
    """
        The **HTML ``<kbd>`` element** represents user input and produces an inline
        element displayed in the browser's default monospace font.
        
        Notes:
        
            A CSS rule can be defined for the ``kbd`` selector to override the browser's default font face. Preferences set by the user might take precedence over the specified CSS.
            
            When the ``<kbd>`` element is nested inside a ``<samp>`` element, it represents the input as it was echoed by the system.
            
            When the ``<kbd>`` element *contains* a ``<samp>`` element, it represents input based on system output, for example invoking a menu item.
            
            When the ``<kbd>`` element is nested inside another ``<kbd>`` element, it represents an actual key or other single unit of input as appropriate for the input mechanism.
        
        Examples::
        
            p('Type the following in the Run dialog: ',
              kbd('cmd'), br(), 'Then click the OK button.')
        
        ::
        
            p('Save the document by pressing ', kbd('Ctrl'), ' + ', kbd('S'))
    """


class mark(Component):
    """
        The **HTML ``<mark>`` element** represents highlighted text, i.e., a run of text
        marked for reference purpose, due to its *relevance* in a particular context.
        For example it can be used in a page showing search results to highlight every
        instance of the searched-for word.
        
        Examples::
        
            p('The <mark> element is used to ', mark('highlight'), ' text')
    """


class q(Component):
    """
        The **HTML ``<q>`` element** indicates that the enclosed text is a short inline
        quotation. This element is intended for short quotations that don't require
        paragraph breaks; for long quotations use the ```<blockquote>`` </en-
        US/docs/Web/HTML/Element/blockquote>`_ element.
        
        Examples::
        
            p("According to Mozilla's website, ",
              q('Firefox 1.0 was released in 2004 and became a big success.',
                cite='https://www.mozilla.org/en-US/about/history/details/'))
    """


class rp(Component):
    """
        The **HTML ``<rp>`` element** is used to provide fall-back parentheses for
        browsers that do not support display of ruby annotations using the ```<ruby>``
        </en-US/docs/Web/HTML/Element/ruby>`_ element.
        
        Examples::
        
            ruby('漢', rp('('), rt('Kan'), rp(')'), ' 字 ', rp('('), rt('ji'), rp(')'))
    """


class rt(Component):
    """
        The **HTML ``<rt>`` element** embraces pronunciation of characters presented in
        a ruby annotations, which are used to describe the pronunciation of East Asian
        characters. This element is always used inside a ```<ruby>`` </en-
        US/docs/Web/HTML/Element/ruby>`_ element.
        
        Examples::
        
            ruby('漢', rt('Kan'), ' 字 ', rt('ji'))
    """


class rtc(Component):
    """
        The **HTML ``<rtc>`` element** embraces semantic annotations of characters
        presented in a ruby of ```<rb>`` </en-US/docs/Web/HTML/Element/rb>`_ elements
        used inside of ```<ruby>`` </en-US/docs/Web/HTML/Element/ruby>`_ element.
        ```<rb>```_ elements can have both pronunciation (```<rt>`` </en-
        US/docs/Web/HTML/Element/rt>`_) and semantic (```<rtc>`` </en-
        US/docs/Web/HTML/Element/rtc>`_) annotations.
        
        Examples::
        
            ruby(
                rb('旧'),
                rb('金'), rb('山'), rt('jiù'), rt('jīn'), rt('shān'), rtc('San Francisco'))
    """


class ruby(Component):
    """
        The **HTML ``<ruby>`` element** represents a ruby annotation. Ruby annotations
        are for showing pronunciation of East Asian characters.
    """


class s(Component):
    """
        The **HTML ``<s>`` element** renders text with a strikethrough, or a line
        through it. Use the ``<s>`` element to represent things that are no longer
        relevant or no longer accurate. However, ``<s>`` is not appropriate when
        indicating document edits; for that, use the ```<del>`` </en-
        US/docs/Web/HTML/Element/del>`_ and ```<ins>`` </en-
        US/docs/Web/HTML/Element/ins>`_ elements, as appropriate.
    """


class samp(Component):
    """
        The **HTML ``<samp>`` element** is an element intended to identify sample output
        from a computer program. It is usually displayed in the browser's default
        monotype font (such as Lucida Console).
        
        Notes:
        
            A CSS rule can be defined for the ``samp`` selector to override the browser's default font face. Preferences set by the user might take precedence over the specified CSS.
        
        Examples::
        
            p('The diet-tracking app said: ',
              samp("You're not eating your veggies"), ' and that was true')
    """


class small(Component):
    """
        The **HTML ``<small>``** **element** makes the text *font size* one size smaller
        (for example, from large to medium, or from small to x-small) down to the
        browser's minimum font size.  In HTML5, this element is repurposed to represent
        side-comments and small print, including copyright and legal text, independent
        of its styled presentation.
        
        Notes:
        
            Although the ``<small>`` element, like the ``<b>`` and ``<i>`` elements, may be perceived to violate the principle of separation between structure and presentation, all three are valid in HTML5. Authors are encouraged to use their best judgement when determining whether to use ``<small>`` or CSS.
        
        Examples::
        
            p('This is the first sentence. ',
              small('This whole sentence is in small letters.'))
    """


class span(Component):
    """
        The **HTML ``<span>`` element** is a generic inline container for phrasing
        content, which does not inherently represent anything. It can be used to group
        elements for styling purposes (using the ``class`` or ``id`` attributes), or
        because they share attribute values, such as ``lang``. It should be used only
        when no other semantic element is appropriate. ``<span>`` is very much like a
        ```<div>`` </en-US/docs/Web/HTML/Element/div>`_ element, but ```<div>```_ is a
        `block-level element </en-US/docs/HTML/Block-level_elements>`_ whereas a
        ``<span>`` is an `inline element </en-US/docs/HTML/Inline_elements>`_.
    """


class strong(Component):
    """
        The **HTML** ``**<strong>**`` **element** gives text strong importance, and is
        typically displayed in bold.
        
        Examples::
        
            p('When doing x it is ', strong('imperative'), ' to do y before proceeding.')
    """


class sub(Component):
    """
        The **HTML ``<sub>`` element** defines a span of text that should be displayed,
        for typographic reasons, lower, and often smaller, than the main span of text.
        
        Examples::
        
            p('The chemical formula of water: H', sub('2'), 'O')
    """


class sup(Component):
    """
        The **HTML ``<sup>`` element** defines a span of text that should be displayed,
        for typographic reasons, higher, and often smaller, than the main span of text.
        
        Examples::
        
            p('This text is ', sup('superscripted'))
    """


class time(Component):
    """
        The **HTML ``<time>`` element** represents either a time on a 24-hour clock or a
        precise date in the `Gregorian calendar
        <https://en.wikipedia.org/wiki/Gregorian_calendar>`_ (with optional time and
        timezone information).
        
        Examples::
        
            p('The concert starts at ', time('20:00'), '.')
    """


class u(Component):
    """
        The **HTML ``<u>`` element** renders text with an underline, a line under the
        baseline of its content. In HTML5, this element represents a span of text with
        an unarticulated, though explicitly rendered, non-textual annotation, such as
        labeling the text as being a proper name in Chinese text (a Chinese proper name
        mark), or labeling the text as being misspelled.
        
        Examples::
        
            u("Today's Special")
        
        ::
        
            br()
        
        ::
        
            span("Today's Special", style='text-decoration:underline;')
        
        ::
        
            '#  Here <span> is used as the underlining is purely decorative   and it is\n# applied with CSS'
    """


class var(Component):
    """
        The **HTML ``<var>`` element** represents a variable in a mathematical
        expression or a programming context.
    """


class wbr(Component):
    """
        The **HTML ``<wbr>`` element** represents a word break opportunity—a position
        within text where the browser may optionally break a line, though its line-
        breaking rules would not otherwise create a break at that location.
        
        Notes:
        
            On UTF-8 encoded pages, ``<wbr>`` behaves like the ``U+200B`` ``ZERO-WIDTH SPACE`` code point. In particular, it behaves like a Unicode bidi BN code point, meaning it has no effect on bidi-ordering: ``<div dir=rtl>123,<wbr>456</div>`` displays, when not broken on two lines, ``123,456`` and not ``456,123``.
            
            For the same reason, the ``<﻿wbr﻿>`` element does not introduce a hyphen at the line break point. To make a hyphen appear only at the end of a line, use the soft hyphen character entity (``&﻿shy;``) instead.
            
            This element was first implemented in Internet Explorer 5.5 and was officially defined in HTML5.
    """


# == Image and multimedia ==

# HTML supports various multimedia resources such as images, audio, and video.


class area(Component):
    """
        The **HTML ``<area>`` element** defines a hot-spot region on an image, and
        optionally associates it with a `hypertext link </en-
        US/docs/Glossary/Hyperlink>`_. This element is used only within a ```<map>``
        </en-US/docs/Web/HTML/Element/map>`_ element.
        
        Notes:
        
            Under the HTML 3.2, 4.0, and 5 specifications, the closing tag ``</area>`` is forbidden.
            
            The XHTML 1.0 specification requires a trailing slash: ``<area />``.
            
            The **id**, **class**, and **style** attributes have the same meaning as the core attributes defined in the HTML 4 specification, but only Netscape and Microsoft define them.
            
            Netscape 1–level browsers do not understand the **target** attribute as it relates to frames.
            
            HTML 3.2 defines only **alt**, **coords**, **href**, **nohref**, and **shape**.
            
            HTML 5.1 `defines <https://www.w3.org/TR/html51/obsolete.html#obsolete>`_ obsolete the attribute **type** on this tag.
    """


class audio(Component):
    """
        The **HTML ``<audio>`` element** is used to embed sound content in documents. It
        may contain one or more audio sources, represented using the ``src`` attribute
        or the ```<source>`` </en-US/docs/Web/HTML/Element/source>`_ element: the
        browser will choose the most suitable one. It can also be the destination for
        streamed media, using a ```MediaStream`` </en-US/docs/Web/API/MediaStream>`_.
    """


class img(Component):
    'The **HTML ``<img>`` element** represents an image in the document.'


class map_(Component):
    """
        The **HTML ``<map>`` element** is used with ```<area>`` </en-
        US/docs/Web/HTML/Element/area>`_ elements to define an image map (a clickable
        link area).
    """
    tag_name = 'map'


class track(Component):
    """
        The **HTML ``<track>`` element** is used as a child of the media elements
        ```<audio>`` </en-US/docs/Web/HTML/Element/audio>`_ and ```<video>`` </en-
        US/docs/Web/HTML/Element/video>`_. It lets you specify timed text tracks (or
        time-based data), for example to automatically handle subtitles. The tracks are
        formatted in `WebVTT format </en-US/docs/Web/API/Web_Video_Text_Tracks_Format>`_
        (``.vtt`` files) — Web Video Text Tracks.
    """


class video(Component):
    'Use the **HTML ``<video>`` element** to embed video content in a document.'


# == Embedded content ==

# In addition to regular multimedia content, HTML can include a variety of other
# content, even if it's not always easy to interact with.


class embed(Component):
    """
        The **HTML ``<embed>`` element** represents an integration point for an external
        application or interactive content (in other words, a plug-in).
        
        **Note:**This topic documents only the element that is defined as part of HTML5.
        It does not address earlier, non-standardized implementation of the element.
    """


class object_(Component):
    """
        The **HTML ``<object>`` element** represents an external resource, which can be
        treated as an image, a nested browsing context, or a resource to be handled by a
        plugin.
    """
    tag_name = 'object'


class param(Component):
    """
        The **HTML ``<param>`` element** defines parameters for an ```<object>`` </en-
        US/docs/Web/HTML/Element/object>`_ element.
    """


class source(Component):
    """
        The **HTML ``<source>`` element** specifies multiple media resources for either
        the ```<picture>`` </en-US/docs/Web/HTML/Element/picture>`_, the ```<audio>``
        </en-US/docs/Web/HTML/Element/audio>`_ or the ```<video>`` </en-
        US/docs/Web/HTML/Element/video>`_ element. It is an empty element. It is
        commonly used to serve the same media content in `multiple formats supported by
        different browsers </en-
        US/docs/Media_formats_supported_by_the_audio_and_video_elements>`_.
    """


# == Scripting ==

# In order to create dynamic content and Web applications, HTML supports the use
# of scripting languages, most prominently JavaScript. Certain elements support
# this capability.


class canvas(Component):
    """
        Use the **HTML ``<canvas>`` element** with the `canvas scripting API </en-
        US/docs/Web/API/Canvas_API>`_ to draw graphics and animations.
        
        Examples::
        
            canvas(
                'An alternative text describing what your canvas displays.',
                id_='canvas',
                width='300',
                height='300')
    """


class noscript(Component):
    """
        The **HTML ``<noscript>`` element** defines a section of HTML to be inserted if
        a script type on the page is unsupported or if scripting is currently turned off
        in the browser.
        
        Examples::
        
            noscript('# anchor linking to external file',
                     a('External Link', href='https://www.mozilla.com/'))
        
        ::
        
            p('Rocks!')
    """


class script(Component):
    """
        The **HTML ``<script>`` element** is used to embed or reference an executable
        script.
        
        Notes:
        
            Scripts without ``async`` or ``defer`` attributes, as well as inline scripts, are fetched and executed immediately, before the browser continues to parse the page.
            
            The script should be served with the ``text/javascript`` MIME type, but browsers are lenient and only block them if the script is served with an image type (``image/*``), a video type (``video/*``), an audio (``audio/*``) type, or ``text/csv``. If the script is blocked, an ```error </en-US/docs/Web/Events/error>`_`` is sent to the element, if not a ```load </en-US/docs/Web/Events/load>`_`` event is sent.
        
        Examples::
        
            '#  HTML4 and (x)HTML'
        
        ::
        
            script(type_='text/javascript', src='javascript.js')
        
        ::
        
            '#  HTML5'
        
        ::
        
            script(src='javascript.js')
    """


# == Demarcating edits ==

# These elements let you provide indications that specific parts of the text
# have been altered.


class del_(Component):
    """
        The **HTML ``<del>`` element** represents a range of text that has been deleted
        from a document. This element is often (but need not be) rendered with strike-
        through text.
        
        Examples::
        
            p(del_('This text has been deleted'), ', here is the rest of the paragraph.')
        
        ::
        
            del_(p('This paragraph has been deleted.'))
    """
    tag_name = 'del'


class ins(Component):
    """
        The **HTML ``<ins>`` element** represents a range of text that has been added to
        a document.
        
        Examples::
        
            ins('This text has been inserted')
    """


# == Table content ==

# The elements here are used to create and handle tabular data.


class caption(Component):
    """
        The **HTML ``<caption>`` element** represents the title of a table. Though it is
        always the first descendant of a ```<table>`` </en-
        US/docs/Web/HTML/Element/table>`_, its styling, using CSS, may place it
        elsewhere, relative to the table.
    """


class col(Component):
    """
        The **HTML ``<col>`` element** defines a column within a table and is used for
        defining common semantics on all common cells. It is generally found within a
        ```<colgroup>`` </en-US/docs/Web/HTML/Element/colgroup>`_ element.
        
        This element allows styling columns using CSS, but only a few attributes will
        have an effect on the column (`see the CSS 2.1 specification
        <https://www.w3.org/TR/CSS21/tables.html#columns>`_ for a list).
    """


class colgroup(Component):
    'The **HTML ``<colgroup>`` element** defines a group of columns within a table.'


class table(Component):
    """
        The **HTML ``<table>`` element** represents tabular data — that is, information
        expressed via a two-dimensional data table.
        
        Examples::
        
            table(tr(td('John'), td('Doe')), tr(td('Jane'), td('Doe')))
    """


class tbody(Component):
    """
        The **HTML ``<tbody>`` element** groups one or more ```<tr>`` </en-
        US/docs/Web/HTML/Element/tr>`_ elements as the body of a ```<table>`` </en-
        US/docs/Web/HTML/Element/table>`_ element.
    """


class td(Component):
    """
        The **HTML ``<td>`` element** defines a cell of a table that contains data. It
        participates in the *table model*.
    """


class tfoot(Component):
    """
        The **HTML ``<tfoot>`` element** defines a set of rows summarizing the columns
        of the table.
    """


class th(Component):
    """
        The **HTML ``<th>`` element** defines a cell as header of a group of table
        cells. The exact nature of this group is defined by the ```scope </en-
        US/docs/Web/HTML/Element/th#attr-scope>`_`` and ```headers </en-
        US/docs/Web/HTML/Element/th#attr-headers>`_`` attributes.
    """


class thead(Component):
    """
        The **HTML ``<thead>`` element** defines a set of rows defining the head of the
        columns of the table.
    """


class tr(Component):
    """
        The HTML **``<tr>``** element specifies that the markup contained inside the
        ``<tr>`` block comprises one row of a table, inside which the ```<th>`` </en-
        US/docs/Web/HTML/Element/th>`_ and ```<td>`` </en-US/docs/Web/HTML/Element/td>`_
        elements create header and data cells, respectively, within the row. Each cell
        is placed into its own column; the `user agent </en-
        US/docs/Glossary/user_agent>`_ follows specific rules to determine how the cells
        in each row are placed into columns with those coming from other rows.
        
        To provide additional control over how cells fit into (or span across) columns,
        both ``<th>`` and ``<td>`` support the```colspan </en-
        US/docs/Web/HTML/Element/td#attr-colspan>`_`` attribute, which lets you specify
        how many columns wide the cell should be, with the default being 1. Similarly,
        you can use the```rowspan </en-US/docs/Web/HTML/Element/td#attr-rowspan>`_``
        attribute on cells to indicate they should span more than one table row.
        
        This can take a little practice to get right when building your tables. We have
        some `examples <#Examples>`_ below, but for more examples and an in-depth
        tutorial, see the `HTML tables </en-US/docs/Learn/HTML/Tables>`_ series in our
        `Learn web development </en-US/docs/Learn>`_ area, where you'll learn how to use
        the table elements and their attributes to get just the right layout and
        formatting for your tabular data.
        
        Examples::
        
            table(
                tr(th('Name'), th('ID'), th('Member Since'), th('Balance')),
                tr(
                    td('Margaret Nguyen'),
                    td('427311'),
                    td(time('June 3, 2010', datetime='2010-06-03')), td('0.00')),
                tr(
                    td('Edvard Galinski'),
                    td('533175'),
                    td(time('January 13, 2011', datetime='2011-01013')), td('37.00')),
                tr(
                    td('Hoshi Nakamura'),
                    td('601942'),
                    td(time('July 23, 2012', datetime='2012-07-23')), td('15.00')))
    """


# == Forms ==

# HTML provides a number of elements which can be used together to create forms
# which the user can fill out and submit to the Web site or application. There's
# a great deal of further information about this available in the `HTML forms
# guide </en-US/docs/Web/Guide/HTML/Forms>`_.


class button(Component):
    """
        The **HTML ``<button>`` element** represents a clickable button.
        
        Notes:
        
            ``<button>`` elements are much easier to style than ```<input>`` </en-US/docs/Web/HTML/Element/input>`_ elements. You can add inner HTML content (think ``<em>``, ``<strong>`` or even ``<img>``), and make use of ```:after`` </en-US/docs/Web/CSS/:after>`_ and ```:before`` </en-US/docs/Web/CSS/:before>`_ pseudo-element to achieve complex rendering while ```<input>```_ only accepts a text value attribute.
            
            IE7 has a bug where when submitting a form with ``<button type="submit" name="myButton" value="foo">Click me</button>``, the ``POST`` data sent will result in ``myButton=Click me`` instead of ``myButton=foo``.
            IE6 has an even worse bug where submitting a form through a button will submit ALL buttons of the form, with the same bug as IE7.
            This bug has been fixed in IE8.
            
            Firefox will add, for accessibility purposes, a small dotted border on a focused button. This border is declared through CSS, in the browser stylesheet, but you can override it if necessary to add your own focused style using ``button```::-moz-focus-inner`` </en-US/docs/Web/CSS/::-moz-focus-inner>`_ { }``
            
            Firefox will, unlike other browsers, by default, `persist the dynamic disabled state <https://stackoverflow.com/questions/5985839/bug-with-firefox-disabled-attribute-of-input-not-resetting-when-refreshing>`_ of a ```<button>`` </en-US/docs/Web/HTML/Element/button>`_ across page loads. Setting the value of the ```autocomplete </en-US/docs/Web/HTML/Element/button#attr-autocomplete>`_`` attribute to ``off`` disables this feature. See `bug 654072 <https://bugzilla.mozilla.org/show_bug.cgi?id=654072>`_.
            
            Firefox <35 for Android sets a default ```background-image`` </en-US/docs/Web/CSS/background-image>`_ gradient on all buttons (see `bug 763671 <https://bugzilla.mozilla.org/show_bug.cgi?id=763671>`_). This can be disabled using ``background-image: none``.
            
            Clicking and focus
            ==================
            
            Whether clicking on a ```<button>`` </en-US/docs/Web/HTML/Element/button>`_ causes it to (by default) become focused varies by browser and OS. The results for ```<input>`` </en-US/docs/Web/HTML/Element/input>`_ of ``type="button"`` and ``type="submit"`` were the same.
    """


class datalist(Component):
    """
        The **HTML ``<datalist>`` element** contains a set of ```<option>`` </en-
        US/docs/Web/HTML/Element/option>`_ elements that represent the values available
        for other controls.
    """


class fieldset(Component):
    """
        The **HTML ``<fieldset>`` element** is used to group several controls as well as
        labels (```<label>`` </en-US/docs/Web/HTML/Element/label>`_) within a web form.
    """


class form(Component):
    """
        The **HTML ``<form>`` element** represents a document section that contains
        interactive controls to submit information to a web server.
        
        It is possible to use the ```:valid`` </en-US/docs/Web/CSS/:valid>`_ and
        ```:invalid`` </en-US/docs/Web/CSS/:invalid>`_ CSS pseudo-classes to style a
        ``<form>`` element.
    """


class input_(Component):
    """
        The **HTML ``<input>`` element** is used to create interactive controls for web-
        based forms in order to accept data from the user.
        
        Notes:
        
            File inputs
            ===========
            
            #. Starting in Gecko 2.0, calling the ``click()`` method on an ``<input>`` element of type ``file`` opens the file picker and lets the user select files. See `Using files from web applications </en-US/docs/Using_files_from_web_applications>`_ for an example and more details.
            
            #. You cannot set the value of a file picker from a script — doing something like the following has no effect:
            
            var e = getElementById("someFileInputElement"); e.value = "foo";
            
            #. When a file is chosen using an ``<input type="file">``, the real path to the source file is not shown in the input's ``value`` attribute for obvious security reasons. Instead, the filename is shown, with ``C:\fakepath`` appended to the beginning of it. There are some historical reasons for this quirk, but it is supported across all modern browsers, and in fact is `defined in the spec <https://html.spec.whatwg.org/multipage/forms.html#fakepath-srsly>`_.
            
            Error messages
            ==============
            
            If you want Firefox to present a custom error message when a field fails to validate, you can use the ``x-moz-errormessage`` attribute to do so:
            
            <input type="email" x-moz-errormessage="Please specify a valid email address.">
            
            Note, however, that this is not standard and will not have an effect on other browsers.
            
            Localization
            ============
            
            The allowed inputs for certain <input> types depend on the locale. In some locales, 1,000.00 is a valid number, while in other locales the valid way to enter this number is 1.000,00.
            
            Firefox uses the following heuristics to determine the locale to validate the user's input (at least for ``type="number"``):
            
            * Try the language specified by a ``lang``/``xml:lang`` attribute on the element or any of its parents.
            
            * Try the language specified by any Content-Language HTTP header or
            
            * If none specified, use the browser's locale.
            
            Using mozactionhint on Firefox mobile
            =====================================
            
            You can use the ```mozactionhint </en-US/docs/Web/HTML/Element/input#attr-mozactionhint>`_`` attribute to specify the text for the label of the enter key on the virtual keyboard when your form is rendered on Firefox mobile. For example, to have a "Next" label, you can do this:
            
            <input type="text" mozactionhint="next">
            
            The result is:
            
            `|mozactionhint.png| </@api/deki/files/4970/=mozactionhint.png>`_
            
            .. |mozactionhint.png| image:: /@api/deki/files/4970/=mozactionhint.png?size=webview
    """
    tag_name = 'input'


class label(Component):
    """
        The **HTML ``<label>`` element** represents a caption for an item in a user
        interface.
    """


class legend(Component):
    """
        The **HTML ``<legend>`` element** represents a caption for the content of its
        parent ```<fieldset>`` </en-US/docs/Web/HTML/Element/fieldset>`_.
    """


class meter(Component):
    """
        The **HTML ``<meter>`` element** represents either a scalar value within a known
        range or a fractional value.
        
        Examples::
        
            p('Heat the oven to ',
              meter('350 degrees', min_='200', max_='500', value='350'), '.')
    """


class optgroup(Component):
    """
        The **HTML ``<optgroup>`` element** creates a grouping of options within a
        ```<select>`` </en-US/docs/Web/HTML/Element/select>`_ element.
    """


class option(Component):
    """
        The **HTML ``<option>`` element** is used to define an item contained in a
        ```<select>`` </en-US/docs/Web/HTML/Element/select>`_, an ```<optgroup>`` </en-
        US/docs/Web/HTML/Element/optgroup>`_, or a ```<datalist>`` </en-
        US/docs/Web/HTML/Element/datalist>`_element. As such,``<option>``can represent
        menu items in popups and other lists of items in an HTML document.
    """


class output(Component):
    """
        Introduced in `HTML5 </en-US/docs/HTML/HTML5>`_
        
        The **HTML ``<output>`` element** represents the result of a calculation or user
        action.
        
        Examples::
        
            form(
                input_(type_='range', name='b', value='50'),
                ' + ',
                input_(type_='number', name='a', value='10'),
                ' = ',
                output('60', name='result'),
                oninput='result.value=parseInt(a.value)+parseInt(b.value)')
    """


class progress(Component):
    """
        Introduced in `HTML5 </en-US/docs/HTML/HTML5>`_
        
        The **HTML ``<progress>`` element** represents the completion progress of a
        task, typically displayed as a progress bar.
        
        Examples::
        
            progress('70 %', value='70', max_='100')
    """


class select(Component):
    """
        The **HTML ``<select>`` element** represents a control that provides a menu of
        options:
        
        Notes:
        
            The content of this element is static and not `editable </en-US/docs/HTML/Content_Editable>`_.
    """


class textarea(Component):
    """
        The **HTML ``<textarea>`` element** represents a multi-line plain-text editing
        control.
        
        Examples::
        
            textarea('Write something here', name='textarea', rows='10', cols='50')
    """


# == Interactive elements ==

# HTML offers a selection of elements which help to create interactive user
# interface objects.


class details(Component):
    """
        The **HTML ``<details>`` element** is used as a disclosure widget from which the
        user can retrieve additional information.
    """


class dialog(Component):
    """
        The **HTML ``<dialog>`` element** represents a dialog box or other interactive
        component, such as an inspector or window.
    """


class menu(Component):
    """
        ** **This is an `experimental technology </en-US/docs/MDN/Contribute/Guidelines/
        Conventions_definitions#Experimental>`_**\\Check the `Browser compatibility
        table <#Browser_compatibility>`_ carefully before using this in production.
        
        The **HTML ``<menu>`` element** represents a group of commands that a user can
        perform or activate. This includes both list menus, which might appear across
        the top of a screen, as well as context menus, such as those that might appear
        underneath a button after it has been clicked.
    """


class menuitem(Component):
    """
        ** **This is an `experimental technology </en-US/docs/MDN/Contribute/Guidelines/
        Conventions_definitions#Experimental>`_**\\Check the `Browser compatibility
        table <#Browser_compatibility>`_ carefully before using this in production.
        
        The **HTML ``<menuitem>`` element** represents a command that a user is able to
        invoke through a popup menu. This includes context menus, as well as menus that
        might be attached to a menu button.
        
        A command can either be defined explicitly, with a textual label and optional
        icon to describe its appearance, or alternatively as an *indirect command* whose
        behavior is defined by a separate element. Commands can also optionally include
        a checkbox or be grouped to share radio buttons. (Menu items for indirect
        commands gain checkboxes or radio buttons when defined against elements ``<input
        type="checkbox">`` and ``<input type="radio">``.)
    """


class summary(Component):
    """
        The **HTML ``<summary>`` element** is used as a summary, caption, or legend for
        the content of a ```<details>`` </en-US/docs/Web/HTML/Element/details>`_
        element.
    """


# == Web Components ==

# Web Components is an HTML-related technology which makes it possible to,
# essentially, create and use custom elements as if it were regular HTML. In
# addition, you can create custom versions of standard HTML elements.


class content(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **HTML ``<content>`` element**—an obsolete part of the `Web Components </en-
        US/docs/Web/Web_Components>`_ suite of technologies—was used inside of `Shadow
        DOM </en-US/docs/Web/Web_Components/Shadow_DOM>`_ as an `insertion point </en-
        US/docs/Glossary/insertion_point>`_, and wasn't meant to be used in ordinary
        HTML It has now been replaced by the ```<slot>`` </en-
        US/docs/Web/HTML/Element/slot>`_ element, which creates a point in the DOM at
        which a shadow DOM can be inserted.
        
        **Note:** Though present in early draft of the specifications and implemented in
        several browsers, this element has been removed in later versions of the spec.
    """


class element(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The **HTML ``<element>`` element** was part of `Web Components </en-
        US/docs/Web/Web_Components>`_; this element was intended to be used to define
        new custom DOM elements. It was removed in favor of a JavaScript-driven
        methodology for creating new custom elements; however, that technology is not
        mature and no browers fully implement it.
        
        **Note:** This element has been removed from the specification. See `this
        <http://lists.w3.org/Archives/Public/public-webapps/2013JulSep/0287.html>`_ for
        more information from the editor of the specification.
    """


class shadow(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The **HTML ``<shadow>`` element**—an obsolete part of the `Web Components </en-
        US/docs/Web/Web_Components>`_ technology suite—was intended to be used as a
        shadow DOM `insertion point </en-US/docs/Glossary/insertion_point>`_. You might
        have used it if you have created multiple shadow roots under a shadow host. It
        is not useful in ordinary HTML.
    """


class slot(Component):
    """
        ** **This is an `experimental technology </en-US/docs/MDN/Contribute/Guidelines/
        Conventions_definitions#Experimental>`_**\\Check the `Browser compatibility
        table <#Browser_compatibility>`_ carefully before using this in production.
        
        The **HTML ``<slot>`` element**—part of the `Web Components </en-
        US/docs/Web/Web_Components>`_ technology suite—is a placeholder inside a web
        component that you can fill with your own markup, which lets you create separate
        DOM trees and present them together.
        
        Examples::
        
            element_details(
                span('slot', slot='element-name'),
                span(
                    'A placeholder inside a web component that users can fill with their own markup, with the effect of composing different DOM trees together.',
                    slot='description'),
                dl(dt('name'), dd('The name of the slot.'), slot='attributes'))
        
        ::
        
            element_details(
                span('template', slot='element-name'),
                span(
                    'A mechanism for holding client- side content that is not to be rendered when a page is loaded but may subsequently be instantiated during runtime using JavaScript.',
                    slot='description'))
    """


class template(Component):
    """
        The **HTML ``<template>`` element** is a mechanism for holding client-side
        content that is not to be rendered when a page is loaded but may subsequently be
        instantiated during runtime using JavaScript.
        
        Think of a template as a content fragment that is being stored for subsequent
        use in the document. While the parser does process the contents of the
        **``<template>`` **element while loading the page, it does so only to ensure
        that those contents are valid; the element's contents are not rendered, however.
        
        Examples::
        
            table(
                thead(tr(td('UPC_Code'), td('Product_Name'))),
                tbody('# existing data could optionally be included here'),
                id_='producttable')
        
        ::
        
            template(tr(td(class_='record'), td()), id_='productrow')
    """


# == Obsolete and deprecated elements ==

# **Warning:** These are old HTML elements which are deprecated and should not
# be used.**You should never use them in new projects, and should replace them
# in old projects as soon as you can.**They are listed here for informational
# purposes only.


class acronym(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


class applet(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The HTML Applet Element (``<applet>``) identifies the inclusion of a Java
        applet.
        
        **Note**: The ```<applet>`` </en-US/docs/Web/HTML/Element/applet>`_ element was
        removed in `Gecko 56 <https://bugzilla.mozilla.org/show_bug.cgi?id=1279218>`_
        and `Chrome in late 2015
        <https://bugs.chromium.org/p/chromium/issues/detail?id=470301>`_. Removal is
        being considered in `WebKit <https://bugs.webkit.org/show_bug.cgi?id=157926>`_
        and `Edge <https://developer.microsoft.com/en-us/microsoft-
        edge/platform/issues/11946645/>`_.
        
        Notes:
        
            The W3C specification does not encourage the use of ``<applet>`` and prefers the use of the ```<object>`` </en-US/docs/Web/HTML/Element/object>`_ tag. Under the strict definition of HTML 4.01, this element is deprecated and entirely obsolete in HTML5.
            
    """


class basefont(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Notes:
        
            * HTML 3.2 supports the basefont element but only with the size attribute.
            
            * The strict HTML and XHTML specifications do not support this element.
            
            * Despite being part of transitional standards, some standards-focused browsers like Mozilla and Opera do not support this element.
            
            * This element can be imitated with a CSS rule on the ```<body>`` </en-US/docs/Web/HTML/Element/body>`_ element.
            
            * XHTML 1.0 requires a trailing slash for this element: ``<basefont />``.
            
    """


class big(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


class blink(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.\\**** Obsolete**\\This
        feature is obsolete. Although it may still work in some browsers, its use is
        discouraged since it could be removed at any time. Try to avoid using it.
        
        The **HTML Blink Element** (``<blink>``) is a non-standard element causing the
        enclosed text to flash slowly.
        
        Do not use this element as it is **obsolete** and bad design practice. Blinking
        text is frowned upon by several accessibility standards and the CSS
        specification allows browsers to ignore the blink value.
    """


class center(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        Notes:
        
            Applying ```text-align`` </en-US/docs/Web/CSS/text-align>`_``:center`` to a```<div>`` </en-US/docs/Web/HTML/Element/div>`_ or ```<p>`` </en-US/docs/Web/HTML/Element/p>`_ element centers the *contents* of those elements while leaving their overall dimensions unchanged.
    """


class command(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        **Note:** The ``command`` element has been removed from Gecko 24.0 in favor of
        the ```<menuitem>`` </en-US/docs/Web/HTML/Element/menuitem>`_ element. Firefox
        has never supported this ``command`` element, and the existing implementation of
        the ```HTMLCommandElement`` </en-US/docs/Web/API/HTMLCommandElement>`_ DOM
        interface has been dropped from `Firefox 24 </en-
        US/docs/Site_Compatibility_for_Firefox_24>`_.
    """


# content: see above under 'Web Components'


class dir_(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """
    tag_name = 'dir'


# element: see above under 'Web Components'


class font(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


class frame(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        Examples::
        
            frameset(
                frame(src='https://developer.mozilla.org/en/HTML/Element/iframe'),
                frame(src='https://developer.mozilla.org/en/HTML/Element/frame'),
                cols='50%,50%')
    """


class frameset(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
    """


class image(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        **** Non-standard**\\This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.
        
        The HTML ``<image>`` element is an obsolete remnant of an ancient version of
        HTML lost in the mists of time; use the standard ```<img>`` </en-
        US/docs/Web/HTML/Element/img>`_ element instead. Seriously, the specification
        even literally uses the words "Don't ask" when describing this element.
        
        **Do not use this! ****In order to display images, use the standard ```<img>``
        </en-US/docs/Web/HTML/Element/img>`_ element.
        
        While browsers will attempt to automatically convert this into an ```<img>``
        </en-US/docs/Web/HTML/Element/img>`_ element, it won't always do so, and won't
        always succeed when it tries, due to the various ways this can happen. So just
        don't use it if you like your users.
    """


class isindex(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            head(isindex(prompt='Search Document... '))
    """


class keygen(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The HTML ``<keygen>`` element exists to facilitate generation of key material,
        and submission of the public key as part of an `HTML form </en-
        US/docs/Web/Guide/HTML/Forms>`_. This mechanism is designed for use with Web-
        based certificate management systems. It is expected that the ``<keygen>``
        element will be used in an HTML form along with other information needed to
        construct a certificate request, and that the result of the process will be a
        signed certificate.
        
        There is currently discussion among Web browser makers whether to keep this
        feature or not. Until a decision is reached, it is better to continue to
        consider this feature as deprecated and going away.
    """


class listing(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


class marquee(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The HTML ``<marquee>`` element is used to insert a scrolling area of text. You
        can control what happens when the text reaches the edges of its content area
        using its attributes.
        
        The ``<marquee>`` element is **obsolete** and must not be used. While some
        browsers still support it, it's not required.
        
        Examples::
        
            marquee('This text will scroll from right to left')
        
        ::
        
            marquee('This text will scroll from bottom to top', direction='up')
        
        ::
        
            marquee(
                marquee('This text will bounce', behavior='alternate'),
                direction='down',
                width='250',
                height='200',
                behavior='alternate',
                style='border:solid')
    """


class multicol(Component):
    """
        **** Non-standard**\\This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.\\**** Obsolete**\\This feature is
        obsolete. Although it may still work in some browsers, its use is discouraged
        since it could be removed at any time. Try to avoid using it.
    """


class nextid(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
    """


class noembed(Component):
    """
        **** Non-standard**\\This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.\\**** Deprecated**\\This feature has
        been removed from the Web standards. Though some browsers may still support it,
        it is in the process of being dropped. Avoid using it and update existing code
        if possible; see the `compatibility table <#Browser_compatibility>`_ at the
        bottom of this page to guide your decision. Be aware that this feature may cease
        to work at any time.
        
        The ``**<noembed>**`` element is a deprecated and non-standard way to provide
        alternative, or "fallback", content for browsers that do not support the
        ```<embed>`` </en-US/docs/Web/HTML/Element/embed>`_ element or do not support
        `embedded content </en-
        US/docs/Web/Guide/HTML/Content_categories#Embedded_content>`_ an author wishes
        to use. This element was deprecated in HTML 4.01 and above in favor
        of```<object>`` </en-US/docs/Web/HTML/Element/object>`_. Fallback content should
        be inserted between the opening and closing ```<object>```_ tags.
        
        While this element currently still works in many browsers, it has been
        deprecated and should not be used. Use ```<object>`` </en-
        US/docs/Web/HTML/Element/object>`_ instead.
    """


class plaintext(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


# shadow: see above under 'Web Components'


class spacer(Component):
    """
        **** Non-standard**\\This feature is non-standard and is not on a standards
        track. Do not use it on production sites facing the Web: it will not work for
        every user. There may also be large incompatibilities between implementations
        and the behavior may change in the future.\\**** Obsolete**\\This feature is
        obsolete. Although it may still work in some browsers, its use is discouraged
        since it could be removed at any time. Try to avoid using it.
        
        **``<spacer>``** is an obsolete HTML element which allowed insertion of empty
        spaces on pages. It was devised by Netscape to accomplish the same effect as a
        single-pixel layout image, which was something web designers used to use to add
        white spaces to web pages without actually using an image. However, ``<spacer>``
        no longer supported by any major browser and the same effects can now be
        achieved using simple CSS.
        
        Firefox, which is the descendant of Netscape's browsers, removed support for
        ``<spacer>`` in version 4.
    """


class strike(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


class tt(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Notes:
        
            * A CSS rule can be defined for the ``tt`` selector to override the browser's default font face. Preferences set by the user might take precedence over the specified CSS.
            
            * Although this element was not deprecated in the HTML 4.01 specification, its use is discouraged in favor of style sheets.
    """


class xmp(Component):
    """
        **** Obsolete**\\This feature is obsolete. Although it may still work in some
        browsers, its use is discouraged since it could be removed at any time. Try to
        avoid using it.
    """


__all__ = [
    'a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside',
    'audio', 'b', 'basefont', 'bdi', 'bdo', 'big', 'blink', 'blockquote',
    'body', 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code',
    'col', 'colgroup', 'command', 'content', 'data', 'datalist', 'dd', 'del_',
    'details', 'dfn', 'dialog', 'dir_', 'div', 'dl', 'dt', 'element', 'em',
    'embed', 'fieldset', 'figcaption', 'figure', 'font', 'footer', 'form',
    'frame', 'frameset', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header',
    'hgroup', 'hr', 'html', 'i', 'image', 'img', 'input_', 'ins', 'isindex',
    'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'listing', 'main',
    'map_', 'mark', 'marquee', 'menu', 'menuitem', 'meta', 'meter', 'multicol',
    'nav', 'nextid', 'noembed', 'noscript', 'object_', 'ol', 'optgroup',
    'option', 'output', 'p', 'param', 'plaintext', 'pre', 'progress', 'q',
    'rp', 'rt', 'rtc', 'ruby', 's', 'samp', 'script', 'section', 'select',
    'shadow', 'slot', 'small', 'source', 'spacer', 'span', 'strike', 'strong',
    'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template',
    'textarea', 'tfoot', 'th', 'thead', 'time', 'tr', 'track', 'tt', 'u', 'ul',
    'var', 'video', 'wbr', 'xmp'
]

