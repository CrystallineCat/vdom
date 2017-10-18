# -*- coding: utf-8 -*-


from .core import create_component


# From https://developer.mozilla.org/en-US/docs/Web/SVG/Element


# == Animation elements ==

animate = create_component(
    'animate',
    """
        The `animate` element is put inside a shape element and defines how an
        attribute of an element changes over the animation. The attribute will change
        from the initial value to the end value in the duration specified.
    """,
)

animateColor = create_component(
    'animateColor',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  This element has been deprecated in SVG 1.1 Second
        Edition and may be removed in a future version of SVG. It provides no features
        not already available by using the [`<animate>`](/en-
        US/docs/Web/SVG/Element/animate "The animate element is put inside a shape
        element and defines how an attribute of an element changes over the animation.
        The attribute will change from the initial value to the end value in the
        duration specified.") element. So, authors should use the `<animate>` element
        instead.  The **`<animateColor>`** [SVG](/en-US/docs/Web/SVG) element specifies
        a color transformation over time.
    """,
)

animateMotion = create_component(
    'animateMotion',
    """
        The **`<animateMotion>`** element causes a referenced element to move along a
        motion path.
    """,
)

animateTransform = create_component(
    'animateTransform',
    """
        The `animateTransform` element animates a transformation attribute on a target
        element, thereby allowing animations to control translation, scaling, rotation
        and/or skewing.
    """,
)

discard = create_component(
    'discard',
    """
        The **`<discard>`** [SVG](/en-US/docs/Web/SVG) element allows authors to
        specify the time at which particular elements are to be discarded, thereby
        reducing the resources required by an SVG user agent. This is particularly
        useful to help SVG viewers conserve memory while displaying long-running
        documents.  The `<discard>` element may occur wherever the [`<animate>`](/en-
        US/docs/Web/SVG/Element/animate "The animate element is put inside a shape
        element and defines how an attribute of an element changes over the animation.
        The attribute will change from the initial value to the end value in the
        duration specified.") element may.
    """,
)

mpath = create_component(
    'mpath',
    """
        The **`<mpath>`** sub-element for the [`<animateMotion>`](/en-
        US/docs/Web/SVG/Element/animateMotion "The animateMotion element causes a
        referenced element to move along a motion path.") element provides the ability
        to reference an external [`<path>`](/en-US/docs/Web/SVG/Element/path "The path
        element is the generic element to define a shape. All the basic shapes can be
        created with a path element.") element as the definition of a motion path.
    """,
)

set_ = create_component(
    'set',
    """
        The **`<set>`** element provides a simple means of just setting the value of
        an attribute for a specified duration. It supports all attribute types,
        including those that cannot reasonably be interpolated, such as string and
        boolean values. The `<set>` element is non-additive. The additive and accumulate
        attributes are not allowed, and will be ignored if specified.
    """,
)


# == Basic shapes ==

circle = create_component(
    'circle',
    """
        The **`<circle>`** [SVG](/en-US/docs/Web/SVG) element is an SVG basic shape,
        used to create circles based on a center point and a radius.
    """,
)

ellipse = create_component(
    'ellipse',
    """
        The `ellipse` element is an SVG basic shape, used to create ellipses based on
        a center coordinate, and both their x and y radius.  Ellipses are unable to
        specify the exact orientation of the ellipse (if, for example, you wanted to
        draw an ellipse tilted at a 45 degree angle), but can be rotated by using the
        `[transform](/en-US/docs/Web/SVG/Attribute/transform)` attribute.
    """,
)

line = create_component(
    'line',
    """
        The **`<line>`** element is an SVG basic shape used to create a line
        connecting two points.
    """,
)

polygon = create_component(
    'polygon',
    """
        The **`<polygon>`** element defines a closed shape consisting of a set of
        connected straight line segments. The last point is connected to the first
        point. For open shapes see the [`<polyline>`](/en-
        US/docs/Web/SVG/Element/polyline "The <polyline> SVG element is an SVG basic
        shape that creates straight lines connecting several points. Typically a
        polyline is used to create open shapes as the last point doesn't have to be
        connected to the first point. For closed shapes see the <polygon> element.")
        element.
    """,
)

polyline = create_component(
    'polyline',
    """
        The **`<polyline>`** [SVG](/en-US/docs/Web/SVG) element is an SVG basic shape
        that creates straight lines connecting several points. Typically a `polyline` is
        used to create open shapes as the last point doesn't have to be connected to the
        first point. For closed shapes see the [`<polygon>`](/en-
        US/docs/Web/SVG/Element/polygon "The <polygon> element defines a closed shape
        consisting of a set of connected straight line segments. The last point is
        connected to the first point. For open shapes see the <polyline> element.")
        element.
    """,
)

rect = create_component(
    'rect',
    """
        The **`<rect>`** element is a basic SVG shape that creates rectangles, defined
        by their corner's position, their width, and their height. The rectangles may
        have their corners rounded.
    """,
)


# == Container elements ==

a = create_component(
    'a',
    """
        The **`<a>`** SVG element defines a hyperlink.  Since this element shares its
        tag name with [HTML's `<a>` element](/en- US/docs/Web/HTML/Element/a), selecting
        "`a`" with CSS or [`querySelector`](/en-US/docs/Web/API/Document/querySelector)
        may apply to the wrong kind of element. Try [the `@namespace` rule](/en-
        US/docs/Web/CSS/@namespace) to distinguish between the two.
    """,
)

defs = create_component(
    'defs',
    """
        SVG allows graphical objects to be defined for later reuse. It is recommended
        that, wherever possible, referenced elements be defined inside of a **`<defs>`**
        element. Defining these elements inside of a `<defs>` element promotes
        understandability of the SVG content and thus promotes accessibility. Graphical
        elements defined in a `<defs>` element will not be directly rendered. You can
        use a [`<use>`](/en-US/docs/Web/SVG/Element/use "The <use> element takes nodes
        from within the SVG document, and duplicates them somewhere else. The effect is
        the same as if the nodes were deeply cloned into a non-exposed DOM, and then
        pasted where the use element is, much like cloned template elements in HTML5.
        Since the cloned nodes are not exposed, care must be taken when using CSS to
        style a use element and its hidden descendants. CSS attributes are not
        guaranteed to be inherited by the hidden, cloned DOM unless you explicitly
        request it using CSS inheritance.") element to render those elements wherever
        you want on the viewport.
    """,
)

g = create_component(
    'g',
    """
        The **`<g>`** [SVG](/en-US/docs/Web/SVG) element is a container used to group
        other SVG elements. Transformations applied to the `<g>` element are performed
        on all of its child elements, and any of its attributes are inherited by its
        child elements. It can also group multiple elements to be referenced later with
        the [`<use>`](/en-US/docs/Web/SVG/Element/use "The <use> element takes nodes
        from within the SVG document, and duplicates them somewhere else. The effect is
        the same as if the nodes were deeply cloned into a non-exposed DOM, and then
        pasted where the use element is, much like cloned template elements in HTML5.
        Since the cloned nodes are not exposed, care must be taken when using CSS to
        style a use element and its hidden descendants. CSS attributes are not
        guaranteed to be inherited by the hidden, cloned DOM unless you explicitly
        request it using CSS inheritance.") element.
    """,
)

marker = create_component(
    'marker',
    """
        The **`<marker>`** element defines the graphics that is to be used for drawing
        arrowheads or polymarkers on a given [`<path>`](/en-
        US/docs/Web/SVG/Element/path "The <path> SVG element is the generic element to
        define a shape. All the basic shapes can be created with a path element."),
        [`<line>`](/en-US/docs/Web/SVG/Element/line "The <line> element is an SVG basic
        shape used to create a line connecting two points."), [`<polyline>`](/en-
        US/docs/Web/SVG/Element/polyline "The <polyline> SVG element is an SVG basic
        shape that creates straight lines connecting several points. Typically a
        polyline is used to create open shapes as the last point doesn't have to be
        connected to the first point. For closed shapes see the <polygon> element.") or
        [`<polygon>`](/en-US/docs/Web/SVG/Element/polygon "The <polygon> element defines
        a closed shape consisting of a set of connected straight line segments. The last
        point is connected to the first point. For open shapes see the <polyline>
        element.") element.
    """,
)

mask = create_component(
    'mask',
    """
        In SVG, you can specify that any other graphics object or [`<g>`](/en-
        US/docs/Web/SVG/Element/g "The <g> SVG element is a container used to group
        other SVG elements.") element can be used as an alpha mask for compositing the
        current object into the background. A mask is defined with the **`<mask>`**
        element. A mask is used/referenced using the `[mask](/en-
        US/docs/Web/SVG/Attribute/mask)` property.
    """,
)

missing_glyph = create_component(
    'missing-glyph',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<missing-glyph>`** [SVG](/en-US/docs/Web/SVG)
        element's content is rendered, if for a given character the font doesn't define
        an appropriate [`<glyph>`](/en-US/docs/Web/SVG/Element/glyph "A <glyph> defines
        a single glyph in an SVG font.").
    """,
)

pattern = create_component(
    'pattern',
    """
        The **`<pattern>`** element defines a graphics object which can be redrawn at
        repeated x and y-coordinate intervals ("tiled") to cover an area. The
        `<pattern>` is referenced by the `[fill](/en-US/docs/Web/SVG/Attribute/fill)`
        and/or `[stroke](/en-US/docs/Web/SVG/Attribute/stroke)` attributes on other
        [graphics elements](/en-US/docs/Web/SVG/Tutorial/Basic_Shapes) to fill or stroke
        those elements with the referenced pattern.
    """,
)

svg = create_component(
    'svg',
    """
        The `svg` element can be used to embed an SVG fragment inside the current
        document (for example, an HTML document). This SVG fragment has its own
        [viewport](/en-US/docs/Web/SVG/Attribute/viewBox) and coordinate system.
    """,
)

switch = create_component(
    'switch',
    """
        The **`<switch>`** [SVG](/en-US/docs/Web/SVG) element evaluates the
        `[requiredFeatures](/en-US/docs/Web/SVG/Attribute/requiredFeatures)`,
        `[requiredExtensions](/en-US/docs/Web/SVG/Attribute/requiredExtensions)` and
        `[systemLanguage](/en-US/docs/Web/SVG/Attribute/systemLanguage)` attributes on
        its direct child elements in order, and then processes and renders the first
        child for which these attributes evaluate to true. All others will be bypassed
        and therefore not rendered. If the child element is a container element such as
        a [`<g>`](/en-US/docs/Web/SVG/Element/g "The <g> SVG element is a container used
        to group other SVG elements."), then the entire subtree is either
        processed/rendered or bypassed/not rendered.  Note that the values of properties
        `display` and `visibility` have no effect on `switch` element processing. In
        particular, setting `display` to none on a child of a `switch` element has no
        effect on true/false testing associated with `switch` element processing.
    """,
)

symbol = create_component(
    'symbol',
    """
        The **`<symbol>`** element is used to define graphical template objects which
        can be instantiated by a [`<use>`](/en-US/docs/Web/SVG/Element/use "The <use>
        element takes nodes from within the SVG document, and duplicates them somewhere
        else. The effect is the same as if the nodes were deeply cloned into a non-
        exposed DOM, and then pasted where the use element is, much like cloned template
        elements in HTML5. Since the cloned nodes are not exposed, care must be taken
        when using CSS to style a use element and its hidden descendants. CSS attributes
        are not guaranteed to be inherited by the hidden, cloned DOM unless you
        explicitly request it using CSS inheritance.") element. The use of `symbol`
        elements for graphics that are used multiple times in the same document adds
        structure and semantics. Documents that are rich in structure may be rendered
        graphically, as speech, or as Braille, and thus promote accessibility. Note that
        a `symbol` element itself is not rendered. Only instances of a `symbol` element
        (i.e., a reference to a `symbol` by a [`<use>`](/en-US/docs/Web/SVG/Element/use
        "The <use> element takes nodes from within the SVG document, and duplicates them
        somewhere else. The effect is the same as if the nodes were deeply cloned into a
        non-exposed DOM, and then pasted where the use element is, much like
        cloned template elements in HTML5. Since the cloned nodes are not exposed, care
        must be taken when using CSS to style a use element and its hidden descendants.
        CSS attributes are not guaranteed to be inherited by the hidden, cloned DOM
        unless you explicitly request it using CSS inheritance.") element) are rendered.
    """,
)

unknown = create_component(
    'unknown',
    '',
)


# == Descriptive elements ==

desc = create_component(
    'desc',
    """
        Each container element or graphics element in an SVG drawing can supply a
        description string using the **`<desc>`** element where the description is text-
        only.  When the current SVG document fragment is rendered as SVG on visual
        media, `<desc>` elements are not rendered as part of the graphics. Alternate
        presentations are possible, both visual and aural, which display the `<desc>`
        element but do not display [`<path>`](/en-US/docs/Web/SVG/Element/path "The
        <path> SVG element is the generic element to define a shape. All the basic
        shapes can be created with a path element.") elements or other graphics
        elements. The `<desc>` element generally improves accessibility of SVG
        documents.
    """,
)

metadata = create_component(
    'metadata',
    """
        The **`<metadata>`** [SVG](/en-US/docs/Web/SVG) element allows to add metadata
        to SVG content. Metadata is structured information about data. The contents of
        `<metadata>` elements should be elements from other [XML](/en-
        US/docs/Glossary/XML "XML: eXtensible Markup Language \(XML\) is a generic
        markup language specified by the W3C. The information technology \(IT\) industry
        uses many languages based on XML as data-description languages.")
        [namespaces](/en-US/docs/Glossary/namespace "namespaces: Namespace is a context
        for identifiers, a logical grouping of names used in a program. Within the same
        context and same scope,  an identifier must uniquely identify an entity.") such
        as [RDF](/en-US/docs/Glossary/RDF "RDF: RDF \(Resource Description Framework\)
        is a language developed by W3C for representing information on the World Wide
        Web, such as Webpages. RDF provides a standard way of encoding resource
        information so that it can be exchanged in a fully automated way between
        applications."), [FOAF](https://en.wikipedia.org/wiki/FOAF_\(ontology\)), etc.
    """,
)

title = create_component(
    'title',
    """
        Each container element or graphics element in an SVG drawing can supply a
        **`<title>`** element containing a description string where the description is
        text-only. When the current SVG document fragment is rendered as SVG on visual
        media, `<title>` element is not rendered as part of the graphics. However, some
        user agents may, for example, display the `<title>` element as a tooltip.
        Alternate presentations are possible, both visual and aural, which display the
        `<title>` element but do not display `path` elements or other graphics elements.
        The `<title>` element generally improves accessibility of SVG documents.
        Generally `<title>` element should be the first child element of its parent.
        Note that those implementations that do use `<title>` to display a tooltip often
        will only do so if the `<title>` is indeed the first child element of its
        parent.
    """,
)


# == Filter primitive elements ==

feBlend = create_component(
    'feBlend',
    """
        The **`<feBlend>`** [SVG](/en-US/docs/Web/SVG) filter primitive composes two
        objects together ruled by a certain blending mode. This is similar to what is
        known from image editing software when blending two layers. The mode is defined
        by the `[mode](/en-US/docs/Web/SVG/Attribute/mode)` attribute.
    """,
)

feColorMatrix = create_component(
    'feColorMatrix',
    """
        The **`<feColorMatrix>`** SVG filter element changes colors based on a
        transformation matrix. Every pixel's color value (represented by an [R,G,B,A]
        vector) is [matrix
        multiplied](https://en.wikipedia.org/wiki/Matrix_multiplication
        "http://en.wikipedia.org/wiki/Matrix_multiplication") to create a new color.
    """,
)

feComponentTransfer = create_component(
    'feComponentTransfer',
    """
        Th **`<feComponentTransfer>`** [SVG](/en-US/docs/Web/SVG) filter primitive
        performs color-component-wise remapping of data for each pixel. It allows
        operations like brightness adjustment, contrast adjustment, color balance or
        thresholding.  The calculations are performed on non-premultiplied color values.
        The colors are modified by changing each channel (R, G, B, and A) to the result
        of what the children [`<feFuncR>`](/en-US/docs/Web/SVG/Element/feFuncR "The
        <feFuncR> SVG filter primitive defines the transfer function for the red
        component of the input graphic of its parent <feComponentTransfer> element."),
        [`<feFuncB>`](/en-US/docs/Web/SVG/Element/feFuncB "The <feFuncB> SVG filter
        primitive defines the transfer function for the blue component of the input
        graphic of its parent <feComponentTransfer> element."), [`<feFuncG>`](/en-
        US/docs/Web/SVG/Element/feFuncG "The <feFuncG> SVG filter primitive defines the
        transfer function for the green component of the input graphic of its parent
        <feComponentTransfer> element."), and [`<feFuncA>`](/en-
        US/docs/Web/SVG/Element/feFuncA "The <feFuncA> SVG filter primitive defines the
        transfer function for the alpha component of the input graphic of its parent
        <feComponentTransfer> element.") return.
    """,
)

feComposite = create_component(
    'feComposite',
    """
        This filter primitive performs the combination of two input images pixel-wise
        in image space using one of the Porter-Duff compositing operations: `over`
        _,_`in` _,_`atop` _,_`out` _,_`xor` and `lighter`. Additionally, a component-
        wise `arithmetic` operation (with the result clamped between [0..1]) can be
        applied.  The `arithmetic` operation is useful for combining the output from the
        [`<feDiffuseLighting>`](/en-US/docs/Web/SVG/Element/feDiffuseLighting "The
        <feDiffuseLighting> SVG filter primitive lights an image using the alpha channel
        as a bump map. The resulting image, which is an RGBA opaque image, depends on
        the light color, light position and surface geometry of the input bump map.")
        and [`<feSpecularLighting>`](/en- US/docs/Web/SVG/Element/feSpecularLighting
        "The <feSpecularLighting> SVG filter primitive lights a source graphic using the
        alpha channel as a bump map. The resulting image is an RGBA image based on the
        light color. The lighting calculation follows the standard specular component of
        the Phong lighting model. The resulting image depends on the light color, light
        position and surface geometry of the input bump map. The result of the lighting
        calculation is added. The filter primitive assumes that the viewer is at
        infinity in the z direction.") filters with texture data. If the `arithmetic`
        operation is chosen, each result pixel is computed using the following formula:
        result = k1*i1*i2 + k2*i1 + k3*i2 + k4       where:    * `i1` and `i2` indicate
        the corresponding pixel channel values of the input image, which map to
        `[in](/en-US/docs/Web/SVG/Attribute/in)` and `[in2](/en-
        US/docs/Web/SVG/Attribute/in2)` respectively   * `k1, k2, k3` and `k4` indicate
        the values of the attributes with the same name
    """,
)

feConvolveMatrix = create_component(
    'feConvolveMatrix',
    """
        The **`<feConvolveMatrix>`** [SVG](/en-US/docs/Web/SVG) filter primitive
        applies a matrix convolution filter effect. A convolution combines pixels in the
        input image with neighboring pixels to produce a resulting image. A wide variety
        of imaging operations can be achieved through convolutions, including blurring,
        edge detection, sharpening, embossing and beveling.  A matrix convolution is
        based on an n-by-m matrix (the convolution kernel) which describes how a given
        pixel value in the input image is combined with its neighboring pixel values to
        produce a resulting pixel value. Each result pixel is determined by applying the
        kernel matrix to the corresponding source pixel and its neighboring pixels. The
        basic convolution formula which is applied to each color value for a given pixel
        is:  COLORX,Y = (   SUM I=0 to [[orderY](https://www.w3.org/TR/SVG11/filters.htm
        l#feConvolveMatrixElementOrderAttribute)-1] {   SUM J=0 to [[orderX](https://www
        .w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute)-1] {
        SOURCE X-[targetX](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElem
        entTargetXAttribute)+J, Y-[targetY](https://www.w3.org/TR/SVG11/filters.html#feC
        onvolveMatrixElementTargetYAttribute)+I * [kernelMatrix](https://www.w3.org/TR/S
        VG11/filters.html#feConvolveMatrixElementKernelMatrixAttribute)[orderX](https://
        www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute)-J-1, [or
        derY](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttri
        bute)-I-1   }   }   ) / [divisor](https://www.w3.org/TR/SVG11/filters.html#feCon
        volveMatrixElementDivisorAttribute) \+ [bias](https://www.w3.org/TR/SVG11/filter
        s.html#feConvolveMatrixElementBiasAttribute) * ALPHAX,Y  where "orderX" and
        "orderY" represent the X and Y values for the [‘order’](https://www.w3.org/TR/SV
        G11/filters.html#feConvolveMatrixElementOrderAttribute) attribute, "targetX"
        represents the value of the [‘targetX’](https://www.w3.org/TR/SVG11/filters.html
        #feConvolveMatrixElementTargetXAttribute) attribute, "targetY" represents the
        value of the [‘targetY’](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatr
        ixElementTargetYAttribute) attribute, "kernelMatrix" represents the value of the
        [‘kernelMatrix’](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElemen
        tKernelMatrixAttribute) attribute, "divisor" represents the value of the [‘divis
        or’](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementDivisorAttr
        ibute) attribute, and "bias" represents the value of the [‘bias’](https://www.w3
        .org/TR/SVG11/filters.html#feConvolveMatrixElementBiasAttribute) attribute.
        Note in the above formulas that the values in the kernel matrix are applied such
        that the kernel matrix is rotated 180 degrees relative to the source and
        destination images in order to match convolution theory as described in many
        computer graphics textbooks.  To illustrate, suppose you have a input image
        which is 5 pixels by 5 pixels, whose color values for one of the color channels
        are as follows:           0  20  40 235 235       100 120 140 235 235       200
        220 240 235 235       225 225 255 255 255       225 225 255 255 255       and
        you define a 3-by-3 convolution kernel as follows:         1 2 3       4 5 6
        7 8 9       Let's focus on the color value at the second row and second column
        of the image (source pixel value is 120). Assuming the simplest case (where the
        input image's pixel grid aligns perfectly with the kernel's pixel grid) and
        assuming default values for attributes [‘divisor’](https://www.w3.org/TR/SVG11/f
        ilters.html#feConvolveMatrixElementDivisorAttribute), [‘targetX’](https://www.w3
        .org/TR/SVG11/filters.html#feConvolveMatrixElementTargetXAttribute) and [‘target
        Y’](https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetYAttri
        bute), then resulting color value will be:       (9*  0 + 8* 20 + 7* 40 +
        6*100 + 5*120 + 4*140 +     3*200 + 2*220 + 1*240) / (9+8+7+6+5+4+3+2+1)
    """,
)

feDiffuseLighting = create_component(
    'feDiffuseLighting',
    """
        The **`<feDiffuseLighting>`** [SVG](/en-US/docs/Web/SVG) filter primitive
        lights an image using the alpha channel as a bump map. The resulting image,
        which is an RGBA opaque image, depends on the light color, light position and
        surface geometry of the input bump map.  The light map produced by this filter
        primitive can be combined with a texture image using the multiply term of the
        `arithmetic` operator of the [`<feComposite>`](/en-
        US/docs/Web/SVG/Element/feComposite "This filter primitive performs the
        combination of two input images pixel-wise in image space using one of the
        Porter-Duff compositing operations: over, in, atop, out, xor and lighter.
        Additionally, a component-wise arithmetic operation \(with the result clamped
        between \[0..1\]\) can be applied.") filter primitive. Multiple light sources
        can be simulated by adding several of these light maps together before applying
        it to the texture image.
    """,
)

feDisplacementMap = create_component(
    'feDisplacementMap',
    """
        The **`<feDisplacementMap>`** [SVG](/en-US/docs/Web/SVG) filter primitive uses
        the pixel values from the image from `[in2](/en- US/docs/Web/SVG/Attribute/in2)`
        to spatially displace the image from `[in](/en-US/docs/Web/SVG/Attribute/in)`.
        The formula for the transformation looks like this:  `P'(x,y) ← P( x + scale *
        (XC(x,y) - 0.5), y + scale * (YC(x,y) - 0.5))`  where `P(x,y)` is the input
        image, `[in](/en-US/docs/Web/SVG/Attribute/in)`, and `P'(x,y)` is the
        destination. `XC(x,y)` and `YC(x,y)` are the component values of the channel
        designated by `[xChannelSelector](/en-
        US/docs/Web/SVG/Attribute/xChannelSelector)` and `[yChannelSelector](/en-
        US/docs/Web/SVG/Attribute/yChannelSelector)`.
    """,
)

feDropShadow = create_component(
    'feDropShadow',
    """
        The **`<feDropShadow>`** filter primitive creates a drop shadow of the input
        image. It is a shorthand filter, and is defined in terms of combinations of
        other filter primitives.  The result of the `<feDropShadow>` filter is
        equivalent to the following:       <feGaussianBlur in="alpha-channel-of-
        feDropShadow-in"         stdDeviation="stdDeviation-of-feDropShadow"/>
        <feOffset dx="dx-of-feDropShadow" dy="dy-of-feDropShadow"
        result="offsetblur"/>     <feFlood flood-color="flood-color-of-feDropShadow"
        flood-opacity="flood-opacity-of-feDropShadow"/>     <feComposite
        in2="offsetblur" operator="in"/>     <feMerge>       <feMergeNode/>
        <feMergeNode in="in-of-feDropShadow"/>     </feMerge>
    """,
)

feFlood = create_component(
    'feFlood',
    """
        The **`<feFlood>`** SVG filter primitive fills the filter subregion with the
        color and opacity defined by `[flood-color](/en-
        US/docs/Web/SVG/Attribute/flood-color)` and `[flood-opacity](/en-
        US/docs/Web/SVG/Attribute/flood-opacity)`.
    """,
)

feFuncA = create_component(
    'feFuncA',
    """
        The **`<feFuncA>`** [SVG](/en-US/docs/Web/SVG) filter primitive defines the
        transfer function for the alpha component of the input graphic of its parent
        [`<feComponentTransfer>`](/en-US/docs/Web/SVG/Element/feComponentTransfer "Th
        <feComponentTransfer> SVG filter primitive performs color-component-wise
        remapping of data for each pixel. It allows operations like brightness
        adjustment, contrast adjustment, color balance or thresholding.") element.
    """,
)

feFuncB = create_component(
    'feFuncB',
    """
        The **`<feFuncB>`** [SVG](/en-US/docs/Web/SVG) filter primitive defines the
        transfer function for the blue component of the input graphic of its parent
        [`<feComponentTransfer>`](/en-US/docs/Web/SVG/Element/feComponentTransfer "Th
        <feComponentTransfer> SVG filter primitive performs color-component-wise
        remapping of data for each pixel. It allows operations like brightness
        adjustment, contrast adjustment, color balance or thresholding.") element.
    """,
)

feFuncG = create_component(
    'feFuncG',
    """
        The **`<feFuncG>`** [SVG](/en-US/docs/Web/SVG) filter primitive defines the
        transfer function for the green component of the input graphic of its parent
        [`<feComponentTransfer>`](/en-US/docs/Web/SVG/Element/feComponentTransfer "Th
        <feComponentTransfer> SVG filter primitive performs color-component-wise
        remapping of data for each pixel. It allows operations like brightness
        adjustment, contrast adjustment, color balance or thresholding.") element.
    """,
)

feFuncR = create_component(
    'feFuncR',
    """
        The `**< feFuncR>**` [SVG](/en-US/docs/Web/SVG) filter primitive defines the
        transfer function for the red component of the input graphic of its parent
        [`<feComponentTransfer>`](/en-US/docs/Web/SVG/Element/feComponentTransfer "Th
        <feComponentTransfer> SVG filter primitive performs color-component-wise
        remapping of data for each pixel. It allows operations like brightness
        adjustment, contrast adjustment, color balance or thresholding.") element.
    """,
)

feGaussianBlur = create_component(
    'feGaussianBlur',
    """
        The **`<feGaussianBlur>`** [SVG](/en-US/docs/Web/SVG) filter primitive blurs
        the input image by the amount specified in `[stdDeviation](/en-
        US/docs/Web/SVG/Attribute/stdDeviation)`, which defines the bell-curve.
    """,
)

feImage = create_component(
    'feImage',
    """
        The **`<feImage>`** [SVG](/en-US/docs/Web/SVG) filter primitive fetches image
        data from an external source and provides the pixel data as output (meaning if
        the external source is an SVG image, it is rasterized.)
    """,
)

feMerge = create_component(
    'feMerge',
    """
        The **`<feMerge>`** SVG element allows filter effects to be applied
        concurrently instead of sequentially. This is achieved by other filters storing
        their output via the `[result](/en-US/docs/Web/SVG/Attribute/result)` attribute
        and then accessing it in a [`<feMergeNode>`](/en-
        US/docs/Web/SVG/Element/feMergeNode "The feMergeNode takes the result of another
        filter to be processed by its parent <feMerge>.") child.
    """,
)

feMergeNode = create_component(
    'feMergeNode',
    """
        The `feMergeNode` takes the result of another filter to be processed by its
        parent [`<feMerge>`](/en-US/docs/Web/SVG/Element/feMerge "The <feMerge> SVG
        element allows filter effects to be applied concurrently instead of
        sequentially. This is achieved by other filters storing their output via the
        result attribute and then accessing it in a <feMergeNode> child.").
    """,
)

feMorphology = create_component(
    'feMorphology',
    """
        The **`<feMorphology>`** [SVG](/en-US/docs/Web/SVG) filter primitive is used
        to erode or dilate the input image. It's usefulness lies especially in fattening
        or thinning effects.
    """,
)

feOffset = create_component(
    'feOffset',
    """
        The **`<feOffset>`** SVG filter primitive allows to offset the input image.
        The input image as a whole is offset by the values specified in the `[dx](/en-
        US/docs/Web/SVG/Attribute/dx)` and `[dy](/en-US/docs/Web/SVG/Attribute/dy)`
        attributes.
    """,
)

feSpecularLighting = create_component(
    'feSpecularLighting',
    """
        The **`<feSpecularLighting>`** [SVG](/en-US/docs/Web/SVG) filter primitive
        lights a source graphic using the alpha channel as a bump map. The resulting
        image is an RGBA image based on the light color. The lighting calculation
        follows the standard specular component of [the Phong lighting
        model](https://en.wikipedia.org/wiki/Phong_reflection_model
        "http://en.wikipedia.org/wiki/Phong_reflection_model"). The resulting image
        depends on the light color, light position and surface geometry of the input
        bump map. The result of the lighting calculation is added. The filter primitive
        assumes that the viewer is at infinity in the z direction.  This filter
        primitive produces an image which contains the specular reflection part of the
        lighting calculation. Such a map is intended to be combined with a texture using
        the `add` term of the arithmetic [`<feComposite>`](/en-
        US/docs/Web/SVG/Element/feComposite "This filter primitive performs the
        combination of two input images pixel-wise in image space using one of the
        Porter-Duff compositing operations: over, in, atop, out, xor and lighter.
        Additionally, a component-wise arithmetic operation \(with the result clamped
        between \[0..1\]\) can be applied.") method. Multiple light sources can be
        simulated by adding several of these light maps before applying it to the
        texture image.
    """,
)

feTile = create_component(
    'feTile',
    """
        The **`<feTile>`** [SVG](/en-US/docs/Web/SVG) filter primitive allows to fill
        a target rectangle with a repeated, tiled pattern of an input image. The effect
        is similar to the one of a [`<pattern>`](/en- US/docs/Web/SVG/Element/pattern
        "The <pattern> element defines a graphics object which can be redrawn at
        repeated x and y-coordinate intervals \("tiled"\) to cover an area.").
    """,
)

feTurbulence = create_component(
    'feTurbulence',
    """
        The **`<feTurbulence>`** [SVG](/en-US/docs/Web/SVG) filter primitive creates
        an image using the [Perlin turbulence
        function](https://en.wikipedia.org/wiki/Perlin_noise). It allows the synthesis
        of artificial textures like clouds or marble. The resulting image will fill the
        entire filter primitive subregion.
    """,
)


# == Font elements ==

font = create_component(
    'font',
    """
        The **`<font>`** [SVG](/en-US/docs/Web/SVG) element defines a font to be used
        for text layout.
    """,
)

font_face = create_component(
    'font-face',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<font-face>`** [SVG](/en-US/docs/Web/SVG)
        element corresponds to the CSS [`@font-face`](/en-US/docs/Web/CSS/@font-face
        "The @font-face CSS at-rule allows authors to specify online fonts to display
        text on their web pages. By allowing authors to provide their own fonts, @font-
        face eliminates the need to depend on the limited number of fonts users have
        installed on their computers. The @font-face at-rule may be used not only at the
        top level of a CSS, but also inside any CSS conditional-group at-rule.") rule.
        It defines a font's outer properties.
    """,
)

font_face_format = create_component(
    'font-face-format',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<font-face-format>`** [SVG](/en-
        US/docs/Web/SVG) element describes the type of font referenced by its parent
        [`<font-face-uri>`](/en- US/docs/Web/SVG/Element/font-face-uri "The font-face-
        uri element points to a remote definition of the current font.").
    """,
)

font_face_name = create_component(
    'font-face-name',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<font-face-name>`** element points to a
        locally installed copy of this font, identified by its name.
    """,
)

font_face_src = create_component(
    'font-face-src',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<font-face-src>`** [SVG](/en-US/docs/Web/SVG)
        element corresponds to the [`src`](/en-US/docs/Web/CSS/@font-face/src "The
        documentation about this has not yet been written; please consider
        contributing!") descriptor in CSS [`@font-face`](/en-US/docs/Web/CSS/@font-face
        "The @font-face CSS at-rule allows authors to specify online fonts to display
        text on their web pages. By allowing authors to provide their own fonts, @font-
        face eliminates the need to depend on the limited number of fonts users have
        installed on their computers. The @font-face at-rule may be used not only at the
        top level of a CSS, but also inside any CSS conditional-group at-rule.") rules.
        It serves as container for [`<font-face-name>`](/en-
        US/docs/Web/SVG/Element/font-face-name "The <font-face-name> element points to a
        locally installed copy of this font, identified by its name."), pointing to
        locally installed copies of this font, and [`<font-face-uri>`](/en-
        US/docs/Web/SVG/Element/font-face-uri "The font- face-uri element points to a
        remote definition of the current font."), utilizing remotely defined fonts.
    """,
)

font_face_uri = create_component(
    'font-face-uri',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<font-face-uri>`** [SVG](/en-US/docs/Web/SVG)
        element points to a remote definition of the current font.
    """,
)

hkern = create_component(
    'hkern',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<hkern>`** [SVG](/en-US/docs/Web/SVG) element
        allows to fine-tweak the horizontal distance between two glyphs. This process is
        known as [kerning](https://en.wikipedia.org/wiki/Kerning).
    """,
)

vkern = create_component(
    'vkern',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<vkern>`** SVG element allows to fine-tweak
        the vertical distance between two glyphs in top-to-bottom fonts. This process is
        known as [kerning](https://en.wikipedia.org/wiki/Kerning).
    """,
)


# == Gradient elements ==

linearGradient = create_component(
    'linearGradient',
    """
        The **`<linearGradient>`** [SVG](/en-US/docs/Web/SVG) element lets authors
        define linear gradients to fill or stroke graphical elements.
    """,
)

meshgradient = create_component(
    'meshgradient',
    '',
)

radialGradient = create_component(
    'radialGradient',
    """
        The **`<radialGradient>`** [SVG](/en-US/docs/Web/SVG) element lets authors
        define radial gradients to fill or stroke graphical elements.
    """,
)

stop = create_component(
    'stop',
    """
        The **`<stop>`** [SVG](/en-US/docs/Web/SVG) element defines the ramp of colors
        to use on a gradient, which is a child element to either the
        [`<linearGradient>`](/en-US/docs/Web/SVG/Element/linearGradient "The
        <linearGradient> SVG element lets authors define linear gradients to fill or
        stroke graphical elements.") or the [`<radialGradient>`](/en-
        US/docs/Web/SVG/Element/radialGradient "The <radialGradient> SVG element lets
        authors define radial gradients to fill or stroke graphical elements.") element.
    """,
)


# == Graphics elements ==

# circle: see above under 'Basic shapes'

# ellipse: see above under 'Basic shapes'

image = create_component(
    'image',
    """
        The **`<image>`** SVG element includes images inside SVG documents. It can
        display [raster image](/en-US/docs/Glossary/raster_image "raster image: A raster
        image is an image file defined as a grid of pixels. They’re also referred to as
        bitmaps. Common raster image formats on the Web are JPEG, PNG, GIF, and ICO.")
        files or other SVG files.  The only image formats SVG software must support are
        [JPEG](/en- US/docs/Glossary/jpeg), [PNG](/en-US/docs/Glossary/PNG), and other
        SVG files. Animated [GIF](/en-US/docs/Glossary/gif) behavior is undefined.  SVG
        files displayed with `<image>` are [treated as an image](/en-
        US/docs/Web/SVG/SVG_as_an_Image): external resources aren't loaded,
        [:visited](/en-US/docs/Web/CSS/:visited) styles [aren't applied](/en-
        US/docs/Web/CSS/Privacy_and_the_:visited_selector), and they cannot be
        interactive. To include dynamic SVG elements, try [<use>](/en-
        US/docs/Web/SVG/Element/use) with an external URL. To include SVG files and run
        scripts inside them, try [<object>](/en-US/docs/Web/HTML/Element/object) inside
        of [<foreignObject>](/en-US/docs/Web/SVG/Element/foreignObject).  **Note:** The
        HTML spec defines `<image>` as a synonym for [<img>](/en-
        US/docs/Web/HTML/Element/img) while parsing HTML. This specific element and its
        behavior only apply inside SVG documents or [inline SVG](/en-
        US/docs/SVG_In_HTML_Introduction).
    """,
)

# line: see above under 'Basic shapes'

mesh = create_component(
    'mesh',
    '',
)

path = create_component(
    'path',
    """
        **[Getting started](/en-US/docs/Web/SVG/Tutorial/Paths)**   This tutorial will
        help get you started using SVG paths.  The **`<path>`** [SVG](/en-
        US/docs/Web/SVG) element is the generic element to define a shape. All the basic
        shapes can be created with a path element.
    """,
)

# polygon: see above under 'Basic shapes'

# polyline: see above under 'Basic shapes'

# rect: see above under 'Basic shapes'

text = create_component(
    'text',
    """
        The SVG **`<text>`** element defines a graphics element consisting of text.
        It's possible to apply a gradient, pattern, clipping path, mask, or filter to
        `<text>`, just like any other SVG graphics element.  If text is included within
        SVG not inside of a `<text>` element, it is not rendered. This is different from
        being hidden by default, as setting [the display property](/en-
        US/docs/Web/SVG/Attribute/display) will not show the text.
    """,
)

use = create_component(
    'use',
    """
        The **`<use>`** element takes nodes from within the SVG document, and
        duplicates them somewhere else. The effect is the same as if the nodes were
        deeply cloned into a non-exposed DOM, and then pasted where the `use` element
        is, much like cloned [template elements](/en- US/docs/Web/HTML/Element/template)
        in HTML5. Since the cloned nodes are not exposed, care must be taken when using
        [CSS](/en-US/docs/Web/CSS "en/CSS") to style a `use` element and its hidden
        descendants. CSS attributes are not guaranteed to be inherited by the hidden,
        cloned DOM unless you explicitly request it using [CSS inheritance](/en-
        US/docs/Web/CSS/inheritance "en/CSS/inheritance").  For security reasons, some
        browsers could apply a same-origin policy on `use` elements and could refuse to
        load a cross-origin URI within the `[href](/en- US/docs/Web/SVG/Attribute/href)`
        attribute.  Since SVG 2, the `[xlink:href](/en-
        US/docs/Web/SVG/Attribute/xlink:href)` attribute is deprecated. See
        `[xlink:href](/en- US/docs/Web/SVG/Attribute/xlink:href)` page for more
        information.
        
        ### Notes
    """,
)


# == Graphics referencing elements ==

audio = create_component(
    'audio',
    '',
)

iframe = create_component(
    'iframe',
    """
        The **HTML`<iframe>` element** represents a nested browsing context,
        effectively embedding another HTML page into the current page. In HTML 4.01, a
        document may contain a `head` and a `body` or a `head` and a `frameset`, but not
        both a `body` and a `frameset`. However, an `<iframe>` can be used within a
        normal document body. Each browsing context has its own session history and
        active document. The browsing context that contains the embedded content is
        called the  parent browsing context. The top-level browsing context (which has
        no parent) is typically the browser window.
        
        ## Notes
    """,
)

# image: see above under 'Graphics elements'

# mesh: see above under 'Graphics elements'

# use: see above under 'Graphics elements'

video = create_component(
    'video',
    '',
)


# == HTML elements ==

# audio: see above under 'Graphics referencing elements'

canvas = create_component(
    'canvas',
    '',
)

# iframe: see above under 'Graphics referencing elements'

# video: see above under 'Graphics referencing elements'


# == Light source elements ==

feDistantLight = create_component(
    'feDistantLight',
    """
        The **`<feDistantLight>`** filter primitive defines a distant light source
        that can be used within a lighting filter primitive:
        [`<feDiffuseLighting>`](/en-US/docs/Web/SVG/Element/feDiffuseLighting "The
        <feDiffuseLighting> SVG filter primitive lights an image using the alpha channel
        as a bump map. The resulting image, which is an RGBA opaque image, depends on
        the light color, light position and surface geometry of the input bump map.") or
        [`<feSpecularLighting>`](/en- US/docs/Web/SVG/Element/feSpecularLighting "The
        <feSpecularLighting> SVG filter primitive lights a source graphic using the
        alpha channel as a bump map. The resulting image is an RGBA image based on the
        light color. The lighting calculation follows the standard specular component of
        the Phong lighting model. The resulting image depends on the light color, light
        position and surface geometry of the input bump map. The result of the lighting
        calculation is added. The filter primitive assumes that the viewer is at
        infinity in the z direction.").
    """,
)

fePointLight = create_component(
    'fePointLight',
    'The <fePointLight> SVG filter primitive allows to create a point light effect.',
)

feSpotLight = create_component(
    'feSpotLight',
    """
        The **`<feSpotLight>`** [SVG](/en-US/docs/Web/SVG) filter primitive allows to
        create a spotlight effect.
    """,
)


# == Never-rendered elements ==

clipPath = create_component(
    'clipPath',
    """
        The **`<clipPath>`** [SVG](/en-US/docs/Web/SVG) element defines a clipping
        path. A clipping path is used/referenced using the `[clip-path](/en-
        US/docs/Web/SVG/Attribute/clip-path)` property.  The clipping path restricts the
        region to which paint can be applied. Conceptually, any parts of the drawing
        that lie outside of the region bounded by the currently active clipping path are
        not drawn.  A clipping path is conceptually equivalent to a custom viewport for
        the referencing element. Thus, it affects the rendering of an element, but not
        the element's inherent geometry. The bounding box of a clipped element (meaning,
        an element which references a `<clipPath>` element via a `[clip-path](/en-
        US/docs/Web/SVG/Attribute/clip-path)` property, or a child of the referencing
        element) must remain the same as if it were not clipped.  By default, pointer-
        events must not be dispatched on the clipped (non-visible) regions of a shape.
        For example, a circle with a radius of 10 which is clipped to a circle with a
        radius of 5 will not receive "click" events outside the smaller radius.
    """,
)

# defs: see above under 'Container elements'

hatch = create_component(
    'hatch',
    """
        __ **This is an experimental technology**   Because this technology's
        specification has not stabilized, check the compatibility table for usage in
        various browsers. Also note that the syntax and behavior of an experimental
        technology is subject to change in future versions of browsers as the
        specification changes.  The **`<hatch>`** [SVG](/en-US/docs/Web/SVG) element is
        used to fill or stroke an object using one or more pre-defined paths that are
        repeated at fixed intervals in a specified direction to cover the areas to be
        painted.  Hatches defined by the `<hatch>` element can then referenced by the
        [`fill`](/en-US/docs/Web/CSS/fill "The documentation about this has not yet been
        written; please consider contributing!") and [`stroke`](/en-
        US/docs/Web/CSS/stroke "The documentation about this has not yet been written;
        please consider contributing!") [CSS](/en-US/docs/Glossary/CSS "CSS: CSS
        \(Cascading Style Sheets\) is a declarative language that controls how webpages
        look in the browser.") properties on a given [graphics element](/en-
        US/docs/Web/SVG/Element#Graphics_elements) to indicate that the given element
        shall be filled or stroked with the hatch. Paths are defined by
        [`<hatchpath>`](/en-US/docs/Web/SVG/Element/hatchpath "The <hatchpath> SVG
        element defines a hatch path used by the <hatch> element.") elements.
    """,
)

# linearGradient: see above under 'Gradient elements'

# marker: see above under 'Container elements'

# mask: see above under 'Container elements'

# meshgradient: see above under 'Gradient elements'

# metadata: see above under 'Descriptive elements'

# pattern: see above under 'Container elements'

# radialGradient: see above under 'Gradient elements'

script = create_component(
    'script',
    """
        A SVG `script` element is equivalent to the [`script`](/en-
        US/HTML/Element/Script) element in HTML and thus is the place for scripts (e.g.,
        ECMAScript).  Any functions defined within any `script` element have a global
        scope across the entire current document.
    """,
)

style = create_component(
    'style',
    """
        The **`<style>`** [SVG](/en-US/docs/Web/SVG) element allows style sheets to be
        embedded directly within SVG content. SVG's `style` element has the same
        attributes as the corresponding element in HTML (see HTML's [`<style>`](/en-
        US/docs/Web/HTML/Element/style "The HTML <style> element contains style
        information for a document, or part of a document. By default, the style
        instructions written inside that element are expected to be CSS.") element).
    """,
)

# symbol: see above under 'Container elements'

# title: see above under 'Descriptive elements'


# == Paint server elements ==

# hatch: see above under 'Never-rendered elements'

# linearGradient: see above under 'Gradient elements'

# meshgradient: see above under 'Gradient elements'

# pattern: see above under 'Container elements'

# radialGradient: see above under 'Gradient elements'

solidcolor = create_component(
    'solidcolor',
    """
        __ **This is an experimental technology**   Because this technology's
        specification has not stabilized, check the compatibility table for usage in
        various browsers. Also note that the syntax and behavior of an experimental
        technology is subject to change in future versions of browsers as the
        specification changes.  The **`<solidcolor>`** [SVG](/en-US/docs/Web/SVG)
        element lets authors define a single color for use in multiple places in an SVG
        document. It is also useful as away of animating a palette colors.  **Note:**
        This is an experimental technology, and not yet implemented in browsers. A
        workaround is to use a [`<linearGradient>`](/en-
        US/docs/Web/SVG/Element/linearGradient "The <linearGradient> SVG element lets
        authors define linear gradients to fill or stroke graphical elements.") with
        only one color stop. This is less elegant, and unlike `<solidcolor>`, cannot
        itself be used in the definition of gradients.
    """,
)


# == Renderable elements ==

# a: see above under 'Container elements'

# audio: see above under 'Graphics referencing elements'

# canvas: see above under 'HTML elements'

# circle: see above under 'Basic shapes'

# ellipse: see above under 'Basic shapes'

foreignObject = create_component(
    'foreignObject',
    """
        The **`<foreignObject>`** [SVG](/en-US/docs/Web/SVG) element allows for
        inclusion of a foreign XML namespace which has its graphical content drawn by a
        different user agent. The included foreign graphical content is subject to SVG
        transformations and compositing.  The contents of `foreignObject` are assumed to
        be from a different namespace. Any SVG elements within a `foreignObject` will
        not be drawn, except in the situation where a properly defined SVG subdocument
        with a proper `xmlns` attribute specification is embedded recursively. One
        situation where this can occur is when an SVG document fragment is embedded
        within another non-SVG document fragment, which in turn is embedded within an
        SVG document fragment (e.g., an SVG document fragment contains an XHTML document
        fragment which in turn contains yet another SVG document fragment).  Usually, a
        `foreignObject` will be used in conjunction with the [`<switch>`](/en-
        US/docs/Web/SVG/Element/switch "The <switch> SVG element evaluates the
        requiredFeatures, requiredExtensions and systemLanguage attributes on its direct
        child elements in order, and then processes and renders the first child for
        which these attributes evaluate to true. All others will be bypassed and
        therefore not rendered. If the child element is a container element such as a
        <g>, then the entire subtree is either processed/rendered or bypassed/not
        rendered.") element and the `[requiredExtensions](/en-
        US/docs/Web/SVG/Attribute/requiredExtensions)` attribute to provide proper
        checking for user agent support and provide an alternate rendering in case user
        agent support is not available.
    """,
)

# g: see above under 'Container elements'

# iframe: see above under 'Graphics referencing elements'

# image: see above under 'Graphics elements'

# line: see above under 'Basic shapes'

# mesh: see above under 'Graphics elements'

# path: see above under 'Graphics elements'

# polygon: see above under 'Basic shapes'

# polyline: see above under 'Basic shapes'

# rect: see above under 'Basic shapes'

# svg: see above under 'Container elements'

# switch: see above under 'Container elements'

# symbol: see above under 'Container elements'

# text: see above under 'Graphics elements'

textPath = create_component(
    'textPath',
    """
        In addition to text drawn in a straight line, SVG also includes the ability to
        place text along the shape of a [`<path>`](/en-US/docs/Web/SVG/Element/path "The
        path element is the generic element to define a shape. All the basic shapes can
        be created with a path element.") element. To specify that a block of text is to
        be rendered along the shape of a [`<path>`](/en- US/docs/Web/SVG/Element/path
        "The path element is the generic element to define a shape. All the basic shapes
        can be created with a path element."), include the given text within a
        **`<textPath>`** element which includes an `[href](/en-
        US/docs/Web/SVG/Attribute/href)` attribute with a reference to a [`<path>`](/en-
        US/docs/Web/SVG/Element/path "The path element is the generic element to define
        a shape. All the basic shapes can be created with a path element.") element.
    """,
)

tspan = create_component(
    'tspan',
    """
        Within a [`<text>`](/en-US/docs/Web/SVG/Element/text "The SVG <text> element
        defines a graphics element consisting of text. It's possible to apply a
        gradient, pattern, clipping path, mask, or filter to <text>, just like any other
        SVG graphics element.") element, text and font properties and the current text
        position can be adjusted with absolute or relative coordinate values by
        including a **`<tspan>`** element.
    """,
)

# unknown: see above under 'Container elements'

# use: see above under 'Graphics elements'

# video: see above under 'Graphics referencing elements'


# == Shape elements ==

# circle: see above under 'Basic shapes'

# ellipse: see above under 'Basic shapes'

# line: see above under 'Basic shapes'

# mesh: see above under 'Graphics elements'

# path: see above under 'Graphics elements'

# polygon: see above under 'Basic shapes'

# polyline: see above under 'Basic shapes'

# rect: see above under 'Basic shapes'


# == Structural elements ==

# defs: see above under 'Container elements'

# g: see above under 'Container elements'

# svg: see above under 'Container elements'

# symbol: see above under 'Container elements'

# use: see above under 'Graphics elements'


# == Text content elements ==

altGlyph = create_component(
    'altGlyph',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<altGlyph>`** [SVG](/en-US/docs/Web/SVG)
        element allows sophisticated selection of the glyphs used to render its child
        character data.
    """,
)

altGlyphDef = create_component(
    'altGlyphDef',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<altGlyphDef>`** [SVG](/en-US/docs/Web/SVG)
        element defines a substitution representation for glyphs.
    """,
)

altGlyphItem = create_component(
    'altGlyphItem',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The **`<altGlyphItem>`** element provides a set of
        candidates for glyph substitution by the [`<altGlyph>`](/en-
        US/docs/Web/SVG/Element/altGlyph "The altGlyph element allows sophisticated
        selection of the glyphs used to render its child character data.") element.
    """,
)

glyph = create_component(
    'glyph',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  A **`<glyph>`** defines a single glyph in an SVG
        font.
    """,
)

glyphRef = create_component(
    'glyphRef',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Do
        not use it in old or new projects. Pages or Web apps using it may break at any
        time.  The `glyphRef` element provides a single possible glyph to the
        referencing [`<altGlyph>`](/en-US/docs/Web/SVG/Element/altGlyph "The altGlyph
        element allows sophisticated selection of the glyphs used to render its child
        character data.") substitution.
    """,
)

# textPath: see above under 'Renderable elements'

# text: see above under 'Graphics elements'

tref = create_component(
    'tref',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  The textual content for a [`<text>`](/en-
        US/docs/Web/SVG/Element/text "The SVG <text> element defines a graphics element
        consisting of text. It's possible to apply a gradient, pattern, clipping path,
        mask, or filter to <text>, just like any other SVG graphics element.")
        [SVG](/en-US/docs/Web/SVG) element can be either character data directly
        embedded within the [`<text>`](/en- US/docs/Web/SVG/Element/text "The SVG <text>
        element defines a graphics element consisting of text. It's possible to apply a
        gradient, pattern, clipping path, mask, or filter to <text>, just like any other
        SVG graphics element.") element or the character data content of a referenced
        element, where the referencing is specified with a **`<tref>`** element.
    """,
)

# tspan: see above under 'Renderable elements'


# == Text content child elements ==

# altGlyph: see above under 'Text content elements'

# textPath: see above under 'Renderable elements'

# tref: see above under 'Text content elements'

# tspan: see above under 'Renderable elements'


# == Uncategorized elements ==

# clipPath: see above under 'Never-rendered elements'

color_profile = create_component(
    'color-profile',
    """
        The **`<color-profile>`** element allows describing the color profile used for
        the image.
    """,
)

cursor = create_component(
    'cursor',
    """
        **__ Deprecated**   This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the compatibility table at
        the bottom of this page to guide your decision. Be aware that this feature may
        cease to work at any time.  **Note:** The CSS [`cursor`](/en-
        US/docs/Web/CSS/cursor "The cursor CSS property specifies the mouse cursor
        displayed when the mouse pointer is over an element.") property should be used
        instead of this element.  The **`<cursor>`** [SVG](/en-US/docs/Web/SVG) element
        can be used to define a platform-independent custom cursor. A recommended
        approach for defining a platform-independent custom cursor is to create a PNG
        image and define a `cursor` element that references the PNG image and identifies
        the exact position within the image which is the pointer position (i.e., the hot
        spot).  The PNG format is recommended because it supports the ability to define
        a transparency mask via an alpha channel. If a different image format is used,
        this format should support the definition of a transparency mask (two options:
        provide an explicit alpha channel or use a particular pixel color to indicate
        transparency). If the transparency mask can be determined, the mask defines the
        shape of the cursor; otherwise, the cursor is an opaque rectangle. Typically,
        the other pixel information (e.g., the R, G and B channels) defines the colors
        for those parts of the cursor which are not masked out. Note that cursors
        usually contain at least two colors so that the cursor can be visible over most
        backgrounds.
    """,
)

filter_ = create_component(
    'filter',
    """
        The **`<filter>`** [SVG](/en-US/docs/Web/SVG) element serves as container for
        atomic filter operations. It is never rendered directly. A filter is referenced
        by using the `[filter](/en-US/docs/Web/SVG/Attribute/filter)` attribute on the
        target SVG element or via the [`filter`](/en- US/docs/Web/CSS/filter "The filter
        CSS property lets you apply graphical effects like blurring, sharpening, or
        color shifting to an element. Filters are commonly used to adjust the rendering
        of images, backgrounds, and borders.") [CSS](/en-US/docs/Glossary/CSS "CSS: CSS
        \(Cascading Style Sheets\) is a declarative language that controls how webpages
        look in the browser.") property.
    """,
)

# foreignObject: see above under 'Renderable elements'

hatchpath = create_component(
    'hatchpath',
    """
        __ **This is an experimental technology**   Because this technology's
        specification has not stabilized, check the compatibility table for usage in
        various browsers. Also note that the syntax and behavior of an experimental
        technology is subject to change in future versions of browsers as the
        specification changes.  The **`<hatchpath>`** [SVG](/en-US/docs/Web/SVG) element
        defines a hatch path used by the [`<hatch>`](/en-US/docs/Web/SVG/Element/hatch
        "The <hatch> SVG element is used to fill or stroke an object using one or more
        pre-defined paths that are repeated at fixed intervals in a specified direction
        to cover the areas to be painted.") element.
    """,
)

meshpatch = create_component(
    'meshpatch',
    '',
)

meshrow = create_component(
    'meshrow',
    '',
)

# script: see above under 'Never-rendered elements'

# style: see above under 'Never-rendered elements'

view = create_component(
    'view',
    'A view is a defined way to view the image, like a zoom level or a detail view.',
)


__all__ = [
    'a', 'altGlyph', 'altGlyphDef', 'altGlyphItem', 'animate', 'animateColor',
    'animateMotion', 'animateTransform', 'audio', 'canvas', 'circle',
    'clipPath', 'color_profile', 'cursor', 'defs', 'desc', 'discard',
    'ellipse', 'feBlend', 'feColorMatrix', 'feComponentTransfer',
    'feComposite', 'feConvolveMatrix', 'feDiffuseLighting',
    'feDisplacementMap', 'feDistantLight', 'feDropShadow', 'feFlood',
    'feFuncA', 'feFuncB', 'feFuncG', 'feFuncR', 'feGaussianBlur', 'feImage',
    'feMerge', 'feMergeNode', 'feMorphology', 'feOffset', 'fePointLight',
    'feSpecularLighting', 'feSpotLight', 'feTile', 'feTurbulence', 'filter_',
    'font', 'font_face', 'font_face_format', 'font_face_name', 'font_face_src',
    'font_face_uri', 'foreignObject', 'g', 'glyph', 'glyphRef', 'hatch',
    'hatchpath', 'hkern', 'iframe', 'image', 'line', 'linearGradient',
    'marker', 'mask', 'mesh', 'meshgradient', 'meshpatch', 'meshrow',
    'metadata', 'missing_glyph', 'mpath', 'path', 'pattern', 'polygon',
    'polyline', 'radialGradient', 'rect', 'script', 'set_', 'solidcolor',
    'stop', 'style', 'svg', 'switch', 'symbol', 'text', 'textPath', 'title',
    'tref', 'tspan', 'unknown', 'use', 'video', 'view', 'vkern'
]

