# -*- coding: utf-8 -*-


from vdom.core import Component


# From https://developer.mozilla.org/en-US/docs/Web/SVG/Element


# == Animation elements ==


class animate(Component):
    """
        The ``animate`` element is put inside a shape element and defines how an
        attribute of an element changes over the animation. The attribute will change
        from the initial value to the end value in the duration specified.
    """


class animateColor(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        This element has been deprecated in SVG 1.1 Second Edition and may be removed in
        a future version of SVG. It provides no features not already available by using
        the ```<animate>`` </en-US/docs/Web/SVG/Element/animate>`_ element. So, authors
        should use the ``<animate>`` element instead.
        
        The **``<animateColor>``** `SVG </en-US/docs/Web/SVG>`_ element specifies a
        color transformation over time.
    """


class animateMotion(Component):
    """
        The **``<animateMotion>``** element causes a referenced element to move along a
        motion path.
    """


class animateTransform(Component):
    """
        The ``animateTransform`` element animates a transformation attribute on a target
        element, thereby allowing animations to control translation, scaling, rotation
        and/or skewing.
    """


class discard(Component):
    """
        The **``<discard>``** `SVG </en-US/docs/Web/SVG>`_ element allows authors to
        specify the time at which particular elements are to be discarded, thereby
        reducing the resources required by an SVG user agent. This is particularly
        useful to help SVG viewers conserve memory while displaying long-running
        documents.
        
        The ``<discard>`` element may occur wherever the ```<animate>`` </en-
        US/docs/Web/SVG/Element/animate>`_ element may.
    """


class mpath(Component):
    """
        The **``<mpath>``** sub-element for the ```<animateMotion>`` </en-
        US/docs/Web/SVG/Element/animateMotion>`_ element provides the ability to
        reference an external ```<path>`` </en-US/docs/Web/SVG/Element/path>`_ element
        as the definition of a motion path.
    """


class set_(Component):
    """
        The **``<set>``** element provides a simple means of just setting the value of
        an attribute for a specified duration. It supports all attribute types,
        including those that cannot reasonably be interpolated, such as string and
        boolean values. The ``<set>`` element is non-additive. The additive and
        accumulate attributes are not allowed, and will be ignored if specified.
    """

    tag_name = 'set'


# == Basic shapes ==


class circle(Component):
    """
        The **``<circle>``** `SVG </en-US/docs/Web/SVG>`_ element is an SVG basic shape,
        used to create circles based on a center point and a radius.
    """


class ellipse(Component):
    """
        The ``ellipse`` element is an SVG basic shape, used to create ellipses based on
        a center coordinate, and both their x and y radius.
        
        Ellipses are unable to specify the exact orientation of the ellipse (if, for
        example, you wanted to draw an ellipse tilted at a 45 degree angle), but can be
        rotated by using the ```transform </en-US/docs/Web/SVG/Attribute/transform>`_``
        attribute.
    """


class line(Component):
    """
        The **``<line>``** element is an SVG basic shape used to create a line
        connecting two points.
    """


class polygon(Component):
    """
        The **``<polygon>``** element defines a closed shape consisting of a set of
        connected straight line segments. The last point is connected to the first
        point. For open shapes see the```<polyline>`` </en-
        US/docs/Web/SVG/Element/polyline>`_ element.
    """


class polyline(Component):
    """
        The **``<polyline>``** `SVG </en-US/docs/Web/SVG>`_ element is an SVG basic
        shape that creates straight lines connecting several points. Typically a
        ``polyline`` is used to create open shapes as the last point doesn't have to be
        connected to the first point. For closed shapes see the ```<polygon>`` </en-
        US/docs/Web/SVG/Element/polygon>`_ element.
    """


class rect(Component):
    """
        The **``<rect>``** element is a basic SVG shape that creates rectangles, defined
        by their corner's position, their width, and their height. The rectangles may
        have their corners rounded.
    """


# == Container elements ==


class a(Component):
    """
        The **``<a>``** SVG element defines a hyperlink.
        
        Since this element shares its tag name with `HTML's ``<a>`` element </en-
        US/docs/Web/HTML/Element/a>`_, selecting "``a``" with CSS or ```querySelector``
        </en-US/docs/Web/API/Document/querySelector>`_ may apply to the wrong kind of
        element. Try `the ``@namespace`` rule </en-US/docs/Web/CSS/@namespace>`_ to
        distinguish between the two.
    """


class defs(Component):
    """
        SVG allows graphical objects to be defined for later reuse. It is recommended
        that, wherever possible, referenced elements be defined inside of a
        **``<defs>``** element. Defining these elements inside of a ``<defs>`` element
        promotes understandability of the SVG content and thus promotes accessibility.
        Graphical elements defined in a ``<defs>`` element will not be directly
        rendered. You can use a ```<use>`` </en-US/docs/Web/SVG/Element/use>`_ element
        to render those elements wherever you want on the viewport.
    """


class g(Component):
    """
        The **``<g>``** `SVG </en-US/docs/Web/SVG>`_ element is a container used to
        group other SVG elements. Transformations applied to the ``<g>`` element are
        performed on all of its child elements, and any of its attributes are inherited
        by its child elements. It can also group multiple elements to be referenced
        later with the ```<use>`` </en-US/docs/Web/SVG/Element/use>`_ element.
    """


class marker(Component):
    """
        The **``<marker>``** element defines the graphics that is to be used for drawing
        arrowheads or polymarkers on a given ```<path>`` </en-
        US/docs/Web/SVG/Element/path>`_, ```<line>`` </en-
        US/docs/Web/SVG/Element/line>`_, ```<polyline>`` </en-
        US/docs/Web/SVG/Element/polyline>`_ or ```<polygon>`` </en-
        US/docs/Web/SVG/Element/polygon>`_ element.
    """


class mask(Component):
    """
        In SVG, you can specify that any other graphics object or ```<g>`` </en-
        US/docs/Web/SVG/Element/g>`_ element can be used as an alpha mask for
        compositing the current object into the background. A mask is defined with the
        **``<mask>``** element. A mask is used/referenced using the ```mask </en-
        US/docs/Web/SVG/Attribute/mask>`_`` property.
    """


class missing_glyph(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<missing-glyph>``** `SVG </en-US/docs/Web/SVG>`_ element's content is
        rendered, if for a given character the font doesn't define an appropriate
        ```<glyph>`` </en-US/docs/Web/SVG/Element/glyph>`_.
    """

    tag_name = 'missing-glyph'


class pattern(Component):
    """
        The **``<pattern>``** element defines a graphics object which can be redrawn at
        repeated x and y-coordinate intervals ("tiled") to cover an area. The
        ``<pattern>`` is referenced by the ```fill </en-
        US/docs/Web/SVG/Attribute/fill>`_`` and/or ```stroke </en-
        US/docs/Web/SVG/Attribute/stroke>`_`` attributes on other `graphics elements
        </en-US/docs/Web/SVG/Tutorial/Basic_Shapes>`_ to fill or stroke those elements
        with the referenced pattern.
    """


class svg(Component):
    """
        The ``svg`` element can be used to embed an SVG fragment inside the current
        document (for example, an HTML document). This SVG fragment has its own
        `viewport </en-US/docs/Web/SVG/Attribute/viewBox>`_ and coordinate system.
    """


class switch(Component):
    """
        The **``<switch>``** `SVG </en-US/docs/Web/SVG>`_ element evaluates the
        ```requiredFeatures </en-US/docs/Web/SVG/Attribute/requiredFeatures>`_``,
        ```requiredExtensions </en-US/docs/Web/SVG/Attribute/requiredExtensions>`_`` and
        ```systemLanguage </en-US/docs/Web/SVG/Attribute/systemLanguage>`_`` attributes
        on its direct child elements in order, and then processes and renders the first
        child for which these attributes evaluate to true. All others will be bypassed
        and therefore not rendered. If the child element is a container element such as
        a ```<g>`` </en-US/docs/Web/SVG/Element/g>`_, then the entire subtree is either
        processed/rendered or bypassed/not rendered.
        
        Note that the values of properties ``display`` and ``visibility`` have no effect
        on ``switch`` element processing. In particular, setting ``display`` to none on
        a child of a ``switch`` element has no effect on true/false testing associated
        with ``switch`` element processing.
    """


class symbol(Component):
    """
        The **``<symbol>``** element is used to define graphical template objects which
        can be instantiated by a ```<use>`` </en-US/docs/Web/SVG/Element/use>`_ element.
        The use of ``symbol`` elements for graphics that are used multiple times in the
        same document adds structure and semantics. Documents that are rich in structure
        may be rendered graphically, as speech, or as Braille, and thus promote
        accessibility. Note that a ``symbol`` element itself is not rendered. Only
        instances of a ``symbol`` element (i.e., a reference to a ``symbol`` by a
        ```<use>```_ element) are rendered.
    """


class unknown(Component):
    ''


# == Descriptive elements ==


class desc(Component):
    """
        Each container element or graphics element in an SVG drawing can supply a
        description string using the **``<desc>``** element where the description is
        text-only.
        
        When the current SVG document fragment is rendered as SVG on visual media,
        ``<desc>`` elements are not rendered as part of the graphics. Alternate
        presentations are possible, both visual and aural, which display the ``<desc>``
        element but do not display ```<path>`` </en-US/docs/Web/SVG/Element/path>`_
        elements or other graphics elements. The ``<desc>`` element generally improves
        accessibility of SVG documents.
    """


class metadata(Component):
    """
        The **``<metadata>``** `SVG </en-US/docs/Web/SVG>`_ element allows to add
        metadata to SVG content. Metadata is structured information about data. The
        contents of ``<metadata>`` elements should be elements from other `XML </en-
        US/docs/Glossary/XML>`_ `namespaces </en-US/docs/Glossary/namespace>`_ such as
        `RDF </en-US/docs/Glossary/RDF>`_, `FOAF
        <https://en.wikipedia.org/wiki/FOAF_(ontology)>`_, etc.
    """


class title(Component):
    """
        Each container element or graphics element in an SVG drawing can supply a
        **``<title>``** element containing a description string where the description is
        text-only. When the current SVG document fragment is rendered as SVG on visual
        media, ``<title>`` element is not rendered as part of the graphics. However,
        some user agents may, for example, display the ``<title>`` element as a tooltip.
        Alternate presentations are possible, both visual and aural, which display the
        ``<title>`` element but do not display ``path`` elements or other graphics
        elements. The ``<title>`` element generally improves accessibility of SVG
        documents.
        
        Generally ``<title>`` element should be the first child element of its parent.
        Note that those implementations that do use ``<title>`` to display a tooltip
        often will only do so if the ``<title>`` is indeed the first child element of
        its parent.
    """


# == Filter primitive elements ==


class feBlend(Component):
    """
        The **``<feBlend>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive composes two
        objects together ruled by a certain blending mode. This is similar to what is
        known from image editing software when blending two layers. The mode is defined
        by the ```mode </en-US/docs/Web/SVG/Attribute/mode>`_`` attribute.
    """


class feColorMatrix(Component):
    """
        The **``<feColorMatrix>``** SVG filter element changes colors based on a
        transformation matrix. Every pixel's color value (represented by an [R,G,B,A]
        vector) is `matrix multiplied
        <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ to create a new color.
    """


class feComponentTransfer(Component):
    """
        Th **``<feComponentTransfer>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive
        performs color-component-wise remapping of data for each pixel. It allows
        operations like brightness adjustment, contrast adjustment, color balance or
        thresholding.
        
        The calculations are performed on non-premultiplied color values. The colors are
        modified by changing each channel (R, G, B, and A) to the result of what the
        children ```<feFuncR>`` </en-US/docs/Web/SVG/Element/feFuncR>`_, ```<feFuncB>``
        </en-US/docs/Web/SVG/Element/feFuncB>`_, ```<feFuncG>`` </en-
        US/docs/Web/SVG/Element/feFuncG>`_, and ```<feFuncA>`` </en-
        US/docs/Web/SVG/Element/feFuncA>`_ return.
    """


class feComposite(Component):
    """
        This filter primitive performs the combination of two input images pixel-wise in
        image space using one of the Porter-Duff compositing operations: ``over``*,*
        ``in``*,* ``atop``*,* ``out``*,* ``xor`` and ``lighter``. Additionally, a
        component-wise ``arithmetic`` operation (with the result clamped between [0..1])
        can be applied.
        
        The ``arithmetic`` operation is useful for combining the output from the
        ```<feDiffuseLighting>`` </en-US/docs/Web/SVG/Element/feDiffuseLighting>`_ and
        ```<feSpecularLighting>`` </en-US/docs/Web/SVG/Element/feSpecularLighting>`_
        filters with texture data. If the ``arithmetic`` operation is chosen, each
        result pixel is computed using the following formula:
        
        result = k1*i1*i2 + k2*i1 + k3*i2 + k4
        
        where:
        
        * ``i1`` and ``i2`` indicate the corresponding pixel channel values of the input
        image, which map to ```in </en-US/docs/Web/SVG/Attribute/in>`_`` and ```in2
        </en-US/docs/Web/SVG/Attribute/in2>`_`` respectively
        
        * ``k1, k2, k3`` and ``k4`` indicate the values of the attributes with the same
        name
    """


class feConvolveMatrix(Component):
    """
        The **``<feConvolveMatrix>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive
        applies a matrix convolution filter effect. A convolution combines pixels in the
        input image with neighboring pixels to produce a resulting image. A wide variety
        of imaging operations can be achieved through convolutions, including blurring,
        edge detection, sharpening, embossing and beveling.
        
        A matrix convolution is based on an n-by-m matrix (the convolution kernel) which
        describes how a given pixel value in the input image is combined with its
        neighboring pixel values to produce a resulting pixel value. Each result pixel
        is determined by applying the kernel matrix to the corresponding source pixel
        and its neighboring pixels. The basic convolution formula which is applied to
        each color value for a given pixel is:
        
        COLORX,Y= ( SUMI=0 to [`orderY <https://www.w3.org/TR/SVG11/filters.html#feConvo
        lveMatrixElementOrderAttribute>`_-1]{ SUMJ=0 to [`orderX <https://www.w3.org/TR/
        SVG11/filters.html#feConvolveMatrixElementOrderAttribute>`_-1]{ SOURCEX-`targetX
        <https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetXAttribut
        e>`_+J, Y-`targetY <https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixEle
        mentTargetYAttribute>`_+I*`kernelMatrix <https://www.w3.org/TR/SVG11/filters.htm
        l#feConvolveMatrixElementKernelMatrixAttribute>`_`orderX`_-J-1,`orderY`_-I-1 } }
        ) /`divisor <https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementDiv
        isorAttribute>`_+`bias <https://www.w3.org/TR/SVG11/filters.html#feConvolveMatri
        xElementBiasAttribute>`_* ALPHAX,Y
        
        where "orderX" and "orderY" represent the X and Y values for the`‘order’ <https:
        //www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementOrderAttribute>`_attri
        bute, "targetX" represents the value of the`‘targetX’ <https://www.w3.org/TR/SVG
        11/filters.html#feConvolveMatrixElementTargetXAttribute>`_attribute, "targetY"
        represents the value of the`‘targetY’ <https://www.w3.org/TR/SVG11/filters.html#
        feConvolveMatrixElementTargetYAttribute>`_attribute, "kernelMatrix" represents
        the value of the`‘kernelMatrix’ <https://www.w3.org/TR/SVG11/filters.html#feConv
        olveMatrixElementKernelMatrixAttribute>`_attribute, "divisor" represents the
        value of the`‘divisor’ <https://www.w3.org/TR/SVG11/filters.html#feConvolveMatri
        xElementDivisorAttribute>`_attribute, and "bias" represents the value of
        the`‘bias’ <https://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElementBias
        Attribute>`_attribute.
        
        Note in the above formulas that the values in the kernel matrix are applied such
        that the kernel matrix is rotated 180 degrees relative to the source and
        destination images in order to match convolution theory as described in many
        computer graphics textbooks.
        
        To illustrate, suppose you have a input image which is 5 pixels by 5 pixels,
        whose color values for one of the color channels are as follows:
        
        <pre>    0  20  40 235 235   100 120 140 235 235   200 220 240 235 235   225 225
        255 255 255   225 225 255 255 255 </pre>
        
        and you define a 3-by-3 convolution kernel as follows:
        
        <pre>  1 2 3   4 5 6   7 8 9 </pre>
        
        Let's focus on the color value at the second row and second column of the image
        (source pixel value is 120). Assuming the simplest case (where the input image's
        pixel grid aligns perfectly with the kernel's pixel grid) and assuming default
        values for attributes`‘divisor’ <https://www.w3.org/TR/SVG11/filters.html#feConv
        olveMatrixElementDivisorAttribute>`_,`‘targetX’ <https://www.w3.org/TR/SVG11/fil
        ters.html#feConvolveMatrixElementTargetXAttribute>`_and`‘targetY’ <https://www.w
        3.org/TR/SVG11/filters.html#feConvolveMatrixElementTargetYAttribute>`_, then
        resulting color value will be:
        
        <pre>(9*  0 + 8* 20 + 7* 40 + 6*100 + 5*120 + 4*140 + 3*200 + 2*220 + 1*240) /
        (9+8+7+6+5+4+3+2+1)</pre>
    """


class feDiffuseLighting(Component):
    """
        The **``<feDiffuseLighting>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive
        lights an image using the alpha channel as a bump map. The resulting image,
        which is an RGBA opaque image, depends on the light color, light position and
        surface geometry of the input bump map.
        
        The light map produced by this filter primitive can be combined with a texture
        image using the multiply term of the ``arithmetic`` operator of the
        ```<feComposite>`` </en-US/docs/Web/SVG/Element/feComposite>`_ filter primitive.
        Multiple light sources can be simulated by adding several of these light maps
        together before applying it to the texture image.
    """


class feDisplacementMap(Component):
    """
        The **``<feDisplacementMap>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive
        uses the pixel values from the image from ```in2 </en-
        US/docs/Web/SVG/Attribute/in2>`_`` to spatially displace the image from ```in
        </en-US/docs/Web/SVG/Attribute/in>`_``.
        
        The formula for the transformation looks like this:
        
        ``P'(x,y) ← P( x + scale * (XC(x,y) - 0.5), y + scale * (YC(x,y) - 0.5))``
        
        where ``P(x,y)`` is the input image, ```in </en-
        US/docs/Web/SVG/Attribute/in>`_``, and ``P'(x,y)`` is the destination.
        ``XC(x,y)`` and ``YC(x,y)`` are the component values of the channel designated
        by ```xChannelSelector </en-US/docs/Web/SVG/Attribute/xChannelSelector>`_`` and
        ```yChannelSelector </en-US/docs/Web/SVG/Attribute/yChannelSelector>`_``.
    """


class feDropShadow(Component):
    """
        The **``<feDropShadow>``** filter primitive creates a drop shadow of the input
        image. It is a shorthand filter, and is defined in terms of combinations of
        other filter primitives.
        
        The result of the ``<feDropShadow>`` filter is equivalent to the following:
        
        <feGaussianBlur in="alpha-channel-of-feDropShadow-in"
        stdDeviation="stdDeviation-of-feDropShadow"/> <feOffset dx="dx-of-feDropShadow"
        dy="dy-of-feDropShadow" result="offsetblur"/> <feFlood flood-color="flood-color-
        of-feDropShadow" flood-opacity="flood-opacity-of-feDropShadow"/> <feComposite
        in2="offsetblur" operator="in"/> <feMerge> <feMergeNode/> <feMergeNode in="in-
        of-feDropShadow"/> </feMerge>
    """


class feFlood(Component):
    """
        The **``<feFlood>``** SVG filter primitive fills the filter subregion with the
        color and opacity defined by ```flood-color </en-
        US/docs/Web/SVG/Attribute/flood-color>`_`` and ```flood-opacity </en-
        US/docs/Web/SVG/Attribute/flood-opacity>`_``.
    """


class feFuncA(Component):
    """
        The **``<feFuncA>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive defines the
        transfer function for the alpha component of the input graphic of its parent
        ```<feComponentTransfer>`` </en-US/docs/Web/SVG/Element/feComponentTransfer>`_
        element.
    """


class feFuncB(Component):
    """
        The **``<feFuncB>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive defines the
        transfer function for the blue component of the input graphic of its parent
        ```<feComponentTransfer>`` </en-US/docs/Web/SVG/Element/feComponentTransfer>`_
        element.
    """


class feFuncG(Component):
    """
        The **``<feFuncG>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive defines the
        transfer function for the green component of the input graphic of its parent
        ```<feComponentTransfer>`` </en-US/docs/Web/SVG/Element/feComponentTransfer>`_
        element.
    """


class feFuncR(Component):
    """
        The ``**<feFuncR>**`` `SVG </en-US/docs/Web/SVG>`_ filter primitive defines the
        transfer function for the red component of the input graphic of its parent
        ```<feComponentTransfer>`` </en-US/docs/Web/SVG/Element/feComponentTransfer>`_
        element.
    """


class feGaussianBlur(Component):
    """
        The **``<feGaussianBlur>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive blurs
        the input image by the amount specified in ```stdDeviation </en-
        US/docs/Web/SVG/Attribute/stdDeviation>`_``, which defines the bell-curve.
    """


class feImage(Component):
    """
        The **``<feImage>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive fetches
        image data from an external source and provides the pixel data as output
        (meaning if the external source is an SVG image, it is rasterized.)
    """


class feMerge(Component):
    """
        The **``<feMerge>``** SVG element allows filter effects to be applied
        concurrently instead of sequentially. This is achieved by other filters storing
        their output via the ```result </en-US/docs/Web/SVG/Attribute/result>`_``
        attribute and then accessing it in a ```<feMergeNode>`` </en-
        US/docs/Web/SVG/Element/feMergeNode>`_ child.
    """


class feMergeNode(Component):
    """
        The ``feMergeNode`` takes the result of another filter to be processed by its
        parent ```<feMerge>`` </en-US/docs/Web/SVG/Element/feMerge>`_.
    """


class feMorphology(Component):
    """
        The **``<feMorphology>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive is used
        to erode or dilate the input image. It's usefulness lies especially in fattening
        or thinning effects.
    """


class feOffset(Component):
    """
        The **``<feOffset>``** SVG filter primitive allows to offset the input image.
        The input image as a whole is offset by the values specified in the ```dx </en-
        US/docs/Web/SVG/Attribute/dx>`_`` and ```dy </en-
        US/docs/Web/SVG/Attribute/dy>`_`` attributes.
    """


class feSpecularLighting(Component):
    """
        The **``<feSpecularLighting>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive
        lights a source graphic using the alpha channel as a bump map. The resulting
        image is an RGBA image based on the light color. The lighting calculation
        follows the standard specular component of `the Phong lighting model
        <https://en.wikipedia.org/wiki/Phong_reflection_model>`_. The resulting image
        depends on the light color, light position and surface geometry of the input
        bump map. The result of the lighting calculation is added. The filter primitive
        assumes that the viewer is at infinity in the z direction.
        
        This filter primitive produces an image which contains the specular reflection
        part of the lighting calculation. Such a map is intended to be combined with a
        texture using the ``add`` term of the arithmetic ```<feComposite>`` </en-
        US/docs/Web/SVG/Element/feComposite>`_ method. Multiple light sources can be
        simulated by adding several of these light maps before applying it to the
        texture image.
    """


class feTile(Component):
    """
        The **``<feTile>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive allows to
        fill a target rectangle with a repeated, tiled pattern of an input image. The
        effect is similar to the one of a ```<pattern>`` </en-
        US/docs/Web/SVG/Element/pattern>`_.
    """


class feTurbulence(Component):
    """
        The **``<feTurbulence>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive creates
        an image using the `Perlin turbulence function
        <https://en.wikipedia.org/wiki/Perlin_noise>`_. It allows the synthesis of
        artificial textures like clouds or marble. The resulting image will fill the
        entire filter primitive subregion.
    """


# == Font elements ==


class font(Component):
    """
        The **``<font>``** `SVG </en-US/docs/Web/SVG>`_ element defines a font to be
        used for text layout.
    """


class font_face(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<font-face>``** `SVG </en-US/docs/Web/SVG>`_ element corresponds to the
        CSS ```@font-face`` </en-US/docs/Web/CSS/@font-face>`_ rule. It defines a font's
        outer properties.
    """

    tag_name = 'font-face'


class font_face_format(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<font-face-format>``** `SVG </en-US/docs/Web/SVG>`_ element describes
        the type of font referenced by its parent ```<font-face-uri>`` </en-
        US/docs/Web/SVG/Element/font-face-uri>`_.
    """

    tag_name = 'font-face-format'


class font_face_name(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<font-face-name>``** element points to a locally installed copy of this
        font, identified by its name.
    """

    tag_name = 'font-face-name'


class font_face_src(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<font-face-src>``** `SVG </en-US/docs/Web/SVG>`_ element corresponds to
        the ```src`` </en-US/docs/Web/CSS/@font-face/src>`_ descriptor in CSS ```@font-
        face`` </en-US/docs/Web/CSS/@font-face>`_ rules. It serves as container for
        ```<font-face-name>`` </en-US/docs/Web/SVG/Element/font-face-name>`_, pointing
        to locally installed copies of this font, and ```<font-face-uri>`` </en-
        US/docs/Web/SVG/Element/font-face-uri>`_, utilizing remotely defined fonts.
    """

    tag_name = 'font-face-src'


class font_face_uri(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<font-face-uri>``** `SVG </en-US/docs/Web/SVG>`_ element points to a
        remote definition of the current font.
    """

    tag_name = 'font-face-uri'


class hkern(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<hkern>``** `SVG </en-US/docs/Web/SVG>`_ element allows to fine-tweak
        the horizontal distance between two glyphs. This process is known as `kerning
        <https://en.wikipedia.org/wiki/Kerning>`_.
    """


class vkern(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<vkern>``** SVG element allows to fine-tweak the vertical distance
        between two glyphs in top-to-bottom fonts. This process is known as `kerning
        <https://en.wikipedia.org/wiki/Kerning>`_.
    """


# == Gradient elements ==


class linearGradient(Component):
    """
        The **``<linearGradient>``** `SVG </en-US/docs/Web/SVG>`_ element lets authors
        define linear gradients to fill or stroke graphical elements.
    """


class meshgradient(Component):
    ''


class radialGradient(Component):
    """
        The **``<radialGradient>``** `SVG </en-US/docs/Web/SVG>`_ element lets authors
        define radial gradients to fill or stroke graphical elements.
    """


class stop(Component):
    """
        The **``<stop>``** `SVG </en-US/docs/Web/SVG>`_ element defines the ramp of
        colors to use on a gradient, which is a child element to either the
        ```<linearGradient>`` </en-US/docs/Web/SVG/Element/linearGradient>`_ or the
        ```<radialGradient>`` </en-US/docs/Web/SVG/Element/radialGradient>`_ element.
    """


# == Graphics elements ==

# circle: see above under 'Basic shapes'

# ellipse: see above under 'Basic shapes'


class image(Component):
    """
        The **``<image>``** SVG element includes images inside SVG documents. It can
        display `raster image </en-US/docs/Glossary/raster_image>`_ files or other SVG
        files.
        
        The only image formats SVG software must support are `JPEG </en-
        US/docs/Glossary/jpeg>`_, `PNG </en-US/docs/Glossary/PNG>`_, and other SVG
        files. Animated `GIF </en-US/docs/Glossary/gif>`_ behavior is undefined.
        
        SVG files displayed with ``<image>`` are `treated as an image </en-
        US/docs/Web/SVG/SVG_as_an_Image>`_: external resources aren't loaded, `:visited
        </en-US/docs/Web/CSS/:visited>`_ styles `aren't applied </en-
        US/docs/Web/CSS/Privacy_and_the_:visited_selector>`_, and they cannot be
        interactive. To include dynamic SVG elements, try `<use> </en-
        US/docs/Web/SVG/Element/use>`_ with an external URL. To include SVG files and
        run scripts inside them, try `<object> </en-US/docs/Web/HTML/Element/object>`_
        inside of `<foreignObject> </en-US/docs/Web/SVG/Element/foreignObject>`_.
        
        **Note:** The HTML spec defines ``<image>`` as a synonym for `<img> </en-
        US/docs/Web/HTML/Element/img>`_ while parsing HTML. This specific element and
        its behavior only apply inside SVG documents or `inline SVG </en-
        US/docs/SVG_In_HTML_Introduction>`_.
    """


# line: see above under 'Basic shapes'


class mesh(Component):
    ''


class path(Component):
    """
        **`Getting started </en-US/docs/Web/SVG/Tutorial/Paths>`_**\\This tutorial will
        help get you started using SVG paths.
        
        The **``<path>``** `SVG </en-US/docs/Web/SVG>`_ element is the generic element
        to define a shape. All the basic shapes can be created with a path element.
    """


# polygon: see above under 'Basic shapes'

# polyline: see above under 'Basic shapes'

# rect: see above under 'Basic shapes'


class text(Component):
    """
        The SVG **``<text>``** element defines a graphics element consisting of text.
        It's possible to apply a gradient, pattern, clipping path, mask, or filter to
        ``<text>``, just like any other SVG graphics element.
        
        If text is included within SVG not inside of a ``<text>`` element, it is not
        rendered. This is different from being hidden by default, as setting `the
        display property </en-US/docs/Web/SVG/Attribute/display>`_ will not show the
        text.
    """


class use(Component):
    """
        The **``<use>``** element takes nodes from within the SVG document, and
        duplicates them somewhere else. The effect is the same as if the nodes were
        deeply cloned into a non-exposed DOM, and then pasted where the ``use`` element
        is, much like cloned`template elements </en-
        US/docs/Web/HTML/Element/template>`_in HTML5. Since the cloned nodes are not
        exposed, care must be taken when using `CSS </en-US/docs/Web/CSS>`_ to style a
        ``use`` element and its hidden descendants. CSS attributes are not guaranteed to
        be inherited by the hidden, cloned DOM unless you explicitly request it using
        `CSS inheritance </en-US/docs/Web/CSS/inheritance>`_.
        
        For security reasons, some browsers could apply a same-origin policy on ``use``
        elements and could refuse to load a cross-origin URI within the ```href </en-
        US/docs/Web/SVG/Attribute/href>`_`` attribute.
        
        Since SVG 2, the ```xlink:href </en-US/docs/Web/SVG/Attribute/xlink:href>`_``
        attribute is deprecated. See ```xlink:href`_`` page for more information.
        
        Notes =====
    """


# == Graphics referencing elements ==


class audio(Component):
    ''


class iframe(Component):
    """
        The **HTML ``<iframe>``element**represents a nested browsing context,
        effectively embedding another HTML page into the current page. In HTML 4.01, a
        document may contain a ``head`` and a ``body`` or a ``head`` and a ``frameset``,
        but not both a ``body`` and a ``frameset``. However, an ``<iframe>`` can be used
        within a normal document body. Each browsing context has its own session history
        and active document. The browsing context that contains the embedded content is
        called the parent browsing context. The top-level browsing context (which has no
        parent) is typically the browser window.
        
        ----- Notes -----
    """


# image: see above under 'Graphics elements'

# mesh: see above under 'Graphics elements'

# use: see above under 'Graphics elements'


class video(Component):
    ''


# == HTML elements ==

# audio: see above under 'Graphics referencing elements'


class canvas(Component):
    ''


# iframe: see above under 'Graphics referencing elements'

# video: see above under 'Graphics referencing elements'


# == Light source elements ==


class feDistantLight(Component):
    """
        The **``<feDistantLight>``** filter primitive defines a distant light source
        that can be used within a lighting filter primitive: ```<feDiffuseLighting>``
        </en-US/docs/Web/SVG/Element/feDiffuseLighting>`_ or ```<feSpecularLighting>``
        </en-US/docs/Web/SVG/Element/feSpecularLighting>`_.
    """


class fePointLight(Component):
    'The <fePointLight> SVG filter primitive allows to create a point light effect.'


class feSpotLight(Component):
    """
        The **``<feSpotLight>``** `SVG </en-US/docs/Web/SVG>`_ filter primitive allows
        to create a spotlight effect.
    """


# == Never-rendered elements ==


class clipPath(Component):
    """
        The **``<clipPath>``** `SVG </en-US/docs/Web/SVG>`_ element defines a clipping
        path. A clipping path is used/referenced using the ```clip-path </en-
        US/docs/Web/SVG/Attribute/clip-path>`_`` property.
        
        The clipping path restricts the region to which paint can be applied.
        Conceptually, any parts of the drawing that lie outside of the region bounded by
        the currently active clipping path are not drawn.
        
        A clipping path is conceptually equivalent to a custom viewport for the
        referencing element. Thus, it affects the rendering of an element, but not the
        element's inherent geometry. The bounding box of a clipped element (meaning, an
        element which references a ``<clipPath>`` element via a ```clip-path </en-
        US/docs/Web/SVG/Attribute/clip-path>`_`` property, or a child of the referencing
        element) must remain the same as if it were not clipped.
        
        By default, pointer-events must not be dispatched on the clipped (non-visible)
        regions of a shape. For example, a circle with a radius of 10 which is clipped
        to a circle with a radius of 5 will not receive "click" events outside the
        smaller radius.
    """


# defs: see above under 'Container elements'


class hatch(Component):
    """
        ** **This is an experimental technology**\\Because this technology's
        specification has not stabilized, check the `compatibility table
        <#Browser_compatibility>`_ for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **``<hatch>``** `SVG </en-US/docs/Web/SVG>`_ element is used to fill or
        stroke an object using one or more pre-defined paths that are repeated at fixed
        intervals in a specified direction to cover the areas to be painted.
        
        Hatches defined by the ``<hatch>`` element can then referenced by the```fill``
        </en-US/docs/Web/CSS/fill>`_ and ```stroke`` </en-US/docs/Web/CSS/stroke>`_ `CSS
        </en-US/docs/Glossary/CSS>`_ properties on a given `graphics element </en-
        US/docs/Web/SVG/Element#Graphics_elements>`_ to indicate that the given element
        shall be filled or stroked with the hatch. Paths are defined by ```<hatchpath>``
        </en-US/docs/Web/SVG/Element/hatchpath>`_ elements.
    """


# linearGradient: see above under 'Gradient elements'

# marker: see above under 'Container elements'

# mask: see above under 'Container elements'

# meshgradient: see above under 'Gradient elements'

# metadata: see above under 'Descriptive elements'

# pattern: see above under 'Container elements'

# radialGradient: see above under 'Gradient elements'


class script(Component):
    """
        A SVG ``script`` element is equivalent to the ```script`` </en-
        US/HTML/Element/Script>`_ element in HTML and thus is the place for scripts
        (e.g., ECMAScript).
        
        Any functions defined within any ``script`` element have a global scope across
        the entire current document.
    """


class style(Component):
    """
        The **``<style>``** `SVG </en-US/docs/Web/SVG>`_ element allows style sheets to
        be embedded directly within SVG content. SVG's ``style`` element has the same
        attributes as the corresponding element in HTML (see HTML's ```<style>`` </en-
        US/docs/Web/HTML/Element/style>`_ element).
    """


# symbol: see above under 'Container elements'

# title: see above under 'Descriptive elements'


# == Paint server elements ==

# hatch: see above under 'Never-rendered elements'

# linearGradient: see above under 'Gradient elements'

# meshgradient: see above under 'Gradient elements'

# pattern: see above under 'Container elements'

# radialGradient: see above under 'Gradient elements'


class solidcolor(Component):
    """
        ** **This is an experimental technology**\\Because this technology's
        specification has not stabilized, check the `compatibility table
        <#Browser_compatibility>`_ for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **``<solidcolor>``** `SVG </en-US/docs/Web/SVG>`_ element lets authors
        define a single color for use in multiple places in an SVG document. It is also
        useful as away of animating a palette colors.
        
        **Note:** This is an experimental technology, and not yet implemented in
        browsers. A workaround is to use a ```<linearGradient>`` </en-
        US/docs/Web/SVG/Element/linearGradient>`_ with only one color stop. This is less
        elegant, and unlike ``<solidcolor>``, cannot itself be used in the definition of
        gradients.
    """


# == Renderable elements ==

# a: see above under 'Container elements'

# audio: see above under 'Graphics referencing elements'

# canvas: see above under 'HTML elements'

# circle: see above under 'Basic shapes'

# ellipse: see above under 'Basic shapes'


class foreignObject(Component):
    """
        The **``<foreignObject>``** `SVG </en-US/docs/Web/SVG>`_ element allows for
        inclusion of a foreign XML namespace which has its graphical content drawn by a
        different user agent. The included foreign graphical content is subject to SVG
        transformations and compositing.
        
        The contents of ``foreignObject`` are assumed to be from a different namespace.
        Any SVG elements within a ``foreignObject`` will not be drawn, except in the
        situation where a properly defined SVG subdocument with a proper ``xmlns``
        attribute specification is embedded recursively. One situation where this can
        occur is when an SVG document fragment is embedded within another non-SVG
        document fragment, which in turn is embedded within an SVG document fragment
        (e.g., an SVG document fragment contains an XHTML document fragment which in
        turn contains yet another SVG document fragment).
        
        Usually, a ``foreignObject`` will be used in conjunction with the ```<switch>``
        </en-US/docs/Web/SVG/Element/switch>`_ element and the ```requiredExtensions
        </en-US/docs/Web/SVG/Attribute/requiredExtensions>`_`` attribute to provide
        proper checking for user agent support and provide an alternate rendering in
        case user agent support is not available.
    """


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


class textPath(Component):
    """
        In addition to text drawn in a straight line, SVG also includes the ability to
        place text along the shape of a ```<path>`` </en-US/docs/Web/SVG/Element/path>`_
        element. To specify that a block of text is to be rendered along the shape of a
        ```<path>```_, include the given text within a **``<textPath>``** element which
        includes an ```href </en-US/docs/Web/SVG/Attribute/href>`_`` attribute with a
        reference to a ```<path>```_ element.
    """


class tspan(Component):
    """
        Within a ```<text>`` </en-US/docs/Web/SVG/Element/text>`_ element, text and font
        properties and the current text position can be adjusted with absolute or
        relative coordinate values by including a **``<tspan>``** element.
    """


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


class altGlyph(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<altGlyph>``** `SVG </en-US/docs/Web/SVG>`_ element allows sophisticated
        selection of the glyphs used to render its child character data.
    """


class altGlyphDef(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<altGlyphDef>``** `SVG </en-US/docs/Web/SVG>`_ element defines a
        substitution representation for glyphs.
    """


class altGlyphItem(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The **``<altGlyphItem>``** element provides a set of candidates for glyph
        substitution by the ```<altGlyph>`` </en-US/docs/Web/SVG/Element/altGlyph>`_
        element.
    """


class glyph(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        A **``<glyph>``** defines a single glyph in an SVG font.
    """


class glyphRef(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Do
        not use it in old or new projects. Pages or Web apps using it may break at any
        time.
        
        The ``glyphRef`` element provides a single possible glyph to the referencing
        ```<altGlyph>`` </en-US/docs/Web/SVG/Element/altGlyph>`_ substitution.
    """


# textPath: see above under 'Renderable elements'

# text: see above under 'Graphics elements'


class tref(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        The textual content for a ```<text>`` </en-US/docs/Web/SVG/Element/text>`_ `SVG
        </en-US/docs/Web/SVG>`_ element can be either character data directly embedded
        within the ```<text>```_ element or the character data content of a referenced
        element, where the referencing is specified with a **``<tref>``** element.
    """


# tspan: see above under 'Renderable elements'


# == Text content child elements ==

# altGlyph: see above under 'Text content elements'

# textPath: see above under 'Renderable elements'

# tref: see above under 'Text content elements'

# tspan: see above under 'Renderable elements'


# == Uncategorized elements ==

# clipPath: see above under 'Never-rendered elements'


class color_profile(Component):
    """
        The **``<color-profile>``** element allows describing the color profile used for
        the image.
    """

    tag_name = 'color-profile'


class cursor(Component):
    """
        **** Deprecated**\\This feature has been removed from the Web standards. Though
        some browsers may still support it, it is in the process of being dropped. Avoid
        using it and update existing code if possible; see the `compatibility table
        <#Browser_compatibility>`_ at the bottom of this page to guide your decision. Be
        aware that this feature may cease to work at any time.
        
        **Note:** The CSS ```cursor`` </en-US/docs/Web/CSS/cursor>`_ property should be
        used instead of this element.
        
        The **``<cursor>``** `SVG </en-US/docs/Web/SVG>`_ element can be used to define
        a platform-independent custom cursor. A recommended approach for defining a
        platform-independent custom cursor is to create a PNG image and define a
        ``cursor`` element that references the PNG image and identifies the exact
        position within the image which is the pointer position (i.e., the hot spot).
        
        The PNG format is recommended because it supports the ability to define a
        transparency mask via an alpha channel. If a different image format is used,
        this format should support the definition of a transparency mask (two options:
        provide an explicit alpha channel or use a particular pixel color to indicate
        transparency). If the transparency mask can be determined, the mask defines the
        shape of the cursor; otherwise, the cursor is an opaque rectangle. Typically,
        the other pixel information (e.g., the R, G and B channels) defines the colors
        for those parts of the cursor which are not masked out. Note that cursors
        usually contain at least two colors so that the cursor can be visible over most
        backgrounds.
    """


class filter_(Component):
    """
        The **``<filter>``** `SVG </en-US/docs/Web/SVG>`_ element serves as container
        for atomic filter operations. It is never rendered directly. A filter is
        referenced by using the ```filter </en-US/docs/Web/SVG/Attribute/filter>`_``
        attribute on the target SVG element or via the ```filter`` </en-
        US/docs/Web/CSS/filter>`_ `CSS </en-US/docs/Glossary/CSS>`_ property.
    """

    tag_name = 'filter'


# foreignObject: see above under 'Renderable elements'


class hatchpath(Component):
    """
        ** **This is an experimental technology**\\Because this technology's
        specification has not stabilized, check the `compatibility table
        <#Browser_compatibility>`_ for usage in various browsers. Also note that the
        syntax and behavior of an experimental technology is subject to change in future
        versions of browsers as the specification changes.
        
        The **``<hatchpath>``** `SVG </en-US/docs/Web/SVG>`_ element defines a hatch
        path used by the ```<hatch>`` </en-US/docs/Web/SVG/Element/hatch>`_ element.
    """


class meshpatch(Component):
    ''


class meshrow(Component):
    ''


# script: see above under 'Never-rendered elements'

# style: see above under 'Never-rendered elements'


class view(Component):
    'A view is a defined way to view the image, like a zoom level or a detail view.'


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

