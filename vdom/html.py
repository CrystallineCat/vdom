# -*- coding: utf-8 -*-
from vdom.core import Component

# From https://developer.mozilla.org/en-US/docs/Web/HTML/Element


# == Main root ==
class html(Component):
    """
        The **HTML <html> element** represents the root (top-level element) of
        an HTML document, so it is also referred to as the *root element*. All
        other elements must be descendants of this element.
        
        Examples::
        
            <article>
            
              ...
              ...
            
            </article>
        
        Notes:
        
        
    """



# == Document metadata ==
# Metadata contains information about the page. This includes information about
# styles, scripts and data to help software (search engines, browsers, etc.) use
# and render the page. Metadata for styles and scripts may be defined in the
# page or link to another file that has the information.
class link(Component):
    """
        The **HTML <link> element** specifies relationships between the
        current document and an external resource. Possible uses for this
        element include defining a relational framework for navigation. This
        element is most used to link to style sheets.
        
        Examples::
        
            <article><link href="style.css" rel="stylesheet">
            <link href="default.css" rel="stylesheet" title="Default Style">
            <link href="fancy.css" rel="alternate stylesheet" title="Fancy">
            <link href="basic.css" rel="alternate stylesheet" title="Basic">
            <script>
            function sheetLoaded() {
              // Do something interesting; the sheet has been loaded
            }
            
            function sheetError() {
              console.log("An error occurred loading the stylesheet!");
            }
            </script>
            
            <link rel="stylesheet" href="mystylesheet.css" onload="sheetLoaded()" onerror="sheetError()">
            </article>
        
        Notes:
        
            * A ``<link>`` tag can occur either in the head element or in the body
            element (or both), depending on whether it has a link type that is
            **body-ok**. For example, the ``stylesheet`` link type is body-ok, and
            therefore a ``<link rel="stylesheet">`` is permitted in the body.
            
            * HTML 3.2 defines only the **href**, **rel**, **rev**, and **title**
            attributes for the link element.
            
            * HTML 2 defines the **href**, **methods**, **rel**, **rev**,
            **title**, and **urn** attributes for the ``<link>`` element. The
            **methods** and **urn** attributes were later removed from the
            specifications.
            
            * The HTML and XHTML specifications define event handlers for the
            ``<link>`` element, but it is unclear how they would be used.
            
            * Under XHTML 1.0, empty elements such as ``<link>`` require a
            trailing slash: ``<link />``.
    """

class meta(Component):
    """
        The **HTML <meta> element** represents metadata that cannot be
        represented by other HTML meta-related elements, like ``<base>``,
        ``<link>``, ``<script>``, ``<style>`` or ``<title>``.
        
        Examples::
        
            <article><meta charset="utf-8">
            
            <!-- Redirect page after 3 seconds -->
            <meta http-equiv="refresh" content="3;url=https://www.mozilla.org">
            </article>
        
        Notes:
        
            Depending on the attributes set, the kind of metadata can be one of
            the following:* If ``name`` is set, it is *document-level* *metadata*,
            applying to the whole page.
            
            * If ``http-equiv`` is set, it is a *pragma directive* — information
            normally given by the web server about how the web page is served.
            
            * If ``charset`` is set, it is a *charset declaration* — the character
            encoding used by the webpage.
            
            * If ``itemprop`` is set, it is *user-defined metadata* — transparent
            for the user-agent as the semantics of the metadata is user-specific.
            **
    """

class style(Component):
    """
        The **HTML <style> element** contains style information for a
        document, or part of a document. By default, the style instructions
        written inside that element are expected to be CSS.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Sectioning root ==
class body(Component):
    """
        The **HTML <body> Element** represents the content of an
        HTML document. There can be only one ``<body>`` element in a document.
        
        Examples::
        
            <article>
              
                <title>Document title</title>
              
              
                <p>This is a paragraph</p>
              
            
            </article>
        
        Notes:
        
        
    """



# == Content sectioning ==
# Content sectioning elements allow you to organize the document content into
# logical pieces. Use the sectioning elements to create a broad outline for your
# page content, including header and footer navigation, and heading elements to
# identify sections of content.
class address(Component):
    """
        The **HTML <address> element** supplies contact information for its
        nearest ``<article>`` or ``<body>`` ancestor; in the latter case, it
        applies to the whole document.
        
        Examples::
        
            <article>  <address>
                You can contact author at <a href="http://www.somedomain.com/contact">www.somedomain.com</a>.<br>
                If you see any bugs, please <a href="mailto:webmaster@somedomain.com">contact webmaster</a>.<br>
                You may also want to visit us:<br>
                Mozilla Foundation<br>
                1981 Landings Drive<br>
                Building K<br>
                Mountain View, CA 94043-0801<br>
                USA
              </address>
            </article>
        
        Notes:
        
        
    """

class article(Component):
    """
        The **HTML <article> element** represents a self-contained composition
        in a document, page, application, or site, which is intended to be
        independently distributable or reusable (e.g., in syndication).
        Examples include: a forum post, a magazine or newspaper article, or a
        blog entry.
        
        Examples::
        
            <article><article class="film_review">
            &#160; <header>
            &#160; &#160; <h2>Jurassic Park</h2>
            &#160; </header>
            &#160; <section class="main_review">
            &#160; &#160; <p>Dinos were great!</p>
            &#160; </section>
            &#160; <section class="user_reviews">
            &#160; &#160; <article class="user_review">
            &#160; &#160; &#160; <p>Way too scary for me.</p>
            &#160; &#160; &#160; <footer>
            &#160; &#160; &#160; &#160; <p>
            &#160; &#160; &#160; &#160; &#160; Posted on
                      <time datetime="2015-05-16 19:00">May 16</time>
                      by Lisa.
            &#160; &#160; &#160; &#160; </p>
            &#160; &#160; &#160; </footer>
            &#160; &#160; </article>
            &#160; &#160; <article class="user_review">
            &#160; &#160; &#160; <p>I agree, dinos are my favorite.</p>
            &#160; &#160; &#160; <footer>
            &#160; &#160; &#160; &#160; <p>
            &#160; &#160; &#160; &#160; &#160; Posted on
                      <time datetime="2015-05-17 19:00">May 17</time>
                      by Tom.
            &#160; &#160; &#160; &#160; </p>
            &#160; &#160; &#160; </footer>
            &#160; &#160; </article>
            &#160; </section>
            &#160; <footer>
            &#160; &#160; <p>
            &#160; &#160; &#160; Posted on
                  <time datetime="2015-05-15 19:00">May 15</time>
                  by Staff.
            &#160; &#160; </p>
            &#160; </footer>
            </article>
            </article>
        
        Notes:
        
        
    """

class aside(Component):
    """
        The **HTML <aside> element** represents a section of a document with
        content connected tangentially to the main content of the document
        (often presented as a sidebar).
        
        Examples::
        
            <article><article>
              <p>
                The Disney movie <cite>The Little Mermaid</cite> was
                first released to theatres in 1989.
              </p>
              <aside>
                <p>
                  The movie earned $87 million during its initial release.
                </p>
              </aside>
              <p>
                More info about the movie...
              </p>
            </article></article>
        
        Notes:
        
        
    """

class footer(Component):
    """
        The **HTML <footer> element** represents a footer for its nearest
        sectioning content or sectioning root element. A footer typically
        contains information about the author of the section, copyright data
        or links to related documents.
        
        Examples::
        
            <article><footer>
              Some copyright info or perhaps some author
              info for an &lt;article&gt;?
            </footer> 
            </article>
        
        Notes:
        
        
    """

class h1(Component):
    """
        The **HTML <h1>–<h6> elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the
        lowest.
        
        Examples::
        
            <article><h1>Heading level 1</h1>
            <h2>Heading level 2</h2>
            <h3>Heading level 3</h3>
            <h4>Heading level 4</h4>
            <h5>Heading level 5</h5>
            <h6>Heading level 6</h6>
            <h1>Heading elements</h1>
            <h2>Summary</h2>
            <p>Some text here...</p>
            
            <h2>Examples</h2>
            <h3>Example 1</h3>
            <p>Some text here...</p>
            
            <h3>Example 2</h3>
            <p>Some text here...</p>
            
            <h2>See also</h2>
            <p>Some text here...</p>
            </article>
        
        Notes:
        
        
    """

class h2(Component):
    """
        The **HTML <h1>–<h6> elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the
        lowest.
        
        Examples::
        
            <article><h1>Heading level 1</h1>
            <h2>Heading level 2</h2>
            <h3>Heading level 3</h3>
            <h4>Heading level 4</h4>
            <h5>Heading level 5</h5>
            <h6>Heading level 6</h6>
            <h1>Heading elements</h1>
            <h2>Summary</h2>
            <p>Some text here...</p>
            
            <h2>Examples</h2>
            <h3>Example 1</h3>
            <p>Some text here...</p>
            
            <h3>Example 2</h3>
            <p>Some text here...</p>
            
            <h2>See also</h2>
            <p>Some text here...</p>
            </article>
        
        Notes:
        
        
    """

class h3(Component):
    """
        The **HTML <h1>–<h6> elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the
        lowest.
        
        Examples::
        
            <article><h1>Heading level 1</h1>
            <h2>Heading level 2</h2>
            <h3>Heading level 3</h3>
            <h4>Heading level 4</h4>
            <h5>Heading level 5</h5>
            <h6>Heading level 6</h6>
            <h1>Heading elements</h1>
            <h2>Summary</h2>
            <p>Some text here...</p>
            
            <h2>Examples</h2>
            <h3>Example 1</h3>
            <p>Some text here...</p>
            
            <h3>Example 2</h3>
            <p>Some text here...</p>
            
            <h2>See also</h2>
            <p>Some text here...</p>
            </article>
        
        Notes:
        
        
    """

class h4(Component):
    """
        The **HTML <h1>–<h6> elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the
        lowest.
        
        Examples::
        
            <article><h1>Heading level 1</h1>
            <h2>Heading level 2</h2>
            <h3>Heading level 3</h3>
            <h4>Heading level 4</h4>
            <h5>Heading level 5</h5>
            <h6>Heading level 6</h6>
            <h1>Heading elements</h1>
            <h2>Summary</h2>
            <p>Some text here...</p>
            
            <h2>Examples</h2>
            <h3>Example 1</h3>
            <p>Some text here...</p>
            
            <h3>Example 2</h3>
            <p>Some text here...</p>
            
            <h2>See also</h2>
            <p>Some text here...</p>
            </article>
        
        Notes:
        
        
    """

class h5(Component):
    """
        The **HTML <h1>–<h6> elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the
        lowest.
        
        Examples::
        
            <article><h1>Heading level 1</h1>
            <h2>Heading level 2</h2>
            <h3>Heading level 3</h3>
            <h4>Heading level 4</h4>
            <h5>Heading level 5</h5>
            <h6>Heading level 6</h6>
            <h1>Heading elements</h1>
            <h2>Summary</h2>
            <p>Some text here...</p>
            
            <h2>Examples</h2>
            <h3>Example 1</h3>
            <p>Some text here...</p>
            
            <h3>Example 2</h3>
            <p>Some text here...</p>
            
            <h2>See also</h2>
            <p>Some text here...</p>
            </article>
        
        Notes:
        
        
    """

class h6(Component):
    """
        The **HTML <h1>–<h6> elements** represent six levels of section
        headings. ``<h1>`` is the highest section level and ``<h6>`` is the
        lowest.
        
        Examples::
        
            <article><h1>Heading level 1</h1>
            <h2>Heading level 2</h2>
            <h3>Heading level 3</h3>
            <h4>Heading level 4</h4>
            <h5>Heading level 5</h5>
            <h6>Heading level 6</h6>
            <h1>Heading elements</h1>
            <h2>Summary</h2>
            <p>Some text here...</p>
            
            <h2>Examples</h2>
            <h3>Example 1</h3>
            <p>Some text here...</p>
            
            <h3>Example 2</h3>
            <p>Some text here...</p>
            
            <h2>See also</h2>
            <p>Some text here...</p>
            </article>
        
        Notes:
        
        
    """

class header(Component):
    """
        The **HTML <header> element** represents introductory content,
        typically a group of introductory or navigational aids. It may contain
        some heading elements but also other elements like a logo, a search
        form, an author name, and so on.
        
        Examples::
        
            <article><header>
            &#160; <h1>Main Page Title</h1>
            &#160; <img src="mdn-logo-sm.png" alt="MDN logo">
            </header> 
            </article>
        
        Notes:
        
        
    """

class hgroup(Component):
    """
        ** **This is an experimental technology**
        
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change
        in future versions of browsers as the specification changes.The **HTML
        <hgroup> element** represents a multi-level heading for a section of a
        document. It groups a set of ``<h1>–<h6>`` elements.
        
        Examples::
        
            <article><hgroup id="document-title">
              <h1>HTML</h1>
              <h2>Living Standard &#8212; Last Updated 12 August 2016</h2>
            </hgroup>
            </article>
        
        Notes:
        
        
    """

class nav(Component):
    """
        The **HTML <nav> element** represents a section of a page whose
        purpose is to provide navigation links, either within the current
        document or to other documents. Common examples of navigation sections
        are menus, tables of contents, and indexes.
        
        Examples::
        
            <article><nav class="menu">
              <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
              </ul>
            </nav>
            </article>
        
        Notes:
        
        
    """

class section(Component):
    """
        The **HTML <section> element** represents a standalone section of
        functionality contained within an HTML document, typically with a
        heading, which doesn't have a more specific semantic element to
        represent it.
        
        As an example, a navigation menu should be wrapped in a ``<nav>``
        element, but a list of search results and a map display and its
        controls don't have specific elements, and could be put inside a
        ``<section>``.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Text content ==
# Use HTML text content elements to organize blocks or sections of content
# placed between the opening ``<body>`` and closing ``</body>`` tags. Important
# for accessibility and SEO, these elements identify the purpose or structure of
# that content.
class blockquote(Component):
    """
        The **HTML <blockquote> Element** (or *HTML Block Quotation Element*)
        indicates that the enclosed text is an extended quotation. Usually,
        this is rendered visually by indentation (see Notes for how to change
        it). A URL for the source of the quotation may be given using the
        **cite** attribute, while a text representation of the source can be
        given using the ``<cite>`` element.
        
        Examples::
        
            <article><blockquote cite="http://developer.mozilla.org">
              <p>This is a quotation taken from
              the Mozilla Developer Center.</p>
            </blockquote>
            </article>
        
        Notes:
        
            To change ``<blockquote>`` indent, use CSS ``margin`` property.For
            short quotes use the ``<q>`` element.
    """

class dd(Component):
    """
        The **HTML <dd> element** indicates the description of a term in a
        description list (``<dl>``).
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class div(Component):
    """
        The **HTML <div> element** is the generic container for flow content
        and does not inherently represent anything. Use it to group elements
        for purposes such as styling (using the ``class`` or ``id``
        attributes), marking a section of a document in a different language
        (using the ``lang`` attribute), and so on.
        
        Examples::
        
            <article><div>
              <p>Any kind of content here. Such as
              &lt;p&gt;, &lt;table&gt;. You name it!</p>
            </div> 
            </article>
        
        Notes:
        
        
    """

class dl(Component):
    """
        The **HTML <dl> **element represents a description list.** **The
        element encloses a list of groups of terms and descriptions. Common
        uses for this element are to implement a glossary or to display
        metadata (a list of key-value pairs).
        
        Examples::
        
            <article><dl>
              <dt>Firefox</dt>
              <dd>
                A free, open source, cross-platform,
                graphical web browser developed by the
                Mozilla Corporation and hundreds of
                volunteers.
              </dd>
            
              <!-- Other terms and descriptions -->
            </dl>
            <dl>
              <dt>Firefox</dt>
              <dt>Mozilla Firefox</dt>
              <dt>Fx</dt>
              <dd>
                A free, open source, cross-platform,
                graphical web browser developed by the
                Mozilla Corporation and hundreds of
                volunteers.
              </dd>
            
              <!-- Other terms and descriptions -->
            </dl>
            <dl>
              <dt>Firefox</dt>
              <dd>
                A free, open source, cross-platform,
                graphical web browser developed by the
                Mozilla Corporation and hundreds of
                volunteers.
              </dd>
              <dd>
                The Red Panda also known as the Lesser
                Panda, Wah, Bear Cat or Firefox, is a
                mostly herbivorous mammal, slightly larger
                than a domestic cat (60 cm long).
              </dd>
            
              <!-- Other terms and descriptions -->
            </dl>
            <dl>
              <dt>Name</dt>    
              <dd>Godzilla</dd>
              <dt>Born</dt>
              <dd>1952</dd>
              <dt>Birthplace</dt>
              <dd>Japan</dd>
              <dt>Color</dt>
              <dd>Green</dd>
            </dl>
            <dl>
              <div>
                <dt>Name</dt>
                <dd>Godzilla</dd>
              </div>
              <div>
                <dt>Born</dt>
                <dd>1952</dd>
              </div>
              <div>
                <dt>Birthplace</dt>
                <dd>Japan</dd>
              </div>
              <div>
                <dt>Color</dt>
                <dd>Green</dd>
              </div>
            </dl>
            </article>
        
        Notes:
        
            Do not use this element (nor ``<ul>`` elements) to merely create
            indentation on a page. Although it works, this is a bad practice and
            obscures the meaning of description lists.To change the indentation of
            a description term, use the CSS ``margin`` property.
    """

class dt(Component):
    """
        The **HTML <dt> element** identifies a term in a description list.
        This element can occur only as a child element of a ``<dl>``. It is
        usually followed by a ``<dd>`` element; however, multiple ``<dt>``
        elements in a row indicate several terms that are all defined by the
        immediate next ``<dd>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class figcaption(Component):
    """
        The **HTML <figcaption> element** represents a caption or a legend
        associated with a figure or an illustration described by the rest of
        the data of the ``<figure>`` element which is its immediate ancestor.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class figure(Component):
    """
        The **HTML <figure> element** represents self-contained content,
        frequently with a caption (``<figcaption>``), and is typically
        referenced as a single unit.
        
        Examples::
        
            <article><!-- Just a figure -->
            <figure>
              <img src="https://developer.cdn.mozilla.net/media/img/mdn-logo-sm.png" alt="An awesome picture">
            </figure>
            <p></p>
            <!-- Figure with figcaption -->
            <figure>
              <img src="https://developer.cdn.mozilla.net/media/img/mdn-logo-sm.png" alt="An awesome picture">	
              <figcaption>Fig1. MDN Logo</figcaption>
            </figure>
            <p></p>
            <figure>
              <figcaption>Get browser details
            using navigator</figcaption>
              <pre>
            function NavigatorExample() {
              var txt;
              txt = "Browser CodeName: " + navigator.appCodeName;
              txt+= "Browser Name: " + navigator.appName;
              txt+= "Browser Version: " + navigator.appVersion ;
              txt+= "Cookies Enabled: " + navigator.cookieEnabled;
              txt+= "Platform: " + navigator.platform;
              txt+= "User-agent header: " + navigator.userAgent;
            }            
              </pre>
            </figure>
            <figure>
              <figcaption><cite>Edsger Dijkstra :-</cite></figcaption>
              <p>"If debugging is the process of removing software bugs,
              <br>
              then programming must be the process of putting them in"</p>
            </figure>
            </article>
        
        Notes:
        
        
    """

class hr(Component):
    """
        The **HTML <hr> element** represents a thematic break between
        paragraph-level elements (for example, a change of scene in a story,
        or a shift of topic with a section). In previous versions of HTML, it
        represented a horizontal rule. It may still be displayed as a
        horizontal rule in visual browsers, but is now defined in semantic
        terms, rather than presentational terms.
        
        Examples::
        
            <article><p>
              This is the first paragraph of text.
              This is the first paragraph of text.
              This is the first paragraph of text.
              This is the first paragraph of text.
            </p>
            
            <hr>
            
            <p>
              This is the second paragraph of text.
              This is the second paragraph of text.
              This is the second paragraph of text.
              This is the second paragraph of text.
            </p></article>
        
        Notes:
        
        
    """

class li(Component):
    """
        The **HTML <li> element** is used to represent an item in a list. It
        must be contained in a parent element: an ordered list (``<ol>``), an
        unordered list (``<ul>``), or a menu (``<menu>``). In menus and
        unordered lists, list items are usually displayed using bullet points.
        In ordered lists, they are usually displayed with an ascending counter
        on the left, such as a number or letter.
        
        Examples::
        
            <article><ol>
                <li>first item</li>
                <li>second item</li>
                <li>third item</li>
            </ol>	
            <ol type="I">
                <li value="3">third item</li>
                <li>fourth item</li>
                <li>fifth item</li>
            </ol>	
            <ul>
                <li>first item</li>
                <li>second item</li>
                <li>third item</li>
            </ul></article>
        
        Notes:
        
        
    """

class main(Component):
    """
        The **HTML <main> element** represents the main content of the
        ``<body>`` of a document, portion of a document, or application. The
        main content area consists of content that is directly related to, or
        expands upon the central topic of, a document or the central
        functionality of an application.
        
        You can use multiple ``<main>`` elements within the same page when it
        makes sense to do so. For instance, if you have a page presenting
        multiple articles (each inside an ``<article>`` element, each of which
        has some extra material within (such as toolbars for editing, ads, and
        so forth), it may make sense to include a ``<main>`` element within
        each article to identify the primary contents of that specific
        article.
        
        Examples::
        
            <article><!-- other content -->
            
            <main>
              <h1>Apples</h1>
              <p>The apple is the pomaceous fruit of the apple tree.</p>
              
              <article>
                <h2>Red Delicious</h2>
                <p>These bright red apples are the most common found in many
                supermarkets.</p>
                <p>... </p>
                <p>... </p>
              </article>
            
              <article>
                <h2>Granny Smith</h2>
                <p>These juicy, green apples make a great filling for
                apple pies.</p>
                <p>... </p>
                <p>... </p>
              </article>
            </main>
            
            <!-- other content --></article>
        
        Notes:
        
        
    """

class ol(Component):
    """
        The **HTML <ol> element** represents an ordered list of items,
        typically rendered as a numbered list.
        
        Examples::
        
            <article><ol>
              <li>first item</li>
              <li>second item</li>
              <li>third item</li>
            </ol>
            <ol start="7">
              <li>first item</li>
              <li>second item</li>
              <li>third item</li>
            </ol>
            <ol>
              <li>first item</li>
              <li>second item  <!-- closing </li> tag not here! -->
                <ol>
                  <li>second item first subitem</li>
                  <li>second item second subitem</li>
                  <li>second item third subitem</li>
                </ol>
              </li>            <!-- Here's the closing </li> tag -->
              <li>third item</li>
            </ol>
            <ol>
              <li>first item</li>
              <li>second item  <!-- closing </li> tag not here! -->
                <ul>
                  <li>second item first subitem</li>
                  <li>second item second subitem</li>
                  <li>second item third subitem</li>
                </ul>
              </li>            <!-- Here's the closing </li> tag -->
              <li>third item</li>
            </ol>
            </article>
        
        Notes:
        
        
    """

class p(Component):
    """
        The **HTML <p> element** represents a paragraph of text. Paragraphs
        are usually represented in visual media as blocks of text that are
        separated from adjacent blocks by vertical blank space and/or first-
        line indentation. Paragraphs are block-level elements.
        
        Examples::
        
            <article><p>This is the first paragraph of text.
              This is the first paragraph of text.
              This is the first paragraph of text.
              This is the first paragraph of text.</p>
            <p>This is the second paragraph.
             This is the second paragraph.
             This is the second paragraph.
             This is the second paragraph.</p>
            </article>
        
        Notes:
        
        
    """

class pre(Component):
    """
        The **HTML <pre> element** represents preformatted text. Text within
        this element is typically displayed in a non-proportional
        ("monospace") font exactly as it is laid out in the file. Whitespace
        inside this element is displayed as typed.
        
        Examples::
        
            <article><!-- Some example CSS code -->
            <pre>
            body {
              color:red;
            }
            </pre> 
            </article>
        
        Notes:
        
        
    """

class ul(Component):
    """
        The **HTML <ul> element** represents an unordered list of items,
        typically rendered as a bulleted list.
        
        Examples::
        
            <article><ul>
              <li>first item</li>
              <li>second item</li>
              <li>third item</li>
            </ul>
            <ul>
              <li>first item</li>
              <li>second item     
              <!-- Look, the closing </li> tag is not placed here! -->
                <ul>
                  <li>second item first subitem</li>
                  <li>second item second subitem
                  <!-- Same for the second nested unordered list! -->
                    <ul>
                      <li>second item second subitem first sub-subitem</li>
                      <li>second item second subitem second sub-subitem</li>
                      <li>second item second subitem third sub-subitem</li>
                    </ul>
                  </li> <!-- Closing </li> tag for the li that
                              contains the third unordered list -->
                  <li>second item third subitem</li>
                </ul>
              <!-- Here is the closing </li> tag -->
              </li>
              <li>third item</li>
            </ul>
            <ul>
              <li>first item</li>
              <li>second item
              <!-- Look, the closing </li> tag is not placed here! -->
                <ol>
                  <li>second item first subitem</li>
                  <li>second item second subitem</li>
                  <li>second item third subitem</li>
                </ol>
              <!-- Here is the closing </li> tag -->
              </li>
              <li>third item</li>
            </ul>
            </article>
        
        Notes:
        
        
    """



# == Inline text semantics ==
# Use the HTML inline text semantic to define the meaning, structure, or style
# of a word, line, or any arbitrary piece of text.
class a(Component):
    """
        The **HTML <a> element** (or *anchor* element) creates a hyperlink to
        other web pages, files, locations within the same page, email
        addresses, or any other URL.
        
        Examples::
        
            <article><!-- anchor linking to external file -->
            <a href="https://www.mozilla.com/">
            External Link
            </a>
            <!-- links to element on this page with id="attr-href" -->
            <a href="#attr-href">
            Description of Same-Page Links
            </a> 
            <a href="https://developer.mozilla.org/en-US/" target="_blank">
              <img src="https://mdn.mozillademos.org/files/6851/mdn_logo.png" alt="MDN logo">
            </a>
            <a href="mailto:nowhere@mozilla.org">Send email to nowhere</a><a href="tel:+491570156">+49 157 0156</a></article>
        
        Notes:
        
            HTML 3.2 defines only the ``name``, ``href``, ``rel``, ``rev``, and
            ``title`` attributes.Accessibility recommendations
            =============================
            
            Anchor tags are often abused with the ``onclick`` event to create
            pseudo-buttons by setting **href** to ``"#"`` or
            ``"javascript:void(0)"`` to prevent the page from refreshing. These
            values cause unexpected behavior when copying/dragging links, opening
            links in a new tabs/windows, bookmarking, and when JavaScript is still
            downloading, errors out, or is disabled. This also conveys incorrect
            semantics to assistive technologies (e.g., screen readers). In these
            cases, it is recommended to use a ``<button>`` instead. In general you
            should only use an anchor for navigation using a proper URL. 
            
            Clicking and focus ==================
            
            Whether clicking on an ``<a>`` causes it to become focused varies by
            browser and OS.
    """

class abbr(Component):
    """
        The **HTML <abbr> element** represents an abbreviation and optionally
        provides a full description for it. If present, the ``title``
        attribute must contain this full description and nothing else.
        
        Examples::
        
            <article><abbr title="Internationalization">I18N</abbr></article>
        
        Notes:
        
        
    """

class b(Component):
    """
        The **HTML <b> element** represents a span of text stylistically
        different from normal text, without conveying any special importance
        or relevance, and that is typically rendered in boldface.
        
        Examples::
        
            <article><p>
              This article describes several <b class="keywords">text-level</b> elements.
              It explains their usage in an <b class="keywords">HTML</b> document.   
            </p>
            Keywords are displayed with the default style of the <b>
            element, likely in bold.
            </b></article>
        
        Notes:
        
        
    """

class bdi(Component):
    """
        The **HTML <bdi> element** (*bidirectional isolation*) isolates a span
        of text that might be formatted in a different direction from other
        text outside it.This element is useful when embedding text with an
        unknown directionality, from a database for example, inside text with
        a fixed directionality.
        
        Examples::
        
            <article><p dir="ltr">This arabic word <bdi>ARABIC_PLACEHOLDER</bdi>
            is automatically displayed right-to-left.</p>
            </article>
        
        Notes:
        
        
    """

class bdo(Component):
    """
        The **HTML <bdo> element** (*bidirectional override*) is used to
        override the current directionality of text. It causes the
        directionality of the characters to be ignored in favor of the
        specified directionality.
        
        Examples::
        
            <article><!-- Switch text direction -->
            <p>This text will go left to right.</p>
            <p><bdo dir="rtl">This text will go right
            to left.</bdo></p>
            </article>
        
        Notes:
        
            The HTML 4 specification did not specify events for this element; they
            were added in XHTML. This is most likely an oversight.
    """

class br(Component):
    """
        The **HTML <br> element** produces a line break in text (carriage-
        return). It is useful for writing a poem or an address, where the
        division of lines is significant.
        
        Examples::
        
            <article>Mozilla Foundation<br>
            1981 Landings Drive<br>
            Building K<br>
            Mountain View, CA 94043-0801<br>
            USA
            </article>
        
        Notes:
        
            Do not use ``<br>`` to increase the gap between lines of text; use the
            CSS ``margin`` property or the ``<p>`` element.
    """

class cite(Component):
    """
        The **HTML <cite> element** represents a reference to a creative work.
        It must include the title of a work or a URL reference, which may be
        in an abbreviated form according to the conventions used for the
        addition of citation metadata.
        
        Examples::
        
            <article>More information can be found in <cite>[ISO-0000]</cite>.</article>
        
        Notes:
        
        
    """

class code(Component):
    """
        The **HTML <code> element** represents a fragment of computer code. By
        default, it is displayed in the browser's default monospace font.
        
        Examples::
        
            <article><p>This is how we declare a Javascript variable:<br>
            <code>var i = 0;</code>
            </p>
            </article>
        
        Notes:
        
            A CSS rule can be defined for the ``code`` selector to override the
            browser's default font face. Preferences set by the user might take
            precedence over the specified CSS.
    """

class data(Component):
    """
        The **HTML <data> element** links a given content with a machine-
        readable translation. If the content is time- or date-related, the
        ``<time>`` element must be used.
        
        Examples::
        
            <article><p>New Products</p>
            <ul>
             <li><data value="398">Mini Ketchup</data></li>
             <li><data value="399">Jumbo Ketchup</data></li>
             <li><data value="400">Mega Jumbo Ketchup</data></li>
            </ul>
            </article>
        
        Notes:
        
        
    """

class dfn(Component):
    """
        The **HTML <dfn> element** represents the defining instance of a term.
        
        Examples::
        
            <article><!-- Define "The Internet" -->
            <p><dfn id="def-internet">The Internet</dfn> is a global
            system of interconnected networks that use the Internet
            Protocol Suite (TCP/IP) to serve billions of users
            worldwide.</p>
            <dl>
              <!-- Define "World-Wide Web" and reference
                   definition for "the Internet" -->
              <dt>
                <dfn>
                  <abbr title="World-Wide Web">WWW</abbr>
                </dfn>
              </dt>
              <dd>The World-Wide Web (WWW) is a system of
              interlinked hypertext documents accessed on
              <a href="#def-internet">the Internet</a>.</dd>
            </dl>
            </article>
        
        Notes:
        
        
    """

class em(Component):
    """
        The **HTML <em> element** marks text that has stress emphasis. The
        ``<em>`` element can be nested, with each level of nesting indicating
        a greater degree of emphasis.
        
        Examples::
        
            <article><p>
              In HTML 5, what was previously called
              <em>block-level</em> content is now called
              <em>flow</em> content.
            </p></article>
        
        Notes:
        
        
    """

class i(Component):
    """
        The **HTML <i> element** represents a range of text that is set off
        from the normal text for some reason, for example, technical terms,
        foreign language phrases, or fictional character thoughts. It is
        typically displayed in italic type.
        
        Examples::
        
            <article><p>The Latin phrase <i class="latin">Veni, vidi, vici</i> is often
            mentioned in music, art, and literature.</p>
            </article>
        
        Notes:
        
            In earlier versions of the HTML specification, the ``<i>`` tag was
            merely a presentational element used to display text in italics, much
            like the ``<b>`` tag was used to display text in bold letters. This is
            no longer true, as these tags now define semantics rather than
            typographic appearance. The ``<i>`` tag should represent a range of
            text with a different semantic meaning whose typical typographic
            representation is italicized. This means a browser will typically
            still display its contents in italic type, but is, by definition, no
            longer required to.Use this element only when there is not a more
            appropriate semantic element. For example:
            
            * Use ``<em>`` to indicate emphasis or stress.
            
            * Use ``<strong>`` to indicate importance.
            
            * Use ``<mark>`` to indicate relevance.
            
            * Use ``<cite>`` to mark the name of a work, such as a book, play, or
            song.
            
            * Use ``<dfn>`` to mark the defining instance of a term.
            
            It is a good idea to use the **class** attribute to identify why the
            element is being used, so that if the presentation needs to change at
            a later date, it can be done selectively with style sheets.
    """

class kbd(Component):
    """
        The **HTML <kbd> element** represents user input and produces an
        inline element displayed in the browser's default monospace font.
        
        Examples::
        
            <article><p>Type the following in the Run dialog:
              <kbd>cmd</kbd><br>Then click the OK button.</p>
            
            <p>Save the document by pressing
              <kbd>Ctrl</kbd> + <kbd>S</kbd></p></article>
        
        Notes:
        
            A CSS rule can be defined for the ``kbd`` selector to override the
            browser's default font face. Preferences set by the user might take
            precedence over the specified CSS.When the ``<kbd>`` element is nested
            inside a ``<samp>`` element, it represents the input as it was echoed
            by the system.
            
            When the ``<kbd>`` element *contains* a ``<samp>`` element, it
            represents input based on system output, for example invoking a menu
            item.
            
            When the ``<kbd>`` element is nested inside another ``<kbd>`` element,
            it represents an actual key or other single unit of input as
            appropriate for the input mechanism.
    """

class mark(Component):
    """
        The **HTML <mark> element** represents highlighted text, i.e., a run
        of text marked for reference purpose, due to its *relevance* in a
        particular context. For example it can be used in a page showing
        search results to highlight every instance of the searched-for word.
        
        Examples::
        
            <article><p>The &lt;mark&gt; element is used to
              <mark>highlight</mark> text</p> 
            </article>
        
        Notes:
        
        
    """

class q(Component):
    """
        The **HTML <q> element** indicates that the enclosed text is a short
        inline quotation. This element is intended for short quotations that
        don't require paragraph breaks; for long quotations use the
        ``<blockquote>`` element.
        
        Examples::
        
            <article><p>According to Mozilla's website,
            &#160; <q cite="https://www.mozilla.org/en-US/about/history/details/">Firefox 1.0
              was released in 2004 and became a big success.</q></p>
            </article>
        
        Notes:
        
        
    """

class rp(Component):
    """
        The **HTML <rp> element** is used to provide fall-back parentheses for
        browsers that do not support display of ruby annotations using the
        ``<ruby>`` element.
        
        Examples::
        
            <article><ruby>
              &#28450; <rp>(</rp><rt>Kan</rt><rp>)</rp>
              &#23383; <rp>(</rp><rt>ji</rt><rp>)</rp>
            </ruby></article>
        
        Notes:
        
        
    """

class rt(Component):
    """
        The **HTML <rt> element** embraces pronunciation of characters
        presented in a ruby annotations, which are used to describe the
        pronunciation of East Asian characters. This element is always used
        inside a ``<ruby>`` element.
        
        Examples::
        
            <article><ruby>
              &#28450; <rt>Kan</rt>
              &#23383; <rt>ji</rt>
            </ruby>
            </article>
        
        Notes:
        
        
    """

class rtc(Component):
    """
        The **HTML <rtc> element** embraces semantic annotations of characters
        presented in a ruby of ``<rb>`` elements used inside of ``<ruby>``
        element. ``<rb>`` elements can have both pronunciation (``<rt>``) and
        semantic (``<rtc>``) annotations.
        
        Examples::
        
            <article><ruby>
               <rb>&#26087;</rb>
               <rb>&#37329;</rb>
               <rb>&#23665;</rb>
               <rt>ji&#249;</rt>
               <rt>j&#299;n</rt>
               <rt>sh&#257;n</rt>
               <rtc>San Francisco</rtc>
            </ruby>
            </article>
        
        Notes:
        
        
    """

class ruby(Component):
    """
        The **HTML <ruby> element** represents a ruby annotation. Ruby
        annotations are for showing pronunciation of East Asian characters.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class s(Component):
    """
        The **HTML <s> element** renders text with a strikethrough, or a line
        through it. Use the ``<s>`` element to represent things that are no
        longer relevant or no longer accurate. However, ``<s>`` is not
        appropriate when indicating document edits; for that, use the
        ``<del>`` and ``<ins>`` elements, as appropriate.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class samp(Component):
    """
        The **HTML <samp> element** is an element intended to identify sample
        output from a computer program. It is usually displayed in the
        browser's default monotype font (such as Lucida Console).
        
        Examples::
        
            <article><p>The diet-tracking app said: <samp>You're not eating your veggies</samp> and that was true</p>
            </article>
        
        Notes:
        
            A CSS rule can be defined for the ``samp`` selector to override the
            browser's default font face. Preferences set by the user might take
            precedence over the specified CSS.
    """

class small(Component):
    """
        The **HTML <small>** **element** makes the text *font size* one size
        smaller (for example, from large to medium, or from small to x-small)
        down to the browser's minimum font size.  In HTML5, this element is
        repurposed to represent side-comments and small print, including
        copyright and legal text, independent of its styled presentation.
        
        Examples::
        
            <article><p>This is the first sentence. <small>This whole sentence
              is in small letters.</small></p>
            <p>This is the first sentence.
              <span style="font-size:0.8em">This whole sentence is in small
              letters.</span></p>
            </article>
        
        Notes:
        
            Although the ``<small>`` element, like the ``<b>`` and ``<i>``
            elements, may be perceived to violate the principle of separation
            between structure and presentation, all three are valid in HTML5.
            Authors are encouraged to use their best judgement when determining
            whether to use ``<small>`` or CSS.
    """

class span(Component):
    """
        The **HTML <span> element** is a generic inline container for phrasing
        content, which does not inherently represent anything. It can be used
        to group elements for styling purposes (using the ``class`` or ``id``
        attributes), or because they share attribute values, such as ``lang``.
        It should be used only when no other semantic element is appropriate.
        ``<span>`` is very much like a ``<div>`` element, but ``<div>`` is a
        block-level element whereas a ``<span>`` is an inline element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class strong(Component):
    """
        The **HTML** ``<strong>`` **element** gives text strong importance,
        and is typically displayed in bold.
        
        Examples::
        
            <article><p>When doing x it is <strong>imperative</strong>
               to do y before proceeding.</p>
            </article>
        
        Notes:
        
        
    """

class sub(Component):
    """
        The **HTML <sub> element** defines a span of text that should be
        displayed, for typographic reasons, lower, and often smaller, than the
        main span of text.
        
        Examples::
        
            <article><p>The chemical formula of water: H<sub>2</sub>O</p>
            </article>
        
        Notes:
        
        
    """

class sup(Component):
    """
        The **HTML <sup> element** defines a span of text that should be
        displayed, for typographic reasons, higher, and often smaller, than
        the main span of text.
        
        Examples::
        
            <article><p>This text is <sup>superscripted</sup></p>
            </article>
        
        Notes:
        
        
    """

class time(Component):
    """
        The **HTML <time> element** represents either a time on a 24-hour
        clock or a precise date in the Gregorian calendar (with optional time
        and timezone information).
        
        Examples::
        
            <article><p>The concert starts at <time>20:00</time>.</p>
            <p>The concert took place on <time datetime="2001-05-15T19:00">May 15</time>.</p>
            </article>
        
        Notes:
        
        
    """

class u(Component):
    """
        The **HTML <u> element** renders text with an underline, a line under
        the baseline of its content. In HTML5, this element represents a span
        of text with an unarticulated, though explicitly rendered, non-textual
        annotation, such as labeling the text as being a proper name in
        Chinese text (a Chinese proper name mark), or labeling the text as
        being misspelled.
        
        Examples::
        
            <article><u>Today's Special</u>: Salmon<br>
            <span style="text-decoration:underline;">Today's Special</span>:
              Salmon
            <!-- Here <span> is used as the underlining is purely decorative
              and it is applied with CSS -->
            <p><u>All</u> of that is explained in
              <u>Dive into Python</u></p>
            <p><em>All</em> of that is explained in
              <i>Dive into Python</i></p>
            <!-- Here the "All" is marked as stressed, using <em>,
              while "Dive into Python" is marked as a name using <i> --> </article>
        
        Notes:
        
        
    """

class var(Component):
    """
        The **HTML <var> element** represents a variable in a mathematical
        expression or a programming context.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class wbr(Component):
    """
        The **HTML <wbr> element** represents a word break opportunity—a
        position within text where the browser may optionally break a line,
        though its line-breaking rules would not otherwise create a break at
        that location.
        
        Examples::
        
            <article><p>http://this<wbr>.is<wbr>.a<wbr>.really<wbr>.long<wbr>.example<wbr>.com/With<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages<wbr>/deeper<wbr>/level<wbr>/pages</wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></wbr></p>
            </article>
        
        Notes:
        
            On UTF-8 encoded pages, ``<wbr>`` behaves like the ``U+200B`` ``ZERO-
            WIDTH SPACE`` code point. In particular, it behaves like a Unicode
            bidi BN code point, meaning it has no effect on bidi-ordering: ``<div
            dir=rtl>123,<wbr>456</div>`` displays, when not broken on two lines,
            ``123,456`` and not ``456,123``.For the same reason, the ``<﻿wbr﻿>``
            element does not introduce a hyphen at the line break point. To make a
            hyphen appear only at the end of a line, use the soft hyphen character
            entity (``&﻿shy;``) instead.
            
            This element was first implemented in Internet Explorer 5.5 and was
            officially defined in HTML5.
    """



# == Image and multimedia ==
# HTML supports various multimedia resources such as images, audio, and video.
class area(Component):
    """
        The **HTML <area> element** defines a hot-spot region on an image, and
        optionally associates it with a hypertext link. This element is used
        only within a ``<map>`` element.
        
        Examples::
        
            <article><map name="primary">
              <area shape="circle" coords="75,75,75" href="left.html" alt="Click to go Left">
              <area shape="circle" coords="275,75,75" href="right.html" alt="Click to go Right">
            </map>
            <img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic"></article>
        
        Notes:
        
            Under the HTML 3.2, 4.0, and 5 specifications, the closing tag
            ``</area>`` is forbidden.The XHTML 1.0 specification requires a
            trailing slash: ``<area />``.
            
            The **id**, **class**, and **style** attributes have the same meaning
            as the core attributes defined in the HTML 4 specification, but only
            Netscape and Microsoft define them.
            
            Netscape 1–level browsers do not understand the **target** attribute
            as it relates to frames.
            
            HTML 3.2 defines only **alt**, **coords**, **href**, **nohref**, and
            **shape**.
            
            HTML 5.1 defines obsolete the attribute **type** on this tag.
    """

class audio(Component):
    """
        The **HTML <audio> element** is used to embed sound content in
        documents. It may contain one or more audio sources, represented using
        the ``src`` attribute or the ``<source>`` element: the browser will
        choose the most suitable one. It can also be the destination for
        streamed media, using a ``MediaStream``.
        
        Examples::
        
            <article><!-- Simple audio playback -->
            <audio src="http://developer.mozilla.org/@api/deki/files/2926/=AudioTest_(1).ogg" autoplay>
              Your browser does not support the <code>audio</code> element.
            </audio>
            <audio controls="controls">
              Your browser does not support the <code>audio</code> element.
              <source src="foo.wav" type="audio/wav">
            </source></audio>
            </article>
        
        Notes:
        
        
    """

class img(Component):
    """
        The **HTML <img> element** represents an image in the document.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 17)
# class map_(Component):"""
#         The **HTML <map> element** is used with ``<area>`` elements to define
#         an image map (a clickable link area).
#         
#         Examples::
#         
#             <article><map name="primary">
#             &#160; <area shape="circle" coords="75,75,75" href="left.html">
#             &#160; <area shape="circle" coords="275,75,75" href="right.html">
#             </map>
#             <img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic">
#             </article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'map'
class track(Component):
    """
        The **HTML <track> element** is used as a child of the media elements
        ``<audio>`` and ``<video>``. It lets you specify timed text tracks (or
        time-based data), for example to automatically handle subtitles. The
        tracks are formatted in WebVTT format (``.vtt`` files) — Web Video
        Text Tracks.
        
        Examples::
        
            <article><video controls poster="/images/sample.gif">
               <source src="sample.mp4" type="video/mp4">
               <source src="sample.ogv" type="video/ogv">
               <track kind="captions" src="sampleCaptions.vtt" srclang="en">
               <track kind="descriptions" src="sampleDescriptions.vtt" srclang="en">
               <track kind="chapters" src="sampleChapters.vtt" srclang="en">
               <track kind="subtitles" src="sampleSubtitles_de.vtt" srclang="de">
               <track kind="subtitles" src="sampleSubtitles_en.vtt" srclang="en">
               <track kind="subtitles" src="sampleSubtitles_ja.vtt" srclang="ja">
               <track kind="subtitles" src="sampleSubtitles_oz.vtt" srclang="oz">
               <track kind="metadata" src="keyStage1.vtt" srclang="en" label="Key Stage 1">
               <track kind="metadata" src="keyStage2.vtt" srclang="en" label="Key Stage 2">
               <track kind="metadata" src="keyStage3.vtt" srclang="en" label="Key Stage 3">
               <!-- Fallback -->
               ...
            </track></track></track></track></track></track></track></track></track></track></source></source></video>
            </article>
        
        Notes:
        
        
    """

class video(Component):
    """
        Use the **HTML <video> element** to embed video content in a document.
        
        Examples::
        
            <article><!-- Simple video example -->
            <video src="videofile.webm" autoplay poster="posterimage.jpg">
            Sorry, your browser doesn't support embedded videos, 
            but don't worry, you can <a href="videofile.webm">download it</a>
            and watch it with your favorite video player!
            </video>
            
            <!-- Video with subtitles -->
            <video src="foo.webm">
              <track kind="subtitles" src="foo.en.vtt" srclang="en" label="English">
              <track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska">
            </track></track></video>
            </article>
        
        Notes:
        
        
    """



# == Embedded content ==
# In addition to regular multimedia content, HTML can include a variety of other
# content, even if it's not always easy to interact with.
class embed(Component):
    """
        The **HTML <embed> element** represents an integration point for an
        external application or interactive content (in other words, a plug-
        in).
        
        **Note:** This topic documents only the element that is defined as
        part of HTML5. It does not address earlier, non-standardized
        implementation of the element.
        
        Examples::
        
            <article><embed type="video/quicktime" src="movie.mov" width="640" height="480">
            </embed></article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 20)
# class object_(Component):"""
#         The **HTML <object> element** represents an external resource, which
#         can be treated as an image, a nested browsing context, or a resource
#         to be handled by a plugin.
#         
#         Examples::
#         
#             <article><!-- Embed a flash movie -->
#             <object data="movie.swf" type="application/x-shockwave-flash"></object>
#             
#             <!-- Embed a flash movie with parameters -->
#             <object data="movie.swf" type="application/x-shockwave-flash">
#               <param name="foo" value="bar">
#             </object> 
#             </article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'object'
class param(Component):
    """
        The **HTML <param> element** defines parameters for an ``<object>``
        element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class source(Component):
    """
        The **HTML <source> element** specifies multiple media resources for
        either the ``<picture>``, the ``<audio>`` or the ``<video>`` element.
        It is an empty element. It is commonly used to serve the same media
        content in multiple formats supported by different browsers.
        
        Examples::
        
            <article><video controls>
              <source src="foo.webm" type="video/webm">
              <source src="foo.ogg" type="video/ogg"> 
              <source src="foo.mov" type="video/quicktime">
            &#160; I'm sorry; your browser doesn't support HTML5 video.
            </source></source></source></video>
            </article>
        
        Notes:
        
        
    """



# == Scripting ==
# In order to create dynamic content and Web applications, HTML supports the use
# of scripting languages, most prominently JavaScript. Certain elements support
# this capability.
class canvas(Component):
    """
        Use the **HTML <canvas> element** with the canvas scripting API to
        draw graphics and animations.
        
        Examples::
        
            <article><canvas id="canvas" width="300" height="300">
              An alternative text describing what your canvas displays. 
            </canvas> <canvas id="myCanvas" moz-opaque></canvas></article>
        
        Notes:
        
        
    """

class noscript(Component):
    """
        The **HTML <noscript> element** defines a section of HTML to be
        inserted if a script type on the page is unsupported or if scripting
        is currently turned off in the browser.
        
        Examples::
        
            <article><noscript>
              <!-- anchor linking to external file -->
              <a href="https://www.mozilla.com/">External Link</a>
            </noscript>
            <p>Rocks!</p>
            </article>
        
        Notes:
        
        
    """

class script(Component):
    """
        The **HTML <script> element** is used to embed or reference an
        executable script.
        
        Examples::
        
            <article><!-- HTML4 and (x)HTML -->
            <script type="text/javascript" src="javascript.js"></script>
            
            <!-- HTML5 -->
            <script src="javascript.js"></script>
            </article>
        
        Notes:
        
            Scripts without ``async`` or ``defer`` attributes, as well as inline
            scripts, are fetched and executed immediately, before the browser
            continues to parse the page.The script should be served with the
            ``text/javascript`` MIME type, but browsers are lenient and only block
            them if the script is served with an image type (``image/*``), a video
            type (``video/*``), an audio (``audio/*``) type, or ``text/csv``. If
            the script is blocked, an ``error`` is sent to the element, if not a
            ``load`` event is sent.
    """



# == Demarcating edits ==
# These elements let you provide indications that specific parts of the text
# have been altered.
# FIXME: invalid syntax (<unknown>, line 15)
# class del_(Component):"""
#         The **HTML <del> element** represents a range of text that has been
#         deleted from a document. This element is often (but need not be)
#         rendered with strike-through text.
#         
#         Examples::
#         
#             <article><p><del>This text has been deleted</del>,
#             here is the rest of the paragraph.</p>
#             <del><p>This paragraph has been deleted.</p></del></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'del'
class ins(Component):
    """
        The **HTML <ins> element** represents a range of text that has been
        added to a document.
        
        Examples::
        
            <article><ins>This text has been inserted</ins></article>
        
        Notes:
        
        
    """



# == Table content ==
# The elements here are used to create and handle tabular data.
class caption(Component):
    """
        The **HTML <caption> element** represents the title of a table. Though
        it is always the first descendant of a ``<table>``, its styling, using
        CSS, may place it elsewhere, relative to the table.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class col(Component):
    """
        The **HTML <col> element** defines a column within a table and is used
        for defining common semantics on all common cells. It is generally
        found within a ``<colgroup>`` element.
        
        This element allows styling columns using CSS, but only a few
        attributes will have an effect on the column (see the CSS 2.1
        specification for a list).
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class colgroup(Component):
    """
        The **HTML <colgroup> element** defines a group of columns within a
        table.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class table(Component):
    """
        The **HTML <table> element** represents tabular data — that is,
        information expressed via a two-dimensional data table.
        
        Examples::
        
            <article><table>
              <tr>
                <td>John</td>
                <td>Doe</td>
              </tr>
              <tr>
                <td>Jane</td>
                <td>Doe</td>
              </tr>
            </table>
            <p>Simple table with header</p>
            <table>
              <tr>
                <th>First name</th>
                <th>Last name</th>
              </tr>
              <tr>
                <td>John</td>
                <td>Doe</td>
              </tr>
              <tr>
                <td>Jane</td>
                <td>Doe</td>
              </tr>
            </table>
            
            <p>Table with thead, tfoot, and tbody</p>
            <table>
              <thead>
                <tr>
                  <th>Header content 1</th>
                  <th>Header content 2</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Body content 1</td>
                  <td>Body content 2</td>
                </tr>
              </tbody>
              <tfoot>
            &#160;   <tr>
            &#160;     <td>Footer content 1</td>
            &#160;     <td>Footer content 2</td>
            &#160;   </tr>
              </tfoot>
            </table>
            
            <p>Table with colgroup</p>
            <table>
              <colgroup span="4"></colgroup>
              <tr>
                <th>Countries</th>
                <th>Capitals</th>
                <th>Population</th>
                <th>Language</th>
              </tr>
              <tr>
                <td>USA</td>
                <td>Washington D.C.</td>
                <td>309 million</td>
                <td>English</td>
              </tr>
              <tr>
                <td>Sweden</td>
                <td>Stockholm</td>
                <td>9 million</td>
                <td>Swedish</td>
              </tr>
            </table>
            
            <p>Table with colgroup and col</p>
            <table>
              <colgroup>
                <col style="background-color: #0f0">
                <col span="2">
              </colgroup>
              <tr>
                <th>Lime</th>
                <th>Lemon</th>
                <th>Orange</th>
              </tr>
              <tr>
                <td>Green</td>
                <td>Yellow</td>
                <td>Orange</td>
              </tr>
            </table>
            
            <p>Simple table with caption</p>
            <table>
              <caption>Awesome caption</caption>
              <tr>
                <td>Awesome data</td>
              </tr>
            </table>
            </article>
        
        Notes:
        
        
    """

class tbody(Component):
    """
        The **HTML <tbody> element** groups one or more ``<tr>`` elements as
        the body of a ``<table>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class td(Component):
    """
        The **HTML <td> element** defines a cell of a table that contains
        data. It participates in the *table model*.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class tfoot(Component):
    """
        The **HTML <tfoot> element** defines a set of rows summarizing the
        columns of the table.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class th(Component):
    """
        The **HTML <th> element** defines a cell as header of a group of table
        cells. The exact nature of this group is defined by the ``scope`` and
        ``headers`` attributes.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class thead(Component):
    """
        The **HTML <thead> element** defines a set of rows defining the head
        of the columns of the table.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class tr(Component):
    """
        The HTML **<tr>** element specifies that the markup contained inside
        the ``<tr>`` block comprises one row of a table, inside which the
        ``<th>`` and ``<td>`` elements create header and data cells,
        respectively, within the row. Each cell is placed into its own column;
        the user agent follows specific rules to determine how the cells in
        each row are placed into columns with those coming from other rows.To
        provide additional control over how cells fit into (or span across)
        columns, both ``<th>`` and ``<td>`` support the ``colspan`` attribute,
        which lets you specify how many columns wide the cell should be, with
        the default being 1. Similarly, you can use the ``rowspan`` attribute
        on cells to indicate they should span more than one table row.
        
        This can take a little practice to get right when building your
        tables. We have some examples below, but for more examples and an in-
        depth tutorial, see the HTML tables series in our Learn web
        development area, where you'll learn how to use the table elements and
        their attributes to get just the right layout and formatting for your
        tabular data.
        
        Examples::
        
            <article><table>
              <tr>
                <th>Name</th>
                <th>ID</th>
                <th>Member Since</th>
                <th>Balance</th>
              </tr>
              <tr>
                <td>Margaret Nguyen</td>
                <td>427311</td>
                <td><time datetime="2010-06-03">June 3, 2010</time></td>
                <td>0.00</td>
              </tr>
              <tr>
                <td>Edvard Galinski</td>
                <td>533175</td>
                <td><time datetime="2011-01013">January 13, 2011</time></td>
                <td>37.00</td>
              </tr>
              <tr>
                <td>Hoshi Nakamura</td>
                <td>601942</td>
                <td><time datetime="2012-07-23">July 23, 2012</time></td>
                <td>15.00</td>
              </tr>
            </table>
            <table>
              <tr>
                <th rowspan="2">Name</th>
                <th rowspan="2">ID</th>
                <th colspan="2">Membership Dates</th>
                <th rowspan="2">Balance</th>
              </tr>
              <tr>
                <th>Joined</th>
                <th>Canceled</th>
              </tr>
              <tr>
                <th>Margaret Nguyen
                </th>
            <td>427311</td>
                <td><time datetime="2010-06-03">June 3, 2010</time></td>
                <td>n/a</td>
                <td>0.00</td>
              </tr>
              <tr>
                <th>Edvard Galinski
                </th>
            <td>533175</td>
                <td><time datetime="2011-01013">January 13, 2011</time></td>
                <td><time datetime="2017-04008">April 8, 2017</time></td>
                <td>37.00</td>
              </tr>
              <tr>
                <th>Hoshi Nakamura
                </th>
            <td>601942</td>
                <td><time datetime="2012-07-23">July 23, 2012</time></td>
                <td>n/a</td>
                <td>15.00</td>
              </tr>
            </table>
            <table>
            &#160; <thead>
            &#160;&#160;&#160; <tr>
            &#160;&#160;&#160;&#160;&#160; <th rowspan="2">Name</th>
            &#160;&#160;&#160;&#160;&#160; <th rowspan="2">ID</th>
            &#160;&#160;&#160;&#160;&#160; <th colspan="2">Membership Dates</th>
            &#160;&#160;&#160;&#160;&#160; <th rowspan="2">Balance</th>
            &#160;&#160;&#160; </tr>
            &#160;&#160;&#160; <tr>
            &#160;&#160;&#160;&#160;&#160; <th>Joined</th>
            &#160;&#160;&#160;&#160;&#160; <th>Canceled</th>
            &#160;&#160;&#160; </tr>
            &#160; </thead>
            &#160; <tbody>
            &#160;&#160;&#160; <tr>
            &#160;&#160;&#160;&#160;&#160; <th scope="rowgroup">Margaret Nguyen
            &#160;&#160;&#160;&#160;&#160; </th>
            <td>427311</td>
            &#160;&#160;&#160;&#160;&#160; <td><time datetime="2010-06-03">June 3, 2010</time></td>
            &#160;&#160;&#160;&#160;&#160; <td>n/a</td>
            &#160;&#160;&#160;&#160;&#160; <td>0.00</td>
            &#160;&#160;&#160; </tr>
            &#160;&#160;&#160; <tr>
            &#160;&#160;&#160;&#160;&#160; <th scope="rowgroup">Edvard Galinski
            &#160;&#160;&#160;&#160;&#160; </th>
            <td>533175</td>
            &#160;&#160;&#160;&#160;&#160; <td><time datetime="2011-01013">January 13, 2011</time></td>
            &#160;&#160;&#160;&#160;&#160; <td><time datetime="2017-04008">April 8, 2017</time></td>
            &#160;&#160;&#160;&#160;&#160; <td>37.00</td>
            &#160;&#160;&#160; </tr>
            &#160;&#160;&#160; <tr>
            &#160;&#160;&#160;&#160;&#160; <th scope="rowgroup">Hoshi Nakamura
            &#160;&#160;&#160;&#160;&#160; </th>
            <td>601942</td>
            &#160;&#160;&#160;&#160;&#160; <td><time datetime="2012-07-23">July 23, 2012</time></td>
            &#160;&#160;&#160;&#160;&#160; <td>n/a</td>
            &#160;&#160;&#160;&#160;&#160; <td>15.00</td>
            &#160;&#160;&#160; </tr>
            &#160; </tbody>
            </table></article>
        
        Notes:
        
        
    """



# == Forms ==
# HTML provides a number of elements which can be used together to create forms
# which the user can fill out and submit to the Web site or application. There's
# a great deal of further information about this available in the HTML forms
# guide.
class button(Component):
    """
        The **HTML <button> element** represents a clickable button.
        
        Examples::
        
            <article></article>
        
        Notes:
        
            ``<button>`` elements are much easier to style than ``<input>``
            elements. You can add inner HTML content (think ``<em>``, ``<strong>``
            or even ``<img>``), and make use of ``:after`` and ``:before`` pseudo-
            element to achieve complex rendering while ``<input>`` only accepts a
            text value attribute.IE7 has a bug where when submitting a form with
            ``<button type="submit" name="myButton" value="foo">Click
            me</button>``, the ``POST`` data sent will result in ``myButton=Click
            me`` instead of ``myButton=foo``. IE6 has an even worse bug where
            submitting a form through a button will submit ALL buttons of the
            form, with the same bug as IE7. This bug has been fixed in IE8.
            
            Firefox will add, for accessibility purposes, a small dotted border on
            a focused button. This border is declared through CSS, in the browser
            stylesheet, but you can override it if necessary to add your own
            focused style using ``button``::-moz-focus-inner`` { }``
            
            Firefox will, unlike other browsers, by default, persist the dynamic
            disabled state of a ``<button>`` across page loads. Setting the value
            of the ``autocomplete`` attribute to ``off`` disables this feature.
            See bug 654072.
            
            Firefox <35 for Android sets a default ``background-image`` gradient
            on all buttons (see bug 763671). This can be disabled using
            ``background-image: none``.
            
            Clicking and focus ==================
            
            Whether clicking on a ``<button>`` causes it to (by default) become
            focused varies by browser and OS. The results for ``<input>`` of
            ``type="button"`` and ``type="submit"`` were the same.
    """

class datalist(Component):
    """
        The **HTML <datalist> element** contains a set of ``<option>``
        elements that represent the values available for other controls.
        
        Examples::
        
            <article><label>Choose a browser from this list:
            <input list="browsers" name="myBrowser"></label>
            <datalist id="browsers">
              <option value="Chrome">
              </option>
            <option value="Firefox">
              </option>
            <option value="Internet Explorer">
              </option>
            <option value="Opera">
              </option>
            <option value="Safari">
              </option>
            <option value="Microsoft Edge">
            </option></datalist>
            </article>
        
        Notes:
        
        
    """

class fieldset(Component):
    """
        The **HTML <fieldset> element** is used to group several controls as
        well as labels (``<label>``) within a web form.
        
        Examples::
        
            <article><form action="test.php" method="post">
              <fieldset>
                <legend>Title</legend>
                <input type="radio" id="radio">
                <label for="radio">Click me</label>
              </fieldset>
            </form>
            
            
            <meta charset="UTF-8">
            <title>Editable [pseudo]select</title>
            <style type="text/css">
            
            /* Generic form fields */
            
            fieldset.elist, input[type="text"], textarea, select,
            option, fieldset.elist ul, fieldset.elist > legend,
            fieldset.elist input[type="text"],
            fieldset.elist > legend:after {
              -webkit-box-sizing: border-box;
              -moz-box-sizing: border-box;
              box-sizing: border-box;
            }
            
            input[type="text"] {
              padding: 0 20px;
            }
            
            textarea {
              width: 500px;
              height: 200px;
              padding: 20px;
            }
            
            textarea, input[type="text"], fieldset.elist ul,
            select, fieldset.elist > legend {
              border: 2px #cccccc solid;
              border-radius: 10px;
            }
            
            input[type="text"], fieldset.elist, select,
            fieldset.elist > legend {
              height: 32px;
              font-family: Tahoma;
              font-size: 14px;
            }
            
            input[type="text"]:hover, textarea:hover,
            select:hover, fieldset.elist:hover > legend {
              background-color: #ddddff;
            }
            
            select {
              padding: 4px 20px;
            }
            
            option {
              height: 30px;
              padding: 5px 4px;
            }
            
            option:not(:checked), textarea:focus {
              background-color: #ffcccc;
            }
            
            fieldset.elist > legend:after,
            fieldset.elist label {
              height: 28px;
            }
            
            input[type="text"], fieldset.elist {
              width: 316px;
            }
            
            input[type="text"]:focus {
              background: #ffcccc url("data:image/gif;
              base64,R0lGODlhEAAQANU5APnoxuvr6+uxPdvb2+
              rq6ri4uO7qxunp6dPT06SHV+/rx8vLy+
              nezLO0sbe3t9Ksas+qaaCEV8rKyp2dnf39/
              QAAAK6ursifZHFxcc/
              Qzu3mxYyMjExCJnV1dc6maO7u7o+
              Pj2tXNoaGhtfDpKCDVu3lxM+
              tcaKEV9bW1qOFVWNjY8KrisTExNra2nBbObGxsby8vO/
              mu7Kyso9ZAuzs7MSgAIiKhf///8zMzP///
              wAAAAAAAAAAAAAAAAAAAAAAACH5BAEAADkALAAAAAAQ
              ABAAAAaXwJxwSCwOYzWkMpkkZmoAqDQaJdpqAqw2m53
              NRjlboAarFczomcE0C99o8DgNMVM8Tm3bbYDr9x11Dw
              kzDG5yc2oQJIRCenx/MxoeETM2Q3pxATMlF4MYlo17O
              AsdLispMyAioIY0BzMcITMTKBasjgssFTMqGxItMjYU
              oTQBBAQHxgE0wZcfMtDRMi/QrA022NnaNg1CQQA7")
              no-repeat 2px center !important;
            }
            
            input[type="text"]:focus, textarea:focus,
            select:focus, fieldset.elist > legend {
              border: 2px #ccaaaa solid;
            }
            
            fieldset {
              border: 2px #af3333 solid;
              border-radius: 10px;
            }
            
            /* Editable [pseudo]select
            (i.e. fieldsets with [class=elist]) */
            
            fieldset.elist {
              display: inline-block;
              position: relative;
              vertical-align: middle;
              overflow: visible;
              padding: 0;
              margin: 0;
              border: none;
            }
            
            fieldset.elist ul {
              position: absolute;
              width: 100%;
              max-height: 320px;
              padding: 0;
              margin: 0;
              overflow: hidden;
              background-color: transparent;
            }
            
            fieldset.elist:hover ul {
              background-color: #ffffff;
              border: 2px #af3333 solid;
              left: 2px;
              overflow: auto;
            }
            
            fieldset.elist ul > li {
              list-style-type: none;
              background-color: transparent;
            }
            
            fieldset.elist label {
              display: none;
              width: 100%;
            }
            
            fieldset.elist input[type="text"] {
              width: 100%;
              height: 30px;
              line-height: 30px;
              border: none;
              background-color: transparent;
              border-radius: 0;
            }
            
            fieldset.elist > legend {
              display: block;
              margin: 0;
              padding: 0 0 0 5px;
              position: absolute;
              width: 100%;
              cursor: default;
              background-color: #ccffcc;
              line-height: 30px;
              font-style: italic;
            }
            
            fieldset.elist:hover > legend {
              position: relative;
              overflow: hidden;
            }
            
            fieldset.elist > legend:after {
              width: 20px;
              content: "\2335";
              float: right;
              text-align: center;
              border-left: 2px #cccccc solid;
              font-style: normal;
              cursor: default;
            }
            
            fieldset.elist:hover > legend:after {
              background-color: #99ff99;
            }
            
            fieldset.elist ul input[type="radio"] {
              display: none;
            }
            
            fieldset.elist input[type="radio"]:checked ~ label {
              display: block;
              width: 292px;
              background-color: #ffffff;
            }
            
            fieldset.elist:hover
            input[type="radio"]:checked ~ label {
              width: 100%;
            }
            
            fieldset.elist:hover label {
              display: block;
              height: 100%;
            }
            
            fieldset.elist label:hover {
              background-color: #3333ff !important;
            }
            
            fieldset.elist:hover
            input[type="radio"]:checked ~ label {
              background-color: #aaaaaa;
            }
            
            </style>
            
            
            
            
            <form method="get" action="test.php">
            
            <fieldset>
                <legend>Order a T-Shirt</legend>
                <p>Write your name (simple textbox):
                <input type="text"></p>
                <p>Choose your size (simple select):
                <select>
                    <option value="s">Small</option>
                    <option value="m">Medium</option>
                    <option value="l">Large</option>
                    <option value="xl">Extra Large</option>
                </select></p>
                <div>What address do you want to use?
                (editable pseudoselect)
                <fieldset class="elist">
                    <legend>Address&#8230;</legend>
                    <ul>
                        <li>
            <input type="radio" value="1" id="address-switch_1" checked><label for="address-switch_1"><input type="text" value="19 Quaker Ridge Rd. Bethel CT 06801"></label>
            </li>
                        <li>
            <input type="radio" value="2" id="address-switch_2"><label for="address-switch_2"><input type="text" value="1000 Coney Island Ave.
                        Brooklyn NY 11230"></label>
            </li>
                        <li>
            <input type="radio" value="3" id="address-switch_3"><label for="address-switch_3"><input type="text" value="2962 Dunedin Cv. Germantown TN 38138"></label>
            </li>
                        <li>
            <input type="radio" value="4" id="address-switch_4"><label for="address-switch_4"><input type="text" value="915 E 7th St. Apt 6L. Brooklyn NY 11230"></label>
            </li>
                    </ul>
                </fieldset>
                </div>
                <p>Write a comment:<br>
                <textarea></textarea></p>
                <p><input type="reset" value="Reset">
                <input type="submit" value="Send!"></p>
            </fieldset>
            
            </form>
            
            
            
            </article>
        
        Notes:
        
        
    """

class form(Component):
    """
        The **HTML <form> element** represents a document section that
        contains interactive controls to submit information to a web server.
        
        It is possible to use the ``:valid`` and ``:invalid`` CSS pseudo-
        classes to style a ``<form>`` element.
        
        Examples::
        
            <article><!-- Simple form which will send a GET request -->
            <form action="" method="get">
            &#160; <label for="GET-name">Name:</label>
            &#160; <input id="GET-name" type="text" name="name">
            &#160; <input type="submit" value="Save">
            </form>
            
            <!-- Simple form which will send a POST request -->
            <form action="" method="post">
            &#160; <label for="POST-name">Name:</label>
            &#160; <input id="POST-name" type="text" name="name">
            &#160; <input type="submit" value="Save">
            </form>
            
            <!-- Form with fieldset, legend, and label -->
            <form action="" method="post">
            &#160; <fieldset>
            &#160; &#160; <legend>Title</legend>
            &#160; &#160; <input type="radio" name="radio" id="radio">
                <label for="radio">Click me</label>
            &#160; </fieldset>
            </form>
            </article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 76)
# class input_(Component):"""
#         The **HTML <input> element** is used to create interactive controls
#         for web-based forms in order to accept data from the user.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#             File inputs
#             
#             ===========#. Starting in Gecko 2.0, calling the ``click()`` method on
#             an ``<input>`` element of type ``file`` opens the file picker and lets
#             the user select files. See Using files from web applications for an
#             example and more details.
#             
#             #. You cannot set the value of a file picker from a script — doing
#             something like the following has no effect:
#             
#             var e = getElementById("someFileInputElement"); e.value = "foo";
#             
#             #. When a file is chosen using an ``<input type="file">``, the real
#             path to the source file is not shown in the input's ``value``
#             attribute for obvious security reasons. Instead, the filename is
#             shown, with ``C:
#             
#             fakepath`` appended to the beginning of it. There are some historical
#             reasons for this quirk, but it is supported across all modern
#             browsers, and in fact is defined in the spec.
#             
#             Error messages ==============
#             
#             If you want Firefox to present a custom error message when a field
#             fails to validate, you can use the ``x-moz-errormessage`` attribute to
#             do so:
#             
#             <input type="email" x-moz-errormessage="Please specify a valid email
#             address.">
#             
#             Note, however, that this is not standard and will not have an effect
#             on other browsers.
#             
#             Localization ============
#             
#             The allowed inputs for certain <input> types depend on the locale. In
#             some locales, 1,000.00 is a valid number, while in other locales the
#             valid way to enter this number is 1.000,00.
#             
#             Firefox uses the following heuristics to determine the locale to
#             validate the user's input (at least for ``type="number"``):
#             
#             * Try the language specified by a ``lang``/``xml:lang`` attribute on
#             the element or any of its parents.
#             
#             * Try the language specified by any Content-Language HTTP header or
#             
#             * If none specified, use the browser's locale.
#             
#             Using mozactionhint on Firefox mobile
#             =====================================
#             
#             You can use the ``mozactionhint`` attribute to specify the text for
#             the label of the enter key on the virtual keyboard when your form is
#             rendered on Firefox mobile. For example, to have a "Next" label, you
#             can do this:
#             
#             <input type="text" mozactionhint="next">
#             
#             The result is:
#             
#             |mozactionhint.png|
#             
#             .. |mozactionhint.png| image::
#             /@api/deki/files/4970/=mozactionhint.png?size=webview
#     """    tag_name = 'input'
class label(Component):
    """
        The **HTML <label> element** represents a caption for an item in a
        user interface.
        
        Examples::
        
            <article><label>Click me <input type="text"></label><label for="username">Click me</label>
            <input type="text" id="username"></article>
        
        Notes:
        
        
    """

class legend(Component):
    """
        The **HTML <legend> element** represents a caption for the content of
        its parent ``<fieldset>``.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class meter(Component):
    """
        The **HTML <meter> element** represents either a scalar value within a
        known range or a fractional value.
        
        Examples::
        
            <article><p>Heat the oven to <meter min="200" max="500" value="350">350 degrees</meter>.</p>
            <p>He got a <meter low="69" high="80" max="100" value="84">B</meter> on the exam.</p>
            </article>
        
        Notes:
        
        
    """

class optgroup(Component):
    """
        The **HTML <optgroup> element** creates a grouping of options within a
        ``<select>`` element.
        
        Examples::
        
            <article><select>
              <optgroup label="Group 1">
                <option>Option 1.1</option>
              </optgroup> 
              <optgroup label="Group 2">
                <option>Option 2.1</option>
                <option>Option 2.2</option>
              </optgroup>
              <optgroup label="Group 3" disabled>
                <option>Option 3.1</option>
                <option>Option 3.2</option>
                <option>Option 3.3</option>
              </optgroup>
            </select>
            </article>
        
        Notes:
        
        
    """

class option(Component):
    """
        The **HTML <option> element** is used to define an item contained in a
        ``<select>``, an ``<optgroup>``, or a ``<datalist>`` element. As
        such, ``<option>`` can represent menu items in popups and other lists
        of items in an HTML document.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class output(Component):
    """
        Introduced in HTML5The **HTML <output> element** represents the result
        of a calculation or user action.
        
        Examples::
        
            <article><form oninput="result.value=parseInt(a.value)+parseInt(b.value)">
                <input type="range" name="b" value="50"> +
                <input type="number" name="a" value="10"> =
                <output name="result">60</output>
            </form>
            </article>
        
        Notes:
        
        
    """

class progress(Component):
    """
        Introduced in HTML5The **HTML <progress> element** represents the
        completion progress of a task, typically displayed as a progress bar.
        
        Examples::
        
            <article><progress value="70" max="100">70 %</progress>
            </article>
        
        Notes:
        
        
    """

class select(Component):
    """
        The **HTML <select> element** represents a control that provides a
        menu of options:
        
        Examples::
        
            <article><!-- The second value will be selected initially -->
            <select name="select"> <!--Supplement an id here instead of using 'name'-->
            &#160; <option value="value1">Value 1</option> 
            &#160;&#160;<option value="value2" selected>Value 2</option>
            &#160; <option value="value3">Value 3</option>
            </select>
            </article>
        
        Notes:
        
            The content of this element is static and not editable.
    """

class textarea(Component):
    """
        The **HTML <textarea> element** represents a multi-line plain-text
        editing control.
        
        Examples::
        
            <article><textarea name="textarea" rows="10" cols="50">Write something here</textarea></article>
        
        Notes:
        
        
    """



# == Interactive elements ==
# HTML offers a selection of elements which help to create interactive user
# interface objects.
class details(Component):
    """
        The **HTML <details> element** is used as a disclosure widget from
        which the user can retrieve additional information.
        
        Examples::
        
            <article><details>
              <summary>Some details</summary>
              <p>More info about the details.</p>
            </details>
            
            <details open>
              <summary>Even more details</summary>
              <p>Here are even more details about the details.</p>
            </details>
            </article>
        
        Notes:
        
        
    """

class dialog(Component):
    """
        The **HTML <dialog> element** represents a dialog box or other
        interactive component, such as an inspector or window.
        
        Examples::
        
            <article><dialog open>
              <p>Greetings, one and all!</p>
            </dialog>
            <!-- Simple pop-up dialog box, containing a form -->
            <dialog open id="favDialog">
              <form method="dialog">
                <section>
                  <p><label for="favAnimal">Favorite animal:</label>
                  <select id="favAnimal">
                    <option></option>
                    <option>Brine shrimp</option>
                    <option>Red panda</option>
                    <option>Spider monkey</option>
                  </select></p>
                </section>
                <menu>
                  <button id="cancel" type="reset">Cancel</button>
                  <button type="submit">Confirm</button>
                </menu>
              </form>
            </dialog>
            
            <menu>
              <button id="updateDetails">Update details</button>
            </menu>
            </article>
        
        Notes:
        
        
    """

class menu(Component):
    """
        ** **This is an experimental technology**
        
        Check the Browser compatibility table carefully before using this in
        production.The **HTML <menu> element** represents a group of commands
        that a user can perform or activate. This includes both list menus,
        which might appear across the top of a screen, as well as context
        menus, such as those that might appear underneath a button after it
        has been clicked.
        
        Examples::
        
            <article><!-- A <div> element with a context menu -->
            <div contextmenu="popup-menu">
              Right-click to see the adjusted context menu
            </div>
            
            <menu type="context" id="popup-menu">
              <menuitem>Action</menuitem>
              <menuitem>Another action</menuitem>
              <hr>
              <menuitem>Separated action</menuitem>
            </menu>
            <!-- A button, which displays a menu when clicked. -->
            <button type="menu" menu="popup-menu">
              Dropdown
            </button>
            
            <menu type="context" id="popup-menu">
              <menuitem>Action</menuitem>
              <menuitem>Another action</menuitem>
              <hr>
              <menuitem>Separated action</menuitem>
            </menu>
            <!-- A context menu for a simple editor,
                containing two menu buttons. -->
            <menu type="toolbar">
              <li>
                <button type="menu" menu="file-menu">File</button>
                <menu type="context" id="file-menu">
                  <menuitem label="New..." onclick="newFile()">
                  <menuitem label="Save..." onclick="saveFile()">
                </menuitem></menuitem>
            </menu>
              </li>
              <li>
                <button type="menu" menu="edit-menu">Edit</button>
                <menu type="context" id="edit-menu">
                  <menuitem label="Cut..." onclick="cutEdit()">
                  <menuitem label="Copy..." onclick="copyEdit()">
                  <menuitem label="Paste..." onclick="pasteEdit()">
                </menuitem></menuitem></menuitem>
            </menu>
              </li>
            </menu>
            </article>
        
        Notes:
        
        
    """

class menuitem(Component):
    """
        ** **This is an experimental technology**
        
        Check the Browser compatibility table carefully before using this in
        production.The **HTML <menuitem> element** represents a command that a
        user is able to invoke through a popup menu. This includes context
        menus, as well as menus that might be attached to a menu button.
        
        A command can either be defined explicitly, with a textual label and
        optional icon to describe its appearance, or alternatively as an
        *indirect command* whose behavior is defined by a separate element.
        Commands can also optionally include a checkbox or be grouped to share
        radio buttons. (Menu items for indirect commands gain checkboxes or
        radio buttons when defined against elements ``<input
        type="checkbox">`` and ``<input type="radio">``.)
        
        Examples::
        
            <article><!-- A <div> element with a context menu -->
            <div contextmenu="popup-menu">
            &#160; Right-click to see the adjusted context menu
            </div>
            
            <menu type="context" id="popup-menu">
            &#160; <menuitem type="checkbox" checked>Checkbox</menuitem>
            &#160; <hr>
            &#160; <menuitem type="command" label="This command does nothing" icon="https://developer.cdn.mozilla.net/static/img/favicon144.png">
            &#160; &#160; Commands don't render their contents.
            &#160; </menuitem>
            &#160; <menuitem type="command" label="This command has javascript" onclick="alert('command clicked')">
            &#160; &#160; Commands don't render their contents.
            &#160; </menuitem>
            &#160; <hr>
            &#160; <menuitem type="radio" radiogroup="group1">Radio Button 1</menuitem>
            &#160; <menuitem type="radio" radiogroup="group1">Radio Button 2</menuitem>
            </menu>
            </article>
        
        Notes:
        
        
    """

class summary(Component):
    """
        The **HTML <summary> element** is used as a summary, caption, or
        legend for the content of a ``<details>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Web Components ==
# Web Components is an HTML-related technology which makes it possible to,
# essentially, create and use custom elements as if it were regular HTML. In
# addition, you can create custom versions of standard HTML elements.
class content(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        The **HTML <content> element**—an obsolete part of the Web Components
        suite of technologies—was used inside of Shadow DOM as an insertion
        point, and wasn't meant to be used in ordinary HTML It has now been
        replaced by the ``<slot>`` element, which creates a point in the DOM
        at which a shadow DOM can be inserted.
        
        **Note:** Though present in early draft of the specifications and
        implemented in several browsers, this element has been removed in
        later versions of the spec.
        
        Examples::
        
            <article>
              
              
            &#160; <!-- The original content accessed by <content> -->
            &#160; <div>
            &#160; &#160; <h4>My Content Heading</h4>
            &#160; &#160; <p>My content text</p>
            &#160; </div>
            
            &#160; <script>
            &#160; // Get the <div> above.
            &#160; var myContent = document.querySelector('div');
            &#160; // Create a shadow DOM on the <div>
            &#160; var shadowroot = myContent.createShadowRoot();
            &#160; // Insert into the shadow DOM a new heading and 
            &#160; // part of the original content: the <p> tag.
            &#160; shadowroot.innerHTML =
            &#160;  '<h2>Inserted Heading</h2> <content select="p"></content>';
            &#160; </script>
            
              
            
            </article>
        
        Notes:
        
        
    """

class element(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The **HTML <element> element** was part of Web Components; this
        element was intended to be used to define new custom DOM elements. It
        was removed in favor of a JavaScript-driven methodology for creating
        new custom elements; however, that technology is not mature and no
        browers fully implement it.
        
        **Note:** This element has been removed from the specification. See
        this for more information from the editor of the specification.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class shadow(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The **HTML <shadow> element**—an obsolete part of the Web Components
        technology suite—was intended to be used as a shadow DOM insertion
        point. You might have used it if you have created multiple shadow
        roots under a shadow host. It is not useful in ordinary HTML.
        
        Examples::
        
            <article>
              
              
            
            &#160; <!-- This <div> will hold the shadow roots. -->
            &#160; <div>
            &#160; &#160; <!-- This heading will not be displayed -->
            &#160; &#160; <h4>My Original Heading</h4>
            &#160; </div>
            
            &#160; <script>
            &#160; &#160; // Get the <div> above with its content
            &#160; &#160; var origContent = document.querySelector('div');
            &#160; &#160; // Create the first shadow root
            &#160; &#160; var shadowroot1 = origContent.createShadowRoot();
            &#160; &#160; // Create the second shadow root
            &#160; &#160; var shadowroot2 = origContent.createShadowRoot();
            
            &#160; &#160; // Insert something into the older shadow root
            &#160; &#160; shadowroot1.innerHTML =
            &#160; &#160; &#160; '<p>Older shadow root inserted by
                      &lt;shadow&gt;</p>';
            &#160; &#160; // Insert into younger shadow root, including <shadow>.
            &#160; &#160; // The previous markup will not be displayed unless
            &#160; &#160; // <shadow> is used below.
            &#160; &#160; shadowroot2.innerHTML =
            &#160; &#160; &#160; '<shadow></shadow> <p>Younger shadow
                   root, displayed because it is the youngest.</p>';
            &#160; </script>
            
              
            
            </article>
        
        Notes:
        
        
    """

class slot(Component):
    """
        ** **This is an experimental technology**
        
        Check the Browser compatibility table carefully before using this in
        production.
        
        The **HTML <slot> element**—part of the Web Components technology
        suite—is a placeholder inside a web component that you can fill with
        your own markup, which lets you create separate DOM trees and present
        them together.
        
        Examples::
        
            <article><template id="element-details-template">
            &#160; <style>
            &#160; details {font-family: "Open Sans Light",Helvetica,Arial}
            &#160; .name {font-weight: bold; color: #217ac0; font-size: 120%}
            &#160; h4 { margin: 10px 0 -8px 0; }
            &#160; h4 span { background: #217ac0; padding: 2px 6px 2px 6px }
            &#160; h4 span { border: 1px solid #cee9f9; border-radius: 4px }
            &#160; h4 span { color: white }
            &#160; .attributes { margin-left: 22px; font-size: 90% }
            &#160; .attributes p { margin-left: 16px; font-style: italic }
            &#160; </style>
            &#160; <details>
            &#160;&#160;&#160; <summary>
            &#160;&#160;&#160;&#160;&#160; <span>
                    <code class="name">&lt;<slot name="element-name">NEED NAME</slot>&gt;</code>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; <i class="desc"><slot name="description">NEED DESCRIPTION</slot></i>
            &#160;&#160;&#160;&#160;&#160; </span>
            &#160;&#160;&#160; </summary>
            &#160;&#160;&#160; <div class="attributes">
            &#160;&#160;&#160;&#160;&#160; <h4><span>Attributes</span></h4>
            &#160;&#160;&#160;&#160;&#160; <slot name="attributes"><p>None</p></slot>
            &#160;&#160;&#160; </div>
            &#160; </details>
            &#160; <hr>
            </template>
            <element-details>
              <span slot="element-name">slot</span>
              <span slot="description">A placeholder inside a web
                component that users can fill with their own markup,
                with the effect of composing different DOM trees
                together.</span>
              <dl slot="attributes">
                <dt>name</dt>
                <dd>The name of the slot.</dd>
              </dl>
            </element-details>
            
            <element-details>
              <span slot="element-name">template</span>
              <span slot="description">A mechanism for holding client-
                side content that is not to be rendered when a page is
                loaded but may subsequently be instantiated during
                runtime using JavaScript.</span>
            </element-details> 
            </article>
        
        Notes:
        
        
    """

class template(Component):
    """
        The **HTML <template> element** is a mechanism for holding client-side
        content that is not to be rendered when a page is loaded but may
        subsequently be instantiated during runtime using JavaScript.
        
        Think of a template as a content fragment that is being stored for
        subsequent use in the document. While the parser does process the
        contents of the **<template>** element while loading the page, it does
        so only to ensure that those contents are valid; the element's
        contents are not rendered, however.
        
        Examples::
        
            <article><table id="producttable">
              <thead>
                <tr>
                  <td>UPC_Code</td>
                  <td>Product_Name</td>
                </tr>
              </thead>
              <tbody>
                <!-- existing data could optionally be included here -->
              </tbody>
            </table>
            
            <template id="productrow">
              <tr>
                <td class="record"></td>
                <td></td>
              </tr>
            </template> 
            </article>
        
        Notes:
        
        
    """



# == Obsolete and deprecated elements ==
# **Warning:** These are old HTML elements which are deprecated and should not
# be used. **You should never use them in new projects, and should replace them
# in old projects as soon as you can.** They are listed here for informational
# purposes only.
class acronym(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class applet(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.The HTML Applet Element (``<applet>``) identifies the
        inclusion of a Java applet.
        
        **Note**: The ``<applet>`` element was removed in Gecko 56 and Chrome
        in late 2015. Removal is being considered in WebKit and Edge.
        
        Examples::
        
            <article><applet code="game.class" align="left" archive="game.zip" height="250" width="350">
              <param name="difficulty" value="easy">
              <b>Sorry, you need Java to play this game.</b>
            </applet>
            </article>
        
        Notes:
        
            The W3C specification does not encourage the use of ``<applet>`` and
            prefers the use of the ``<object>`` tag. Under the strict definition
            of HTML 4.01, this element is deprecated and entirely obsolete in
            HTML5.
    """

class basefont(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
            * HTML 3.2 supports the basefont element but only with the size
            attribute.
            
            * The strict HTML and XHTML specifications do not support this
            element.
            
            * Despite being part of transitional standards, some standards-focused
            browsers like Mozilla and Opera do not support this element.
            
            * This element can be imitated with a CSS rule on the ``<body>``
            element.
            
            * XHTML 1.0 requires a trailing slash for this element: ``<basefont
            />``.
    """

class big(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class blink(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.The **HTML Blink Element** (``<blink>``) is a non-
        standard element causing the enclosed text to flash slowly.
        
        Do not use this element as it is **obsolete** and bad design practice.
        Blinking text is frowned upon by several accessibility standards and
        the CSS specification allows browsers to ignore the blink value.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class center(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        Examples::
        
            <article></article>
        
        Notes:
        
            Applying ``text-align````:center`` to a ``<div>`` or ``<p>`` element
            centers the *contents* of those elements while leaving their overall
            dimensions unchanged.
    """

class command(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.**Note:** The ``command`` element has been removed from
        Gecko 24.0 in favor of the ``<menuitem>`` element. Firefox has never
        supported this ``command`` element, and the existing implementation of
        the ``HTMLCommandElement`` DOM interface has been dropped from
        Firefox 24.
        
        Examples::
        
            <article><command type="command" label="Save" icon="icons/save.png" onclick="save()">
            </command></article>
        
        Notes:
        
        
    """

# content: see above under "Web Components"
# FIXME: invalid syntax (<unknown>, line 15)
# class dir_(Component):"""
#         **** Obsolete**
#         
#         This feature is obsolete. Although it may still work in some browsers,
#         its use is discouraged since it could be removed at any time. Try to
#         avoid using it.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'dir'
# element: see above under "Web Components"
class font(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class frame(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        Examples::
        
            <article><frameset cols="50%,50%">
              <frame src="https://developer.mozilla.org/en/HTML/Element/iframe">
              <frame src="https://developer.mozilla.org/en/HTML/Element/frame">
            </frameset>
            </article>
        
        Notes:
        
        
    """

class frameset(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class image(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.**** Non-standard**
        
        This feature is non-standard and is not on a standards track. Do not
        use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between
        implementations and the behavior may change in the future.
        
        The HTML ``<image>`` element is an obsolete remnant of an ancient
        version of HTML lost in the mists of time; use the standard ``<img>``
        element instead. Seriously, the specification even literally uses the
        words "Don't ask" when describing this element.
        
        **Do not use this!** In order to display images, use the standard
        ``<img>`` element.
        
        While browsers will attempt to automatically convert this into an
        ``<img>`` element, it won't always do so, and won't always succeed
        when it tries, due to the various ways this can happen. So just don't
        use it if you like your users.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class isindex(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article>
              <isindex prompt="Search Document... ">
            </article>
        
        Notes:
        
        
    """

class keygen(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        The HTML ``<keygen>`` element exists to facilitate generation of key
        material, and submission of the public key as part of an HTML form.
        This mechanism is designed for use with Web-based certificate
        management systems. It is expected that the ``<keygen>`` element will
        be used in an HTML form along with other information needed to
        construct a certificate request, and that the result of the process
        will be a signed certificate.
        
        There is currently discussion among Web browser makers whether to keep
        this feature or not. Until a decision is reached, it is better to
        continue to consider this feature as deprecated and going away.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class listing(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class marquee(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        The HTML ``<marquee>`` element is used to insert a scrolling area of
        text. You can control what happens when the text reaches the edges of
        its content area using its attributes.
        
        The ``<marquee>`` element is **obsolete** and must not be used. While
        some browsers still support it, it's not required.
        
        Examples::
        
            <article><marquee>This text will scroll from right to left</marquee>
            
            <marquee direction="up">This text will scroll from bottom to top</marquee>
            
            <marquee direction="down" width="250" height="200" behavior="alternate" style="border:solid">
              <marquee behavior="alternate">
                This text will bounce
              </marquee>
            </marquee></article>
        
        Notes:
        
        
    """

class multicol(Component):
    """
        **** Non-standard**
        
        This feature is non-standard and is not on a standards track. Do not
        use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between
        implementations and the behavior may change in the future.
        
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class nextid(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.
        
        Examples::
        
            <article>
                
                    <title> ... whatever ... </title>
                    <link meta base etc. as applicable for the head of this document>
                    <nextid n="z20">
                
                
                
                    <a name="z0" href="#z4">FIRST SECTION HEADING</a>
                    <a name="z1" href="#z5">SECOND SECTION HEADING</a>
                    <a name="z8" href="#z14">NEWLY INSERTED THIRD SECTION HEADING</a>
                    <a name="z9" href="#z15">NEWLY INSERTED FOURTH SECTION HEADING</a>
                    <a name="z2" href="#z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</a>
                    <a name="z3" href="#z7">ORIGINAL FOURTH (NOW SIXTH) SECTION HEADING</a>
                    <a name="z10" href="#z16">SEVENTH SECTION HEADING</a>
                    <a name="z11" href="#z17">EIGHTH SECTION HEADING</a>
                    <a name="z12" href="#z18">NINTH SECTION HEADING</a>
                    <a name="z13" href="#z19">TENTH SECTION HEADING</a>
                    <h2><a name="z4">FIRST SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z5">SECOND SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z14">NEWLY INSERTED THIRD SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z15">NEWLY INSERTED FOURTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z7">ORIGINAL FOURTH (NOW SIXTH) SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z16">SEVENTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z17">EIGHTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z18">NINTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z19">TENTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                
            
            
                
                    <title> ... whatever ... </title>
                    <link meta base etc. as applicable for the head of this document>
                    <nextid n="z30">
                
            
                
                    <a name="z0" href="#z4">FIRST SECTION HEADING</a>
                    <a name="z1" href="#z5">SECOND SECTION HEADING</a>
                    <a name="z8" href="#z14">NEWLY INSERTED THIRD SECTION HEADING</a>
                    <a name="z9" href="#z15">NEWLY INSERTED FOURTH SECTION HEADING</a>
                    <a name="z2" href="#z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</a>
                    <a name="z10" href="#z16">SEVENTH (NOW SIXTH) SECTION HEADING</a>
                    <a name="z11" href="#z17">EIGHTH (NOW SEVENTH) SECTION HEADING</a>
                    <a name="z12" href="#z18">NINTH (NOW EIGHTH) SECTION HEADING</a>
                    <a name="z20" href="#z25">NEW NINTH SECTION HEADING</a>
                    <a name="z21" href="#z26">NEW TENTH SECTION HEADING</a>
                    <a name="z22" href="#z27">NEW ELEVENTH SECTION HEADING</a>
                    <a name="e23" href="#z28">NEW TWELFTH SECTION HEADING</a>
                    <h2><a name="z4">FIRST SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z5">SECOND SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z14">NEWLY INSERTED THIRD SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z15">NEWLY INSERTED FOURTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z6">ORIGINAL THIRD (NOW FIFTH) SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z16">SEVENTH (NOW SIXTH) SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z17">EIGHTH (NOW SEVENTH) SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z18">NINTH (NOW EIGHTH) SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z25">NEW NINTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z26">NEW TENTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z27">NEW ELENENTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                    <h2><a name="z28">NEW TWELFTH SECTION HEADING</a></h2>
            <p> ... whatever ... </p>
                
            
            </nextid></nextid></article>
        
        Notes:
        
        
    """

class noembed(Component):
    """
        **** Non-standard**
        
        This feature is non-standard and is not on a standards track. Do not
        use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between
        implementations and the behavior may change in the future.
        
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The
        ``<noembed>`` element is a deprecated and non-standard way to provide
        alternative, or "fallback", content for browsers that do not support
        the ``<embed>`` element or do not support embedded content an author
        wishes to use. This element was deprecated in HTML 4.01 and above in
        favor of  ``<object>``. Fallback content should be inserted between
        the opening and closing ``<object>`` tags.
        
        While this element currently still works in many browsers, it has been
        deprecated and should not be used. Use ``<object>`` instead.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class plaintext(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# shadow: see above under "Web Components"
class spacer(Component):
    """
        **** Non-standard**
        
        This feature is non-standard and is not on a standards track. Do not
        use it on production sites facing the Web: it will not work for every
        user. There may also be large incompatibilities between
        implementations and the behavior may change in the future.
        
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.**<spacer>** is an obsolete HTML element which allowed
        insertion of empty spaces on pages. It was devised by Netscape to
        accomplish the same effect as a single-pixel layout image, which was
        something web designers used to use to add white spaces to web pages
        without actually using an image. However, ``<spacer>`` no longer
        supported by any major browser and the same effects can now be
        achieved using simple CSS.
        
        Firefox, which is the descendant of Netscape's browsers, removed
        support for ``<spacer>`` in version 4.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class strike(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class tt(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
            * A CSS rule can be defined for the ``tt`` selector to override the
            browser's default font face. Preferences set by the user might take
            precedence over the specified CSS.
            
            * Although this element was not deprecated in the HTML 4.01
            specification, its use is discouraged in favor of style sheets.
    """

class xmp(Component):
    """
        **** Obsolete**
        
        This feature is obsolete. Although it may still work in some browsers,
        its use is discouraged since it could be removed at any time. Try to
        avoid using it.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



__all__ = [
    'html', 'link', 'meta', 'style', 'body', 'address', 'article', 'aside',
    'footer', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup', 'nav',
    'section', 'blockquote', 'dd', 'div', 'dl', 'dt', 'figcaption', 'figure',
    'hr', 'li', 'main', 'ol', 'p', 'pre', 'ul', 'a', 'abbr', 'b', 'bdi', 'bdo',
    'br', 'cite', 'code', 'data', 'dfn', 'em', 'i', 'kbd', 'mark', 'q', 'rp',
    'rt', 'rtc', 'ruby', 's', 'samp', 'small', 'span', 'strong', 'sub', 'sup',
    'time', 'u', 'var', 'wbr', 'area', 'audio', 'img', 'map', 'track', 'video',
    'embed', 'object', 'param', 'source', 'canvas', 'noscript', 'script',
    'del', 'ins', 'caption', 'col', 'colgroup', 'table', 'tbody', 'td',
    'tfoot', 'th', 'thead', 'tr', 'button', 'datalist', 'fieldset', 'form',
    'input', 'label', 'legend', 'meter', 'optgroup', 'option', 'output',
    'progress', 'select', 'textarea', 'details', 'dialog', 'menu', 'menuitem',
    'summary', 'content', 'element', 'shadow', 'slot', 'template', 'acronym',
    'applet', 'basefont', 'big', 'blink', 'center', 'command', 'dir', 'font',
    'frame', 'frameset', 'image', 'isindex', 'keygen', 'listing', 'marquee',
    'multicol', 'nextid', 'noembed', 'plaintext', 'spacer', 'strike', 'tt',
    'xmp'
]

