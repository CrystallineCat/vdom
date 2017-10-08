# -*- coding: utf-8 -*-

from .core import createComponent

# From http://developer.mozilla.org/en-US/docs/Web/HTML/Element

# == Main Root ==
# 

html = createComponent(
    'html',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/html',
    docs="""
        The **HTML`<html>` element** represents the root (top-level element) of an
        HTML document, so it is also referred to as the _root element_. All other
        elements must be descendants of this element.
    """,
    examples=[
        '<!DOCTYPE html>\n<html>\n  <head>...</head>\n  <body>...</body>\n</html>',
    ], )


# == Document Metadata ==
# Metadata contains information about the page. This includes information about
# styles, scripts and data to help software (search engines, browsers, etc.) use
# and render the page. Metadata for styles and scripts may be defined in the
# page or link to another file that has the information.

link = createComponent(
    'link',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/link',
    docs="""
        The **HTML`<link>` element** specifies relationships between the current
        document and an external resource. Possible uses for this element include
        defining a relational framework for navigation. This element is most used to
        link to style sheets.
    """,
    notes="""
          * A `<link>` tag can occur either in the head element or in the body element (or both), depending on whether it has a link type that is **body-ok**. For example, the `stylesheet` link type is body-ok, and therefore a `<link rel="stylesheet">` is permitted in the body.
          * HTML 3.2 defines only the **href** , **rel** , **rev** , and **title** attributes for the link element.
          * HTML 2 defines the **href** , **methods** , **rel** , **rev** , **title** , and **urn** attributes for the `<link>` element. The **methods** and **urn** attributes were later removed from the specifications.
          * The HTML and XHTML specifications define event handlers for the `<link>` element, but it is unclear how they would be used.
          * Under XHTML 1.0, empty elements such as `<link>` require a trailing slash: `<link />`.
    """,
    examples=[
        '<link href="style.css" rel="stylesheet">',
        '<link href="default.css" rel="stylesheet" title="Default Style">\n<link href="fancy.css" rel="alternate stylesheet" title="Fancy">\n<link href="basic.css" rel="alternate stylesheet" title="Basic">',
        '<script>\nfunction sheetLoaded() {\n  // Do something interesting; the sheet has been loaded\n}\n\nfunction sheetError() {\n  console.log("An error occurred loading the stylesheet!");\n}\n</script>\n\n<link rel="stylesheet" href="mystylesheet.css" onload="sheetLoaded()"\n  onerror="sheetError()">',
    ], )


meta = createComponent(
    'meta',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta',
    docs="""
        The **HTML`<meta>` element** represents metadata that cannot be represented by
        other HTML meta-related elements, like `<base>`, `<link>`, `<script>`,
        `<style>` or `<title>`.
    """,
    notes="""
        Depending on the attributes set, the kind of metadata can be one of the
        following:
        
          * If `name` is set, it is _document-level_ _metadata_ , applying to the whole page.
          * If `http-equiv` is set, it is a _pragma directive_ -- information normally given by the web server about how the web page is served.
          * If `charset` is set, it is a _charset declaration_ -- the character encoding used by the webpage.
          * If `itemprop` is set, it is _user-defined metadata_ -- transparent for the user-agent as the semantics of the metadata is user-specific. __
    """,
    examples=[
        '<meta charset="utf-8">\n\n<!-- Redirect page after 3 seconds -->\n<meta http-equiv="refresh" content="3;url=https://www.mozilla.org">',
    ], )


style = createComponent(
    'style',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/style',
    docs="""
        The **HTML`<style>` element** contains style information for a document, or
        part of a document. By default, the style instructions written inside that
        element are expected to be CSS.
    """, )


# == Sectioning Root ==
# 

body = createComponent(
    'body',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/body',
    docs="""
        The **HTML`<body>` Element** represents the content of an HTML document. There
        can be only one `<body>` element in a document.
    """,
    examples=[
        '<html>\n  <head>\n    <title>Document title</title>\n  </head>\n  <body>\n    <p>This is a paragraph</p>\n  </body>\n</html>',
    ], )


# == Content Sectioning ==
# Content sectioning elements allow you to organize the document content into
# logical pieces. Use the sectioning elements to create a broad outline for your
# page content, including header and footer navigation, and heading elements to
# identify sections of content.

address = createComponent(
    'address',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/address',
    docs="""
        The **HTML `<address>` element** supplies contact information for its nearest
        `<article>` or `<body>` ancestor; in the latter case, it applies to the whole
        document.
    """,
    examples=[
        '<address>\n    You can contact author at <a href="http://www.somedomain.com/contact">www.somedomain.com</a>.<br>\n    If you see any bugs, please <a href="mailto:webmaster@somedomain.com">contact webmaster</a>.<br>\n    You may also want to visit us:<br>\n    Mozilla Foundation<br>\n    1981 Landings Drive<br>\n    Building K<br>\n    Mountain View, CA 94043-0801<br>\n    USA\n  </address>',
    ], )


article = createComponent(
    'article',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/article',
    docs="""
        The **HTML`<article>` element** represents a self-contained composition in a
        document, page, application, or site, which is intended to be independently
        distributable or reusable (e.g., in syndication). Examples include: a forum
        post, a magazine or newspaper article, or a blog entry.
    """,
    examples=[
        '<article class="film_review">\n\xa0 <header>\n\xa0 \xa0 <h2>Jurassic Park</h2>\n\xa0 </header>\n\xa0 <section class="main_review">\n\xa0 \xa0 <p>Dinos were great!</p>\n\xa0 </section>\n\xa0 <section class="user_reviews">\n\xa0 \xa0 <article class="user_review">\n\xa0 \xa0 \xa0 <p>Way too scary for me.</p>\n\xa0 \xa0 \xa0 <footer>\n\xa0 \xa0 \xa0 \xa0 <p>\n\xa0 \xa0 \xa0 \xa0 \xa0 Posted on\n          <time datetime="2015-05-16 19:00">May 16</time>\n          by Lisa.\n\xa0 \xa0 \xa0 \xa0 </p>\n\xa0 \xa0 \xa0 </footer>\n\xa0 \xa0 </article>\n\xa0 \xa0 <article class="user_review">\n\xa0 \xa0 \xa0 <p>I agree, dinos are my favorite.</p>\n\xa0 \xa0 \xa0 <footer>\n\xa0 \xa0 \xa0 \xa0 <p>\n\xa0 \xa0 \xa0 \xa0 \xa0 Posted on\n          <time datetime="2015-05-17 19:00">May 17</time>\n          by Tom.\n\xa0 \xa0 \xa0 \xa0 </p>\n\xa0 \xa0 \xa0 </footer>\n\xa0 \xa0 </article>\n\xa0 </section>\n\xa0 <footer>\n\xa0 \xa0 <p>\n\xa0 \xa0 \xa0 Posted on\n      <time datetime="2015-05-15 19:00">May 15</time>\n      by Staff.\n\xa0 \xa0 </p>\n\xa0 </footer>\n</article>',
    ], )


aside = createComponent(
    'aside',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside',
    docs="""
        The **HTML`<aside>` element** represents a section of a document with content
        connected tangentially to the main content of the document (often presented as
        a sidebar).
    """,
    examples=[
        '<article>\n  <p>\n    The Disney movie <cite>The Little Mermaid</cite> was\n    first released to theatres in 1989.\n  </p>\n  <aside>\n    <p>\n      The movie earned $87 million during its initial release.\n    </p>\n  </aside>\n  <p>\n    More info about the movie...\n  </p>\n</article>',
    ], )


footer = createComponent(
    'footer',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer',
    docs="""
        The **HTML`<footer>` element** represents a footer for its nearest sectioning
        content or sectioning root element. A footer typically contains information
        about the author of the section, copyright data or links to related documents.
    """,
    examples=[
        '<footer>\n  Some copyright info or perhaps some author\n  info for an &lt;article&gt;?\n</footer>',
    ], )


h1 = createComponent(
    'h1',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1–h6',
    docs="""
        The **HTML`<h1>`-`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
    examples=[
        '<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
        '<h1>Heading elements</h1>\n<h2>Summary</h2>\n<p>Some text here...</p>\n\n<h2>Examples</h2>\n<h3>Example 1</h3>\n<p>Some text here...</p>\n\n<h3>Example 2</h3>\n<p>Some text here...</p>\n\n<h2>See also</h2>\n<p>Some text here...</p>',
    ], )


h2 = createComponent(
    'h2',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1–h6',
    docs="""
        The **HTML`<h1>`-`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
    examples=[
        '<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
        '<h1>Heading elements</h1>\n<h2>Summary</h2>\n<p>Some text here...</p>\n\n<h2>Examples</h2>\n<h3>Example 1</h3>\n<p>Some text here...</p>\n\n<h3>Example 2</h3>\n<p>Some text here...</p>\n\n<h2>See also</h2>\n<p>Some text here...</p>',
    ], )


h3 = createComponent(
    'h3',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1–h6',
    docs="""
        The **HTML`<h1>`-`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
    examples=[
        '<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
        '<h1>Heading elements</h1>\n<h2>Summary</h2>\n<p>Some text here...</p>\n\n<h2>Examples</h2>\n<h3>Example 1</h3>\n<p>Some text here...</p>\n\n<h3>Example 2</h3>\n<p>Some text here...</p>\n\n<h2>See also</h2>\n<p>Some text here...</p>',
    ], )


h4 = createComponent(
    'h4',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1–h6',
    docs="""
        The **HTML`<h1>`-`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
    examples=[
        '<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
        '<h1>Heading elements</h1>\n<h2>Summary</h2>\n<p>Some text here...</p>\n\n<h2>Examples</h2>\n<h3>Example 1</h3>\n<p>Some text here...</p>\n\n<h3>Example 2</h3>\n<p>Some text here...</p>\n\n<h2>See also</h2>\n<p>Some text here...</p>',
    ], )


h5 = createComponent(
    'h5',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1–h6',
    docs="""
        The **HTML`<h1>`-`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
    examples=[
        '<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
        '<h1>Heading elements</h1>\n<h2>Summary</h2>\n<p>Some text here...</p>\n\n<h2>Examples</h2>\n<h3>Example 1</h3>\n<p>Some text here...</p>\n\n<h3>Example 2</h3>\n<p>Some text here...</p>\n\n<h2>See also</h2>\n<p>Some text here...</p>',
    ], )


h6 = createComponent(
    'h6',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1–h6',
    docs="""
        The **HTML`<h1>`-`<h6>` elements** represent six levels of section headings.
        `<h1>` is the highest section level and `<h6>` is the lowest.
    """,
    examples=[
        '<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
        '<h1>Heading elements</h1>\n<h2>Summary</h2>\n<p>Some text here...</p>\n\n<h2>Examples</h2>\n<h3>Example 1</h3>\n<p>Some text here...</p>\n\n<h3>Example 2</h3>\n<p>Some text here...</p>\n\n<h2>See also</h2>\n<p>Some text here...</p>',
    ], )


header = createComponent(
    'header',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/header',
    docs="""
        The **HTML`<header>` element** represents introductory content, typically a
        group of introductory or navigational aids. It may contain some heading
        elements but also other elements like a logo, a search form, an author name,
        and so on.
    """,
    examples=[
        '<header>\n\xa0 <h1>Main Page Title</h1>\n\xa0 <img src="mdn-logo-sm.png" alt="MDN logo">\n</header>',
    ], )


hgroup = createComponent(
    'hgroup',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup',
    docs="""
        __ **This is an experimental technology**  
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the syntax
        and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **HTML`<hgroup>` element** represents a multi-level heading for a section
        of a document. It groups a set of `<h1>-<h6>` elements.
    """,
    examples=[
        '<hgroup id="document-title">\n  <h1>HTML</h1>\n  <h2>Living Standard — Last Updated 12 August 2016</h2>\n</hgroup>',
    ], )


nav = createComponent(
    'nav',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav',
    docs="""
        The **HTML`<nav>` element** represents a section of a page whose purpose is to
        provide navigation links, either within the current document or to other
        documents. Common examples of navigation sections are menus, tables of
        contents, and indexes.
    """,
    examples=[
        '<nav class="menu">\n  <ul>\n    <li><a href="#">Home</a></li>\n    <li><a href="#">About</a></li>\n    <li><a href="#">Contact</a></li>\n  </ul>\n</nav>',
    ], )


section = createComponent(
    'section',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/section',
    docs="""
        The **HTML`<section>` element** represents a standalone section of
        functionality contained within an HTML document, typically with a heading,
        which doesn't have a more specific semantic element to represent it.
        
        As an example, a navigation menu should be wrapped in a `<nav>` element, but a
        list of search results and a map display and its controls don't have specific
        elements, and could be put inside a `<section>`.
    """, )


# == Text Content ==
# Use HTML text content elements to organize blocks or sections of content
# placed between the opening `<body>` and closing `</body>` tags. Important for
# accessibility and SEO, these elements identify the purpose or structure of
# that content.

blockquote = createComponent(
    'blockquote',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote',
    docs="""
        The **HTML`<blockquote>` Element** (or _HTML Block Quotation Element_ )
        indicates that the enclosed text is an extended quotation. Usually, this is
        rendered visually by indentation (see Notes for how to change it). A URL for
        the source of the quotation may be given using the **cite** attribute, while a
        text representation of the source can be given using the `<cite>` element.
    """,
    notes="""
        To change `<blockquote>` indent, use CSS `margin` property.
        
        For short quotes use the `<q>` element.
    """,
    examples=[
        '<blockquote cite="http://developer.mozilla.org">\n  <p>This is a quotation taken from\n  the Mozilla Developer Center.</p>\n</blockquote>',
    ], )


dd = createComponent(
    'dd',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd',
    docs="""
        The **HTML`<dd>` element** indicates the description of a term in a
        description list (`<dl>`).
    """, )


div = createComponent(
    'div',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/div',
    docs="""
        The **HTML`<div>` element** is the generic container for flow content and does
        not inherently represent anything. Use it to group elements for purposes such
        as styling (using the `class` or `id` attributes), marking a section of a
        document in a different language (using the `lang` attribute), and so on.
    """,
    examples=[
        '<div>\n  <p>Any kind of content here. Such as\n  &lt;p&gt;, &lt;table&gt;. You name it!</p>\n</div>',
    ], )


dl = createComponent(
    'dl',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl',
    docs="""
        The **HTML`<dl>` ** element represents a description list. **** The element
        encloses a list of groups of terms and descriptions. Common uses for this
        element are to implement a glossary or to display metadata (a list of key-
        value pairs).
    """,
    notes="""
        Do not use this element (nor `<ul>` elements) to merely create indentation on
        a page. Although it works, this is a bad practice and obscures the meaning of
        description lists.
        
        To change the indentation of a description term, use the CSS `margin`
        property.
    """,
    examples=[
        '<dl>\n  <dt>Firefox</dt>\n  <dd>\n    A free, open source, cross-platform,\n    graphical web browser developed by the\n    Mozilla Corporation and hundreds of\n    volunteers.\n  </dd>\n\n  <!-- Other terms and descriptions -->\n</dl>',
        '<dl>\n  <dt>Firefox</dt>\n  <dt>Mozilla Firefox</dt>\n  <dt>Fx</dt>\n  <dd>\n    A free, open source, cross-platform,\n    graphical web browser developed by the\n    Mozilla Corporation and hundreds of\n    volunteers.\n  </dd>\n\n  <!-- Other terms and descriptions -->\n</dl>',
        '<dl>\n  <dt>Firefox</dt>\n  <dd>\n    A free, open source, cross-platform,\n    graphical web browser developed by the\n    Mozilla Corporation and hundreds of\n    volunteers.\n  </dd>\n  <dd>\n    The Red Panda also known as the Lesser\n    Panda, Wah, Bear Cat or Firefox, is a\n    mostly herbivorous mammal, slightly larger\n    than a domestic cat (60 cm long).\n  </dd>\n\n  <!-- Other terms and descriptions -->\n</dl>',
        '<dl>\n  <dt>Name</dt>    \n  <dd>Godzilla</dd>\n  <dt>Born</dt>\n  <dd>1952</dd>\n  <dt>Birthplace</dt>\n  <dd>Japan</dd>\n  <dt>Color</dt>\n  <dd>Green</dd>\n</dl>',
        '<dl>\n  <div>\n    <dt>Name</dt>\n    <dd>Godzilla</dd>\n  </div>\n  <div>\n    <dt>Born</dt>\n    <dd>1952</dd>\n  </div>\n  <div>\n    <dt>Birthplace</dt>\n    <dd>Japan</dd>\n  </div>\n  <div>\n    <dt>Color</dt>\n    <dd>Green</dd>\n  </div>\n</dl>',
    ], )


dt = createComponent(
    'dt',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt',
    docs="""
        The **HTML`<dt>` element** identifies a term in a description list. This
        element can occur only as a child element of a `<dl>`. It is usually followed
        by a `<dd>` element; however, multiple `<dt>` elements in a row indicate
        several terms that are all defined by the immediate next `<dd>` element.
    """, )


figcaption = createComponent(
    'figcaption',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption',
    docs="""
        The **HTML`<figcaption>` element** represents a caption or a legend associated
        with a figure or an illustration described by the rest of the data of the
        `<figure>` element which is its immediate ancestor.
    """, )


figure = createComponent(
    'figure',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure',
    docs="""
        The **HTML`<figure>` element** represents self-contained content, frequently
        with a caption (`<figcaption>`), and is typically referenced as a single unit.
    """,
    examples=[
        '<!-- Just a figure -->\n<figure>\n  <img\n  src="https://developer.cdn.mozilla.net/media/img/mdn-logo-sm.png"\n  alt="An awesome picture">\n</figure>\n<p></p>\n<!-- Figure with figcaption -->\n<figure>\n  <img\n  src="https://developer.cdn.mozilla.net/media/img/mdn-logo-sm.png"\n  alt="An awesome picture">\t\n  <figcaption>Fig1. MDN Logo</figcaption>\n</figure>\n<p></p>',
        '<figure>\n  <figcaption>Get browser details\nusing navigator</figcaption>\n  <pre>\nfunction NavigatorExample() {\n  var txt;\n  txt = "Browser CodeName: " + navigator.appCodeName;\n  txt+= "Browser Name: " + navigator.appName;\n  txt+= "Browser Version: " + navigator.appVersion ;\n  txt+= "Cookies Enabled: " + navigator.cookieEnabled;\n  txt+= "Platform: " + navigator.platform;\n  txt+= "User-agent header: " + navigator.userAgent;\n}            \n  </pre>\n</figure>',
        '<figure>\n  <figcaption><cite>Edsger Dijkstra :-</cite></figcaption>\n  <p>"If debugging is the process of removing software bugs,\n  <br />\n  then programming must be the process of putting them in"</p>\n</figure>',
        '<figure>\n <p>\n  Depression is running through my head,<br>\n  These thoughts make me think of death,<br>\n  A darkness which blanks my mind,<br>\n  A walk through the graveyard, what can I find?....\n </p>\n <figcaption><cite>Depression</cite>.\n  By: Darren Harris</figcaption>\n</figure>',
    ], )


hr = createComponent(
    'hr',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr',
    docs="""
        The **HTML`<hr>` element** represents a thematic break between paragraph-level
        elements (for example, a change of scene in a story, or a shift of topic with
        a section). In previous versions of HTML, it represented a horizontal rule. It
        may still be displayed as a horizontal rule in visual browsers, but is now
        defined in semantic terms, rather than presentational terms.
    """,
    examples=[
        '<p>\n  This is the first paragraph of text.\n  This is the first paragraph of text.\n  This is the first paragraph of text.\n  This is the first paragraph of text.\n</p>\n\n<hr>\n\n<p>\n  This is the second paragraph of text.\n  This is the second paragraph of text.\n  This is the second paragraph of text.\n  This is the second paragraph of text.\n</p>',
    ], )


li = createComponent(
    'li',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/li',
    docs="""
        The **HTML`<li>` element** is used to represent an item in a list. It must be
        contained in a parent element: an ordered list (`<ol>`), an unordered list
        (`<ul>`), or a menu (`<menu>`). In menus and unordered lists, list items are
        usually displayed using bullet points. In ordered lists, they are usually
        displayed with an ascending counter on the left, such as a number or letter.
    """,
    examples=[
        '<ol>\n    <li>first item</li>\n    <li>second item</li>\n    <li>third item</li>\n</ol>',
        '<ol type="I">\n    <li value="3">third item</li>\n    <li>fourth item</li>\n    <li>fifth item</li>\n</ol>',
        '<ul>\n    <li>first item</li>\n    <li>second item</li>\n    <li>third item</li>\n</ul>',
    ], )


main = createComponent(
    'main',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/main',
    docs="""
        The **HTML`<main>` element** represents the main content of the `<body>` of a
        document, portion of a document, or application. The main content area
        consists of content that is directly related to, or expands upon the central
        topic of, a document or the central functionality of an application.
        
        You can use multiple `<main>` elements within the same page when it makes
        sense to do so. For instance, if you have a page presenting multiple articles
        (each inside an `<article>` element, each of which has some extra material
        within (such as toolbars for editing, ads, and so forth), it may make sense to
        include a `<main>` element within each article to identify the primary
        contents of that specific article.
    """,
    examples=[
        '<!-- other content -->\n\n<main>\n  <h1>Apples</h1>\n  <p>The apple is the pomaceous fruit of the apple tree.</p>\n  \n  <article>\n    <h2>Red Delicious</h2>\n    <p>These bright red apples are the most common found in many\n    supermarkets.</p>\n    <p>... </p>\n    <p>... </p>\n  </article>\n\n  <article>\n    <h2>Granny Smith</h2>\n    <p>These juicy, green apples make a great filling for\n    apple pies.</p>\n    <p>... </p>\n    <p>... </p>\n  </article>\n</main>\n\n<!-- other content -->',
    ], )


ol = createComponent(
    'ol',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol',
    docs="""
        The **HTML`<ol>` element** represents an ordered list of items, typically
        rendered as a numbered list.
    """,
    examples=[
        '<ol>\n  <li>first item</li>\n  <li>second item</li>\n  <li>third item</li>\n</ol>',
        '<ol start="7">\n  <li>first item</li>\n  <li>second item</li>\n  <li>third item</li>\n</ol>',
        "<ol>\n  <li>first item</li>\n  <li>second item  <!-- closing </li> tag not here! -->\n    <ol>\n      <li>second item first subitem</li>\n      <li>second item second subitem</li>\n      <li>second item third subitem</li>\n    </ol>\n  </li>            <!-- Here's the closing </li> tag -->\n  <li>third item</li>\n</ol>",
        "<ol>\n  <li>first item</li>\n  <li>second item  <!-- closing </li> tag not here! -->\n    <ul>\n      <li>second item first subitem</li>\n      <li>second item second subitem</li>\n      <li>second item third subitem</li>\n    </ul>\n  </li>            <!-- Here's the closing </li> tag -->\n  <li>third item</li>\n</ol>",
    ], )


p = createComponent(
    'p',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/p',
    docs="""
        The **HTML`<p>` element** represents a paragraph of text. Paragraphs are
        usually represented in visual media as blocks of text that are separated from
        adjacent blocks by vertical blank space and/or first-line indentation.
        Paragraphs are block-level elements.
    """,
    examples=[
        '<p>This is the first paragraph of text.\n  This is the first paragraph of text.\n  This is the first paragraph of text.\n  This is the first paragraph of text.</p>\n<p>This is the second paragraph.\n This is the second paragraph.\n This is the second paragraph.\n This is the second paragraph.</p>',
    ], )


pre = createComponent(
    'pre',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre',
    docs="""
        The **HTML`<pre>` element** represents preformatted text. Text within this
        element is typically displayed in a non-proportional ("monospace") font
        exactly as it is laid out in the file. Whitespace inside this element is
        displayed as typed.
    """,
    examples=[
        '<!-- Some example CSS code -->\n<pre>\nbody {\n  color:red;\n}\n</pre>',
    ], )


ul = createComponent(
    'ul',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul',
    docs="""
        The **HTML`<ul>` element** represents an unordered list of items, typically
        rendered as a bulleted list.
    """,
    examples=[
        '<ul>\n  <li>first item</li>\n  <li>second item</li>\n  <li>third item</li>\n</ul>',
        '<ul>\n  <li>first item</li>\n  <li>second item     \n  <!-- Look, the closing </li> tag is not placed here! -->\n    <ul>\n      <li>second item first subitem</li>\n      <li>second item second subitem\n      <!-- Same for the second nested unordered list! -->\n        <ul>\n          <li>second item second subitem first sub-subitem</li>\n          <li>second item second subitem second sub-subitem</li>\n          <li>second item second subitem third sub-subitem</li>\n        </ul>\n      </li> <!-- Closing </li> tag for the li that\n                  contains the third unordered list -->\n      <li>second item third subitem</li>\n    </ul>\n  <!-- Here is the closing </li> tag -->\n  </li>\n  <li>third item</li>\n</ul>',
        '<ul>\n  <li>first item</li>\n  <li>second item\n  <!-- Look, the closing </li> tag is not placed here! -->\n    <ol>\n      <li>second item first subitem</li>\n      <li>second item second subitem</li>\n      <li>second item third subitem</li>\n    </ol>\n  <!-- Here is the closing </li> tag -->\n  </li>\n  <li>third item</li>\n</ul>',
    ], )


# == Inline Text Semantics ==
# Use the HTML inline text semantic to define the meaning, structure, or style
# of a word, line, or any arbitrary piece of text.

a = createComponent(
    'a',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/a',
    docs="""
        The **HTML`<a>` element** (or _anchor_ element) creates a hyperlink to other
        web pages, files, locations within the same page, email addresses, or any
        other URL.
    """,
    notes="""
        HTML 3.2 defines only the `name`, `href`, `rel`, `rev`, and `title`
        attributes.
        
        ### Accessibility recommendations
        
        Anchor tags are often abused with the `onclick` event to create pseudo-buttons
        by setting **href** to `"#"` or `"javascript:void(0)"` to prevent the page
        from refreshing. These values cause unexpected behavior when copying/dragging
        links, opening links in a new tabs/windows, bookmarking, and when JavaScript
        is still downloading, errors out, or is disabled. This also conveys incorrect
        semantics to assistive technologies (e.g., screen readers). In these cases, it
        is recommended to use a `<button>` instead. In general you should only use an
        anchor for navigation using a proper URL.
        
        ### Clicking and focus
        
        Whether clicking on an `<a>` causes it to become focused varies by browser and
        OS.
        
        Does clicking on an `<a>` give it focus? Desktop Browsers | Windows 8.1 | OS X
        10.9  
        ---|---|---  
        Firefox 30.0 | Yes | Yes  
        Chrome ≥39  
        (Chromium bug 388666) | Yes | Yes  
        Safari 7.0.5 | N/A | Only when it has a `tabindex`  
        Internet Explorer 11 | Yes | N/A  
        Presto (Opera 12) | Yes | Yes  
        Does tapping on an `<a>` give it focus? Mobile Browsers | iOS 7.1.2 | Android
        4.4.4  
        ---|---|---  
        Safari Mobile | Only when it has a `tabindex` | N/A  
        Chrome 35 | ??? | Only when it has a `tabindex`
    """,
    examples=[
        '<!-- anchor linking to external file -->\n<a href="https://www.mozilla.com/">\nExternal Link\n</a>',
        '<!-- links to element on this page with id="attr-href" -->\n<a href="#attr-href">\nDescription of Same-Page Links\n</a>',
        '<a href="https://developer.mozilla.org/en-US/" target="_blank">\n  <img src="https://mdn.mozillademos.org/files/6851/mdn_logo.png"\n       alt="MDN logo" />\n</a>',
        '<a href="mailto:nowhere@mozilla.org">Send email to nowhere</a>',
        '<a href="tel:+491570156">+49 157 0156</a>',
    ], )


abbr = createComponent(
    'abbr',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr',
    docs="""
        The **HTML`<abbr>` element** represents an abbreviation and optionally
        provides a full description for it. If present, the `title` attribute must
        contain this full description and nothing else.
    """,
    examples=[
        '<abbr title="Internationalization">I18N</abbr>',
    ], )


b = createComponent(
    'b',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/b',
    docs="""
        The **HTML`<b>` element** represents a span of text stylistically different
        from normal text, without conveying any special importance or relevance, and
        that is typically rendered in boldface.
    """,
    examples=[
        '<p>\n  This article describes several <b class="keywords">text-level</b> elements.\n  It explains their usage in an <b class="keywords">HTML</b> document.   \n</p>\nKeywords are displayed with the default style of the <b>\nelement, likely in bold.',
    ], )


bdi = createComponent(
    'bdi',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi',
    docs="""
        The **HTML`<bdi>` element** ( _bidirectional isolation_ ) isolates a span of
        text that might be formatted in a different direction from other text outside
        it.
        
        This element is useful when embedding text with an unknown directionality,
        from a database for example, inside text with a fixed directionality.
    """,
    examples=[
        '<p dir="ltr">This arabic word <bdi>ARABIC_PLACEHOLDER</bdi>\nis automatically displayed right-to-left.</p>',
    ], )


bdo = createComponent(
    'bdo',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo',
    docs="""
        The **HTML`<bdo>` element** ( _bidirectional override_ ) is used to override
        the current directionality of text. It causes the directionality of the
        characters to be ignored in favor of the specified directionality.
    """,
    notes="""
        The HTML 4 specification did not specify events for this element; they were
        added in XHTML. This is most likely an oversight.
    """,
    examples=[
        '<!-- Switch text direction -->\n<p>This text will go left to right.</p>\n<p><bdo dir="rtl">This text will go right\nto left.</bdo></p>',
    ], )


br = createComponent(
    'br',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/br',
    docs="""
        The **HTML`<br>` element** produces a line break in text (carriage-return). It
        is useful for writing a poem or an address, where the division of lines is
        significant.
    """,
    notes="""
        Do not use `<br>` to increase the gap between lines of text; use the CSS
        `margin` property or the `<p>` element.
    """,
    examples=[
        'Mozilla Foundation<br>\n1981 Landings Drive<br>\nBuilding K<br>\nMountain View, CA 94043-0801<br>\nUSA',
    ], )


cite = createComponent(
    'cite',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite',
    docs="""
        The **HTML <cite> element** represents a reference to a creative work. It must
        include the title of a work or a URL reference, which may be in an abbreviated
        form according to the conventions used for the addition of citation metadata.
    """,
    examples=[
        'More information can be found in <cite>[ISO-0000]</cite>.',
    ], )


code = createComponent(
    'code',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/code',
    docs="""
        The **HTML`<code>` element** represents a fragment of computer code. By
        default, it is displayed in the browser's default monospace font.
    """,
    examples=[
        '<p>This is how we declare a Javascript variable:<br/>\n<code>var i = 0;</code>\n</p>',
    ], )


data = createComponent(
    'data',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/data',
    docs="""
        The **HTML`<data>` element** links a given content with a machine-readable
        translation. If the content is time- or date-related, the `<time>` element
        must be used.
    """,
    examples=[
        '<p>New Products</p>\n<ul>\n <li><data value="398">Mini Ketchup</data></li>\n <li><data value="399">Jumbo Ketchup</data></li>\n <li><data value="400">Mega Jumbo Ketchup</data></li>\n</ul>',
    ], )


dfn = createComponent(
    'dfn',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn',
    docs="""
        The **HTML <dfn> element** represents the defining instance of a term.
    """,
    examples=[
        '<!-- Define "The Internet" -->\n<p><dfn id="def-internet">The Internet</dfn> is a global\nsystem of interconnected networks that use the Internet\nProtocol Suite (TCP/IP) to serve billions of users\nworldwide.</p>',
        '<dl>\n  <!-- Define "World-Wide Web" and reference\n       definition for "the Internet" -->\n  <dt>\n    <dfn>\n      <abbr title="World-Wide Web">WWW</abbr>\n    </dfn>\n  </dt>\n  <dd>The World-Wide Web (WWW) is a system of\n  interlinked hypertext documents accessed on\n  <a href="#def-internet">the Internet</a>.</dd>\n</dl>',
    ], )


em = createComponent(
    'em',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/em',
    docs="""
        The **HTML`<em>` element** marks text that has stress emphasis. The `<em>`
        element can be nested, with each level of nesting indicating a greater degree
        of emphasis.
    """,
    examples=[
        '<p>\n  In HTML 5, what was previously called\n  <em>block-level</em> content is now called\n  <em>flow</em> content.\n</p>',
    ], )


i = createComponent(
    'i',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/i',
    docs="""
        The **HTML`<i>` element** represents a range of text that is set off from the
        normal text for some reason, for example, technical terms, foreign language
        phrases, or fictional character thoughts. It is typically displayed in italic
        type.
    """,
    notes="""
        In earlier versions of the HTML specification, the `<i>` tag was merely a
        presentational element used to display text in italics, much like the `<b>`
        tag was used to display text in bold letters. This is no longer true, as these
        tags now define semantics rather than typographic appearance. The `<i>` tag
        should represent a range of text with a different semantic meaning whose
        typical typographic representation is italicized. This means a browser will
        typically still display its contents in italic type, but is, by definition, no
        longer required to.
        
        Use this element only when there is not a more appropriate semantic element.
        For example:
        
          * Use `<em>` to indicate emphasis or stress.
          * Use `<strong>` to indicate importance.
          * Use `<mark>` to indicate relevance.
          * Use `<cite>` to mark the name of a work, such as a book, play, or song.
          * Use `<dfn>` to mark the defining instance of a term.
        
        It is a good idea to use the **class** attribute to identify why the element
        is being used, so that if the presentation needs to change at a later date, it
        can be done selectively with style sheets.
    """,
    examples=[
        '<p>The Latin phrase <i class="latin">Veni, vidi, vici</i> is often\nmentioned in music, art, and literature.</p>',
    ], )


kbd = createComponent(
    'kbd',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd',
    docs="""
        The **HTML`<kbd>` element** represents user input and produces an inline
        element displayed in the browser's default monospace font.
    """,
    examples=[
        '<p>Type the following in the Run dialog:\n  <kbd>cmd</kbd><br />Then click the OK button.</p>\n\n<p>Save the document by pressing\n  <kbd>Ctrl</kbd> + <kbd>S</kbd></p>',
    ], )


mark = createComponent(
    'mark',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark',
    docs="""
        The **HTML`<mark>` element** represents highlighted text, i.e., a run of text
        marked for reference purpose, due to its _relevance_ in a particular context.
        For example it can be used in a page showing search results to highlight every
        instance of the searched-for word.
    """,
    examples=[
        '<p>The &lt;mark&gt; element is used to\n  <mark>highlight</mark> text</p>',
    ], )


q = createComponent(
    'q',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/q',
    docs="""
        The **HTML`<q>` element ** indicates that the enclosed text is a short inline
        quotation. This element is intended for short quotations that don't require
        paragraph breaks; for long quotations use the `<blockquote>` element.
    """,
    examples=[
        '<p>According to Mozilla\'s website,\n\xa0 <q\n  cite="https://www.mozilla.org/en-US/about/history/details/">Firefox 1.0\n  was released in 2004 and became a big success.</q></p>',
    ], )


rp = createComponent(
    'rp',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp',
    docs="""
        The **HTML`<rp>` element** is used to provide fall-back parentheses for
        browsers that do not support display of ruby annotations using the `<ruby>`
        element.
    """,
    examples=[
        '<ruby>\n  漢 <rp>(</rp><rt>Kan</rt><rp>)</rp>\n  字 <rp>(</rp><rt>ji</rt><rp>)</rp>\n</ruby>',
    ], )


rt = createComponent(
    'rt',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt',
    docs="""
        The **HTML`<rt>` element** embraces pronunciation of characters presented in a
        ruby annotations, which are used to describe the pronunciation of East Asian
        characters. This element is always used inside a `<ruby>` element.
    """,
    examples=[
        '<ruby>\n  漢 <rt>Kan</rt>\n  字 <rt>ji</rt>\n</ruby>',
    ], )


rtc = createComponent(
    'rtc',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/rtc',
    docs="""
        The **HTML`<rtc>` element** embraces semantic annotations of characters
        presented in a ruby of `<rb>` elements used inside of `<ruby>` element. `<rb>`
        elements can have both pronunciation (`<rt>`) and semantic (`<rtc>`)
        annotations.
    """,
    examples=[
        '<ruby>\n   <rb>旧</rb>\n   <rb>金</rb>\n   <rb>山</rb>\n   <rt>jiù</rt>\n   <rt>jīn</rt>\n   <rt>shān</rt>\n   <rtc>San Francisco</rtc>\n</ruby>',
    ], )


ruby = createComponent(
    'ruby',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby',
    docs="""
        The **HTML`<ruby>` element** represents a ruby annotation. Ruby annotations
        are for showing pronunciation of East Asian characters.
    """, )


s = createComponent(
    's',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/s',
    docs="""
        The **HTML`<s>` element** renders text with a strikethrough, or a line through
        it. Use the `<s>` element to represent things that are no longer relevant or
        no longer accurate. However, `<s>` is not appropriate when indicating document
        edits; for that, use the `<del>` and `<ins>` elements, as appropriate.
    """, )


samp = createComponent(
    'samp',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp',
    docs="""
        The **HTML`<samp>` element** is an element intended to identify sample output
        from a computer program. It is usually displayed in the browser's default
        monotype font (such as Lucida Console).
    """,
    examples=[
        "<p>The diet-tracking app said: <samp>You're not eating your veggies</samp> and that was true</p>",
    ], )


small = createComponent(
    'small',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/small',
    docs="""
        The **HTML`<small>`** **element** makes the text _font size_ one size smaller
        (for example, from large to medium, or from small to x-small) down to the
        browser's minimum font size. In HTML5, this element is repurposed to represent
        side-comments and small print, including copyright and legal text, independent
        of its styled presentation.
    """,
    notes="""
        Although the `<small>` element, like the `<b>` and `<i>` elements, may be
        perceived to violate the principle of separation between structure and
        presentation, all three are valid in HTML5. Authors are encouraged to use
        their best judgement when determining whether to use `<small>` or CSS.
    """,
    examples=[
        '<p>This is the first sentence. <small>This whole sentence\n  is in small letters.</small></p>',
        '<p>This is the first sentence.\n  <span style="font-size:0.8em">This whole sentence is in small\n  letters.</span></p>',
    ], )


span = createComponent(
    'span',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/span',
    docs="""
        The **HTML`<span>` element** is a generic inline container for phrasing
        content, which does not inherently represent anything. It can be used to group
        elements for styling purposes (using the `class` or `id` attributes), or
        because they share attribute values, such as `lang`. It should be used only
        when no other semantic element is appropriate. `<span>` is very much like a
        `<div>` element, but `<div>` is a block-level element whereas a `<span>` is an
        inline element.
    """, )


strong = createComponent(
    'strong',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong',
    docs="""
        The **HTML**` **< strong>**` **element** gives text strong importance, and is
        typically displayed in bold.
    """,
    examples=[
        '<p>When doing x it is <strong>imperative</strong>\n   to do y before proceeding.</p>',
    ], )


sub = createComponent(
    'sub',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub',
    docs="""
        The **HTML`<sub>` element** defines a span of text that should be displayed,
        for typographic reasons, lower, and often smaller, than the main span of text.
    """,
    examples=[
        '<p>The chemical formula of water: H<sub>2</sub>O</p>',
    ], )


sup = createComponent(
    'sup',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup',
    docs="""
        The **HTML`<sup>` element** defines a span of text that should be displayed,
        for typographic reasons, higher, and often smaller, than the main span of
        text.
    """,
    examples=[
        '<p>This text is <sup>superscripted</sup></p>',
    ], )


time = createComponent(
    'time',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/time',
    docs="""
        The **HTML`<time>` element** represents either a time on a 24-hour clock or a
        precise date in the Gregorian calendar (with optional time and timezone
        information).
    """,
    examples=[
        '<p>The concert starts at <time>20:00</time>.</p>',
        '<p>The concert took place on <time\n  datetime="2001-05-15T19:00">May 15</time>.</p>',
    ], )


u = createComponent(
    'u',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/u',
    docs="""
        The **HTML`<u>` element** renders text with an underline, a line under the
        baseline of its content. In HTML5, this element represents a span of text with
        an unarticulated, though explicitly rendered, non-textual annotation, such as
        labeling the text as being a proper name in Chinese text (a Chinese proper
        name mark), or labeling the text as being misspelled.
    """,
    examples=[
        '<u>Today\'s Special</u>: Salmon<br />\n<span style="text-decoration:underline;">Today\'s Special</span>:\n  Salmon\n<!-- Here <span> is used as the underlining is purely decorative\n  and it is applied with CSS -->',
        '<p><u>All</u> of that is explained in\n  <u>Dive into Python</u></p>\n<p><em>All</em> of that is explained in\n  <i>Dive into Python</i></p>\n<!-- Here the "All" is marked as stressed, using <em>,\n  while "Dive into Python" is marked as a name using <i> -->',
    ], )


var = createComponent(
    'var',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/var',
    docs="""
        The **HTML`<var>` element** represents a variable in a mathematical expression
        or a programming context.
    """, )


wbr = createComponent(
    'wbr',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr',
    docs="""
        The **HTML`<wbr>` element** represents a word break opportunity --a position
        within text where the browser may optionally break a line, though its line-
        breaking rules would not otherwise create a break at that location.
    """,
    notes="""
        On UTF-8 encoded pages, `<wbr>` behaves like the `U+200B`` ZERO-WIDTH SPACE`
        code point. In particular, it behaves like a Unicode bidi BN code point,
        meaning it has no effect on bidi-ordering: `<div dir=rtl>123,<wbr>456</div>`
        displays, when not broken on two lines, `123,456` and not `456,123`.
        
        For the same reason, the `<﻿wbr﻿>` element does not introduce a hyphen at the
        line break point. To make a hyphen appear only at the end of a line, use the
        soft hyphen character entity (`&﻿shy;`) instead.
        
        This element was first implemented in Internet Explorer 5.5 and was officially
        defined in HTML5.
    """,
    examples=[
        '<p>http://this<wbr>.is<wbr>.a<wbr>.really<wbr>.long<wbr>.example<wbr>.com/With<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages</p>',
    ], )


# == Image And Multimedia ==
# HTML supports various multimedia resources such as images, audio, and video.

area = createComponent(
    'area',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/area',
    docs="""
        The **HTML`<area>` element** defines a hot-spot region on an image, and
        optionally associates it with a hypertext link. This element is used only
        within a `<map>` element.
    """,
    notes="""
        Under the HTML 3.2, 4.0, and 5 specifications, the closing tag `</area>` is
        forbidden.
        
        The XHTML 1.0 specification requires a trailing slash: `<area />`.
        
        The **id** , **class** , and **style** attributes have the same meaning as the
        core attributes defined in the HTML 4 specification, but only Netscape and
        Microsoft define them.
        
        Netscape 1-level browsers do not understand the **target** attribute as it
        relates to frames.
        
        HTML 3.2 defines only **alt** , **coords** , **href** , **nohref** , and
        **shape**.
        
        HTML 5.1 defines obsolete the attribute **type** on this tag.
    """,
    examples=[
        '<map name="primary">\n  <area shape="circle" coords="75,75,75" href="left.html" alt="Click to go Left">\n  <area shape="circle" coords="275,75,75" href="right.html" alt="Click to go Right">\n</map>\n<img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic">',
    ], )


audio = createComponent(
    'audio',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio',
    docs="""
        The **HTML`<audio>` element** is used to embed sound content in documents. It
        may contain one or more audio sources, represented using the `src` attribute
        or the `<source>` element: the browser will choose the most suitable one. It
        can also be the destination for streamed media, using a `MediaStream`.
    """,
    examples=[
        '<!-- Simple audio playback -->\n<audio\n  src="http://developer.mozilla.org/@api/deki/files/2926/=AudioTest_(1).ogg"\n  autoplay>\n  Your browser does not support the <code>audio</code> element.\n</audio>',
        '<audio controls="controls">\n  Your browser does not support the <code>audio</code> element.\n  <source src="foo.wav" type="audio/wav">\n</audio>',
    ], )


img = createComponent(
    'img',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/img',
    docs="""
        The **HTML`<img>` element** represents an image in the document.
    """, )


map = createComponent(
    'map',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/map',
    docs="""
        The **HTML`<map>` element** is used with `<area>` elements to define an image
        map (a clickable link area).
    """,
    examples=[
        '<map name="primary">\n\xa0 <area shape="circle" coords="75,75,75" href="left.html">\n\xa0 <area shape="circle" coords="275,75,75" href="right.html">\n</map>\n<img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic">',
    ], )


track = createComponent(
    'track',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/track',
    docs="""
        The **HTML`<track>` element** is used as a child of the media elements
        `<audio>` and `<video>`. It lets you specify timed text tracks (or time-based
        data), for example to automatically handle subtitles. The tracks are formatted
        in WebVTT format (`.vtt` files) -- Web Video Text Tracks.
    """,
    examples=[
        '<video controls poster="/images/sample.gif">\n   <source src="sample.mp4" type="video/mp4">\n   <source src="sample.ogv" type="video/ogv">\n   <track kind="captions" src="sampleCaptions.vtt" srclang="en">\n   <track kind="descriptions"\n     src="sampleDescriptions.vtt" srclang="en">\n   <track kind="chapters" src="sampleChapters.vtt" srclang="en">\n   <track kind="subtitles" src="sampleSubtitles_de.vtt" srclang="de">\n   <track kind="subtitles" src="sampleSubtitles_en.vtt" srclang="en">\n   <track kind="subtitles" src="sampleSubtitles_ja.vtt" srclang="ja">\n   <track kind="subtitles" src="sampleSubtitles_oz.vtt" srclang="oz">\n   <track kind="metadata" src="keyStage1.vtt" srclang="en"\n     label="Key Stage 1">\n   <track kind="metadata" src="keyStage2.vtt" srclang="en"\n     label="Key Stage 2">\n   <track kind="metadata" src="keyStage3.vtt" srclang="en"\n     label="Key Stage 3">\n   <!-- Fallback -->\n   ...\n</video>',
    ], )


video = createComponent(
    'video',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/video',
    docs="""
        Use the **HTML`<video>` element** to embed video content in a document.
    """,
    examples=[
        '<!-- Simple video example -->\n<video src="videofile.webm" autoplay poster="posterimage.jpg">\nSorry, your browser doesn\'t support embedded videos, \nbut don\'t worry, you can <a href="videofile.webm">download it</a>\nand watch it with your favorite video player!\n</video>\n\n<!-- Video with subtitles -->\n<video src="foo.webm">\n  <track kind="subtitles" src="foo.en.vtt" srclang="en"\n    label="English">\n  <track kind="subtitles" src="foo.sv.vtt" srclang="sv"\n    label="Svenska">\n</video>',
    ], )


# == Embedded Content ==
# In addition to regular multimedia content, HTML can include a variety of other
# content, even if it's not always easy to interact with.

embed = createComponent(
    'embed',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed',
    docs="""
        The **HTML`<embed>` element** represents an integration point for an external
        application or interactive content (in other words, a plug-in).
        
        **Note:** This topic documents only the element that is defined as part of
        HTML5. It does not address earlier, non-standardized implementation of the
        element.
    """,
    examples=[
        '<embed type="video/quicktime" src="movie.mov" width="640" height="480">',
    ], )


object = createComponent(
    'object',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/object',
    docs="""
        The **HTML`<object>` element** represents an external resource, which can be
        treated as an image, a nested browsing context, or a resource to be handled by
        a plugin.
    """,
    examples=[
        '<!-- Embed a flash movie -->\n<object data="movie.swf"\n  type="application/x-shockwave-flash"></object>\n\n<!-- Embed a flash movie with parameters -->\n<object data="movie.swf" type="application/x-shockwave-flash">\n  <param name="foo" value="bar">\n</object>',
    ], )


param = createComponent(
    'param',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/param',
    docs="""
        The **HTML`<param>` element** defines parameters for an `<object>` element.
    """, )


source = createComponent(
    'source',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/source',
    docs="""
        The **HTML`<source>` element** specifies multiple media resources for either
        the `<picture>`, the `<audio>` or the `<video>` element. It is an empty
        element. It is commonly used to serve the same media content in multiple
        formats supported by different browsers.
    """,
    examples=[
        '<video controls>\n  <source src="foo.webm" type="video/webm">\n  <source src="foo.ogg" type="video/ogg"> \n  <source src="foo.mov" type="video/quicktime">\n\xa0 I\'m sorry; your browser doesn\'t support HTML5 video.\n</video>',
    ], )


# == Scripting ==
# In order to create dynamic content and Web applications, HTML supports the use
# of scripting languages, most prominently JavaScript. Certain elements support
# this capability.

canvas = createComponent(
    'canvas',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas',
    docs="""
        Use the **HTML`<canvas>` element** with the canvas scripting API to draw
        graphics and animations.
    """,
    examples=[
        '<canvas id="canvas" width="300" height="300">\n  An alternative text describing what your canvas displays. \n</canvas>',
        '<canvas id="myCanvas" moz-opaque></canvas>',
    ], )


noscript = createComponent(
    'noscript',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript',
    docs="""
        The **HTML`<noscript>` element** defines a section of HTML to be inserted if a
        script type on the page is unsupported or if scripting is currently turned off
        in the browser.
    """,
    examples=[
        '<noscript>\n  <!-- anchor linking to external file -->\n  <a href="https://www.mozilla.com/">External Link</a>\n</noscript>\n<p>Rocks!</p>',
    ], )


script = createComponent(
    'script',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/script',
    docs="""
        The **HTML`<script>` element** is used to embed or reference an executable
        script.
    """,
    notes="""
        Scripts without `async` or `defer` attributes, as well as inline scripts, are
        fetched and executed immediately, before the browser continues to parse the
        page.
        
        The script should be served with the `text/javascript` MIME type, but browsers
        are lenient and only block them if the script is served with an image type
        (`image/*`), a video type (`video/*`), an audio (`audio/*`) type, or
        `text/csv`. If the script is blocked, an `error` is sent to the element, if
        not a `load` event is sent.
    """,
    examples=[
        '<!-- HTML4 and (x)HTML -->\n<script type="text/javascript" src="javascript.js"></script>\n\n<!-- HTML5 -->\n<script src="javascript.js"></script>',
    ], )


# == Demarcating Edits ==
# These elements let you provide indications that specific parts of the text
# have been altered.

del_ = createComponent(
    'del',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/del',
    docs="""
        The **HTML`<del>` element** represents a range of text that has been deleted
        from a document. This element is often (but need not be) rendered with strike-
        through text.
    """,
    examples=[
        '<p><del>This text has been deleted</del>,\nhere is the rest of the paragraph.</p>\n<del><p>This paragraph has been deleted.</p></del>',
    ], )


ins = createComponent(
    'ins',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins',
    docs="""
        The **HTML`<ins>` element** represents a range of text that has been added to
        a document.
    """,
    examples=[
        '<ins>This text has been inserted</ins>',
    ], )


# == Table Content ==
# The elements here are used to create and handle tabular data.

caption = createComponent(
    'caption',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption',
    docs="""
        The **HTML`<caption>` element** represents the title of a table. Though it is
        always the first descendant of a `<table>`, its styling, using CSS, may place
        it elsewhere, relative to the table.
    """, )


col = createComponent(
    'col',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/col',
    docs="""
        The **HTML`<col>` element** defines a column within a table and is used for
        defining common semantics on all common cells. It is generally found within a
        `<colgroup>` element.
        
        This element allows styling columns using CSS, but only a few attributes will
        have an effect on the column (see the CSS 2.1 specification for a list).
    """, )


colgroup = createComponent(
    'colgroup',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup',
    docs="""
        The **HTML`<colgroup>` element** defines a group of columns within a table.
    """, )


table = createComponent(
    'table',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/table',
    docs="""
        The **HTML`<table>` element** represents tabular data  -- that is, information
        expressed via a two-dimensional data table.
    """,
    examples=[
        '<table>\n  <tr>\n    <td>John</td>\n    <td>Doe</td>\n  </tr>\n  <tr>\n    <td>Jane</td>\n    <td>Doe</td>\n  </tr>\n</table>',
        '<p>Simple table with header</p>\n<table>\n  <tr>\n    <th>First name</th>\n    <th>Last name</th>\n  </tr>\n  <tr>\n    <td>John</td>\n    <td>Doe</td>\n  </tr>\n  <tr>\n    <td>Jane</td>\n    <td>Doe</td>\n  </tr>\n</table>\n\n<p>Table with thead, tfoot, and tbody</p>\n<table>\n  <thead>\n    <tr>\n      <th>Header content 1</th>\n      <th>Header content 2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Body content 1</td>\n      <td>Body content 2</td>\n    </tr>\n  </tbody>\n  <tfoot>\n\xa0   <tr>\n\xa0     <td>Footer content 1</td>\n\xa0     <td>Footer content 2</td>\n\xa0   </tr>\n  </tfoot>\n</table>\n\n<p>Table with colgroup</p>\n<table>\n  <colgroup span="4"></colgroup>\n  <tr>\n    <th>Countries</th>\n    <th>Capitals</th>\n    <th>Population</th>\n    <th>Language</th>\n  </tr>\n  <tr>\n    <td>USA</td>\n    <td>Washington D.C.</td>\n    <td>309 million</td>\n    <td>English</td>\n  </tr>\n  <tr>\n    <td>Sweden</td>\n    <td>Stockholm</td>\n    <td>9 million</td>\n    <td>Swedish</td>\n  </tr>\n</table>\n\n<p>Table with colgroup and col</p>\n<table>\n  <colgroup>\n    <col style="background-color: #0f0">\n    <col span="2">\n  </colgroup>\n  <tr>\n    <th>Lime</th>\n    <th>Lemon</th>\n    <th>Orange</th>\n  </tr>\n  <tr>\n    <td>Green</td>\n    <td>Yellow</td>\n    <td>Orange</td>\n  </tr>\n</table>\n\n<p>Simple table with caption</p>\n<table>\n  <caption>Awesome caption</caption>\n  <tr>\n    <td>Awesome data</td>\n  </tr>\n</table>',
    ], )


tbody = createComponent(
    'tbody',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody',
    docs="""
        The **HTML`<tbody>` element** groups one or more `<tr>` elements as the body
        of a `<table>` element.
    """, )


td = createComponent(
    'td',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/td',
    docs="""
        The **HTML`<td>` element** defines a cell of a table that contains data. It
        participates in the _table model_.
    """, )


tfoot = createComponent(
    'tfoot',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot',
    docs="""
        The **HTML`<tfoot>` element** defines a set of rows summarizing the columns of
        the table.
    """, )


th = createComponent(
    'th',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/th',
    docs="""
        The **HTML`<th>` element** defines a cell as header of a group of table cells.
        The exact nature of this group is defined by the `scope` and `headers`
        attributes.
    """, )


thead = createComponent(
    'thead',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead',
    docs="""
        The **HTML`<thead>` element** defines a set of rows defining the head of the
        columns of the table.
    """, )


tr = createComponent(
    'tr',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr',
    docs="""
        The HTML **`<tr>`** element specifies that the markup contained inside the
        `<tr>` block comprises one row of a table, inside which the `<th>` and `<td>`
        elements create header and data cells, respectively, within the row. Each cell
        is placed into its own column; the user agent follows specific rules to
        determine how the cells in each row are placed into columns with those coming
        from other rows.
        
        To provide additional control over how cells fit into (or span across)
        columns, both `<th>` and `<td>` support the `colspan` attribute, which lets
        you specify how many columns wide the cell should be, with the default being
        1. Similarly, you can use the `rowspan` attribute on cells to indicate they
        should span more than one table row.
        
        This can take a little practice to get right when building your tables. We
        have some examples below, but for more examples and an in-depth tutorial, see
        the HTML tables series in our Learn web development area, where you'll learn
        how to use the table elements and their attributes to get just the right
        layout and formatting for your tabular data.
    """,
    examples=[
        '<table>\n  <tr>\n    <th>Name</th>\n    <th>ID</th>\n    <th>Member Since</th>\n    <th>Balance</th>\n  </tr>\n  <tr>\n    <td>Margaret Nguyen</td>\n    <td>427311</td>\n    <td><time datetime="2010-06-03">June 3, 2010</time></td>\n    <td>0.00</td>\n  </tr>\n  <tr>\n    <td>Edvard Galinski</td>\n    <td>533175</td>\n    <td><time datetime="2011-01013">January 13, 2011</time></td>\n    <td>37.00</td>\n  </tr>\n  <tr>\n    <td>Hoshi Nakamura</td>\n    <td>601942</td>\n    <td><time datetime="2012-07-23">July 23, 2012</time></td>\n    <td>15.00</td>\n  </tr>\n</table>',
        '<table>\n  <tr>\n    <th rowspan="2">Name</th>\n    <th rowspan="2">ID</th>\n    <th colspan="2">Membership Dates</th>\n    <th rowspan="2">Balance</th>\n  </tr>\n  <tr>\n    <th>Joined</th>\n    <th>Canceled</th>\n  </tr>\n  <tr>\n    <th>Margaret Nguyen</td>\n    <td>427311</td>\n    <td><time datetime="2010-06-03">June 3, 2010</time></td>\n    <td>n/a</td>\n    <td>0.00</td>\n  </tr>\n  <tr>\n    <th>Edvard Galinski</td>\n    <td>533175</td>\n    <td><time datetime="2011-01013">January 13, 2011</time></td>\n    <td><time datetime="2017-04008">April 8, 2017</time></td>\n    <td>37.00</td>\n  </tr>\n  <tr>\n    <th>Hoshi Nakamura</td>\n    <td>601942</td>\n    <td><time datetime="2012-07-23">July 23, 2012</time></td>\n    <td>n/a</td>\n    <td>15.00</td>\n  </tr>\n</table>',
        '<table>\n\xa0 <thead>\n\xa0\xa0\xa0 <tr>\n\xa0\xa0\xa0\xa0\xa0 <th rowspan="2">Name</th>\n\xa0\xa0\xa0\xa0\xa0 <th rowspan="2">ID</th>\n\xa0\xa0\xa0\xa0\xa0 <th colspan="2">Membership Dates</th>\n\xa0\xa0\xa0\xa0\xa0 <th rowspan="2">Balance</th>\n\xa0\xa0\xa0 </tr>\n\xa0\xa0\xa0 <tr>\n\xa0\xa0\xa0\xa0\xa0 <th>Joined</th>\n\xa0\xa0\xa0\xa0\xa0 <th>Canceled</th>\n\xa0\xa0\xa0 </tr>\n\xa0 </thead>\n\xa0 <tbody>\n\xa0\xa0\xa0 <tr>\n\xa0\xa0\xa0\xa0\xa0 <th scope="rowgroup">Margaret Nguyen</td>\n\xa0\xa0\xa0\xa0\xa0 <td>427311</td>\n\xa0\xa0\xa0\xa0\xa0 <td><time datetime="2010-06-03">June 3, 2010</time></td>\n\xa0\xa0\xa0\xa0\xa0 <td>n/a</td>\n\xa0\xa0\xa0\xa0\xa0 <td>0.00</td>\n\xa0\xa0\xa0 </tr>\n\xa0\xa0\xa0 <tr>\n\xa0\xa0\xa0\xa0\xa0 <th scope="rowgroup">Edvard Galinski</td>\n\xa0\xa0\xa0\xa0\xa0 <td>533175</td>\n\xa0\xa0\xa0\xa0\xa0 <td><time datetime="2011-01013">January 13, 2011</time></td>\n\xa0\xa0\xa0\xa0\xa0 <td><time datetime="2017-04008">April 8, 2017</time></td>\n\xa0\xa0\xa0\xa0\xa0 <td>37.00</td>\n\xa0\xa0\xa0 </tr>\n\xa0\xa0\xa0 <tr>\n\xa0\xa0\xa0\xa0\xa0 <th scope="rowgroup">Hoshi Nakamura</td>\n\xa0\xa0\xa0\xa0\xa0 <td>601942</td>\n\xa0\xa0\xa0\xa0\xa0 <td><time datetime="2012-07-23">July 23, 2012</time></td>\n\xa0\xa0\xa0\xa0\xa0 <td>n/a</td>\n\xa0\xa0\xa0\xa0\xa0 <td>15.00</td>\n\xa0\xa0\xa0 </tr>\n\xa0 </tbody>\n</table>',
        '<table>\n  <thead>\n    <tr>\n      <th rowspan="2">Name</th>\n      <th rowspan="2">ID</th>\n      <th colspan="2">Membership Dates</th>\n      <th rowspan="2">Balance</th>\n    </tr>\n    <tr>\n      <th>Joined</th>\n      <th>Canceled</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th scope="rowgroup">Margaret Nguyen</td>\n      <td>427311</td>\n      <td><time datetime="2010-06-03">June 3, 2010</time></td>\n      <td>n/a</td>\n      <td>0.00</td>\n    </tr>\n    <tr>\n      <th scope="rowgroup">Edvard Galinski</td>\n      <td>533175</td>\n      <td><time datetime="2011-01013">January 13, 2011</time></td>\n      <td><time datetime="2017-04008">April 8, 2017</time></td>\n      <td>37.00</td>\n    </tr>\n    <tr>\n      <th scope="rowgroup">Hoshi Nakamura</td>\n      <td>601942</td>\n      <td><time datetime="2012-07-23">July 23, 2012</time></td>\n      <td>n/a</td>\n      <td>15.00</td>\n    </tr>\n  </tbody>\n</table>',
        '<table>\n  <thead>\n    <tr>\n      <th rowspan="2">Name</th>\n      <th rowspan="2">ID</th>\n      <th colspan="2">Membership Dates</th>\n      <th rowspan="2">Balance</th>\n    </tr>\n    <tr>\n      <th>Joined</th>\n      <th>Canceled</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th scope="rowgroup">Margaret Nguyen</td>\n      <td>427311</td>\n      <td><time datetime="2010-06-03">June 3, 2010</time></td>\n      <td>n/a</td>\n      <td>0.00</td>\n    </tr>\n    <tr>\n      <th scope="rowgroup">Edvard Galinski</td>\n      <td>533175</td>\n      <td><time datetime="2011-01013">January 13, 2011</time></td>\n      <td><time datetime="2017-04008">April 8, 2017</time></td>\n      <td>37.00</td>\n    </tr>\n    <tr>\n      <th scope="rowgroup">Hoshi Nakamura</td>\n      <td>601942</td>\n      <td><time datetime="2012-07-23">July 23, 2012</time></td>\n      <td>n/a</td>\n      <td>15.00</td>\n    </tr>\n  </tbody>\n</table>',
    ], )


# == Forms ==
# HTML provides a number of elements which can be used together to create forms
# which the user can fill out and submit to the Web site or application. There's
# a great deal of further information about this available in the HTML forms
# guide.

button = createComponent(
    'button',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/button',
    docs="""
        The **HTML`<button>` element** represents a clickable button.
    """,
    notes="""
        `<button>` elements are much easier to style than `<input>` elements. You can
        add inner HTML content (think `<em>`, `<strong>` or even `<img>`), and make
        use of `:after` and `:before` pseudo-element to achieve complex rendering
        while `<input>` only accepts a text value attribute.
        
        IE7 has a bug where when submitting a form with `<button type="submit"
        name="myButton" value="foo">Click me</button>`, the `POST` data sent will
        result in `myButton=Click me` instead of `myButton=foo`.  
        IE6 has an even worse bug where submitting a form through a button will submit
        ALL buttons of the form, with the same bug as IE7.  
        This bug has been fixed in IE8.
        
        Firefox will add, for accessibility purposes, a small dotted border on a
        focused button. This border is declared through CSS, in the browser
        stylesheet, but you can override it if necessary to add your own focused style
        using `button`::-moz-focus-inner` { }`
        
        Firefox will, unlike other browsers, by default, persist the dynamic disabled
        state of a `<button>` across page loads. Setting the value of the
        `autocomplete` attribute to `off` disables this feature. See bug 654072.
        
        Firefox <35 for Android sets a default `background-image` gradient on all
        buttons (see bug 763671). This can be disabled using `background-image: none`.
        
        ### Clicking and focus
        
        Whether clicking on a `<button>` causes it to (by default) become focused
        varies by browser and OS. The results for `<input>` of `type="button"` and
        `type="submit"` were the same.
        
        Does clicking on a `<button>` give it the focus? Desktop Browsers | Windows
        8.1 | OS X 10.9  
        ---|---|---  
        Firefox 30.0 | Yes | No (even with a `tabindex`)  
        Chrome 35 | Yes | Yes  
        Safari 7.0.5 | N/A | No (even with a `tabindex`)  
        Internet Explorer 11 | Yes | N/A  
        Presto (Opera 12) | Yes | Yes  
        Does tapping on a `<button>` give it the focus? Mobile Browsers | iOS 7.1.2 |
        Android 4.4.4  
        ---|---|---  
        Safari Mobile | No (even with a `tabindex`) | N/A  
        Chrome 35 | No (even with a `tabindex`) | Yes
    """, )


datalist = createComponent(
    'datalist',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist',
    docs="""
        The **HTML`<datalist>` element** contains a set of `<option>` elements that
        represent the values available for other controls.
    """,
    examples=[
        '<label>Choose a browser from this list:\n<input list="browsers" name="myBrowser" /></label>\n<datalist id="browsers">\n  <option value="Chrome">\n  <option value="Firefox">\n  <option value="Internet Explorer">\n  <option value="Opera">\n  <option value="Safari">\n  <option value="Microsoft Edge">\n</datalist>',
    ], )


fieldset = createComponent(
    'fieldset',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset',
    docs="""
        The **HTML`<fieldset>` element** is used to group several controls as well as
        labels (`<label>`) within a web form.
    """,
    examples=[
        '<form action="test.php" method="post">\n  <fieldset>\n    <legend>Title</legend>\n    <input type="radio" id="radio">\n    <label for="radio">Click me</label>\n  </fieldset>\n</form>',
        '<!doctype html>\n<html>\n<head>\n<meta charset="UTF-8" />\n<title>Editable [pseudo]select</title>\n<style type="text/css">\n\n/* Generic form fields */\n\nfieldset.elist, input[type="text"], textarea, select,\noption, fieldset.elist ul, fieldset.elist > legend,\nfieldset.elist input[type="text"],\nfieldset.elist > legend:after {\n  -webkit-box-sizing: border-box;\n  -moz-box-sizing: border-box;\n  box-sizing: border-box;\n}\n\ninput[type="text"] {\n  padding: 0 20px;\n}\n\ntextarea {\n  width: 500px;\n  height: 200px;\n  padding: 20px;\n}\n\ntextarea, input[type="text"], fieldset.elist ul,\nselect, fieldset.elist > legend {\n  border: 2px #cccccc solid;\n  border-radius: 10px;\n}\n\ninput[type="text"], fieldset.elist, select,\nfieldset.elist > legend {\n  height: 32px;\n  font-family: Tahoma;\n  font-size: 14px;\n}\n\ninput[type="text"]:hover, textarea:hover,\nselect:hover, fieldset.elist:hover > legend {\n  background-color: #ddddff;\n}\n\nselect {\n  padding: 4px 20px;\n}\n\noption {\n  height: 30px;\n  padding: 5px 4px;\n}\n\noption:not(:checked), textarea:focus {\n  background-color: #ffcccc;\n}\n\nfieldset.elist > legend:after,\nfieldset.elist label {\n  height: 28px;\n}\n\ninput[type="text"], fieldset.elist {\n  width: 316px;\n}\n\ninput[type="text"]:focus {\n  background: #ffcccc url("data:image/gif;\n  base64,R0lGODlhEAAQANU5APnoxuvr6+uxPdvb2+\n  rq6ri4uO7qxunp6dPT06SHV+/rx8vLy+\n  nezLO0sbe3t9Ksas+qaaCEV8rKyp2dnf39/\n  QAAAK6ursifZHFxcc/\n  Qzu3mxYyMjExCJnV1dc6maO7u7o+\n  Pj2tXNoaGhtfDpKCDVu3lxM+\n  tcaKEV9bW1qOFVWNjY8KrisTExNra2nBbObGxsby8vO/\n  mu7Kyso9ZAuzs7MSgAIiKhf///8zMzP///\n  wAAAAAAAAAAAAAAAAAAAAAAACH5BAEAADkALAAAAAAQ\n  ABAAAAaXwJxwSCwOYzWkMpkkZmoAqDQaJdpqAqw2m53\n  NRjlboAarFczomcE0C99o8DgNMVM8Tm3bbYDr9x11Dw\n  kzDG5yc2oQJIRCenx/MxoeETM2Q3pxATMlF4MYlo17O\n  AsdLispMyAioIY0BzMcITMTKBasjgssFTMqGxItMjYU\n  oTQBBAQHxgE0wZcfMtDRMi/QrA022NnaNg1CQQA7")\n  no-repeat 2px center !important;\n}\n\ninput[type="text"]:focus, textarea:focus,\nselect:focus, fieldset.elist > legend {\n  border: 2px #ccaaaa solid;\n}\n\nfieldset {\n  border: 2px #af3333 solid;\n  border-radius: 10px;\n}\n\n/* Editable [pseudo]select\n(i.e. fieldsets with [class=elist]) */\n\nfieldset.elist {\n  display: inline-block;\n  position: relative;\n  vertical-align: middle;\n  overflow: visible;\n  padding: 0;\n  margin: 0;\n  border: none;\n}\n\nfieldset.elist ul {\n  position: absolute;\n  width: 100%;\n  max-height: 320px;\n  padding: 0;\n  margin: 0;\n  overflow: hidden;\n  background-color: transparent;\n}\n\nfieldset.elist:hover ul {\n  background-color: #ffffff;\n  border: 2px #af3333 solid;\n  left: 2px;\n  overflow: auto;\n}\n\nfieldset.elist ul > li {\n  list-style-type: none;\n  background-color: transparent;\n}\n\nfieldset.elist label {\n  display: none;\n  width: 100%;\n}\n\nfieldset.elist input[type="text"] {\n  width: 100%;\n  height: 30px;\n  line-height: 30px;\n  border: none;\n  background-color: transparent;\n  border-radius: 0;\n}\n\nfieldset.elist > legend {\n  display: block;\n  margin: 0;\n  padding: 0 0 0 5px;\n  position: absolute;\n  width: 100%;\n  cursor: default;\n  background-color: #ccffcc;\n  line-height: 30px;\n  font-style: italic;\n}\n\nfieldset.elist:hover > legend {\n  position: relative;\n  overflow: hidden;\n}\n\nfieldset.elist > legend:after {\n  width: 20px;\n  content: "\\2335";\n  float: right;\n  text-align: center;\n  border-left: 2px #cccccc solid;\n  font-style: normal;\n  cursor: default;\n}\n\nfieldset.elist:hover > legend:after {\n  background-color: #99ff99;\n}\n\nfieldset.elist ul input[type="radio"] {\n  display: none;\n}\n\nfieldset.elist input[type="radio"]:checked ~ label {\n  display: block;\n  width: 292px;\n  background-color: #ffffff;\n}\n\nfieldset.elist:hover\ninput[type="radio"]:checked ~ label {\n  width: 100%;\n}\n\nfieldset.elist:hover label {\n  display: block;\n  height: 100%;\n}\n\nfieldset.elist label:hover {\n  background-color: #3333ff !important;\n}\n\nfieldset.elist:hover\ninput[type="radio"]:checked ~ label {\n  background-color: #aaaaaa;\n}\n\n</style>\n\n</head>\n<body>\n\n<form method="get" action="test.php">\n\n<fieldset>\n    <legend>Order a T-Shirt</legend>\n    <p>Write your name (simple textbox):\n    <input type="text" /></p>\n    <p>Choose your size (simple select):\n    <select>\n        <option value="s">Small</option>\n        <option value="m">Medium</option>\n        <option value="l">Large</option>\n        <option value="xl">Extra Large</option>\n    </select></p>\n    <div>What address do you want to use?\n    (editable pseudoselect)\n    <fieldset class="elist">\n        <legend>Address&hellip;</legend>\n        <ul>\n            <li><input type="radio" value="1"\n            id="address-switch_1" checked\n            /><label for="address-switch_1"\n            ><input type="text"\n            value="19 Quaker Ridge Rd. Bethel CT 06801"\n            /></label></li>\n            <li><input type="radio" value="2"\n            id="address-switch_2"\n            /><label for="address-switch_2"\n            ><input type="text"\n            value="1000 Coney Island Ave.\n            Brooklyn NY 11230"\n            /></label></li>\n            <li><input type="radio" value="3"\n            id="address-switch_3"\n            /><label for="address-switch_3"\n            ><input type="text"\n            value="2962 Dunedin Cv. Germantown TN 38138"\n            /></label></li>\n            <li><input type="radio" value="4"\n            id="address-switch_4"\n            /><label for="address-switch_4"\n            ><input type="text"\n            value="915 E 7th St. Apt 6L. Brooklyn NY 11230"\n            /></label></li>\n        </ul>\n    </fieldset>\n    </div>\n    <p>Write a comment:<br />\n    <textarea></textarea></p>\n    <p><input type="reset" value="Reset" />\n    <input type="submit" value="Send!" /></p>\n</fieldset>\n\n</form>\n\n</body>\n</html>',
    ], )


form = createComponent(
    'form',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/form',
    docs="""
        The **HTML`<form>` element** represents a document section that contains
        interactive controls to submit information to a web server.
        
        It is possible to use the `:valid` and `:invalid` CSS pseudo-classes to style
        a `<form>` element.
    """,
    examples=[
        '<!-- Simple form which will send a GET request -->\n<form action="" method="get">\n\xa0 <label for="GET-name">Name:</label>\n\xa0 <input id="GET-name" type="text" name="name">\n\xa0 <input type="submit" value="Save">\n</form>\n\n<!-- Simple form which will send a POST request -->\n<form action="" method="post">\n\xa0 <label for="POST-name">Name:</label>\n\xa0 <input id="POST-name" type="text" name="name">\n\xa0 <input type="submit" value="Save">\n</form>\n\n<!-- Form with fieldset, legend, and label -->\n<form action="" method="post">\n\xa0 <fieldset>\n\xa0 \xa0 <legend>Title</legend>\n\xa0 \xa0 <input type="radio" name="radio" id="radio">\n    <label for="radio">Click me</label>\n\xa0 </fieldset>\n</form>',
    ], )


input = createComponent(
    'input',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/input',
    docs="""
        The **HTML`<input>` element** is used to create interactive controls for web-
        based forms in order to accept data from the user.
    """,
    notes="""
        ### File inputs
        
          1. Starting in Gecko 2.0, calling the `click()` method on an `<input>` element of type `file` opens the file picker and lets the user select files. See Using files from web applications for an example and more details.
        
          2. You cannot set the value of a file picker from a script -- doing something like the following has no effect:
            
                var e = getElementById("someFileInputElement");
            e.value = "foo";
            
        
          3. When a file is chosen using an `<input type="file">`, the real path to the source file is not shown in the input's `value` attribute for obvious security reasons. Instead, the filename is shown, with `C:\fakepath\` appended to the beginning of it. There are some historical reasons for this quirk, but it is supported across all modern browsers, and in fact is defined in the spec.
        
        ### Error messages
        
        If you want Firefox to present a custom error message when a field fails to
        validate, you can use the `x-moz-errormessage` attribute to do so:
        
            
            
            <input type="email"
             x-moz-errormessage="Please specify a valid email address.">
            
        
        Note, however, that this is not standard and will not have an effect on other
        browsers.
        
        ### Localization
        
        The allowed inputs for certain <input> types depend on the locale. In some
        locales, 1,000.00 is a valid number, while in other locales the valid way to
        enter this number is 1.000,00.
        
        Firefox uses the following heuristics to determine the locale to validate the
        user's input (at least for `type="number"`):
        
          * Try the language specified by a `lang`/`xml:lang` attribute on the element or any of its parents.
          * Try the language specified by any Content-Language HTTP header or
          * If none specified, use the browser's locale.
        
        ### Using mozactionhint on Firefox mobile
        
        You can use the `mozactionhint` attribute to specify the text for the label of
        the enter key on the virtual keyboard when your form is rendered on Firefox
        mobile. For example, to have a "Next" label, you can do this:
        
            
            
            <input type="text" mozactionhint="next">
            
        
        The result is:
        
        ![mozactionhint.png](/@api/deki/files/4970/=mozactionhint.png?size=webview)
    """, )


label = createComponent(
    'label',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/label',
    docs="""
        The **HTML`<label>` element** represents a caption for an item in a user
        interface.
    """,
    examples=[
        '<label>Click me <input type="text"></label>',
        '<label for="username">Click me</label>\n<input type="text" id="username">',
    ], )


legend = createComponent(
    'legend',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend',
    docs="""
        The **HTML`<legend>` element** represents a caption for the content of its
        parent `<fieldset>`.
    """, )


meter = createComponent(
    'meter',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter',
    docs="""
        The **HTML`<meter>` element** represents either a scalar value within a known
        range or a fractional value.
    """,
    examples=[
        '<p>Heat the oven to <meter min="200" max="500"\n  value="350">350 degrees</meter>.</p>',
        '<p>He got a <meter low="69" high="80" max="100"\n  value="84">B</meter> on the exam.</p>',
    ], )


optgroup = createComponent(
    'optgroup',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup',
    docs="""
        The **HTML`<optgroup>` element** creates a grouping of options within a
        `<select>` element.
    """,
    examples=[
        '<select>\n  <optgroup label="Group 1">\n    <option>Option 1.1</option>\n  </optgroup> \n  <optgroup label="Group 2">\n    <option>Option 2.1</option>\n    <option>Option 2.2</option>\n  </optgroup>\n  <optgroup label="Group 3" disabled>\n    <option>Option 3.1</option>\n    <option>Option 3.2</option>\n    <option>Option 3.3</option>\n  </optgroup>\n</select>',
    ], )


option = createComponent(
    'option',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/option',
    docs="""
        The **HTML`<option>` element** is used to define an item contained in a
        `<select>`, an `<optgroup>`, or a `<datalist>` element. As such, `<option>`
        can represent menu items in popups and other lists of items in an HTML
        document.
    """, )


output = createComponent(
    'output',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/output',
    docs="""
        Introduced in HTML5
        
        The **HTML`<output>` element** represents the result of a calculation or user
        action.
    """,
    examples=[
        '<form oninput="result.value=parseInt(a.value)+parseInt(b.value)">\n    <input type="range" name="b" value="50" /> +\n    <input type="number" name="a" value="10" /> =\n    <output name="result">60</output>\n</form>',
    ], )


progress = createComponent(
    'progress',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress',
    docs="""
        Introduced in HTML5
        
        The **HTML`<progress>` element** represents the completion progress of a task,
        typically displayed as a progress bar.
    """,
    examples=[
        '<progress value="70" max="100">70 %</progress>',
    ], )


select = createComponent(
    'select',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/select',
    docs="""
        The **HTML`<select>` element** represents a control that provides a menu of
        options:
    """,
    examples=[
        '<!-- The second value will be selected initially -->\n<select name="select"> <!--Supplement an id here instead of using \'name\'-->\n\xa0 <option value="value1">Value 1</option> \n\xa0\xa0<option value="value2" selected>Value 2</option>\n\xa0 <option value="value3">Value 3</option>\n</select>',
    ], )


textarea = createComponent(
    'textarea',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea',
    docs="""
        The **HTML`<textarea>` element** represents a multi-line plain-text editing
        control.
    """,
    examples=[
        '<textarea name="textarea"\n   rows="10" cols="50">Write something here</textarea>',
    ], )


# == Interactive Elements ==
# HTML offers a selection of elements which help to create interactive user
# interface objects.

details = createComponent(
    'details',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/details',
    docs="""
        The **HTML`<details>` element** is used as a disclosure widget from which the
        user can retrieve additional information.
    """,
    examples=[
        '<details>\n  <summary>Some details</summary>\n  <p>More info about the details.</p>\n</details>\n\n<details open>\n  <summary>Even more details</summary>\n  <p>Here are even more details about the details.</p>\n</details>',
    ], )


dialog = createComponent(
    'dialog',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog',
    docs="""
        The **HTML`<dialog>` element** represents a dialog box or other interactive
        component, such as an inspector or window.
    """,
    examples=[
        '<dialog open>\n  <p>Greetings, one and all!</p>\n</dialog>',
        '<!-- Simple pop-up dialog box, containing a form -->\n<dialog open id="favDialog">\n  <form method="dialog">\n    <section>\n      <p><label for="favAnimal">Favorite animal:</label>\n      <select id="favAnimal">\n        <option></option>\n        <option>Brine shrimp</option>\n        <option>Red panda</option>\n        <option>Spider monkey</option>\n      </select></p>\n    </section>\n    <menu>\n      <button id="cancel" type="reset">Cancel</button>\n      <button type="submit">Confirm</button>\n    </menu>\n  </form>\n</dialog>\n\n<menu>\n  <button id="updateDetails">Update details</button>\n</menu>',
    ], )


menu = createComponent(
    'menu',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu',
    docs="""
        __ **This is anexperimental technology**  
        Check the Browser compatibility table carefully before using this in
        production.
        
        The **HTML`<menu>` element** represents a group of commands that a user can
        perform or activate. This includes both list menus, which might appear across
        the top of a screen, as well as context menus, such as those that might appear
        underneath a button after it has been clicked.
    """,
    examples=[
        '<!-- A <div> element with a context menu -->\n<div contextmenu="popup-menu">\n  Right-click to see the adjusted context menu\n</div>\n\n<menu type="context" id="popup-menu">\n  <menuitem>Action</menuitem>\n  <menuitem>Another action</menuitem>\n  <hr>\n  <menuitem>Separated action</menuitem>\n</menu>',
        '<!-- A button, which displays a menu when clicked. -->\n<button type="menu" menu="popup-menu">\n  Dropdown\n</button>\n\n<menu type="context" id="popup-menu">\n  <menuitem>Action</menuitem>\n  <menuitem>Another action</menuitem>\n  <hr>\n  <menuitem>Separated action</menuitem>\n</menu>',
        '<!-- A context menu for a simple editor,\n    containing two menu buttons. -->\n<menu type="toolbar">\n  <li>\n    <button type="menu" menu="file-menu">File</button>\n    <menu type="context" id="file-menu">\n      <menuitem label="New..." onclick="newFile()">\n      <menuitem label="Save..." onclick="saveFile()">\n    </menu>\n  </li>\n  <li>\n    <button type="menu" menu="edit-menu">Edit</button>\n    <menu type="context" id="edit-menu">\n      <menuitem label="Cut..." onclick="cutEdit()">\n      <menuitem label="Copy..." onclick="copyEdit()">\n      <menuitem label="Paste..." onclick="pasteEdit()">\n    </menu>\n  </li>\n</menu>',
    ], )


menuitem = createComponent(
    'menuitem',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/menuitem',
    docs="""
        __ **This is anexperimental technology**  
        Check the Browser compatibility table carefully before using this in
        production.
        
        The **HTML`<menuitem>` element** represents a command that a user is able to
        invoke through a popup menu. This includes context menus, as well as menus
        that might be attached to a menu button.
        
        A command can either be defined explicitly, with a textual label and optional
        icon to describe its appearance, or alternatively as an _indirect command_
        whose behavior is defined by a separate element. Commands can also optionally
        include a checkbox or be grouped to share radio buttons. (Menu items for
        indirect commands gain checkboxes or radio buttons when defined against
        elements `<input type="checkbox">` and `<input type="radio">`.)
    """,
    examples=[
        '<!-- A <div> element with a context menu -->\n<div contextmenu="popup-menu">\n\xa0 Right-click to see the adjusted context menu\n</div>\n\n<menu type="context" id="popup-menu">\n\xa0 <menuitem type="checkbox" checked>Checkbox</menuitem>\n\xa0 <hr>\n\xa0 <menuitem type="command" label="This command does nothing" icon="https://developer.cdn.mozilla.net/static/img/favicon144.png">\n\xa0 \xa0 Commands don\'t render their contents.\n\xa0 </menuitem>\n\xa0 <menuitem type="command" label="This command has javascript" onclick="alert(\'command clicked\')">\n\xa0 \xa0 Commands don\'t render their contents.\n\xa0 </menuitem>\n\xa0 <hr>\n\xa0 <menuitem type="radio" radiogroup="group1">Radio Button 1</menuitem>\n\xa0 <menuitem type="radio" radiogroup="group1">Radio Button 2</menuitem>\n</menu>',
    ], )


summary = createComponent(
    'summary',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary',
    docs="""
        The **HTML`<summary>` element** is used as a summary, caption, or legend for
        the content of a `<details>` element.
    """, )


# == Web Components ==
# Web Components is an HTML-related technology which makes it possible to,
# essentially, create and use custom elements as if it were regular HTML. In
# addition, you can create custom versions of standard HTML elements.

content = createComponent(
    'content',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/content',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **HTML`<content>` element** --an obsolete part of the Web Components suite
        of technologies--was used inside of Shadow DOM as an insertion point, and
        wasn't meant to be used in ordinary HTML It has now been replaced by the
        `<slot>` element, which creates a point in the DOM at which a shadow DOM can
        be inserted.
        
        **Note:** Though present in early draft of the specifications and implemented
        in several browsers, this element has been removed in later versions of the
        spec.
    """,
    examples=[
        '<html>\n  <head></head>\n  <body>\n\xa0 <!-- The original content accessed by <content> -->\n\xa0 <div>\n\xa0 \xa0 <h4>My Content Heading</h4>\n\xa0 \xa0 <p>My content text</p>\n\xa0 </div>\n\n\xa0 <script>\n\xa0 // Get the <div> above.\n\xa0 var myContent = document.querySelector(\'div\');\n\xa0 // Create a shadow DOM on the <div>\n\xa0 var shadowroot = myContent.createShadowRoot();\n\xa0 // Insert into the shadow DOM a new heading and \n\xa0 // part of the original content: the <p> tag.\n\xa0 shadowroot.innerHTML =\n\xa0  \'<h2>Inserted Heading</h2> <content select="p"></content>\';\n\xa0 </script>\n\n  </body>\n</html>',
    ], )


element = createComponent(
    'element',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/element',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        The **HTML`<element>` element** was part of Web Components; this element was
        intended to be used to define new custom DOM elements. It was removed in favor
        of a JavaScript-driven methodology for creating new custom elements; however,
        that technology is not mature and no browers fully implement it.
        
        **Note:** This element has been removed from the specification. See this for
        more information from the editor of the specification.
    """, )


shadow = createComponent(
    'shadow',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/shadow',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        The **HTML`<shadow>` element** --an obsolete part of the Web Components
        technology suite--was intended to be used as a shadow DOM insertion point. You
        might have used it if you have created multiple shadow roots under a shadow
        host. It is not useful in ordinary HTML.
    """,
    examples=[
        "<html>\n  <head></head>\n  <body>\n\n\xa0 <!-- This <div> will hold the shadow roots. -->\n\xa0 <div>\n\xa0 \xa0 <!-- This heading will not be displayed -->\n\xa0 \xa0 <h4>My Original Heading</h4>\n\xa0 </div>\n\n\xa0 <script>\n\xa0 \xa0 // Get the <div> above with its content\n\xa0 \xa0 var origContent = document.querySelector('div');\n\xa0 \xa0 // Create the first shadow root\n\xa0 \xa0 var shadowroot1 = origContent.createShadowRoot();\n\xa0 \xa0 // Create the second shadow root\n\xa0 \xa0 var shadowroot2 = origContent.createShadowRoot();\n\n\xa0 \xa0 // Insert something into the older shadow root\n\xa0 \xa0 shadowroot1.innerHTML =\n\xa0 \xa0 \xa0 '<p>Older shadow root inserted by\n          &lt;shadow&gt;</p>';\n\xa0 \xa0 // Insert into younger shadow root, including <shadow>.\n\xa0 \xa0 // The previous markup will not be displayed unless\n\xa0 \xa0 // <shadow> is used below.\n\xa0 \xa0 shadowroot2.innerHTML =\n\xa0 \xa0 \xa0 '<shadow></shadow> <p>Younger shadow\n       root, displayed because it is the youngest.</p>';\n\xa0 </script>\n\n  </body>\n</html>",
    ], )


slot = createComponent(
    'slot',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot',
    docs="""
        __ **This is anexperimental technology**  
        Check the Browser compatibility table carefully before using this in
        production.
        
        The **HTML`<slot>` element** --part of the Web Components technology suite--is
        a placeholder inside a web component that you can fill with your own markup,
        which lets you create separate DOM trees and present them together.
    """,
    examples=[
        '<template id="element-details-template">\n\xa0 <style>\n\xa0 details {font-family: "Open Sans Light",Helvetica,Arial}\n\xa0 .name {font-weight: bold; color: #217ac0; font-size: 120%}\n\xa0 h4 { margin: 10px 0 -8px 0; }\n\xa0 h4 span { background: #217ac0; padding: 2px 6px 2px 6px }\n\xa0 h4 span { border: 1px solid #cee9f9; border-radius: 4px }\n\xa0 h4 span { color: white }\n\xa0 .attributes { margin-left: 22px; font-size: 90% }\n\xa0 .attributes p { margin-left: 16px; font-style: italic }\n\xa0 </style>\n\xa0 <details>\n\xa0\xa0\xa0 <summary>\n\xa0\xa0\xa0\xa0\xa0 <span>\n        <code class="name">&lt;<slot name="element-name">NEED NAME</slot>&gt;</code>\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 <i class="desc"><slot name="description">NEED DESCRIPTION</slot></i>\n\xa0\xa0\xa0\xa0\xa0 </span>\n\xa0\xa0\xa0 </summary>\n\xa0\xa0\xa0 <div class="attributes">\n\xa0\xa0\xa0\xa0\xa0 <h4><span>Attributes</span></h4>\n\xa0\xa0\xa0\xa0\xa0 <slot name="attributes"><p>None</p></slot>\n\xa0\xa0\xa0 </div>\n\xa0 </details>\n\xa0 <hr>\n</template>',
        '<element-details>\n  <span slot="element-name">slot</span>\n  <span slot="description">A placeholder inside a web\n    component that users can fill with their own markup,\n    with the effect of composing different DOM trees\n    together.</span>\n  <dl slot="attributes">\n    <dt>name</dt>\n    <dd>The name of the slot.</dd>\n  </dl>\n</element-details>\n\n<element-details>\n  <span slot="element-name">template</span>\n  <span slot="description">A mechanism for holding client-\n    side content that is not to be rendered when a page is\n    loaded but may subsequently be instantiated during\n    runtime using JavaScript.</span>\n</element-details>',
    ], )


template = createComponent(
    'template',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/template',
    docs="""
        The **HTML`<template>` element** is a mechanism for holding client-side
        content that is not to be rendered when a page is loaded but may subsequently
        be instantiated during runtime using JavaScript.
        
        Think of a template as a content fragment that is being stored for subsequent
        use in the document. While the parser does process the contents of the
        **`<template>` ** element while loading the page, it does so only to ensure
        that those contents are valid; the element's contents are not rendered,
        however.
    """,
    examples=[
        '<table id="producttable">\n  <thead>\n    <tr>\n      <td>UPC_Code</td>\n      <td>Product_Name</td>\n    </tr>\n  </thead>\n  <tbody>\n    <!-- existing data could optionally be included here -->\n  </tbody>\n</table>\n\n<template id="productrow">\n  <tr>\n    <td class="record"></td>\n    <td></td>\n  </tr>\n</template>',
    ], )


# == Obsolete And Deprecated Elements ==
# **Warning:** These are old HTML elements which are deprecated and should not
# be used. **You should never use them in new projects, and should replace them
# in old projects as soon as you can.** They are listed here for informational
# purposes only.

acronym = createComponent(
    'acronym',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/acronym',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


applet = createComponent(
    'applet',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/applet',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        The HTML Applet Element (`<applet>`) identifies the inclusion of a Java
        applet.
        
        **Note** : The `<applet>` element was removed in Gecko 56 and Chrome in late
        2015. Removal is being considered in WebKit and Edge.
    """,
    notes="""
        The W3C specification does not encourage the use of `<applet>` and prefers the
        use of the `<object>` tag. Under the strict definition of HTML 4.01, this
        element is deprecated and entirely obsolete in HTML5.
        
        Was this article helpful?
        
        Yes __ No __
        
        Thank you!
    """,
    examples=[
        '<applet code="game.class" align="left" archive="game.zip" height="250" width="350">\n  <param name="difficulty" value="easy">\n  <b>Sorry, you need Java to play this game.</b>\n</applet>',
    ], )


basefont = createComponent(
    'basefont',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/basefont',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """,
    notes="""
          * HTML 3.2 supports the basefont element but only with the size attribute.
          * The strict HTML and XHTML specifications do not support this element.
          * Despite being part of transitional standards, some standards-focused browsers like Mozilla and Opera do not support this element.
          * This element can be imitated with a CSS rule on the `<body>` element.
          * XHTML 1.0 requires a trailing slash for this element: `<basefont />`.
        
        Was this article helpful?
        
        Yes __ No __
        
        Thank you!
    """, )


big = createComponent(
    'big',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/big',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


blink = createComponent(
    'blink',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/blink',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        The **HTML Blink Element** (`<blink>`) is a non-standard element causing the
        enclosed text to flash slowly.
        
        Do not use this element as it is **obsolete** and bad design practice.
        Blinking text is frowned upon by several accessibility standards and the CSS
        specification allows browsers to ignore the blink value.
    """, )


center = createComponent(
    'center',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/center',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
    """,
    notes="""
        Applying `text-align``:center` to a` ``<div>` or `<p>` element centers the
        _contents_ of those elements while leaving their overall dimensions unchanged.
    """, )


command = createComponent(
    'command',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/command',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        **Note:** The `command` element has been removed from  Gecko 24.0 in favor of
        the `<menuitem>` element. Firefox has never supported this `command` element,
        and the existing implementation of the `HTMLCommandElement` DOM interface has
        been dropped from Firefox 24.
    """,
    examples=[
        '<command type="command" label="Save" icon="icons/save.png" onclick="save()">',
    ], )


# content: see under `Web Components` above


dir = createComponent(
    'dir',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/dir',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


# element: see under `Web Components` above


font = createComponent(
    'font',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/font',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


frame = createComponent(
    'frame',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/frame',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
    """,
    examples=[
        '<frameset cols="50%,50%">\n  <frame src="https://developer.mozilla.org/en/HTML/Element/iframe" />\n  <frame src="https://developer.mozilla.org/en/HTML/Element/frame" />\n</frameset>',
    ], )


frameset = createComponent(
    'frameset',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/frameset',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
    """, )


image = createComponent(
    'image',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/image',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        **__ Non-standard**  
        This feature is non-standard and is not on a standards track. Do not use it on
        production sites facing the Web: it will not work for every user. There may
        also be large incompatibilities between implementations and the behavior may
        change in the future.
        
        The HTML `<image>` element is an obsolete remnant of an ancient version of
        HTML lost in the mists of time; use the standard `<img>` element instead.
        Seriously, the specification even literally uses the words "Don't ask" when
        describing this element.
        
        **Do not use this! __** In order to display images, use the standard `<img>`
        element.
        
        While browsers will attempt to automatically convert this into an `<img>`
        element, it won't always do so, and won't always succeed when it tries, due to
        the various ways this can happen. So just don't use it if you like your users.
    """, )


isindex = createComponent(
    'isindex',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/isindex',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """,
    examples=[
        '<head>\n  <isindex prompt="Search Document... " />\n</head>',
    ], )


keygen = createComponent(
    'keygen',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/keygen',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The HTML `<keygen>` element exists to facilitate generation of key material,
        and submission of the public key as part of an HTML form. This mechanism is
        designed for use with Web-based certificate management systems. It is expected
        that the `<keygen>` element will be used in an HTML form along with other
        information needed to construct a certificate request, and that the result of
        the process will be a signed certificate.
        
        There is currently discussion among Web browser makers whether to keep this
        feature or not. Until a decision is reached, it is better to continue to
        consider this feature as deprecated and going away.
    """, )


listing = createComponent(
    'listing',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/listing',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


marquee = createComponent(
    'marquee',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        The HTML `<marquee>` element is used to insert a scrolling area of text. You
        can control what happens when the text reaches the edges of its content area
        using its attributes.
        
        The `<marquee>` element is **obsolete** and must not be used. While some
        browsers still support it, it's not required.
    """,
    examples=[
        '<marquee>This text will scroll from right to left</marquee>\n\n<marquee direction="up">This text will scroll from bottom to top</marquee>\n\n<marquee direction="down" width="250" height="200" behavior="alternate" style="border:solid">\n  <marquee behavior="alternate">\n    This text will bounce\n  </marquee>\n</marquee>',
    ], )


multicol = createComponent(
    'multicol',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/multicol',
    docs="""
        **__ Non-standard**  
        This feature is non-standard and is not on a standards track. Do not use it on
        production sites facing the Web: it will not work for every user. There may
        also be large incompatibilities between implementations and the behavior may
        change in the future.
        
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


nextid = createComponent(
    'nextid',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/nextid',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
    """,
    examples=[
        '<HTML>\n    <HEAD>\n        <TITLE> ... whatever ... </TITLE>\n        <LINK, META, BASE, etc. as applicable for the head of this document>\n        <NEXTID N="z20">\n    </HEAD>\n    \n    <BODY>\n        <A NAME="z0" HREF="#z4">FIRST SECTION HEADING</A>\n        <A NAME="z1" HREF="#z5">SECOND SECTION HEADING</A>\n        <A NAME="z8" HREF="#z14">NEWLY INSERTED THIRD SECTION HEADING</A>\n        <A NAME="z9" HREF="#z15">NEWLY INSERTED FOURTH SECTION HEADING</A>\n        <A NAME="z2" HREF="#z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</A>\n        <A NAME="z3" HREF="#z7">ORIGINAL FOURTH (NOW SIXTH) SECTION HEADING</A>\n        <A NAME="z10" HREF="#z16">SEVENTH SECTION HEADING</A>\n        <A NAME="z11" HREF="#z17">EIGHTH SECTION HEADING</A>\n        <A NAME="z12" HREF="#z18">NINTH SECTION HEADING</A>\n        <A NAME="z13" HREF="#z19">TENTH SECTION HEADING</A>\n        <H2><A NAME="z4">FIRST SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z5">SECOND SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z14">NEWLY INSERTED THIRD SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z15">NEWLY INSERTED FOURTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z7">ORIGINAL FOURTH (NOW SIXTH) SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z16">SEVENTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z17">EIGHTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z18">NINTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z19">TENTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n    </BODY>\n</HTML>',
        '<HTML>\n    <HEAD>\n        <TITLE> ... whatever ... </TITLE>\n        <LINK, META, BASE, etc. as applicable for the head of this document>\n        <NEXTID N="z30">\n    </HEAD>\n\n    <BODY>\n        <A NAME="z0" HREF="#z4">FIRST SECTION HEADING</A>\n        <A NAME="z1" HREF="#z5">SECOND SECTION HEADING</A>\n        <A NAME="z8" HREF="#z14">NEWLY INSERTED THIRD SECTION HEADING</A>\n        <A NAME="z9" HREF="#z15">NEWLY INSERTED FOURTH SECTION HEADING</A>\n        <A NAME="z2" HREF="#z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</A>\n        <A NAME="z10" HREF="#z16">SEVENTH (NOW SIXTH) SECTION HEADING</A>\n        <A NAME="z11" HREF="#z17">EIGHTH (NOW SEVENTH) SECTION HEADING</A>\n        <A NAME="z12" HREF="#z18">NINTH (NOW EIGHTH) SECTION HEADING</A>\n        <A NAME="z20" HREF="#z25">NEW NINTH SECTION HEADING</A>\n        <A NAME="z21" HREF="#z26">NEW TENTH SECTION HEADING</A>\n        <A NAME="z22" HREF="#z27">NEW ELEVENTH SECTION HEADING</A>\n        <A NAME="e23" HREF="#z28">NEW TWELFTH SECTION HEADING</A>\n        <H2><A NAME="z4">FIRST SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z5">SECOND SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z14">NEWLY INSERTED THIRD SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z15">NEWLY INSERTED FOURTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z16">SEVENTH (NOW SIXTH) SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z17">EIGHTH (NOW SEVENTH) SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z18">NINTH (NOW EIGHTH) SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z25">NEW NINTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z26">NEW TENTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z27">NEW ELENENTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n        <H2><A NAME="z28">NEW TWELFTH SECTION HEADING</A></H1><P> ... whatever ... </P>\n    </BODY>\n</HTML>',
    ], )


noembed = createComponent(
    'noembed',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/noembed',
    docs="""
        **__ Non-standard**  
        This feature is non-standard and is not on a standards track. Do not use it on
        production sites facing the Web: it will not work for every user. There may
        also be large incompatibilities between implementations and the behavior may
        change in the future.
        
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The `**< noembed>**` element is a deprecated and non-standard way to provide
        alternative, or "fallback", content for browsers that do not support the
        `<embed>` element or do not support embedded content an author wishes to use.
        This element was deprecated in HTML 4.01 and above in favor of `<object>`.
        Fallback content should be inserted between the opening and closing `<object>`
        tags.
        
        While this element currently still works in many browsers, it has been
        deprecated and should not be used. Use `<object>` instead.
    """, )


plaintext = createComponent(
    'plaintext',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/plaintext',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


# shadow: see under `Web Components` above


spacer = createComponent(
    'spacer',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/spacer',
    docs="""
        **__ Non-standard**  
        This feature is non-standard and is not on a standards track. Do not use it on
        production sites facing the Web: it will not work for every user. There may
        also be large incompatibilities between implementations and the behavior may
        change in the future.
        
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
        
        **`<spacer>`** is an obsolete HTML element which allowed insertion of empty
        spaces on pages. It was devised by Netscape to accomplish the same effect as a
        single-pixel layout image, which was something web designers used to use to
        add white spaces to web pages without actually using an image. However,
        `<spacer>` no longer supported by any major browser and the same effects can
        now be achieved using simple CSS.
        
        Firefox, which is the descendant of Netscape's browsers, removed support for
        `<spacer>` in version 4.
    """, )


strike = createComponent(
    'strike',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/strike',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


tt = createComponent(
    'tt',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/tt',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """,
    notes="""
          * A CSS rule can be defined for the `tt` selector to override the browser's default font face. Preferences set by the user might take precedence over the specified CSS.
          * Although this element was not deprecated in the HTML 4.01 specification, its use is discouraged in favor of style sheets.
    """, )


xmp = createComponent(
    'xmp',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/xmp',
    docs="""
        **__ Obsolete**  
        This feature is obsolete. Although it may still work in some browsers, its use
        is discouraged since it could be removed at any time. Try to avoid using it.
    """, )


