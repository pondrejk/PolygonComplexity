# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonComplexity
                                 A QGIS plugin
 Calculating the complexity of polygons
                             -------------------
        begin                : 2015-01-23
        copyright            : (C) 2015 by Peter Ondrejka
        email                : ondrejka@mail.muni.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PolygonComplexity class from file PolygonComplexity.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PolygonComplexity import PolygonComplexity
    return PolygonComplexity(iface)
