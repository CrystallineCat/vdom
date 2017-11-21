# -*- coding: utf-8 -*-
from vdom.core import Component

# From https://developer.mozilla.org/en-US/docs/Web/SVG/Element


# == Animation elements ==
class animate(Component):
    """
        The ``animate`` element is put inside a shape element and defines how
        an attribute of an element changes over the animation. The attribute
        will change from the initial value to the end value in the duration
        specified.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class animateColor(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.This element
        has been deprecated in SVG 1.1 Second Edition and may be removed in a
        future version of SVG. It provides no features not already available
        by using the ``<animate>`` element. So, authors should use the
        ``<animate>`` element instead.
        
        The **<animateColor>** SVG element specifies a color transformation
        over time.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class animateMotion(Component):
    """
        The **<animateMotion>** element causes a referenced element to move
        along a motion path.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class animateTransform(Component):
    """
        The ``animateTransform`` element animates a transformation attribute
        on a target element, thereby allowing animations to control
        translation, scaling, rotation and/or skewing.
        
        Examples::
        
            <article><?xml version="1.0"?>
            <svg width="120" height="120" viewbox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink">
            
                <polygon points="60,30 90,90 30,90">
                    <animatetransform attributename="transform" attributetype="XML" type="rotate" from="0 60 70" to="360 60 70" dur="10s" repeatcount="indefinite"></animatetransform>
                </polygon>
            </svg></article>
        
        Notes:
        
        
    """

class discard(Component):
    """
        The **<discard>** SVG element allows authors to specify the time at
        which particular elements are to be discarded, thereby reducing the
        resources required by an SVG user agent. This is particularly useful
        to help SVG viewers conserve memory while displaying long-running
        documents.
        
        The ``<discard>`` element may occur wherever the ``<animate>`` element
        may.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class mpath(Component):
    """
        The **<mpath>** sub-element for the ``<animateMotion>`` element
        provides the ability to reference an external ``<path>`` element as
        the definition of a motion path.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 16)
# class set_(Component):"""
#         The **<set>** element provides a simple means of just setting the
#         value of an attribute for a specified duration. It supports all
#         attribute types, including those that cannot reasonably be
#         interpolated, such as string and boolean values. The ``<set>`` element
#         is non-additive. The additive and accumulate attributes are not
#         allowed, and will be ignored if specified.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'set'


# == Basic shapes ==
class circle(Component):
    """
        The **<circle>** SVG element is an SVG basic shape, used to create
        circles based on a center point and a radius.
        
        Examples::
        
            <article><svg viewbox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            &#160; <circle cx="100" cy="100" r="100"></circle>
            </svg></article>
        
        Notes:
        
        
    """

class ellipse(Component):
    """
        The ``ellipse`` element is an SVG basic shape, used to create ellipses
        based on a center coordinate, and both their x and y radius.
        
        Ellipses are unable to specify the exact orientation of the ellipse
        (if, for example, you wanted to draw an ellipse tilted at a 45 degree
        angle), but can be rotated by using the ``transform`` attribute.
        
        Examples::
        
            <article><svg width="120" height="120" viewbox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
            
              <ellipse cx="60" cy="60" rx="50" ry="25"></ellipse>
            </svg>
            </article>
        
        Notes:
        
        
    """

class line(Component):
    """
        The **<line>** element is an SVG basic shape used to create a line
        connecting two points.
        
        Examples::
        
            <article><svg width="120" height="120" viewbox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
            
              <line x1="20" y1="100" x2="100" y2="20" stroke-width="2" stroke="black"></line>
            </svg><svg width="120" height="120" viewbox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
              <line x1="20" y1="100" x2="100" y2="100" stroke-width="2" stroke="black" transform="rotate(-45 20 100)"></line>
            </svg>
            </article>
        
        Notes:
        
        
    """

class polygon(Component):
    """
        The **<polygon>** element defines a closed shape consisting of a set
        of connected straight line segments. The last point is connected to
        the first point. For open shapes see the ``<polyline>`` element.
        
        Examples::
        
            <article><svg width="120" height="120" viewbox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
            
              <polygon points="60,20 100,40 100,80 60,100 20,80 20,40"></polygon>
            </svg></article>
        
        Notes:
        
        
    """

class polyline(Component):
    """
        The **<polyline>** SVG element is an SVG basic shape that creates
        straight lines connecting several points. Typically a ``polyline`` is
        used to create open shapes as the last point doesn't have to be
        connected to the first point. For closed shapes see the ``<polygon>``
        element.
        
        Examples::
        
            <article><svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">
              <polyline fill="none" stroke="black" points="20,100 40,60 70,80 100,20"></polyline>
            </svg> <div class="contain-demo">
             &#160; <svg width="150" height="200">
             &#160;&#160;&#160; <desc>
                   First orange polyline demonstrating
                   white fill on open path.
                 </desc>
             &#160;&#160;&#160; <polyline points="0,40 40,40 40,80 80,80 80,120 120,120 120,160" fill="white" stroke="#D07735" stroke-width="6"></polyline>
             &#160; </svg>
             &#160; <svg width="150" height="200">
             &#160;&#160;&#160; <desc>
                   Second orange polyline demonstrating
                   yellow fill on open path.
                 </desc>
             &#160;&#160;&#160; <polyline points="0,40 40,40 40,80 80,80 80,120 120,120 120,160" fill="#F9F38C" stroke="#D07735" stroke-width="6"></polyline>
             &#160; </svg>
             </div>
            <p class="p">
              Demo by Joni Trythall.
              <a href="http://sitepoint.com/understanding-svg-fill-rule-property">See article</a>.
            </p>
            </article>
        
        Notes:
        
        
    """

class rect(Component):
    """
        The **<rect>** element is a basic SVG shape that creates rectangles,
        defined by their corner's position, their width, and their height. The
        rectangles may have their corners rounded.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Container elements ==
class a(Component):
    """
        The **<a>** SVG element defines a hyperlink.
        
        Since this element shares its tag name with HTML's ``<a>`` element,
        selecting "``a``" with CSS or ``querySelector`` may apply to the wrong
        kind of element. Try the ``@namespace`` rule to distinguish between
        the two.
        
        Examples::
        
            <article><svg width="140" height="30" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            
              <a href="https://developer.mozilla.org/en-US/docs/SVG" target="_blank">
                <rect height="30" width="120" y="0" x="0" rx="15"></rect>
                <text fill="white" text-anchor="middle" y="21" x="60">SVG on MDN</text>
              </a>
            </svg></article>
        
        Notes:
        
        
    """

class defs(Component):
    """
        SVG allows graphical objects to be defined for later reuse. It is
        recommended that, wherever possible, referenced elements be defined
        inside of a **<defs>** element. Defining these elements inside of a
        ``<defs>`` element promotes understandability of the SVG content and
        thus promotes accessibility. Graphical elements defined in a
        ``<defs>`` element will not be directly rendered. You can use a
        ``<use>`` element to render those elements wherever you want on the
        viewport.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class g(Component):
    """
        The **<g>** SVG element is a container used to group other SVG
        elements. Transformations applied to the ``<g>`` element are performed
        on all of its child elements, and any of its attributes are inherited
        by its child elements. It can also group multiple elements to be
        referenced later with the ``<use>`` element.
        
        Examples::
        
            <article><svg viewbox="0 0 95 50" xmlns="http://www.w3.org/2000/svg">
               <g stroke="green" fill="white" stroke-width="5">
                 <circle cx="25" cy="25" r="15"></circle>
                 <circle cx="40" cy="25" r="15"></circle>
                 <circle cx="55" cy="25" r="15"></circle>
                 <circle cx="70" cy="25" r="15"></circle>
               </g>
            </svg>
            </article>
        
        Notes:
        
        
    """

class marker(Component):
    """
        The **<marker>** element defines the graphics that is to be used for
        drawing arrowheads or polymarkers on a given ``<path>``, ``<line>``,
        ``<polyline>`` or ``<polygon>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class mask(Component):
    """
        In SVG, you can specify that any other graphics object or ``<g>``
        element can be used as an alpha mask for compositing the current
        object into the background. A mask is defined with the **<mask>**
        element. A mask is used/referenced using the ``mask`` property.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 19)
# class missing_glyph(Component):"""
#         **** Deprecated**
#         
#         This feature has been removed from the Web standards. Though some
#         browsers may still support it, it is in the process of being dropped.
#         Avoid using it and update existing code if possible; see the
#         compatibility table at the bottom of this page to guide your decision.
#         Be aware that this feature may cease to work at any time.The
#         **<missing-glyph>** SVG element's content is rendered, if for a given
#         character the font doesn't define an appropriate ``<glyph>``.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'missing-glyph'
class pattern(Component):
    """
        The **<pattern>** element defines a graphics object which can be
        redrawn at repeated x and y-coordinate intervals ("tiled") to cover an
        area. The ``<pattern>`` is referenced by the ``fill`` and/or
        ``stroke`` attributes on other graphics elements to fill or stroke
        those elements with the referenced pattern.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class svg(Component):
    """
        The ``svg`` element can be used to embed an SVG fragment inside the
        current document (for example, an HTML document). This SVG fragment
        has its own viewport and coordinate system.
        
        Examples::
        
            <article>
            
            
              <meta charset="UTF-8">
              <title>HTML/SVG Example</title>
            
            
            
            
              <svg xmlns="http://www.w3.org/2000/svg" width="150" height="100" viewbox="0 0 3 2">
                <rect width="1" height="2" x="0" fill="#008d46"></rect>
                <rect width="1" height="2" x="1" fill="#ffffff"></rect>
                <rect width="1" height="2" x="2" fill="#d2232c"></rect>
              </svg>
            
            
            </article>
        
        Notes:
        
        
    """

class switch(Component):
    """
        The **<switch>** SVG element evaluates the ``requiredFeatures``,
        ``requiredExtensions`` and ``systemLanguage`` attributes on its direct
        child elements in order, and then processes and renders the first
        child for which these attributes evaluate to true. All others will be
        bypassed and therefore not rendered. If the child element is a
        container element such as a ``<g>``, then the entire subtree is either
        processed/rendered or bypassed/not rendered.
        
        Note that the values of properties ``display`` and ``visibility`` have
        no effect on ``switch`` element processing. In particular, setting
        ``display`` to none on a child of a ``switch`` element has no effect
        on true/false testing associated with ``switch`` element processing.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class symbol(Component):
    """
        The **<symbol>** element is used to define graphical template objects
        which can be instantiated by a ``<use>`` element. The use of
        ``symbol`` elements for graphics that are used multiple times in the
        same document adds structure and semantics. Documents that are rich in
        structure may be rendered graphically, as speech, or as Braille, and
        thus promote accessibility. Note that a ``symbol`` element itself is
        not rendered. Only instances of a ``symbol`` element (i.e., a
        reference to a ``symbol`` by a ``<use>`` element) are rendered.
        
        Examples::
        
            <article><svg width="120" height="140">
            <!-- symbol definition&#160; NEVER draw -->
            <symbol id="sym01" viewbox="0 0 150 110">
            &#160; <circle cx="50" cy="50" r="40" stroke-width="8" stroke="red" fill="red"></circle>
            &#160; <circle cx="90" cy="60" r="40" stroke-width="8" stroke="green" fill="white"></circle>
            </symbol>
            
            <!-- actual drawing by "use" element -->
            <use href="#sym01" x="0" y="0" width="100" height="50"></use>
            <use href="#sym01" x="0" y="50" width="75" height="38"></use>
            <use href="#sym01" x="0" y="100" width="50" height="25"></use>
            </svg>
            </article>
        
        Notes:
        
        
    """

class unknown(Component):
    ''



# == Descriptive elements ==
class desc(Component):
    """
        Each container element or graphics element in an SVG drawing can
        supply a description string using the **<desc>** element where the
        description is text-only.
        
        When the current SVG document fragment is rendered as SVG on visual
        media, ``<desc>`` elements are not rendered as part of the graphics.
        Alternate presentations are possible, both visual and aural, which
        display the ``<desc>`` element but do not display ``<path>`` elements
        or other graphics elements. The ``<desc>`` element generally improves
        accessibility of SVG documents.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class metadata(Component):
    """
        The **<metadata>** SVG element allows to add metadata to SVG content.
        Metadata is structured information about data. The contents of
        ``<metadata>`` elements should be elements from other XML namespaces
        such as RDF, FOAF, etc.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class title(Component):
    """
        Each container element or graphics element in an SVG drawing can
        supply a **<title>** element containing a description string where the
        description is text-only. When the current SVG document fragment is
        rendered as SVG on visual media, ``<title>`` element is not rendered
        as part of the graphics. However, some user agents may, for example,
        display the ``<title>`` element as a tooltip. Alternate presentations
        are possible, both visual and aural, which display the ``<title>``
        element but do not display ``path`` elements or other graphics
        elements. The ``<title>`` element generally improves accessibility of
        SVG documents.
        
        Generally ``<title>`` element should be the first child element of its
        parent. Note that those implementations that do use ``<title>`` to
        display a tooltip often will only do so if the ``<title>`` is indeed
        the first child element of its parent.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Filter primitive elements ==
class feBlend(Component):
    """
        The **<feBlend>** SVG filter primitive composes two objects together
        ruled by a certain blending mode. This is similar to what is known
        from image editing software when blending two layers. The mode is
        defined by the ``mode`` attribute.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feColorMatrix(Component):
    """
        The **<feColorMatrix>** SVG filter element changes colors based on a
        transformation matrix. Every pixel's color value (represented by an
        [R,G,B,A] vector) is matrix multiplied to create a new color.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feComponentTransfer(Component):
    """
        Th **<feComponentTransfer>** SVG filter primitive performs color-
        component-wise remapping of data for each pixel. It allows operations
        like brightness adjustment, contrast adjustment, color balance or
        thresholding.
        
        The calculations are performed on non-premultiplied color values. The
        colors are modified by changing each channel (R, G, B, and A) to the
        result of what the children ``<feFuncR>``, ``<feFuncB>``,
        ``<feFuncG>``, and ``<feFuncA>`` return.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feComposite(Component):
    """
        This filter primitive performs the combination of two input images
        pixel-wise in image space using one of the Porter-Duff compositing
        operations: ``over``*,* ``in``*,* ``atop``*,* ``out``*,* ``xor`` and
        ``lighter``. Additionally, a component-wise ``arithmetic`` operation
        (with the result clamped between [0..1]) can be applied.
        
        The ``arithmetic`` operation is useful for combining the output from
        the ``<feDiffuseLighting>`` and ``<feSpecularLighting>`` filters with
        texture data. If the ``arithmetic`` operation is chosen, each result
        pixel is computed using the following formula:
        
        result = k1*i1*i2 + k2*i1 + k3*i2 + k4
        
        where:
        
        * ``i1`` and ``i2`` indicate the corresponding pixel channel values of
        the input image, which map to ``in`` and ``in2`` respectively
        
        * ``k1, k2, k3`` and ``k4`` indicate the values of the attributes with
        the same name
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feConvolveMatrix(Component):
    """
        The **<feConvolveMatrix>** SVG filter primitive applies a matrix
        convolution filter effect. A convolution combines pixels in the input
        image with neighboring pixels to produce a resulting image. A wide
        variety of imaging operations can be achieved through convolutions,
        including blurring, edge detection, sharpening, embossing and
        beveling.
        
        A matrix convolution is based on an n-by-m matrix (the convolution
        kernel) which describes how a given pixel value in the input image is
        combined with its neighboring pixel values to produce a resulting
        pixel value. Each result pixel is determined by applying the kernel
        matrix to the corresponding source pixel and its neighboring pixels.
        The basic convolution formula which is applied to each color value for
        a given pixel is:
        
        COLORX,Y = (                SUM I=0 to [orderY-1] { 
                        SUM J=0 to [orderX-1] {                    SOURCE X-ta
        rgetX+J, Y-targetY+I *  kernelMatrixorderX-J-1,  orderY-I-1 
                        }                } 
                    ) /  divisor +  bias * ALPHAX,Y 
        
        where "orderX" and "orderY" represent the X and Y values for
        the ‘order’ attribute, "targetX" represents the value of
        the ‘targetX’ attribute, "targetY" represents the value of
        the ‘targetY’ attribute, "kernelMatrix" represents the value of
        the ‘kernelMatrix’ attribute, "divisor" represents the value of
        the ‘divisor’ attribute, and "bias" represents the value of
        the ‘bias’ attribute.
        
        Note in the above formulas that the values in the kernel matrix are
        applied such that the kernel matrix is rotated 180 degrees relative to
        the source and destination images in order to match convolution theory
        as described in many computer graphics textbooks.
        
        To illustrate, suppose you have a input image which is 5 pixels by 5
        pixels, whose color values for one of the color channels are as
        follows:
        
        <pre>    0  20  40 235 235   100 120 140 235 235   200 220 240 235 235
        225 225 255 255 255   225 225 255 255 255 </pre> and you define a
        3-by-3 convolution kernel as follows:
        
        <pre>  1 2 3   4 5 6   7 8 9 </pre> Let's focus on the color value at
        the second row and second column of the image (source pixel value is
        120). Assuming the simplest case (where the input image's pixel grid
        aligns perfectly with the kernel's pixel grid) and assuming default
        values for attributes ‘divisor’, ‘targetX’ and ‘targetY’, then
        resulting color value will be:
        
        <pre>(9*  0 + 8* 20 + 7* 40 + 6*100 + 5*120 + 4*140 + 3*200 + 2*220 +
        1*240) / (9+8+7+6+5+4+3+2+1)</pre>
        
        Examples::
        
            <article><svg viewbox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <defs>
                <filter id="emboss">
                  <feconvolvematrix kernelmatrix="3 0 0
                                    0 0 0
                                    0 0 -3"></feconvolvematrix>
                </filter>
              </defs>
            
              <image xlink:href="/files/12668/MDN.svg" x="0" y="0" height="200" width="200" style="filter:url(#emboss);"></image>
            </svg></article>
        
        Notes:
        
        
    """

class feDiffuseLighting(Component):
    """
        The **<feDiffuseLighting>** SVG filter primitive lights an image using
        the alpha channel as a bump map. The resulting image, which is an RGBA
        opaque image, depends on the light color, light position and surface
        geometry of the input bump map.
        
        The light map produced by this filter primitive can be combined with a
        texture image using the multiply term of the ``arithmetic`` operator
        of the ``<feComposite>`` filter primitive. Multiple light sources can
        be simulated by adding several of these light maps together before
        applying it to the texture image.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feDisplacementMap(Component):
    """
        The **<feDisplacementMap>** SVG filter primitive uses the pixel values
        from the image from ``in2`` to spatially displace the image from
        ``in``.
        
        The formula for the transformation looks like this:
        
        ``P'(x,y) ← P( x + scale * (XC(x,y) - 0.5), y + scale * (YC(x,y) -
        0.5))``
        
        where ``P(x,y)`` is the input image, ``in``, and ``P'(x,y)`` is the
        destination. ``XC(x,y)`` and ``YC(x,y)`` are the component values of
        the channel designated by ``xChannelSelector`` and
        ``yChannelSelector``.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feDropShadow(Component):
    """
        The **<feDropShadow>** filter primitive creates a drop shadow of the
        input image. It is a shorthand filter, and is defined in terms of
        combinations of other filter primitives.
        
        The result of the ``<feDropShadow>`` filter is equivalent to the
        following:
        
        <feGaussianBlur in="alpha-channel-of-feDropShadow-in"
        stdDeviation="stdDeviation-of-feDropShadow"/> <feOffset dx="dx-of-
        feDropShadow" dy="dy-of-feDropShadow" result="offsetblur"/> <feFlood
        flood-color="flood-color-of-feDropShadow" flood-opacity="flood-
        opacity-of-feDropShadow"/> <feComposite in2="offsetblur"
        operator="in"/> <feMerge> <feMergeNode/> <feMergeNode in="in-of-
        feDropShadow"/> </feMerge>
        
        Examples::
        
            <article><svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <filter id="shadow">
                  <fedropshadow dx="4" dy="8" stddeviation="4"></fedropshadow>
                </filter>
              </defs>
            
              <circle cx="50%" cy="50%" r="80" style="fill:blue; filter:url(#shadow);"></circle>
            </svg></article>
        
        Notes:
        
        
    """

class feFlood(Component):
    """
        The **<feFlood>** SVG filter primitive fills the filter subregion with
        the color and opacity defined by ``flood-color`` and ``flood-
        opacity``.
        
        Examples::
        
            <article><svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
              <defs>
                <filter id="floodFilter" filterunits="userSpaceOnUse">
                  <feflood x="50" y="50" width="100" height="100" flood-color="green" flood-opacity="0.5"></feflood>
                </filter>
              </defs>
            
              <use style="filter: url(#floodFilter);"></use>
            </svg></article>
        
        Notes:
        
        
    """

class feFuncA(Component):
    """
        The **<feFuncA>** SVG filter primitive defines the transfer function
        for the alpha component of the input graphic of its parent
        ``<feComponentTransfer>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feFuncB(Component):
    """
        The **<feFuncB>** SVG filter primitive defines the transfer function
        for the blue component of the input graphic of its parent
        ``<feComponentTransfer>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feFuncG(Component):
    """
        The **<feFuncG>** SVG filter primitive defines the transfer function
        for the green component of the input graphic of its parent
        ``<feComponentTransfer>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feFuncR(Component):
    """
        The ``<feFuncR>`` SVG filter primitive defines the transfer function
        for the red component of the input graphic of its parent
        ``<feComponentTransfer>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feGaussianBlur(Component):
    """
        The **<feGaussianBlur>** SVG filter primitive blurs the input image by
        the amount specified in ``stdDeviation``, which defines the bell-
        curve.
        
        Examples::
        
            <article><svg width="230" height="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            
              <filter id="blurMe">
                <fegaussianblur in="SourceGraphic" stddeviation="5"></fegaussianblur>
              </filter>
            
              <circle cx="60" cy="60" r="50" fill="green"></circle>
            
              <circle cx="170" cy="60" r="50" fill="green" filter="url(#blurMe)"></circle>
            </svg><svg width="120" height="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            
              <filter id="dropShadow">
                <fegaussianblur in="SourceAlpha" stddeviation="3"></fegaussianblur>
                <feoffset dx="2" dy="4"></feoffset>
                <femerge>
                    <femergenode></femergenode>
                    <femergenode in="SourceGraphic"></femergenode>
                </femerge>
              </filter>
            
              <circle cx="60" cy="60" r="50" fill="green" filter="url(#dropShadow)"></circle>
            </svg></article>
        
        Notes:
        
        
    """

class feImage(Component):
    """
        The **<feImage>** SVG filter primitive fetches image data from an
        external source and provides the pixel data as output (meaning if the
        external source is an SVG image, it is rasterized.)
        
        Examples::
        
            <article><svg viewbox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <defs>
                <filter id="image">
                  <feimage xlink:href="/files/6457/mdn_logo_only_color.png"></feimage>
                </filter>
              </defs>
            
              <rect x="10%" y="10%" width="80%" height="80%" style="filter:url(#image);"></rect>
            </svg></article>
        
        Notes:
        
        
    """

class feMerge(Component):
    """
        The **<feMerge>** SVG element allows filter effects to be applied
        concurrently instead of sequentially. This is achieved by other
        filters storing their output via the ``result`` attribute and then
        accessing it in a ``<feMergeNode>`` child.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feMergeNode(Component):
    """
        The ``feMergeNode`` takes the result of another filter to be processed
        by its parent ``<feMerge>``.
        
        Examples::
        
            <article><svg width="200" height="200">
            
            
            &#160; &#160; <filter id="feOffset" x="-40" y="-20" width="100" height="200">
            &#160; &#160; &#160; &#160; <feoffset in="SourceGraphic" dx="60" dy="60"></feoffset>
            &#160; &#160; &#160; &#160; <fegaussianblur in="SourceGraphic" stddeviation="5"></fegaussianblur>
            &#160; &#160; &#160; &#160; <femerge>
            &#160; &#160; &#160; &#160; &#160; &#160; <femergenode in="blur2"></femergenode>
            &#160; &#160; &#160; &#160; &#160; &#160; <femergenode in="SourceGraphic"></femergenode>
            &#160; &#160; &#160; &#160; </femerge>
            &#160; &#160; </filter>
            
            <rect x="40" y="40" width="100" height="100" : fill: green filter: url></rect>
            <rect x="40" y="40" width="100" height="100" style="stroke : #000000; fill: green; "></rect>
            &#160; &#160; &#160; </svg>&#160;
            </article>
        
        Notes:
        
        
    """

class feMorphology(Component):
    """
        The **<feMorphology>** SVG filter primitive is used to erode or dilate
        the input image. It's usefulness lies especially in fattening or
        thinning effects.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feOffset(Component):
    """
        The **<feOffset>** SVG filter primitive allows to offset the input
        image. The input image as a whole is offset by the values specified in
        the ``dx`` and ``dy`` attributes.
        
        Examples::
        
            <article><svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <filter id="feOffset" x="-40" y="-20" width="100" height="200">
                  <feoffset in="SourceGraphic" dx="60" dy="60"></feoffset>
                </filter>
              </defs>
            
              <rect x="40" y="40" width="100" height="100" style="stroke : #000000; fill: green; filter: url(#feOffset);"></rect>
              <rect x="40" y="40" width="100" height="100" style="stroke : #000000; fill: green; "></rect>
            </svg>&#160;</article>
        
        Notes:
        
        
    """

class feSpecularLighting(Component):
    """
        The **<feSpecularLighting>** SVG filter primitive lights a source
        graphic using the alpha channel as a bump map. The resulting image is
        an RGBA image based on the light color. The lighting calculation
        follows the standard specular component of the Phong lighting model.
        The resulting image depends on the light color, light position and
        surface geometry of the input bump map. The result of the lighting
        calculation is added. The filter primitive assumes that the viewer is
        at infinity in the z direction.
        
        This filter primitive produces an image which contains the specular
        reflection part of the lighting calculation. Such a map is intended to
        be combined with a texture using the ``add`` term of the arithmetic
        ``<feComposite>`` method. Multiple light sources can be simulated by
        adding several of these light maps before applying it to the texture
        image.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feTile(Component):
    """
        The **<feTile>** SVG filter primitive allows to fill a target
        rectangle with a repeated, tiled pattern of an input image. The effect
        is similar to the one of a ``<pattern>``.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feTurbulence(Component):
    """
        The **<feTurbulence>** SVG filter primitive creates an image using the
        Perlin turbulence function. It allows the synthesis of artificial
        textures like clouds or marble. The resulting image will fill the
        entire filter primitive subregion.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Font elements ==
class font(Component):
    """
        The **<font>** SVG element defines a font to be used for text layout.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 19)
# class font_face(Component):"""
#         **** Deprecated**
#         
#         This feature has been removed from the Web standards. Though some
#         browsers may still support it, it is in the process of being dropped.
#         Avoid using it and update existing code if possible; see the
#         compatibility table at the bottom of this page to guide your decision.
#         Be aware that this feature may cease to work at any time.The **<font-
#         face>** SVG element corresponds to the CSS ``@font-face`` rule. It
#         defines a font's outer properties.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'font-face'
# FIXME: invalid syntax (<unknown>, line 19)
# class font_face_format(Component):"""
#         **** Deprecated**
#         
#         This feature has been removed from the Web standards. Though some
#         browsers may still support it, it is in the process of being dropped.
#         Avoid using it and update existing code if possible; see the
#         compatibility table at the bottom of this page to guide your decision.
#         Be aware that this feature may cease to work at any time.The **<font-
#         face-format>** SVG element describes the type of font referenced by
#         its parent ``<font-face-uri>``.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'font-face-format'
# FIXME: invalid syntax (<unknown>, line 19)
# class font_face_name(Component):"""
#         **** Deprecated**
#         
#         This feature has been removed from the Web standards. Though some
#         browsers may still support it, it is in the process of being dropped.
#         Avoid using it and update existing code if possible; see the
#         compatibility table at the bottom of this page to guide your decision.
#         Be aware that this feature may cease to work at any time.The **<font-
#         face-name>** element points to a locally installed copy of this font,
#         identified by its name.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'font-face-name'
# FIXME: invalid syntax (<unknown>, line 21)
# class font_face_src(Component):"""
#         **** Deprecated**
#         
#         This feature has been removed from the Web standards. Though some
#         browsers may still support it, it is in the process of being dropped.
#         Avoid using it and update existing code if possible; see the
#         compatibility table at the bottom of this page to guide your decision.
#         Be aware that this feature may cease to work at any time.The **<font-
#         face-src>** SVG element corresponds to the ``src`` descriptor in CSS
#         ``@font-face`` rules. It serves as container for ``<font-face-name>``,
#         pointing to locally installed copies of this font, and ``<font-face-
#         uri>``, utilizing remotely defined fonts.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'font-face-src'
# FIXME: invalid syntax (<unknown>, line 19)
# class font_face_uri(Component):"""
#         **** Deprecated**
#         
#         This feature has been removed from the Web standards. Though some
#         browsers may still support it, it is in the process of being dropped.
#         Avoid using it and update existing code if possible; see the
#         compatibility table at the bottom of this page to guide your decision.
#         Be aware that this feature may cease to work at any time.The **<font-
#         face-uri>** SVG element points to a remote definition of the current
#         font.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'font-face-uri'
class hkern(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The
        **<hkern>** SVG element allows to fine-tweak the horizontal distance
        between two glyphs. This process is known as kerning.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class vkern(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The
        **<vkern>** SVG element allows to fine-tweak the vertical distance
        between two glyphs in top-to-bottom fonts. This process is known as
        kerning.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """



# == Gradient elements ==
class linearGradient(Component):
    """
        The **<linearGradient>** SVG element lets authors define linear
        gradients to fill or stroke graphical elements.
        
        Examples::
        
            <article><svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <lineargradient id="MyGradient">
                        <stop offset="5%" stop-color="green"></stop>
                        <stop offset="95%" stop-color="gold"></stop>
                    </lineargradient>
                </defs>
            
                <rect fill="url(#MyGradient)" x="10" y="10" width="100" height="100"></rect>
            </svg></article>
        
        Notes:
        
        
    """

class meshgradient(Component):
    ''

class radialGradient(Component):
    """
        The **<radialGradient>** SVG element lets authors define radial
        gradients to fill or stroke graphical elements.
        
        Examples::
        
            <article><svg width="120" height="120" viewbox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
            
              <defs>
                <radialgradient id="exampleGradient">
                  <stop offset="10%" stop-color="gold"></stop>
                  <stop offset="95%" stop-color="green"></stop>
                </radialgradient>
              </defs>
            
              <circle fill="url(#exampleGradient)" cx="60" cy="60" r="50"></circle>
            </svg></article>
        
        Notes:
        
        
    """

class stop(Component):
    """
        The **<stop>** SVG element defines the ramp of colors to use on a
        gradient, which is a child element to either the ``<linearGradient>``
        or the ``<radialGradient>`` element.
        
        Examples::
        
            <article><svg width="100%" height="100%" viewbox="0 0 80 40" xmlns="http://www.w3.org/2000/svg">
            
              <defs>
                <lineargradient id="MyGradient">
                  <stop offset="5%" stop-color="#F60"></stop>
                  <stop offset="95%" stop-color="#FF6"></stop>
                </lineargradient>
              </defs>
            
              <!-- Outline the drawing area in black -->
              <rect fill="none" stroke="black" x="0.5" y="0.5" width="79" height="39"></rect>
            
              <!-- The rectangle is filled using a linear gradient -->
              <rect fill="url(#MyGradient)" stroke="black" stroke-width="1" x="10" y="10" width="60" height="20"></rect>
            </svg>
            </article>
        
        Notes:
        
        
    """



# == Graphics elements ==
# circle: see above under "Basic shapes"
# ellipse: see above under "Basic shapes"
class image(Component):
    """
        The **<image>** SVG element includes images inside SVG documents. It
        can display raster image files or other SVG files.
        
        The only image formats SVG software must support are JPEG, PNG, and
        other SVG files. Animated GIF behavior is undefined.
        
        SVG files displayed with ``<image>`` are treated as an image: external
        resources aren't loaded, :visited styles aren't applied, and they
        cannot be interactive. To include dynamic SVG elements, try <use> with
        an external URL. To include SVG files and run scripts inside them, try
        <object> inside of <foreignObject>.
        
        **Note:** The HTML spec defines ``<image>`` as a synonym for <img>
        while parsing HTML. This specific element and its behavior only apply
        inside SVG documents or inline SVG.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# line: see above under "Basic shapes"
class mesh(Component):
    ''

class path(Component):
    """
        **Getting started**
        
        This tutorial will help get you started using SVG paths.
        
        The **<path>** SVG element is the generic element to define a shape.
        All the basic shapes can be created with a path element.
        
        Examples::
        
            <article><svg width="100%" height="100%" viewbox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
            
              <path d="M 100 100 L 300 100 L 200 300 z" fill="orange" stroke="black" stroke-width="3"></path>
            </svg>
            </article>
        
        Notes:
        
        
    """

# polygon: see above under "Basic shapes"
# polyline: see above under "Basic shapes"
# rect: see above under "Basic shapes"
class text(Component):
    """
        The SVG **<text>** element defines a graphics element consisting of
        text. It's possible to apply a gradient, pattern, clipping path, mask,
        or filter to ``<text>``, just like any other SVG graphics element.
        
        If text is included within SVG not inside of a ``<text>`` element, it
        is not rendered. This is different from being hidden by default, as
        setting the display property will not show the text.
        
        Examples::
        
            <article><svg xmlns="http://www.w3.org/2000/svg" width="500" height="40" viewbox="0 0 500 40">
            
              <text x="0" y="35" font-family="Verdana" font-size="35">
                Hello, out there
              </text>
            </svg><svg xmlns="http://www.w3.org/2000/svg" width="180" height="120">
              <text x="0" y="20" transform="rotate(30 20,40)">
                SVG Text Rotation example
              </text>
            </svg><svg xmlns="http://www.w3.org/2000/svg" width="200" height="30">
              <text x="10" y="20" stroke="none" fill="red">
                SVG Colored Text
              </text>
            </svg><svg xmlns="http://www.w3.org/2000/svg" width="400" height="60">
              <text x="10" y="40" style="font-family: Times New Roman;
                         font-size: 44px;
                         stroke: #00ff00;
                         fill: #0000ff;">
                SVG text styling
              </text>
            </svg></article>
        
        Notes:
        
        
    """

class use(Component):
    """
        The **<use>** element takes nodes from within the SVG document, and
        duplicates them somewhere else. The effect is the same as if the nodes
        were deeply cloned into a non-exposed DOM, and then pasted where the
        ``use`` element is, much like cloned template elements in HTML5. Since
        the cloned nodes are not exposed, care must be taken when using CSS to
        style a ``use`` element and its hidden descendants. CSS attributes are
        not guaranteed to be inherited by the hidden, cloned DOM unless you
        explicitly request it using CSS inheritance.
        
        For security reasons, some browsers could apply a same-origin policy
        on ``use`` elements and could refuse to load a cross-origin URI within
        the ``href`` attribute.
        
        Since SVG 2, the ``xlink:href`` attribute is deprecated. See
        ``xlink:href`` page for more information.
        
        Examples::
        
            <article></article>
        
        Notes:
        
            * For years, Firefox has suffered from a bug whereby it doesn't
            completely follow the ``<svg:use>`` cascading rules (see bug 265894).
            A fix is documented by Amelia Bellamy-Royds on StackOverflow. The good
            news is that this is finally fixed as of Firefox 56.
    """



# == Graphics referencing elements ==
class audio(Component):
    ''

class iframe(Component):
    """
        The **HTML <iframe> element** represents a nested browsing context,
        effectively embedding another HTML page into the current page. In HTML
        4.01, a document may contain a ``head`` and a ``body`` or a ``head``
        and a ``frameset``, but not both a ``body`` and a ``frameset``.
        However, an ``<iframe>`` can be used within a normal document body.
        Each browsing context has its own session history and active document.
        The browsing context that contains the embedded content is called the
        parent browsing context. The top-level browsing context (which has no
        parent) is typically the browser window.
        
        Examples::
        
            <article><base target="_blank">
            <iframe id="Example2" title="Example2" width="400" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=es-419&amp;geocode=&amp;q=buenos+aires&amp;sll=37.0625,-95.677068&amp;sspn=38.638819,80.859375&amp;t=h&amp;ie=UTF8&amp;hq=&amp;hnear=Buenos+Aires,+Argentina&amp;z=11&amp;ll=-34.603723,-58.381593&amp;output=embed">
            </iframe>
            
            <br>
            <small>
              <a href="https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=es-419&amp;geocode=&amp;q=buenos+aires&amp;sll=37.0625,-95.677068&amp;sspn=38.638819,80.859375&amp;t=h&amp;ie=UTF8&amp;hq=&amp;hnear=Buenos+Aires,+Argentina&amp;z=11&amp;ll=-34.603723,-58.381593" style="color:#0000FF;text-align:left"> See bigger map </a>
            </small></article>
        
        Notes:
        
            Starting in Gecko 6.0, rendering of inline frames correctly respects
            the borders of their containing element when they're rounded using
            ``border-radius``.
    """

# image: see above under "Graphics elements"
# mesh: see above under "Graphics elements"
# use: see above under "Graphics elements"
class video(Component):
    ''



# == HTML elements ==
# audio: see above under "Graphics referencing elements"
class canvas(Component):
    ''

# iframe: see above under "Graphics referencing elements"
# video: see above under "Graphics referencing elements"


# == Light source elements ==
class feDistantLight(Component):
    """
        The **<feDistantLight>** filter primitive defines a distant light
        source that can be used within a lighting filter primitive:
        ``<feDiffuseLighting>`` or ``<feSpecularLighting>``.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class fePointLight(Component):
    """
        The <fePointLight> SVG filter primitive allows to create a point light
        effect.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class feSpotLight(Component):
    """
        The **<feSpotLight>** SVG filter primitive allows to create a
        spotlight effect.
        
        Examples::
        
            <article><svg width="200" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <defs>
                <filter id="spotlight">
                  <fespecularlighting result="spotlight" specularconstant="1.5" specularexponent="4" lighting-color="#FFF">
                    <fespotlight x="600" y="600" z="400" limitingconeangle="5.5"></fespotlight>
                  </fespecularlighting>
                  <fecomposite in="SourceGraphic" in2="spotlight" operator="out" k1="0" k2="1" k3="1" k4="0"></fecomposite>
                </filter>
              </defs>
            
              <image xlink:href="/files/6457/mdn_logo_only_color.png" x="10%" y="10%" width="80%" height="80%" style="filter:url(#spotlight);"></image>
            </svg></article>
        
        Notes:
        
        
    """



# == Never-rendered elements ==
class clipPath(Component):
    """
        The **<clipPath>** SVG element defines a clipping path. A clipping
        path is used/referenced using the ``clip-path`` property.
        
        The clipping path restricts the region to which paint can be applied.
        Conceptually, any parts of the drawing that lie outside of the region
        bounded by the currently active clipping path are not drawn.
        
        A clipping path is conceptually equivalent to a custom viewport for
        the referencing element. Thus, it affects the rendering of an element,
        but not the element's inherent geometry. The bounding box of a clipped
        element (meaning, an element which references a ``<clipPath>`` element
        via a ``clip-path`` property, or a child of the referencing element)
        must remain the same as if it were not clipped.
        
        By default, pointer-events must not be dispatched on the clipped (non-
        visible) regions of a shape. For example, a circle with a radius of 10
        which is clipped to a circle with a radius of 5 will not receive
        "click" events outside the smaller radius.
        
        Examples::
        
            <article><svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <clippath id="myClip">
                  <circle cx="30" cy="30" r="20"></circle>
                  <circle cx="70" cy="70" r="20"></circle>
                </clippath>
              </defs>
            
              <rect x="10" y="10" width="100" height="100" clip-path="url(#myClip)"></rect>
            </svg>
            
            <style>
            svg {
              border: 3px dashed #999;
            }
            svg > rect:hover {
              fill: green;
            }
            </style>
            <svg width="100" height="100">
              <defs>
                <clippath id="myClip">
                  <rect x="0" y="10" width="100" height="35"></rect>
                  <rect x="0" y="55" width="100" height="35"></rect>
                </clippath>
              </defs>
              <circle cx="50" cy="50" r="50" clip-path="url(#myClip)"></circle>
            </svg>
            </article>
        
        Notes:
        
        
    """

# defs: see above under "Container elements"
class hatch(Component):
    """
        ** **This is an experimental technology**
        
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change
        in future versions of browsers as the specification changes.The
        **<hatch>** SVG element is used to fill or stroke an object using one
        or more pre-defined paths that are repeated at fixed intervals in a
        specified direction to cover the areas to be painted.
        
        Hatches defined by the ``<hatch>`` element can then referenced by
        the ``fill`` and ``stroke`` CSS properties on a given graphics element
        to indicate that the given element shall be filled or stroked with the
        hatch. Paths are defined by ``<hatchpath>`` elements.
        
        Examples::
        
            <article><svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <hatch hatchunits="userSpaceOnUse" pitch="5" rotate="135">
            &#160;     <hatchpath stroke="#a080ff" stroke-width="2"></hatchpath>
                </hatch>
              </defs>
            
              <rect fill="url(#hatch)" stroke="black" stroke-width="2" x="10%" y="10%" width="80%" height="80%"></rect>
            </svg></article>
        
        Notes:
        
        
    """

# linearGradient: see above under "Gradient elements"
# marker: see above under "Container elements"
# mask: see above under "Container elements"
# meshgradient: see above under "Gradient elements"
# metadata: see above under "Descriptive elements"
# pattern: see above under "Container elements"
# radialGradient: see above under "Gradient elements"
class script(Component):
    """
        A SVG ``script`` element is equivalent to the ``script`` element in
        HTML and thus is the place for scripts (e.g., ECMAScript).Any
        functions defined within any ``script`` element have a global scope
        across the entire current document.
        
        Examples::
        
            <article><svg width="100%" height="100%" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <script type="text/javascript">
                // <![CDATA[
                function change(evt) {
            &#160;&#160;&#160;&#160;&#160; var target = evt.target;
            &#160;&#160;&#160;&#160;&#160; var radius = target.getAttribute("r");
            
            &#160;&#160;&#160;&#160;&#160; if (radius == 15) {
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; radius = 45;
            &#160;&#160;&#160;&#160;&#160; } else {
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; radius = 15;
            &#160;&#160;&#160;&#160;&#160; }
            
            &#160;&#160;&#160;&#160;&#160; target.setAttribute("r",radius);
               }
               // ]]>
              </script>
            
              <circle cx="50" cy="50" r="45" fill="green" onclick="change(evt)"></circle>
            </svg>
            </article>
        
        Notes:
        
        
    """

class style(Component):
    """
        The **<style>** SVG element allows style sheets to be embedded
        directly within SVG content. SVG's ``style`` element has the same
        attributes as the corresponding element in HTML (see HTML's
        ``<style>`` element).
        
        Examples::
        
            <article><svg width="100%" height="100%" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <style>
                /* <![CDATA[ */
                circle {
                  fill: orange;
                  stroke: black;
                  stroke-width: 10px; /* Note: The value of a pixel depends
                                         on the view box */
                }
                /* ]]> */
              </style>
            
              <circle cx="50" cy="50" r="40"></circle>
            </svg>
            </article>
        
        Notes:
        
        
    """

# symbol: see above under "Container elements"
# title: see above under "Descriptive elements"


# == Paint server elements ==
# hatch: see above under "Never-rendered elements"
# linearGradient: see above under "Gradient elements"
# meshgradient: see above under "Gradient elements"
# pattern: see above under "Container elements"
# radialGradient: see above under "Gradient elements"
class solidcolor(Component):
    """
        ** **This is an experimental technology**
        
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change
        in future versions of browsers as the specification changes.The
        **<solidcolor>** SVG element lets authors define a single color for
        use in multiple places in an SVG document. It is also useful as away
        of animating a palette colors.
        
        **Note:** This is an experimental technology, and not yet implemented
        in browsers. A workaround is to use a ``<linearGradient>`` with only
        one color stop. This is less elegant, and unlike ``<solidcolor>``,
        cannot itself be used in the definition of gradients.
        
        Examples::
        
            <article><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 300 200" height="150">
              <defs>
                <!-- solidColor is experimental. -->
                <solidcolor id="myColor" solid-color="gold" solid-opacity="0.8"></solidcolor>
                  
                <!-- linearGradient with a single color stop is a less elegant way to 
                     achieve the same effect, but it works in current browsers. -->
                <lineargradient id="myGradient">
                  <stop offset="0" stop-color="green"></stop>
                </lineargradient>
              </defs>
               
              <text x="10" y="20">Circles colored with solidColor</text>
              <circle cx="150" cy="65" r="35" stroke-width="2" stroke="url(#myColor)" fill="white"></circle>
              <circle cx="50" cy="65" r="35" fill="url(#myColor)"></circle>
            
              <text x="10" y="120">Circles colored with linearGradient</text>
              <circle cx="150" cy="165" r="35" stroke-width="2" stroke="url(#myGradient)" fill="white"></circle>
              <circle cx="50" cy="165" r="35" fill="url(#myGradient)"></circle>
            </svg>
            </article>
        
        Notes:
        
        
    """



# == Renderable elements ==
# a: see above under "Container elements"
# audio: see above under "Graphics referencing elements"
# canvas: see above under "HTML elements"
# circle: see above under "Basic shapes"
# ellipse: see above under "Basic shapes"
class foreignObject(Component):
    """
        The **<foreignObject>** SVG element allows for inclusion of a foreign
        XML namespace which has its graphical content drawn by a different
        user agent. The included foreign graphical content is subject to SVG
        transformations and compositing.
        
        The contents of ``foreignObject`` are assumed to be from a different
        namespace. Any SVG elements within a ``foreignObject`` will not be
        drawn, except in the situation where a properly defined SVG
        subdocument with a proper ``xmlns`` attribute specification is
        embedded recursively. One situation where this can occur is when an
        SVG document fragment is embedded within another non-SVG document
        fragment, which in turn is embedded within an SVG document fragment
        (e.g., an SVG document fragment contains an XHTML document fragment
        which in turn contains yet another SVG document fragment).
        
        Usually, a ``foreignObject`` will be used in conjunction with the
        ``<switch>`` element and the ``requiredExtensions`` attribute to
        provide proper checking for user agent support and provide an
        alternate rendering in case user agent support is not available.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# g: see above under "Container elements"
# iframe: see above under "Graphics referencing elements"
# image: see above under "Graphics elements"
# line: see above under "Basic shapes"
# mesh: see above under "Graphics elements"
# path: see above under "Graphics elements"
# polygon: see above under "Basic shapes"
# polyline: see above under "Basic shapes"
# rect: see above under "Basic shapes"
# svg: see above under "Container elements"
# switch: see above under "Container elements"
# symbol: see above under "Container elements"
# text: see above under "Graphics elements"
class textPath(Component):
    """
        In addition to text drawn in a straight line, SVG also includes the
        ability to place text along the shape of a ``<path>`` element. To
        specify that a block of text is to be rendered along the shape of a
        ``<path>``, include the given text within a **<textPath>** element
        which includes an ``href`` attribute with a reference to a ``<path>``
        element.
        
        Examples::
        
            <article><svg viewbox="0 0 1000 300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <defs>
                <path id="MyPath" d="M 100 200 
                         C 200 100 300   0 400 100
                         C 500 200 600 300 700 200
                         C 800 100 900 100 900 100"></path>
              </defs>
            
              <use xlink:href="#MyPath" fill="none" stroke="red"></use>
            
             &#160;<text font-family="Verdana" font-size="42.5">
                <textpath xlink:href="#MyPath">
                  We go up, then we go down, then up again
                </textpath>
              </text>
            
              <!-- Show outline of the viewport using 'rect' element -->
              <rect x="1" y="1" width="998" height="298" fill="none" stroke="black" stroke-width="2"></rect>
            </svg>
            </article>
        
        Notes:
        
        
    """

class tspan(Component):
    """
        Within a ``<text>`` element, text and font properties and the current
        text position can be adjusted with absolute or relative coordinate
        values by including a **<tspan>** element.
        
        Examples::
        
            <article><?xml version="1.0"?>
            <svg width="250" height="40" viewbox="0 0 250 40" xmlns="http://www.w3.org/2000/svg" version="1.1">
            
              <style>
            <![CDATA[
            text{
              font: 20px Verdana, Helvetica, Arial, sans-serif;
            }
            
            tspan{
              fill: red;
              font-weight: bold
            }
            ]]>
              </style>
            
              <text x="15" y="30">
                You are 
                <tspan>not</tspan> 
                a banana
              </text>
            </svg>
            </article>
        
        Notes:
        
        
    """

# unknown: see above under "Container elements"
# use: see above under "Graphics elements"
# video: see above under "Graphics referencing elements"


# == Shape elements ==
# circle: see above under "Basic shapes"
# ellipse: see above under "Basic shapes"
# line: see above under "Basic shapes"
# mesh: see above under "Graphics elements"
# path: see above under "Graphics elements"
# polygon: see above under "Basic shapes"
# polyline: see above under "Basic shapes"
# rect: see above under "Basic shapes"


# == Structural elements ==
# defs: see above under "Container elements"
# g: see above under "Container elements"
# svg: see above under "Container elements"
# symbol: see above under "Container elements"
# use: see above under "Graphics elements"


# == Text content elements ==
class altGlyph(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The
        **<altGlyph>** SVG element allows sophisticated selection of the
        glyphs used to render its child character data.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class altGlyphDef(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The
        **<altGlyphDef>** SVG element defines a substitution representation
        for glyphs.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class altGlyphItem(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The
        **<altGlyphItem>** element provides a set of candidates for glyph
        substitution by the ``<altGlyph>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class glyph(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.A **<glyph>**
        defines a single glyph in an SVG font.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class glyphRef(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Do not use it in old or new projects. Pages or Web apps using it may
        break at any time.The ``glyphRef`` element provides a single possible
        glyph to the referencing ``<altGlyph>`` substitution.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# textPath: see above under "Renderable elements"
# text: see above under "Graphics elements"
class tref(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.The textual
        content for a ``<text>`` SVG element can be either character data
        directly embedded within the ``<text>`` element or the character data
        content of a referenced element, where the referencing is specified
        with a **<tref>** element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# tspan: see above under "Renderable elements"


# == Text content child elements ==
# altGlyph: see above under "Text content elements"
# textPath: see above under "Renderable elements"
# tref: see above under "Text content elements"
# tspan: see above under "Renderable elements"


# == Uncategorized elements ==
# clipPath: see above under "Never-rendered elements"
# FIXME: invalid syntax (<unknown>, line 12)
# class color_profile(Component):"""
#         The **<color-profile>** element allows describing the color profile
#         used for the image.
#         
#         Examples::
#         
#             <article></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'color-profile'
class cursor(Component):
    """
        **** Deprecated**
        
        This feature has been removed from the Web standards. Though some
        browsers may still support it, it is in the process of being dropped.
        Avoid using it and update existing code if possible; see the
        compatibility table at the bottom of this page to guide your decision.
        Be aware that this feature may cease to work at any time.**Note:** The
        CSS ``cursor`` property should be used instead of this element.
        
        The **<cursor>** SVG element can be used to define a platform-
        independent custom cursor. A recommended approach for defining a
        platform-independent custom cursor is to create a PNG image and define
        a ``cursor`` element that references the PNG image and identifies the
        exact position within the image which is the pointer position (i.e.,
        the hot spot).
        
        The PNG format is recommended because it supports the ability to
        define a transparency mask via an alpha channel. If a different image
        format is used, this format should support the definition of a
        transparency mask (two options: provide an explicit alpha channel or
        use a particular pixel color to indicate transparency). If the
        transparency mask can be determined, the mask defines the shape of the
        cursor; otherwise, the cursor is an opaque rectangle. Typically, the
        other pixel information (e.g., the R, G and B channels) defines the
        colors for those parts of the cursor which are not masked out. Note
        that cursors usually contain at least two colors so that the cursor
        can be visible over most backgrounds.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

# FIXME: invalid syntax (<unknown>, line 23)
# class filter_(Component):"""
#         The **<filter>** SVG element serves as container for atomic filter
#         operations. It is never rendered directly. A filter is referenced by
#         using the ``filter`` attribute on the target SVG element or via the
#         ``filter`` CSS property.
#         
#         Examples::
#         
#             <article><svg width="230" height="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#             
#              <filter id="blurMe">
#               <fegaussianblur in="SourceGraphic" stddeviation="5"></fegaussianblur>
#              </filter>
#             
#              <circle cx="60" cy="60" r="50" fill="green"></circle>
#             
#              <circle cx="170" cy="60" r="50" fill="green" filter="url(#blurMe)"></circle>
#             </svg></article>
#         
#         Notes:
#         
#         
#     """    tag_name = 'filter'
# foreignObject: see above under "Renderable elements"
class hatchpath(Component):
    """
        ** **This is an experimental technology**
        
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change
        in future versions of browsers as the specification changes.The
        **<hatchpath>** SVG element defines a hatch path used by the
        ``<hatch>`` element.
        
        Examples::
        
            <article></article>
        
        Notes:
        
        
    """

class meshpatch(Component):
    ''

class meshrow(Component):
    ''

# script: see above under "Never-rendered elements"
# style: see above under "Never-rendered elements"
class view(Component):
    """
        A view is a defined way to view the image, like a zoom level or a
        detail view.
        
        Examples::
        
            <article><svg width="600" height="200" viewbox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <defs>
                <radialgradient id="gradient">
                  <stop offset="0%" stop-color="#8cffa0"></stop>
                  <stop offset="100%" stop-color="#8ca0ff"></stop>
                </radialgradient>    
              </defs>
            
              <circle r="50" cx="180" cy="50" style="fill:url(#gradient)"></circle>
            
              <view id="halfSizeView" viewbox="0 0 1200 400"></view>
              <view id="normalSizeView" viewbox="0 0 600 200"></view>
              <view id="doubleSizeView" viewbox="0 0 300 100"></view>
            
              <a xlink:href="#halfSizeView">
                <text x="5" y="20" font-size="20">half size</text>
              </a>
              <a xlink:href="#normalSizeView">
                <text x="5" y="40" font-size="20">normal size</text>
              </a>
              <a xlink:href="#doubleSizeView">
                <text x="5" y="60" font-size="20">double size</text>
              </a>
            </svg></article>
        
        Notes:
        
        
    """



__all__ = [
    'animate', 'animateColor', 'animateMotion', 'animateTransform', 'discard',
    'mpath', 'set', 'circle', 'ellipse', 'line', 'polygon', 'polyline', 'rect',
    'a', 'defs', 'g', 'marker', 'mask', 'missing-glyph', 'pattern', 'svg',
    'switch', 'symbol', 'unknown', 'desc', 'metadata', 'title', 'feBlend',
    'feColorMatrix', 'feComponentTransfer', 'feComposite', 'feConvolveMatrix',
    'feDiffuseLighting', 'feDisplacementMap', 'feDropShadow', 'feFlood',
    'feFuncA', 'feFuncB', 'feFuncG', 'feFuncR', 'feGaussianBlur', 'feImage',
    'feMerge', 'feMergeNode', 'feMorphology', 'feOffset', 'feSpecularLighting',
    'feTile', 'feTurbulence', 'font', 'font-face', 'font-face-format',
    'font-face-name', 'font-face-src', 'font-face-uri', 'hkern', 'vkern',
    'linearGradient', 'meshgradient', 'radialGradient', 'stop', 'image',
    'mesh', 'path', 'text', 'use', 'audio', 'iframe', 'video', 'canvas',
    'feDistantLight', 'fePointLight', 'feSpotLight', 'clipPath', 'hatch',
    'script', 'style', 'solidcolor', 'foreignObject', 'textPath', 'tspan',
    'altGlyph', 'altGlyphDef', 'altGlyphItem', 'glyph', 'glyphRef', 'tref',
    'color-profile', 'cursor', 'filter', 'hatchpath', 'meshpatch', 'meshrow',
    'view'
]

