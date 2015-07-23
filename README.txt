Polygon Complexity

Plugin for QGIS 2.0 that calculates the complexity of polygon features. The complexity measure provides a quantitative description of the polygon shape. It can be used as an input for other geometric algorithms, or to find out if any algorithm depends on the geometric complexity of input polygons in terms of speed or quality of outputs.

The index of complexity used in this plugin is taken from the paper by Brinkhoff, Kriegel, Schneider, and Braun. The advantage of their approach is that it considers local variations of the polygon border. The plugin also calculates a simple compactness measure that relates the area of the polygon to the length of its border.
