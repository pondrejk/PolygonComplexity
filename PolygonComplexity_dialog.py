# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonComplexityDialog
                                 A QGIS plugin
 Calculating the complexity of polygons
                             -------------------
        begin                : 2015-01-23
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Peter Ondrejka
        email                : ondrejka@mail.muni.cz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtGui, uic
import qgis.core as qgis
from PolygonComplexity_dialog_base import Ui_PolygonComplexityDialogBase

import sys, os, imp
import fTools
path = os.path.dirname(fTools.__file__)
ftu = imp.load_source('ftools_utils', os.path.join(path,'tools','ftools_utils.py'))

#FORM_CLASS, _ = uic.loadUiType(os.path.join(
#    os.path.dirname(__file__), 'PolygonComplexity_dialog_base.ui'))


class PolygonComplexityDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(PolygonComplexityDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.ui = Ui_PolygonComplexityDialogBase()
        self.ui.setupUi(self)
        #self.ui.buttonBox.rejected.connect(self.reject)
        #self.ui.buttonBox.accepted.connect(self.accept)
        #self.ui.rdoBuffer.setChecked(True)
        #self.ui.btnBrowse.clicked.connect(self.browse)
        #self.ui.inputLayer.currentIndexChanged.connect(self.populateAttributes)

    def populateLayers( self ):
        myListA = []
        self.ui.inputLayer.clear()
        
        myListA = ftu.getLayerNames( [ qgis.QGis.Polygon ] )
        self.ui.inputLayer.addItems( myListA )


