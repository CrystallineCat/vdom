# -*- coding: utf-8 -*-

from .core import createComponent

# From http://developer.mozilla.org/en-US/docs/Web/SVG/Element

# == Animation Elements ==
# 

animate = createComponent(
    'animate',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/animate',
    docs="""
        The `animate` element is put inside a shape element and defines how an
        attribute of an element changes over the animation. The attribute will change
        from the initial value to the end value in the duration specified.
    """, )


animateColor = createComponent(
    'animateColor',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateColor',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        This element has been deprecated in SVG 1.1 Second Edition and may be removed
        in a future version of SVG. It provides no features not already available by
        using the `<animate>` element. So, authors should use the `<animate>` element
        instead.
        
        The **`<animateColor>`** SVG element specifies a color transformation over
        time.
    """, )


animateMotion = createComponent(
    'animateMotion',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateMotion',
    docs="""
        The **`<animateMotion>`** element causes a referenced element to move along a
        motion path.
    """, )


animateTransform = createComponent(
    'animateTransform',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateTransform',
    docs="""
        The `animateTransform` element animates a transformation attribute on a target
        element, thereby allowing animations to control translation, scaling, rotation
        and/or skewing.
    """,
    examples=[
        '<?xml version="1.0"?>\n<svg width="120" height="120"  viewBox="0 0 120 120"\n     xmlns="http://www.w3.org/2000/svg" version="1.1"\n     xmlns:xlink="http://www.w3.org/1999/xlink" >\n\n    <polygon points="60,30 90,90 30,90">\n        <animateTransform attributeName="transform"\n                          attributeType="XML"\n                          type="rotate"\n                          from="0 60 70"\n                          to="360 60 70"\n                          dur="10s"\n                          repeatCount="indefinite"/>\n    </polygon>\n</svg>',
    ], )


discard = createComponent(
    'discard',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/discard',
    docs="""
        The **`<discard>`** SVG element allows authors to specify the time at which
        particular elements are to be discarded, thereby reducing the resources
        required by an SVG user agent. This is particularly useful to help SVG viewers
        conserve memory while displaying long-running documents.
        
        The `<discard>` element may occur wherever the `<animate>` element may.
    """, )


mpath = createComponent(
    'mpath',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/mpath',
    docs="""
        The **`<mpath>`** sub-element for the `<animateMotion>` element provides the
        ability to reference an external `<path>` element as the definition of a
        motion path.
    """, )


set = createComponent(
    'set',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/set',
    docs="""
        The **`<set>`** element provides a simple means of just setting the value of
        an attribute for a specified duration. It supports all attribute types,
        including those that cannot reasonably be interpolated, such as string and
        boolean values. The `<set>` element is non-additive. The additive and
        accumulate attributes are not allowed, and will be ignored if specified.
    """, )


# == Basic Shapes ==
# 

circle = createComponent(
    'circle',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle',
    docs="""
        The **`<circle>`** SVG element is an SVG basic shape, used to create circles
        based on a center point and a radius.
    """,
    examples=[
        '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">\n\xa0 <circle cx="100" cy="100" r="100"/>\n</svg>',
    ], )


ellipse = createComponent(
    'ellipse',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/ellipse',
    docs="""
        The `ellipse` element is an SVG basic shape, used to create ellipses based on
        a center coordinate, and both their x and y radius.
        
        Ellipses are unable to specify the exact orientation of the ellipse (if, for
        example, you wanted to draw an ellipse tilted at a 45 degree angle), but can
        be rotated by using the `transform` attribute.
    """,
    examples=[
        '<svg width="120" height="120" viewBox="0 0 120 120"\n    xmlns="http://www.w3.org/2000/svg">\n\n  <ellipse cx="60" cy="60" rx="50" ry="25"/>\n</svg>',
    ], )


line = createComponent(
    'line',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/line',
    docs="""
        The **`<line>`** element is an SVG basic shape used to create a line
        connecting two points.
    """,
    examples=[
        '<svg width="120" height="120" viewBox="0 0 120 120"\n    xmlns="http://www.w3.org/2000/svg">\n\n  <line x1="20" y1="100" x2="100" y2="20"\n      stroke-width="2" stroke="black"/>\n</svg>',
        '<svg width="120" height="120" viewBox="0 0 120 120"\n    xmlns="http://www.w3.org/2000/svg">\n  <line x1="20" y1="100" x2="100" y2="100"\n      stroke-width="2" stroke="black" transform="rotate(-45 20 100)"/>\n</svg>',
    ], )


polygon = createComponent(
    'polygon',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon',
    docs="""
        The **`<polygon>`** element defines a closed shape consisting of a set of
        connected straight line segments. The last point is connected to the first
        point. For open shapes see the `<polyline>` element.
    """,
    examples=[
        '<svg width="120" height="120" viewBox="0 0 120 120"\n    xmlns="http://www.w3.org/2000/svg">\n\n  <polygon points="60,20 100,40 100,80 60,100 20,80 20,40"/>\n</svg>',
    ], )


polyline = createComponent(
    'polyline',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/polyline',
    docs="""
        The **`<polyline>`** SVG element is an SVG basic shape that creates straight
        lines connecting several points. Typically a `polyline` is used to create open
        shapes as the last point doesn't have to be connected to the first point. For
        closed shapes see the `<polygon>` element.
    """,
    examples=[
        '<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">\n  <polyline fill="none" stroke="black" \n      points="20,100 40,60 70,80 100,20"/>\n</svg>',
        '<div class="contain-demo">\n \xa0 <svg width="150" height="200">\n \xa0\xa0\xa0 <desc>\n       First orange polyline demonstrating\n       white fill on open path.\n     </desc>\n \xa0\xa0\xa0 <polyline\n         points="0,40 40,40 40,80 80,80 80,120 120,120 120,160"\n         fill="white" stroke="#D07735" stroke-width="6" />\n \xa0 </svg>\n \xa0 <svg width="150" height="200">\n \xa0\xa0\xa0 <desc>\n       Second orange polyline demonstrating\n       yellow fill on open path.\n     </desc>\n \xa0\xa0\xa0 <polyline\n         points="0,40 40,40 40,80 80,80 80,120 120,120 120,160"\n         fill="#F9F38C" stroke="#D07735" stroke-width="6" />\n \xa0 </svg>\n </div>\n<p class="p">\n  Demo by Joni Trythall.\n  <a href="http://sitepoint.com/understanding-svg-fill-rule-property">See article</a>.\n</p>',
    ], )


rect = createComponent(
    'rect',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect',
    docs="""
        The **`<rect>`** element is a basic SVG shape that creates rectangles, defined
        by their corner's position, their width, and their height. The rectangles may
        have their corners rounded.
    """, )


# == Container Elements ==
# 

a = createComponent(
    'a',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/a',
    docs="""
        The **`<a>`** SVG element defines a hyperlink.
        
        Since this element shares its tag name with HTML's `<a>` element, selecting
        "`a`" with CSS or `querySelector` may apply to the wrong kind of element. Try
        the `@namespace` rule to distinguish between the two.
    """,
    examples=[
        '<svg width="140" height="30" xmlns="http://www.w3.org/2000/svg" \n    xmlns:xlink="http://www.w3.org/1999/xlink">\n\n  <a href="https://developer.mozilla.org/en-US/docs/SVG"\n      target="_blank">\n    <rect height="30" width="120" y="0" x="0" rx="15"/>\n    <text fill="white" text-anchor="middle" \n          y="21" x="60">SVG on MDN</text>\n  </a>\n</svg>',
    ], )


defs = createComponent(
    'defs',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs',
    docs="""
        SVG allows graphical objects to be defined for later reuse. It is recommended
        that, wherever possible, referenced elements be defined inside of a
        **`<defs>`** element. Defining these elements inside of a `<defs>` element
        promotes understandability of the SVG content and thus promotes accessibility.
        Graphical elements defined in a `<defs>` element will not be directly
        rendered. You can use a `<use>` element to render those elements wherever you
        want on the viewport.
    """, )


g = createComponent(
    'g',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/g',
    docs="""
        The **`<g>`** SVG element is a container used to group other SVG elements.
        Transformations applied to the `<g>` element are performed on all of its child
        elements, and any of its attributes are inherited by its child elements. It
        can also group multiple elements to be referenced later with the `<use>`
        element.
    """,
    examples=[
        '<svg viewBox="0 0 95 50"\n     xmlns="http://www.w3.org/2000/svg">\n   <g stroke="green" fill="white" stroke-width="5">\n     <circle cx="25" cy="25" r="15"/>\n     <circle cx="40" cy="25" r="15"/>\n     <circle cx="55" cy="25" r="15"/>\n     <circle cx="70" cy="25" r="15"/>\n   </g>\n</svg>',
    ], )


marker = createComponent(
    'marker',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker',
    docs="""
        The **`<marker>`** element defines the graphics that is to be used for drawing
        arrowheads or polymarkers on a given `<path>`, `<line>`, `<polyline>` or
        `<polygon>` element.
    """, )


mask = createComponent(
    'mask',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/mask',
    docs="""
        In SVG, you can specify that any other graphics object or `<g>` element can be
        used as an alpha mask for compositing the current object into the background.
        A mask is defined with the **`<mask>`** element. A mask is used/referenced
        using the `mask` property.
    """, )


missing_glyph = createComponent(
    'missing-glyph',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/missing-glyph',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<missing-glyph>`** SVG element's content is rendered, if for a given
        character the font doesn't define an appropriate `<glyph>`.
    """, )


pattern = createComponent(
    'pattern',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/pattern',
    docs="""
        The **`<pattern>`** element defines a graphics object which can be redrawn at
        repeated x and y-coordinate intervals ("tiled") to cover an area. The
        `<pattern>` is referenced by the `fill` and/or `stroke` attributes on other
        graphics elements to fill or stroke those elements with the referenced
        pattern.
    """, )


svg = createComponent(
    'svg',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg',
    docs="""
        The `svg` element can be used to embed an SVG fragment inside the current
        document (for example, an HTML document). This SVG fragment has its own
        viewport and coordinate system.
    """,
    examples=[
        '<!DOCTYPE html>\n<html>\n<head>\n  <meta charset="UTF-8" />\n  <title>HTML/SVG Example</title>\n</head>\n\n<body>\n\n  <svg xmlns="http://www.w3.org/2000/svg"\n       width="150" height="100" viewBox="0 0 3 2">\n    <rect width="1" height="2" x="0" fill="#008d46" />\n    <rect width="1" height="2" x="1" fill="#ffffff" />\n    <rect width="1" height="2" x="2" fill="#d2232c" />\n  </svg>\n\n</body>\n</html>',
    ], )


switch = createComponent(
    'switch',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/switch',
    docs="""
        The **`<switch>`** SVG element evaluates the `requiredFeatures`,
        `requiredExtensions` and `systemLanguage` attributes on its direct child
        elements in order, and then processes and renders the first child for which
        these attributes evaluate to true. All others will be bypassed and therefore
        not rendered. If the child element is a container element such as a `<g>`,
        then the entire subtree is either processed/rendered or bypassed/not rendered.
        
        Note that the values of properties `display` and `visibility` have no effect
        on `switch` element processing. In particular, setting `display` to none on a
        child of a `switch` element has no effect on true/false testing associated
        with `switch` element processing.
    """, )


symbol = createComponent(
    'symbol',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/symbol',
    docs="""
        The **`<symbol>`** element is used to define graphical template objects which
        can be instantiated by a `<use>` element. The use of `symbol` elements for
        graphics that are used multiple times in the same document adds structure and
        semantics. Documents that are rich in structure may be rendered graphically,
        as speech, or as Braille, and thus promote accessibility. Note that a `symbol`
        element itself is not rendered. Only instances of a `symbol` element (i.e., a
        reference to a `symbol` by a `<use>` element) are rendered.
    """,
    examples=[
        '<svg width="120" height="140">\n<!-- symbol definition\xa0 NEVER draw -->\n<symbol id="sym01" viewBox="0 0 150 110">\n\xa0 <circle cx="50" cy="50" r="40" stroke-width="8"\n      stroke="red" fill="red"/>\n\xa0 <circle cx="90" cy="60" r="40" stroke-width="8"\n      stroke="green" fill="white"/>\n</symbol>\n\n<!-- actual drawing by "use" element -->\n<use href="#sym01"\n\xa0\xa0\xa0\xa0 x="0" y="0" width="100" height="50"/>\n<use href="#sym01"\n\xa0\xa0\xa0\xa0 x="0" y="50" width="75" height="38"/>\n<use href="#sym01"\n\xa0\xa0\xa0\xa0 x="0" y="100" width="50" height="25"/>\n</svg>',
    ], )


unknown = createComponent(
    'unknown',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/unknown',
    notes='FIXME: http response had status 404', )


# == Descriptive Elements ==
# 

desc = createComponent(
    'desc',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/desc',
    docs="""
        Each container element or graphics element in an SVG drawing can supply a
        description string using the **`<desc>`** element where the description is
        text-only.
        
        When the current SVG document fragment is rendered as SVG on visual media,
        `<desc>` elements are not rendered as part of the graphics. Alternate
        presentations are possible, both visual and aural, which display the `<desc>`
        element but do not display `<path>` elements or other graphics elements. The
        `<desc>` element generally improves accessibility of SVG documents.
    """, )


metadata = createComponent(
    'metadata',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/metadata',
    docs="""
        The **`<metadata>`** SVG element allows to add metadata to SVG content.
        Metadata is structured information about data. The contents of `<metadata>`
        elements should be elements from other XML namespaces such as RDF, FOAF, etc.
    """, )


title = createComponent(
    'title',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/title',
    docs="""
        Each container element or graphics element in an SVG drawing can supply a
        **`<title>`** element containing a description string where the description is
        text-only. When the current SVG document fragment is rendered as SVG on visual
        media, `<title>` element is not rendered as part of the graphics. However,
        some user agents may, for example, display the `<title>` element as a tooltip.
        Alternate presentations are possible, both visual and aural, which display the
        `<title>` element but do not display `path` elements or other graphics
        elements. The `<title>` element generally improves accessibility of SVG
        documents.
        
        Generally `<title>` element should be the first child element of its parent.
        Note that those implementations that do use `<title>` to display a tooltip
        often will only do so if the `<title>` is indeed the first child element of
        its parent.
    """, )


# == Filter Primitive Elements ==
# 

feBlend = createComponent(
    'feBlend',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feBlend',
    docs="""
        The **`<feBlend>`** SVG filter primitive composes two objects together ruled
        by a certain blending mode. This is similar to what is known from image
        editing software when blending two layers. The mode is defined by the `mode`
        attribute.
    """, )


feColorMatrix = createComponent(
    'feColorMatrix',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feColorMatrix',
    docs="""
        The **`<feColorMatrix>`** SVG filter element changes colors based on a
        transformation matrix. Every pixel's color value (represented by an [R,G,B,A]
        vector) is matrix multiplied to create a new color.
    """, )


feComponentTransfer = createComponent(
    'feComponentTransfer',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feComponentTransfer',
    docs="""
        Th **`<feComponentTransfer>`** SVG filter primitive performs color-component-
        wise remapping of data for each pixel. It allows operations like brightness
        adjustment, contrast adjustment, color balance or thresholding.
        
        The calculations are performed on non-premultiplied color values. The colors
        are modified by changing each channel (R, G, B, and A) to the result of what
        the children `<feFuncR>`, `<feFuncB>`, `<feFuncG>`, and `<feFuncA>` return.
    """, )


feComposite = createComponent(
    'feComposite',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feComposite',
    docs="""
        This filter primitive performs the combination of two input images pixel-wise
        in image space using one of the Porter-Duff compositing operations: `over`
        _,_`in` _,_`atop` _,_`out` _,_`xor` and `lighter`. Additionally, a component-
        wise `arithmetic` operation (with the result clamped between [0..1]) can be
        applied.
        
        The `arithmetic` operation is useful for combining the output from the
        `<feDiffuseLighting>` and `<feSpecularLighting>` filters with texture data. If
        the `arithmetic` operation is chosen, each result pixel is computed using the
        following formula:
        
            
            
            result = k1*i1*i2 + k2*i1 + k3*i2 + k4
            
        
        where:
        
          * `i1` and `i2` indicate the corresponding pixel channel values of the input image, which map to `in` and `in2` respectively
          * `k1, k2, k3` and `k4` indicate the values of the attributes with the same name
    """, )


feConvolveMatrix = createComponent(
    'feConvolveMatrix',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feConvolveMatrix',
    docs="""
        The **`<feConvolveMatrix>`** SVG filter primitive applies a matrix convolution
        filter effect. A convolution combines pixels in the input image with
        neighboring pixels to produce a resulting image. A wide variety of imaging
        operations can be achieved through convolutions, including blurring, edge
        detection, sharpening, embossing and beveling.
        
        A matrix convolution is based on an n-by-m matrix (the convolution kernel)
        which describes how a given pixel value in the input image is combined with
        its neighboring pixel values to produce a resulting pixel value. Each result
        pixel is determined by applying the kernel matrix to the corresponding source
        pixel and its neighboring pixels. The basic convolution formula which is
        applied to each color value for a given pixel is:
        
        COLORX,Y = (  
        SUM I=0 to [orderY-1] {  
        SUM J=0 to [orderX-1] {  
        SOURCE X-targetX+J, Y-targetY+I * kernelMatrixorderX-J-1, orderY-I-1  
        }  
        }  
        ) / divisor + bias * ALPHAX,Y
        
        where "orderX" and "orderY" represent the X and Y values for the 'order'
        attribute, "targetX" represents the value of the 'targetX' attribute,
        "targetY" represents the value of the 'targetY' attribute, "kernelMatrix"
        represents the value of the 'kernelMatrix' attribute, "divisor" represents the
        value of the 'divisor' attribute, and "bias" represents the value of the
        'bias' attribute.
        
        Note in the above formulas that the values in the kernel matrix are applied
        such that the kernel matrix is rotated 180 degrees relative to the source and
        destination images in order to match convolution theory as described in many
        computer graphics textbooks.
        
        To illustrate, suppose you have a input image which is 5 pixels by 5 pixels,
        whose color values for one of the color channels are as follows:
        
            
            
                0  20  40 235 235
              100 120 140 235 235
              200 220 240 235 235
              225 225 255 255 255
              225 225 255 255 255
            
        
        and you define a 3-by-3 convolution kernel as follows:
        
            
            
              1 2 3
              4 5 6
              7 8 9
            
        
        Let's focus on the color value at the second row and second column of the
        image (source pixel value is 120). Assuming the simplest case (where the input
        image's pixel grid aligns perfectly with the kernel's pixel grid) and assuming
        default values for attributes 'divisor', 'targetX' and 'targetY', then
        resulting color value will be:
        
            
            
            (9*  0 + 8* 20 + 7* 40 +
            6*100 + 5*120 + 4*140 +
            3*200 + 2*220 + 1*240) / (9+8+7+6+5+4+3+2+1)
    """,
    examples=[
        '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"\n    xmlns:xlink="http://www.w3.org/1999/xlink">\n  <defs>\n    <filter id="emboss">\n      <feConvolveMatrix\n          kernelMatrix="3 0 0\n                        0 0 0\n                        0 0 -3"/>\n    </filter>\n  </defs>\n\n  <image xlink:href="/files/12668/MDN.svg" x="0" y="0"\n      height="200" width="200" style="filter:url(#emboss);" />\n</svg>',
    ], )


feDiffuseLighting = createComponent(
    'feDiffuseLighting',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDiffuseLighting',
    docs="""
        The **`<feDiffuseLighting>`** SVG filter primitive lights an image using the
        alpha channel as a bump map. The resulting image, which is an RGBA opaque
        image, depends on the light color, light position and surface geometry of the
        input bump map.
        
        The light map produced by this filter primitive can be combined with a texture
        image using the multiply term of the `arithmetic` operator of the
        `<feComposite>` filter primitive. Multiple light sources can be simulated by
        adding several of these light maps together before applying it to the texture
        image.
    """, )


feDisplacementMap = createComponent(
    'feDisplacementMap',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDisplacementMap',
    docs="""
        The **`<feDisplacementMap>`** SVG filter primitive uses the pixel values from
        the image from `in2` to spatially displace the image from `in`.
        
        The formula for the transformation looks like this:
        
        `P'(x,y) <- P( x + scale * (XC(x,y) - 0.5), y + scale * (YC(x,y) - 0.5))`
        
        where `P(x,y)` is the input image, `in`, and `P'(x,y)` is the destination.
        `XC(x,y)` and `YC(x,y)` are the component values of the channel designated by
        `xChannelSelector` and `yChannelSelector`.
    """, )


feDropShadow = createComponent(
    'feDropShadow',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDropShadow',
    docs="""
        The **`<feDropShadow>`** filter primitive creates a drop shadow of the input
        image. It is a shorthand filter, and is defined in terms of combinations of
        other filter primitives.
        
        The result of the `<feDropShadow>` filter is equivalent to the following:
        
            
            
            <feGaussianBlur in="alpha-channel-of-feDropShadow-in"
                stdDeviation="stdDeviation-of-feDropShadow"/>
            <feOffset dx="dx-of-feDropShadow" dy="dy-of-feDropShadow"
                result="offsetblur"/>
            <feFlood flood-color="flood-color-of-feDropShadow"
                flood-opacity="flood-opacity-of-feDropShadow"/>
            <feComposite in2="offsetblur" operator="in"/>
            <feMerge>
              <feMergeNode/>
              <feMergeNode in="in-of-feDropShadow"/>
            </feMerge>
    """,
    examples=[
        '<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">\n  <defs>\n    <filter id="shadow">\n      <feDropShadow dx="4" dy="8" stdDeviation="4"/>\n    </filter>\n  </defs>\n\n  <circle cx="50%" cy="50%" r="80"\n      style="fill:blue; filter:url(#shadow);"/>\n</svg>',
    ], )


feFlood = createComponent(
    'feFlood',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFlood',
    docs="""
        The **`<feFlood>`** SVG filter primitive fills the filter subregion with the
        color and opacity defined by `flood-color` and `flood-opacity`.
    """,
    examples=[
        '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">\n  <defs>\n    <filter id="floodFilter" filterUnits="userSpaceOnUse">\n      <feFlood x="50" y="50" width="100" height="100"\n          flood-color="green" flood-opacity="0.5"/>\n    </filter>\n  </defs>\n\n  <use style="filter: url(#floodFilter);"/>\n</svg>',
    ], )


feFuncA = createComponent(
    'feFuncA',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncA',
    docs="""
        The **`<feFuncA>`** SVG filter primitive defines the transfer function for the
        alpha component of the input graphic of its parent `<feComponentTransfer>`
        element.
    """, )


feFuncB = createComponent(
    'feFuncB',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncB',
    docs="""
        The **`<feFuncB>`** SVG filter primitive defines the transfer function for the
        blue component of the input graphic of its parent `<feComponentTransfer>`
        element.
    """, )


feFuncG = createComponent(
    'feFuncG',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncG',
    docs="""
        The **`<feFuncG>`** SVG filter primitive defines the transfer function for the
        green component of the input graphic of its parent `<feComponentTransfer>`
        element.
    """, )


feFuncR = createComponent(
    'feFuncR',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncR',
    docs="""
        The `**< feFuncR>**` SVG filter primitive defines the transfer function for
        the red component of the input graphic of its parent `<feComponentTransfer>`
        element.
    """, )


feGaussianBlur = createComponent(
    'feGaussianBlur',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feGaussianBlur',
    docs="""
        The **`<feGaussianBlur>`** SVG filter primitive blurs the input image by the
        amount specified in `stdDeviation`, which defines the bell-curve.
    """,
    examples=[
        '<svg width="230" height="120"\n xmlns="http://www.w3.org/2000/svg"\n xmlns:xlink="http://www.w3.org/1999/xlink">\n\n  <filter id="blurMe">\n    <feGaussianBlur in="SourceGraphic" stdDeviation="5" />\n  </filter>\n\n  <circle cx="60"  cy="60" r="50" fill="green" />\n\n  <circle cx="170" cy="60" r="50" fill="green"\n          filter="url(#blurMe)" />\n</svg>',
        '<svg width="120" height="120"\n xmlns="http://www.w3.org/2000/svg"\n xmlns:xlink="http://www.w3.org/1999/xlink">\n\n  <filter id="dropShadow">\n    <feGaussianBlur in="SourceAlpha" stdDeviation="3" />\n    <feOffset dx="2" dy="4" />\n    <feMerge>\n        <feMergeNode />\n        <feMergeNode in="SourceGraphic" />\n    </feMerge>\n  </filter>\n\n  <circle cx="60"  cy="60" r="50" fill="green"\n          filter="url(#dropShadow)" />\n</svg>',
    ], )


feImage = createComponent(
    'feImage',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feImage',
    docs="""
        The **`<feImage>`** SVG filter primitive fetches image data from an external
        source and provides the pixel data as output (meaning if the external source
        is an SVG image, it is rasterized.)
    """,
    examples=[
        '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"\n    xmlns:xlink="http://www.w3.org/1999/xlink">\n  <defs>\n    <filter id="image">\n      <feImage xlink:href="/files/6457/mdn_logo_only_color.png"/>\n    </filter>\n  </defs>\n\n  <rect x="10%" y="10%" width="80%" height="80%"\n      style="filter:url(#image);"/>\n</svg>',
    ], )


feMerge = createComponent(
    'feMerge',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMerge',
    docs="""
        The **`<feMerge>`** SVG element allows filter effects to be applied
        concurrently instead of sequentially. This is achieved by other filters
        storing their output via the `result` attribute and then accessing it in a
        `<feMergeNode>` child.
    """, )


feMergeNode = createComponent(
    'feMergeNode',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMergeNode',
    docs="""
        The `feMergeNode` takes the result of another filter to be processed by its
        parent `<feMerge>`.
    """,
    examples=[
        '<svg width="200" height="200"\n\xa0xmlns="http://www.w3.org/2000/svg"\n\xa0xmlns:xlink="http://www.w3.org/1999/xlink">\n\n\n\xa0 \xa0 <filter id="feOffset" x="-40" y="-20" width="100" height="200">\n\xa0 \xa0 \xa0 \xa0 <feOffset in="SourceGraphic" dx="60" dy="60" />\n\xa0 \xa0 \xa0 \xa0 <feGaussianBlur in="SourceGraphic" stdDeviation="5" />\n\xa0 \xa0 \xa0 \xa0 <feMerge>\n\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 <feMergeNode in="blur2" />\n\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 <feMergeNode in="SourceGraphic" />\n\xa0 \xa0 \xa0 \xa0 </feMerge>\n\xa0 \xa0 </filter>\n\n<rect x="40" y="40" width="100" height="100"\n\xa0 \xa0 \xa0 \xa0style= "stroke : #000000; fill: green; filter: url(#feOffset);" />\n<rect x="40" y="40" width="100" height="100"\n\xa0 \xa0 \xa0 \xa0 style= "stroke : #000000; fill: green; " />\n\xa0 \xa0 \xa0 </svg>',
    ], )


feMorphology = createComponent(
    'feMorphology',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMorphology',
    docs="""
        The **`<feMorphology>`** SVG filter primitive is used to erode or dilate the
        input image. It's usefulness lies especially in fattening or thinning effects.
    """, )


feOffset = createComponent(
    'feOffset',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feOffset',
    docs="""
        The **`<feOffset>`** SVG filter primitive allows to offset the input image.
        The input image as a whole is offset by the values specified in the `dx` and
        `dy` attributes.
    """,
    examples=[
        '<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">\n  <defs>\n    <filter id="feOffset" x="-40" y="-20" width="100" height="200">\n      <feOffset in="SourceGraphic" dx="60" dy="60" />\n    </filter>\n  </defs>\n\n  <rect x="40" y="40" width="100" height="100"\n      style= "stroke : #000000; fill: green; filter: url(#feOffset);" />\n  <rect x="40" y="40" width="100" height="100"\n      style= "stroke : #000000; fill: green; " />\n</svg>',
    ], )


feSpecularLighting = createComponent(
    'feSpecularLighting',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feSpecularLighting',
    docs="""
        The **`<feSpecularLighting>`** SVG filter primitive lights a source graphic
        using the alpha channel as a bump map. The resulting image is an RGBA image
        based on the light color. The lighting calculation follows the standard
        specular component of the Phong lighting model. The resulting image depends on
        the light color, light position and surface geometry of the input bump map.
        The result of the lighting calculation is added. The filter primitive assumes
        that the viewer is at infinity in the z direction.
        
        This filter primitive produces an image which contains the specular reflection
        part of the lighting calculation. Such a map is intended to be combined with a
        texture using the `add` term of the arithmetic `<feComposite>` method.
        Multiple light sources can be simulated by adding several of these light maps
        before applying it to the texture image.
    """, )


feTile = createComponent(
    'feTile',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTile',
    docs="""
        The **`<feTile>`** SVG filter primitive allows to fill a target rectangle with
        a repeated, tiled pattern of an input image. The effect is similar to the one
        of a `<pattern>`.
    """, )


feTurbulence = createComponent(
    'feTurbulence',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence',
    docs="""
        The **`<feTurbulence>`** SVG filter primitive creates an image using the
        Perlin turbulence function. It allows the synthesis of artificial textures
        like clouds or marble. The resulting image will fill the entire filter
        primitive subregion.
    """, )


# == Font Elements ==
# 

font = createComponent(
    'font',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/font',
    docs="""
        The **`<font>`** SVG element defines a font to be used for text layout.
    """, )


font_face = createComponent(
    'font-face',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/font-face',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<font-face>`** SVG element corresponds to the CSS `@font-face` rule. It
        defines a font's outer properties.
    """, )


font_face_format = createComponent(
    'font-face-format',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/font-face-format',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<font-face-format>`** SVG element describes the type of font referenced
        by its parent `<font-face-uri>`.
    """, )


font_face_name = createComponent(
    'font-face-name',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/font-face-name',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<font-face-name>`** element points to a locally installed copy of this
        font, identified by its name.
    """, )


font_face_src = createComponent(
    'font-face-src',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/font-face-src',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<font-face-src>`** SVG element corresponds to the `src` descriptor in
        CSS `@font-face` rules. It serves as container for `<font-face-name>`,
        pointing to locally installed copies of this font, and `<font-face-uri>`,
        utilizing remotely defined fonts.
    """, )


font_face_uri = createComponent(
    'font-face-uri',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/font-face-uri',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<font-face-uri>`** SVG element points to a remote definition of the
        current font.
    """, )


hkern = createComponent(
    'hkern',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/hkern',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<hkern>`** SVG element allows to fine-tweak the horizontal distance
        between two glyphs. This process is known as kerning.
    """, )


vkern = createComponent(
    'vkern',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/vkern',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<vkern>`** SVG element allows to fine-tweak the vertical distance
        between two glyphs in top-to-bottom fonts. This process is known as kerning.
    """, )


# == Gradient Elements ==
# 

linearGradient = createComponent(
    'linearGradient',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/linearGradient',
    docs="""
        The **`<linearGradient>`** SVG element lets authors define linear gradients to
        fill or stroke graphical elements.
    """,
    examples=[
        '<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">\n    <defs>\n        <linearGradient id="MyGradient">\n            <stop offset="5%"  stop-color="green"/>\n            <stop offset="95%" stop-color="gold"/>\n        </linearGradient>\n    </defs>\n\n    <rect fill="url(#MyGradient)"\n          x="10" y="10" width="100" height="100"/>\n</svg>',
    ], )


meshgradient = createComponent(
    'meshgradient',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/meshgradient',
    notes='FIXME: http response had status 404', )


radialGradient = createComponent(
    'radialGradient',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/radialGradient',
    docs="""
        The **`<radialGradient>`** SVG element lets authors define radial gradients to
        fill or stroke graphical elements.
    """,
    examples=[
        '<svg width="120" height="120" viewBox="0 0 120 120"\n   xmlns="http://www.w3.org/2000/svg">\n\n  <defs>\n    <radialGradient id="exampleGradient">\n      <stop offset="10%" stop-color="gold"/>\n      <stop offset="95%" stop-color="green"/>\n    </radialGradient>\n  </defs>\n\n  <circle fill="url(#exampleGradient)" cx="60" cy="60" r="50"/>\n</svg>',
    ], )


stop = createComponent(
    'stop',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/stop',
    docs="""
        The **`<stop>`** SVG element defines the ramp of colors to use on a gradient,
        which is a child element to either the `<linearGradient>` or the
        `<radialGradient>` element.
    """,
    examples=[
        '<svg width="100%" height="100%" viewBox="0 0 80 40"\n     xmlns="http://www.w3.org/2000/svg">\n\n  <defs>\n    <linearGradient id="MyGradient">\n      <stop offset="5%" stop-color="#F60" />\n      <stop offset="95%" stop-color="#FF6" />\n    </linearGradient>\n  </defs>\n\n  <!-- Outline the drawing area in black -->\n  <rect fill="none" stroke="black" \n        x="0.5" y="0.5" width="79" height="39"/>\n\n  <!-- The rectangle is filled using a linear gradient -->\n  <rect fill="url(#MyGradient)" stroke="black" stroke-width="1"  \n        x="10" y="10" width="60" height="20"/>\n</svg>',
    ], )


# == Graphics Elements ==
# 

# circle: see under `Basic Shapes` above


# ellipse: see under `Basic Shapes` above


image = createComponent(
    'image',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/image',
    docs="""
        The **`<image>`** SVG element includes images inside SVG documents. It can
        display raster image files or other SVG files.
        
        The only image formats SVG software must support are JPEG, PNG, and other SVG
        files. Animated GIF behavior is undefined.
        
        SVG files displayed with `<image>` are treated as an image: external resources
        aren't loaded, :visited styles aren't applied, and they cannot be interactive.
        To include dynamic SVG elements, try <use> with an external URL. To include
        SVG files and run scripts inside them, try <object> inside of <foreignObject>.
        
        **Note:** The HTML spec defines `<image>` as a synonym for <img> while parsing
        HTML. This specific element and its behavior only apply inside SVG documents
        or inline SVG.
    """, )


# line: see under `Basic Shapes` above


mesh = createComponent(
    'mesh',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/mesh',
    notes='FIXME: http response had status 404', )


path = createComponent(
    'path',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/path',
    docs="""
        **Getting started**  
        This tutorial will help get you started using SVG paths.
        
        The **`<path>`** SVG element is the generic element to define a shape. All the
        basic shapes can be created with a path element.
    """,
    examples=[
        '<svg width="100%" height="100%" viewBox="0 0 400 400"\n     xmlns="http://www.w3.org/2000/svg">\n\n  <path d="M 100 100 L 300 100 L 200 300 z"\n        fill="orange" stroke="black" stroke-width="3" />\n</svg>',
    ], )


# polygon: see under `Basic Shapes` above


# polyline: see under `Basic Shapes` above


# rect: see under `Basic Shapes` above


text = createComponent(
    'text',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/text',
    docs="""
        The SVG **`<text>`** element defines a graphics element consisting of text.
        It's possible to apply a gradient, pattern, clipping path, mask, or filter to
        `<text>`, just like any other SVG graphics element.
        
        If text is included within SVG not inside of a `<text>` element, it is not
        rendered. This is different from being hidden by default, as setting the
        display property will not show the text.
    """,
    examples=[
        '<svg xmlns="http://www.w3.org/2000/svg"\n     width="500" height="40" viewBox="0 0 500 40">\n\n  <text x="0" y="35" font-family="Verdana" font-size="35">\n    Hello, out there\n  </text>\n</svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="180" height="120">\n  <text x="0" y="20" transform="rotate(30 20,40)">\n    SVG Text Rotation example\n  </text>\n</svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="30">\n  <text x="10" y="20" stroke="none" fill="red">\n    SVG Colored Text\n  </text>\n</svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="60">\n  <text x="10" y="40"\n      style="font-family: Times New Roman;\n             font-size: 44px;\n             stroke: #00ff00;\n             fill: #0000ff;">\n    SVG text styling\n  </text>\n</svg>',
    ], )


use = createComponent(
    'use',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/use',
    docs="""
        The **`<use>`** element takes nodes from within the SVG document, and
        duplicates them somewhere else. The effect is the same as if the nodes were
        deeply cloned into a non-exposed DOM, and then pasted where the `use` element
        is, much like cloned template elements in HTML5. Since the cloned nodes are
        not exposed, care must be taken when using CSS to style a `use` element and
        its hidden descendants. CSS attributes are not guaranteed to be inherited by
        the hidden, cloned DOM unless you explicitly request it using CSS inheritance.
        
        For security reasons, some browsers could apply a same-origin policy on `use`
        elements and could refuse to load a cross-origin URI within the `href`
        attribute.
        
        Since SVG 2, the `xlink:href` attribute is deprecated. See `xlink:href` page
        for more information.
    """, )


# == Graphics Referencing Elements ==
# 

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


iframe = createComponent(
    'iframe',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe',
    docs="""
        The **HTML`<iframe>` element** represents a nested browsing context,
        effectively embedding another HTML page into the current page. In HTML 4.01, a
        document may contain a `head` and a `body` or a `head` and a `frameset`, but
        not both a `body` and a `frameset`. However, an `<iframe>` can be used within
        a normal document body. Each browsing context has its own session history and
        active document. The browsing context that contains the embedded content is
        called the parent browsing context. The top-level browsing context (which has
        no parent) is typically the browser window.
    """,
    notes="""
        Starting in Gecko 6.0, rendering of inline frames correctly respects the
        borders of their containing element when they're rounded using `border-
        radius`.
    """,
    examples=[
        '<iframe src="https://mdn-samples.mozilla.org/snippets/html/iframe-simple-contents.html" title="iframe example 1" width="400" height="300">\n  <p>Your browser does not support iframes.</p>\n</iframe>',
        '<base target="_blank">\n<iframe id="Example2"\n    title="Example2"\n    width="400"\n    height="300"\n    frameborder="0"\n    scrolling="no"\n    marginheight="0"\n    marginwidth="0"\n    src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=es-419&amp;geocode=&amp;q=buenos+aires&amp;sll=37.0625,-95.677068&amp;sspn=38.638819,80.859375&amp;t=h&amp;ie=UTF8&amp;hq=&amp;hnear=Buenos+Aires,+Argentina&amp;z=11&amp;ll=-34.603723,-58.381593&amp;output=embed">\n</iframe>\n\n<br>\n<small>\n  <a href="https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=es-419&amp;geocode=&amp;q=buenos+aires&amp;sll=37.0625,-95.677068&amp;sspn=38.638819,80.859375&amp;t=h&amp;ie=UTF8&amp;hq=&amp;hnear=Buenos+Aires,+Argentina&amp;z=11&amp;ll=-34.603723,-58.381593" style="color:#0000FF;text-align:left"> See bigger map </a>\n</small>',
    ], )


# image: see under `Graphics Elements` above


# mesh: see under `Graphics Elements` above


# use: see under `Graphics Elements` above


video = createComponent(
    'video',
    url='http://developer.mozilla.org/en-US/docs/Web/HTML/Element/video',
    docs="""
        Use the **HTML`<video>` element** to embed video content in a document.
    """,
    examples=[
        '<!-- Simple video example -->\n<video src="videofile.webm" autoplay poster="posterimage.jpg">\nSorry, your browser doesn\'t support embedded videos, \nbut don\'t worry, you can <a href="videofile.webm">download it</a>\nand watch it with your favorite video player!\n</video>\n\n<!-- Video with subtitles -->\n<video src="foo.webm">\n  <track kind="subtitles" src="foo.en.vtt" srclang="en"\n    label="English">\n  <track kind="subtitles" src="foo.sv.vtt" srclang="sv"\n    label="Svenska">\n</video>',
    ], )


# == Html Elements ==
# 

# audio: see under `Graphics Referencing Elements` above


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


# iframe: see under `Graphics Referencing Elements` above


# video: see under `Graphics Referencing Elements` above


# == Light Source Elements ==
# 

feDistantLight = createComponent(
    'feDistantLight',
    url=
    'http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDistantLight',
    docs="""
        The **`<feDistantLight>`** filter primitive defines a distant light source
        that can be used within a lighting filter primitive: `<feDiffuseLighting>` or
        `<feSpecularLighting>`.
    """, )


fePointLight = createComponent(
    'fePointLight',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/fePointLight',
    docs="""
        The <fePointLight> SVG filter primitive allows to create a point light effect.
    """, )


feSpotLight = createComponent(
    'feSpotLight',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/feSpotLight',
    docs="""
        The **`<feSpotLight>`** SVG filter primitive allows to create a spotlight
        effect.
    """,
    examples=[
        '<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg"\n    xmlns:xlink="http://www.w3.org/1999/xlink">\n  <defs>\n    <filter id="spotlight">\n      <feSpecularLighting result="spotlight" specularConstant="1.5"\n          specularExponent="4" lighting-color="#FFF">\n        <feSpotLight x="600" y="600" z="400" limitingConeAngle="5.5" />\n      </feSpecularLighting>\n      <feComposite in="SourceGraphic" in2="spotlight" operator="out"\n          k1="0" k2="1" k3="1" k4="0"/>\n    </filter>\n  </defs>\n\n  <image xlink:href="/files/6457/mdn_logo_only_color.png" x="10%" y="10%"\n      width="80%" height="80%" style="filter:url(#spotlight);"/>\n</svg>',
    ], )


# == Never-Rendered Elements ==
# 

clipPath = createComponent(
    'clipPath',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/clipPath',
    docs="""
        The **`<clipPath>`** SVG element defines a clipping path. A clipping path is
        used/referenced using the `clip-path` property.
        
        The clipping path restricts the region to which paint can be applied.
        Conceptually, any parts of the drawing that lie outside of the region bounded
        by the currently active clipping path are not drawn.
        
        A clipping path is conceptually equivalent to a custom viewport for the
        referencing element. Thus, it affects the rendering of an element, but not the
        element's inherent geometry. The bounding box of a clipped element (meaning,
        an element which references a `<clipPath>` element via a `clip-path` property,
        or a child of the referencing element) must remain the same as if it were not
        clipped.
        
        By default, pointer-events must not be dispatched on the clipped (non-visible)
        regions of a shape. For example, a circle with a radius of 10 which is clipped
        to a circle with a radius of 5 will not receive "click" events outside the
        smaller radius.
    """,
    examples=[
        '<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">\n  <defs>\n    <clipPath id="myClip">\n      <circle cx="30" cy="30" r="20"/>\n      <circle cx="70" cy="70" r="20"/>\n    </clipPath>\n  </defs>\n\n  <rect x="10" y="10" width="100" height="100"\n      clip-path="url(#myClip)"/>\n</svg>\n\n<style>\nsvg {\n  border: 3px dashed #999;\n}\nsvg > rect:hover {\n  fill: green;\n}\n</style>',
        '<svg width="100" height="100" >\n  <defs>\n    <clipPath id="myClip">\n      <rect x="0" y="10" width="100" height="35" />\n      <rect x="0" y="55" width="100" height="35" />\n    </clipPath>\n  </defs>\n  <circle cx="50" cy="50" r="50" clip-path="url(#myClip)" />\n</svg>',
    ], )


# defs: see under `Container Elements` above


hatch = createComponent(
    'hatch',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/hatch',
    docs="""
        __ **This is an experimental technology**  
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the syntax
        and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **`<hatch>`** SVG element is used to fill or stroke an object using one or
        more pre-defined paths that are repeated at fixed intervals in a specified
        direction to cover the areas to be painted.
        
        Hatches defined by the `<hatch>` element can then referenced by the `fill` and
        `stroke` CSS properties on a given graphics element to indicate that the given
        element shall be filled or stroked with the hatch. Paths are defined by
        `<hatchpath>` elements.
    """,
    examples=[
        '<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">\n  <defs>\n    <hatch\xa0id="hatch" hatchUnits="userSpaceOnUse" pitch="5"\n        rotate="135">\n\xa0     <hatchpath stroke="#a080ff" stroke-width="2"/>\n    </hatch>\n  </defs>\n\n  <rect fill="url(#hatch)" stroke="black" stroke-width="2"\n     x="10%" y="10%" width="80%" height="80%" />\n</svg>',
    ], )


# linearGradient: see under `Gradient Elements` above


# marker: see under `Container Elements` above


# mask: see under `Container Elements` above


# meshgradient: see under `Gradient Elements` above


# metadata: see under `Descriptive Elements` above


# pattern: see under `Container Elements` above


# radialGradient: see under `Gradient Elements` above


script = createComponent(
    'script',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/script',
    docs="""
        A SVG `script` element is equivalent to the `script` element in HTML and thus
        is the place for scripts (e.g., ECMAScript).
        
        Any functions defined within any `script` element have a global scope across
        the entire current document.
    """,
    examples=[
        '<svg width="100%" height="100%" viewBox="0 0 100 100"\n     xmlns="http://www.w3.org/2000/svg">\n  <script type="text/javascript">\n    // <![CDATA[\n    function change(evt) {\n\xa0\xa0\xa0\xa0\xa0 var target = evt.target;\n\xa0\xa0\xa0\xa0\xa0 var radius = target.getAttribute("r");\n\n\xa0\xa0\xa0\xa0\xa0 if (radius == 15) {\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 radius = 45;\n\xa0\xa0\xa0\xa0\xa0 } else {\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 radius = 15;\n\xa0\xa0\xa0\xa0\xa0 }\n\n\xa0\xa0\xa0\xa0\xa0 target.setAttribute("r",radius);\n   }\n   // ]]>\n  </script>\n\n  <circle cx="50" cy="50" r="45" fill="green"\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 onclick="change(evt)" />\n</svg>',
    ], )


style = createComponent(
    'style',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/style',
    docs="""
        The **`<style>`** SVG element allows style sheets to be embedded directly
        within SVG content. SVG's `style` element has the same attributes as the
        corresponding element in HTML (see HTML's `<style>` element).
    """,
    examples=[
        '<svg width="100%" height="100%" viewBox="0 0 100 100"\n     xmlns="http://www.w3.org/2000/svg">\n  <style>\n    /* <![CDATA[ */\n    circle {\n      fill: orange;\n      stroke: black;\n      stroke-width: 10px; /* Note: The value of a pixel depends\n                             on the view box */\n    }\n    /* ]]> */\n  </style>\n\n  <circle cx="50" cy="50" r="40" />\n</svg>',
    ], )


# symbol: see under `Container Elements` above


# title: see under `Descriptive Elements` above


# == Paint Server Elements ==
# 

# hatch: see under `Never-Rendered Elements` above


# linearGradient: see under `Gradient Elements` above


# meshgradient: see under `Gradient Elements` above


# pattern: see under `Container Elements` above


# radialGradient: see under `Gradient Elements` above


solidcolor = createComponent(
    'solidcolor',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/solidcolor',
    docs="""
        __ **This is an experimental technology**  
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the syntax
        and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **`<solidcolor>`** SVG element lets authors define a single color for use
        in multiple places in an SVG document. It is also useful as away of animating
        a palette colors.
        
        **Note:** This is an experimental technology, and not yet implemented in
        browsers. A workaround is to use a `<linearGradient>` with only one color
        stop. This is less elegant, and unlike `<solidcolor>`, cannot itself be used
        in the definition of gradients.
    """,
    examples=[
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" height="150">\n  <defs>\n    <!-- solidColor is experimental. -->\n    <solidcolor id="myColor" solid-color="gold" solid-opacity="0.8"/>\n      \n    <!-- linearGradient with a single color stop is a less elegant way to \n         achieve the same effect, but it works in current browsers. -->\n    <linearGradient id="myGradient">\n      <stop offset="0" stop-color="green" />\n    </linearGradient>\n  </defs>\n   \n  <text x="10" y="20">Circles colored with solidColor</text>\n  <circle cx="150" cy="65" r="35" stroke-width="2" stroke="url(#myColor)"\n      fill="white"/>\n  <circle cx="50" cy="65" r="35" fill="url(#myColor)"/>\n\n  <text x="10" y="120">Circles colored with linearGradient</text>\n  <circle cx="150" cy="165" r="35" stroke-width="2" stroke="url(#myGradient)"\n      fill="white"/>\n  <circle cx="50" cy="165" r="35" fill="url(#myGradient)"/>\n</svg>',
    ], )


# == Renderable Elements ==
# 

# a: see under `Container Elements` above


# audio: see under `Graphics Referencing Elements` above


# canvas: see under `Html Elements` above


# circle: see under `Basic Shapes` above


# ellipse: see under `Basic Shapes` above


foreignObject = createComponent(
    'foreignObject',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject',
    docs="""
        The **`<foreignObject>`** SVG element allows for inclusion of a foreign XML
        namespace which has its graphical content drawn by a different user agent. The
        included foreign graphical content is subject to SVG transformations and
        compositing.
        
        The contents of `foreignObject` are assumed to be from a different namespace.
        Any SVG elements within a `foreignObject` will not be drawn, except in the
        situation where a properly defined SVG subdocument with a proper `xmlns`
        attribute specification is embedded recursively. One situation where this can
        occur is when an SVG document fragment is embedded within another non-SVG
        document fragment, which in turn is embedded within an SVG document fragment
        (e.g., an SVG document fragment contains an XHTML document fragment which in
        turn contains yet another SVG document fragment).
        
        Usually, a `foreignObject` will be used in conjunction with the `<switch>`
        element and the `requiredExtensions` attribute to provide proper checking for
        user agent support and provide an alternate rendering in case user agent
        support is not available.
    """, )


# g: see under `Container Elements` above


# iframe: see under `Graphics Referencing Elements` above


# image: see under `Graphics Elements` above


# line: see under `Basic Shapes` above


# mesh: see under `Graphics Elements` above


# path: see under `Graphics Elements` above


# polygon: see under `Basic Shapes` above


# polyline: see under `Basic Shapes` above


# rect: see under `Basic Shapes` above


# svg: see under `Container Elements` above


# switch: see under `Container Elements` above


# symbol: see under `Container Elements` above


# text: see under `Graphics Elements` above


textPath = createComponent(
    'textPath',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/textPath',
    docs="""
        In addition to text drawn in a straight line, SVG also includes the ability to
        place text along the shape of a `<path>` element. To specify that a block of
        text is to be rendered along the shape of a `<path>`, include the given text
        within a **`<textPath>`** element which includes an `href` attribute with a
        reference to a `<path>` element.
    """,
    examples=[
        '<svg viewBox="0 0 1000 300"\n     xmlns="http://www.w3.org/2000/svg" \n     xmlns:xlink="http://www.w3.org/1999/xlink">\n  <defs>\n    <path id="MyPath"\n          d="M 100 200 \n             C 200 100 300   0 400 100\n             C 500 200 600 300 700 200\n             C 800 100 900 100 900 100" />\n  </defs>\n\n  <use xlink:href="#MyPath" fill="none" stroke="red"  />\n\n \xa0<text font-family="Verdana" font-size="42.5">\n    <textPath xlink:href="#MyPath">\n      We go up, then we go down, then up again\n    </textPath>\n  </text>\n\n  <!-- Show outline of the viewport using \'rect\' element -->\n  <rect x="1" y="1" width="998" height="298"\n        fill="none" stroke="black" stroke-width="2" />\n</svg>',
    ], )


tspan = createComponent(
    'tspan',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan',
    docs="""
        Within a `<text>` element, text and font properties and the current text
        position can be adjusted with absolute or relative coordinate values by
        including a **`<tspan>`** element.
    """,
    examples=[
        '<?xml version="1.0"?>\n<svg width="250" height="40" viewBox="0 0 250 40"\n    xmlns="http://www.w3.org/2000/svg" version="1.1">\n\n  <style>\n<![CDATA[\ntext{\n  font: 20px Verdana, Helvetica, Arial, sans-serif;\n}\n\ntspan{\n  fill: red;\n  font-weight: bold\n}\n]]>\n  </style>\n\n  <text x="15" y="30">\n    You are \n    <tspan>not</tspan> \n    a banana\n  </text>\n</svg>',
    ], )


# unknown: see under `Container Elements` above


# use: see under `Graphics Elements` above


# video: see under `Graphics Referencing Elements` above


# == Shape Elements ==
# 

# circle: see under `Basic Shapes` above


# ellipse: see under `Basic Shapes` above


# line: see under `Basic Shapes` above


# mesh: see under `Graphics Elements` above


# path: see under `Graphics Elements` above


# polygon: see under `Basic Shapes` above


# polyline: see under `Basic Shapes` above


# rect: see under `Basic Shapes` above


# == Structural Elements ==
# 

# defs: see under `Container Elements` above


# g: see under `Container Elements` above


# svg: see under `Container Elements` above


# symbol: see under `Container Elements` above


# use: see under `Graphics Elements` above


# == Text Content Elements ==
# 

altGlyph = createComponent(
    'altGlyph',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/altGlyph',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<altGlyph>`** SVG element allows sophisticated selection of the glyphs
        used to render its child character data.
    """, )


altGlyphDef = createComponent(
    'altGlyphDef',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/altGlyphDef',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<altGlyphDef>`** SVG element defines a substitution representation for
        glyphs.
    """, )


altGlyphItem = createComponent(
    'altGlyphItem',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/altGlyphItem',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The **`<altGlyphItem>`** element provides a set of candidates for glyph
        substitution by the `<altGlyph>` element.
    """, )


glyph = createComponent(
    'glyph',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/glyph',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        A **`<glyph>`** defines a single glyph in an SVG font.
    """, )


glyphRef = createComponent(
    'glyphRef',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/glyphRef',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Do not use it in old
        or new projects. Pages or Web apps using it may break at any time.
        
        The `glyphRef` element provides a single possible glyph to the referencing
        `<altGlyph>` substitution.
    """, )


# textPath: see under `Renderable Elements` above


# text: see under `Graphics Elements` above


tref = createComponent(
    'tref',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/tref',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        The textual content for a `<text>` SVG element can be either character data
        directly embedded within the `<text>` element or the character data content of
        a referenced element, where the referencing is specified with a **`<tref>`**
        element.
    """, )


# tspan: see under `Renderable Elements` above


# == Text Content Child Elements ==
# 

# altGlyph: see under `Text Content Elements` above


# textPath: see under `Renderable Elements` above


# tref: see under `Text Content Elements` above


# tspan: see under `Renderable Elements` above


# == Uncategorized Elements ==
# 

# clipPath: see under `Never-Rendered Elements` above


color_profile = createComponent(
    'color-profile',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/color-profile',
    docs="""
        The **`<color-profile>`** element allows describing the color profile used for
        the image.
    """, )


cursor = createComponent(
    'cursor',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/cursor',
    docs="""
        **__ Deprecated**  
        This feature has been removed from the Web standards. Though some browsers may
        still support it, it is in the process of being dropped. Avoid using it and
        update existing code if possible; see the compatibility table at the bottom of
        this page to guide your decision. Be aware that this feature may cease to work
        at any time.
        
        **Note:** The CSS `cursor` property should be used instead of this element.
        
        The **`<cursor>`** SVG element can be used to define a platform-independent
        custom cursor. A recommended approach for defining a platform-independent
        custom cursor is to create a PNG image and define a `cursor` element that
        references the PNG image and identifies the exact position within the image
        which is the pointer position (i.e., the hot spot).
        
        The PNG format is recommended because it supports the ability to define a
        transparency mask via an alpha channel. If a different image format is used,
        this format should support the definition of a transparency mask (two options:
        provide an explicit alpha channel or use a particular pixel color to indicate
        transparency). If the transparency mask can be determined, the mask defines
        the shape of the cursor; otherwise, the cursor is an opaque rectangle.
        Typically, the other pixel information (e.g., the R, G and B channels) defines
        the colors for those parts of the cursor which are not masked out. Note that
        cursors usually contain at least two colors so that the cursor can be visible
        over most backgrounds.
    """, )


filter = createComponent(
    'filter',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter',
    docs="""
        The **`<filter>`** SVG element serves as container for atomic filter
        operations. It is never rendered directly. A filter is referenced by using the
        `filter` attribute on the target SVG element or via the `filter` CSS property.
    """,
    examples=[
        '<svg width="230" height="120"\n xmlns="http://www.w3.org/2000/svg"\n xmlns:xlink="http://www.w3.org/1999/xlink">\n\n <filter id="blurMe">\n  <feGaussianBlur in="SourceGraphic" stdDeviation="5"/>\n </filter>\n\n <circle cx="60"  cy="60" r="50" fill="green" />\n\n <circle cx="170" cy="60" r="50" fill="green"\n          filter="url(#blurMe)" />\n</svg>',
    ], )


# foreignObject: see under `Renderable Elements` above


hatchpath = createComponent(
    'hatchpath',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/hatchpath',
    docs="""
        __ **This is an experimental technology**  
        Because this technology's specification has not stabilized, check the
        compatibility table for usage in various browsers. Also note that the syntax
        and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **`<hatchpath>`** SVG element defines a hatch path used by the `<hatch>`
        element.
    """, )


meshpatch = createComponent(
    'meshpatch',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/meshpatch',
    notes='FIXME: http response had status 404', )


meshrow = createComponent(
    'meshrow',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/meshrow',
    notes='FIXME: http response had status 404', )


# script: see under `Never-Rendered Elements` above


# style: see under `Never-Rendered Elements` above


view = createComponent(
    'view',
    url='http://developer.mozilla.org/en-US/docs/Web/SVG/Element/view',
    docs="""
        A view is a defined way to view the image, like a zoom level or a detail view.
    """,
    examples=[
        '<svg width="600" height="200" viewBox="0 0 600 200"\n    xmlns="http://www.w3.org/2000/svg"\n    xmlns:xlink="http://www.w3.org/1999/xlink">\n  <defs>\n    <radialGradient id="gradient">\n      <stop offset="0%" stop-color="#8cffa0" />\n      <stop offset="100%" stop-color="#8ca0ff" />\n    </radialGradient>    \n  </defs>\n\n  <circle r="50" cx="180" cy="50" style="fill:url(#gradient)"/>\n\n  <view id="halfSizeView" viewBox="0 0 1200 400"/>\n  <view id="normalSizeView" viewBox="0 0 600 200"/>\n  <view id="doubleSizeView" viewBox="0 0 300 100"/>\n\n  <a xlink:href="#halfSizeView">\n    <text x="5" y="20" font-size="20">half size</text>\n  </a>\n  <a xlink:href="#normalSizeView">\n    <text x="5" y="40" font-size="20">normal size</text>\n  </a>\n  <a xlink:href="#doubleSizeView">\n    <text x="5" y="60" font-size="20">double size</text>\n  </a>\n</svg>',
    ], )


