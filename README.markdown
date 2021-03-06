Polygon Complexity
==================

Plugin for QGIS 2.0 that calculates the complexity of polygon features. The complexity measure provides a quantitative description of the polygon shape. It can be used as an input for other geometric algorithms, or to find out if any algorithm depends on the geometric complexity of input polygons in terms of speed or quality of outputs.

The index of complexity used in this plugin is taken from the [paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.73.1045&rep=rep1&type=pdf) by Brinkhoff, Kriegel, Schneider, and Braun [1]. The advantage of their approach is that it considers local variations of the polygon border. The plugin also calculates a simple compactness measure that relates the area of the polygon to the length of its border.

![](images/polygon_complexity.png "Countries categorized by the complexity index")

*Fig. 1* Countries categorized by the complexity index.

![](images/polygon_compactness.png "Countries categorized by the compactness index")

*Fig. 2* Countries categorized by the compactness index


Using the plugin
----------------
The following options are available in the plugin's dialog window:

*Calculate compactness* (CS): calculates the compactness of the polygon is defined as:

> polgon_boundary / (3.45 \* sqrt(polygon_area))

*Calculate complexity* (CP): calculates the complexity index as defined [1] as: 

> 0.8 \* AP \* FQ \* (0.2 \* CV)

You can also include the following intermediary parameters to the attribute table: 

* *Deviation from the covex hull* (CV) is a normalized difference between the area of the polygon and the area of its convex hull:

> (hull_area - polygon_area) / hull_area

* *Amplitude of the vibration* (AP) is a normalized difference between the length of the polygon boundary and the length of the boundary of its convex hull:

> (poygon_boundary - hull_boundary) / poygon_boundary

* *Frequency of the vibration* (FQ) depicts local variability of the polygons boundary.

> 16 \* (notches_norm - 0.5)<sup>4</sup> - 8 \* (notches_norm - 0.5)<sup>2</sup> - 1

* *Number of vertices* (vert)

![](images/shapes_comparison.png "Complexity measure for different shapes")

*Fig. 3* Complexity measures for different shapes


Notes
-------

The area and boundary length of the convex hull for multipart polygons is calculated as the sum of convex hulls of polygon parts, to avoid distortions given by remoteness of subparts (archipelagos, USA with Alaska and Hawaii, etc.).

The number of vertices for polygons in the shp data model is actually higher by 1 than what is returned by the plugin, as the closing vertex of the boundary is the same as the first vertex.

References
-----------

[1]: Brinkhoff, T., Kriegel, H. P., Schneider, R., & Braun, A. (1995, December). Measuring the Complexity of Polygonal Objects. In ACM-GIS (p. 109). <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.73.1045&rep=rep1&type=pdf> 

Next steps
------------

There are several other polygon complexity measures that could be implemented to extend this plugin, including:

* fractal dimension, fractal dimension estimated with the *box-counting tecnique* (as in Rützel H.: ‘Describing the Complexity of Geometric Objects by Using the Fractal Dimension’ (in German), University of Munich, 1995)
* shape index by [Boyce & Clark 1964](http://www.jstor.org/stable/212982?seq=2#page_scan_tab_contents)
* vertex-lag method by Bunge (Bunge, W., 1962. Theoretical Geography. First Edition. Lund Studies in Geography Series C: General and Mathematical Geography. Lund, Sweden: Gleerup.)
* indexes mentioned in [Moser et al. 2002](http://link.springer.com/article/10.1023/A:1021513729205) (double log fractal dimension, number of shape characteristic points)
* shape variation from [Ferson et al. 1985](http://www.jstor.org/stable/2413345?seq=1#page_scan_tab_contents)
* method by [Lee & Sallee 1970](http://www.jstor.org/stable/213774?seq=8#page_scan_tab_contents)
* maybe also the Fourier-based method from [Ehrlich & Weinberg 1970](http://archives.datapages.com/data/sepm/journals/v38-41/data/040/040001/0205.htm)
