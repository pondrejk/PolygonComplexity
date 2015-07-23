# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonComplexity
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QVariant 
from PyQt4.QtGui import QAction, QIcon, QMessageBox
from qgis.core import QgsField, QgsFeature, QGis
from math import sqrt, acos, pi
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from PolygonComplexity_dialog import PolygonComplexityDialog
import os.path
import imp
import fTools
path = os.path.dirname(fTools.__file__)
ftu = imp.load_source('ftools_utils', os.path.join(path,'tools','ftools_utils.py'))



class PolygonComplexity:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'PolygonComplexity_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = PolygonComplexityDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&PolygonComplexity')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'PolygonComplexity')
        self.toolbar.setObjectName(u'PolygonComplexity')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('PolygonComplexity', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/PolygonComplexity/logo.png'
        self.add_action(
            icon_path,
            text=self.tr(u'PolygonComplexity'),
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&PolygonComplexity'),
                action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        """Run method that performs all the real work"""
        # Populate the combo boxes
        self.dlg.populateLayers()
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed

        if result == 1:
            if not self.dlg.ui.inputLayer.currentText():
                QMessageBox.information( self.iface.mainWindow(),"Info", "Please select a polygon layer")
            else:
                layer = ftu.getMapLayerByName(self.dlg.ui.inputLayer.currentText())
                nFeatures = layer.featureCount()
                pr = layer.dataProvider()
                layer.startEditing()

                if self.dlg.ui.cnessCheckbox.isChecked() and layer.fieldNameIndex("CS") == -1 :
                    pr.addAttributes( [ QgsField("CS", QVariant.Double)] )
                    layer.commitChanges()

                if self.dlg.ui.complCheckbox.isChecked() and layer.fieldNameIndex("CP") == -1 :
                    pr.addAttributes( [ QgsField("CP", QVariant.Double)] )
                    layer.commitChanges()

                if self.dlg.ui.convCheckbox.isChecked() and layer.fieldNameIndex("CV") == -1 :
                    pr.addAttributes( [ QgsField("CV", QVariant.Double)] )
                    layer.commitChanges()

                if self.dlg.ui.amplCheckbox.isChecked() and layer.fieldNameIndex("AP") == -1 :
                    pr.addAttributes( [ QgsField("AP", QVariant.Double)] )
                    layer.commitChanges()

                if self.dlg.ui.freqCheckbox.isChecked() and layer.fieldNameIndex("FQ") == -1 :
                    pr.addAttributes( [ QgsField("FQ", QVariant.Double)] )
                    layer.commitChanges()

                if self.dlg.ui.vertCheckbox.isChecked() and layer.fieldNameIndex("vert") == -1 :
                    pr.addAttributes( [ QgsField("vert", QVariant.Int)] )
                    layer.commitChanges()

                # Loop over the features
                for i, feature in enumerate(layer.dataProvider().getFeatures()):
                    self.iface.mainWindow().statusBar().showMessage(
                        "Processing feature {} of {}".format(i + 1, nFeatures))

                    geom = feature.geometry()
                    feature_compactness = find_feature_compactness(geom)
                    feature_convexity = find_feature_convexity(geom)
                    feature_amplitude = find_feature_amplitude(geom)
                    feature_vertices = find_feature_vertices(geom)
                    feature_notches = find_feature_notches(geom, self)
                    feature_notches_normalized = float(feature_notches) / (feature_vertices - 3)
                    feature_frequency = (16*((feature_notches_normalized - 0.5)**4)) - (8*(feature_notches_normalized - 0.5)**2) + 1
                    feature_complexity = find_feature_complexity(feature_convexity, feature_amplitude, feature_frequency)

                    if self.dlg.ui.cnessCheckbox.isChecked():
                        layer.startEditing()
                        feature['CS'] = feature_compactness
                        layer.updateFeature(feature)

                    if self.dlg.ui.complCheckbox.isChecked():
                        layer.startEditing()
                        feature['CP'] = feature_complexity
                        layer.updateFeature(feature)

                    if self.dlg.ui.convCheckbox.isChecked():
                        layer.startEditing()
                        feature['CV'] = feature_convexity
                        layer.updateFeature(feature)

                    if self.dlg.ui.amplCheckbox.isChecked():
                        layer.startEditing()
                        feature['AP'] = feature_amplitude
                        layer.updateFeature(feature)

                    if self.dlg.ui.freqCheckbox.isChecked():
                        layer.startEditing()
                        feature['FQ'] = feature_frequency
                        layer.updateFeature(feature)

                    if self.dlg.ui.vertCheckbox.isChecked():
                        layer.startEditing()
                        feature['vert'] = feature_vertices - 1
                        layer.updateFeature(feature)

                layer.commitChanges()

def find_feature_compactness(geom):
    return (geom.length()/(3.54 * sqrt(geom.area()))) # 1 for a circle

def find_feature_convexity(geom):
    hull_area = 0
    geom_area = 0
    if geom.isMultipart():
      new_features = []
      temp_feature = QgsFeature()
      for part in geom.asGeometryCollection():
        temp_feature.setGeometry(part)
        new_features.append(QgsFeature(temp_feature))
      for subfeature in new_features:
          hull_area += subfeature.geometry().convexHull().area()
          geom_area += subfeature.geometry().area()
      return (hull_area - geom_area)/hull_area
    else:
      hull_area = geom.convexHull().area()
      return (hull_area - geom.area())/hull_area

def find_feature_amplitude(geom):
    hull_length = 0
    geom_length = 0
    if geom.isMultipart():
      new_features = []
      temp_feature = QgsFeature()
      for part in geom.asGeometryCollection():
        temp_feature.setGeometry(part)
        new_features.append(QgsFeature(temp_feature))
      for subfeature in new_features:
          hull_length += subfeature.geometry().convexHull().length()
          geom_length += subfeature.geometry().length()
      return (geom_length - hull_length)/geom_length
    else:
      hull_length =  geom.convexHull().length()
      geom_length =  geom.length()
      return (geom_length - hull_length)/geom_length

def find_feature_notches(geom, self):
    if geom is None: return None
    if geom.type() == QGis.Polygon:
        notches = 0
        if geom.isMultipart():
          polygons = geom.asMultiPolygon()
        else:
          polygons = [ geom.asPolygon() ]
        for polygon in polygons:
          for ring in polygon:
            triplet = []
            ring.append(ring[1])
            for i in ring:
                triplet.append(i) 
                if len(triplet) > 3:
                    del triplet[0]
                if len(triplet) == 3:
                    zcp = find_convex(triplet)
                    if zcp > 0: 
                        notches +=1

    return notches

def find_feature_vertices(geom):
    if geom is None: return None
    if geom.type() == QGis.Polygon:
        count = 0
        if geom.isMultipart():
          polygons = geom.asMultiPolygon()
        else:
          polygons = [ geom.asPolygon() ]
        for polygon in polygons:
          for ring in polygon:
            count += len(ring)
    count = count - 1.0
    return count

def find_feature_complexity(conv, ampl, freq):
    return ((0.8 * ampl * freq) + (0.2 * conv))

def find_convex(triplet):
    a1,a2,a3 = triplet[0], triplet[1], triplet[2]
    dx1 = a2[0] - a1[0]
    dy1 = a2[1] - a1[1]
    dx2 = a3[0] - a2[0]
    dy2 = a3[1] - a2[1]
    zcrossproduct = dx1*dy2 - dy1*dx2
    return zcrossproduct
