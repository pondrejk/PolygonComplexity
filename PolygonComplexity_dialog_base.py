# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PolygonComplexity_dialog_base.ui'
#
# Created: Sun Mar  1 17:15:09 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PolygonComplexityDialogBase(object):
    def setupUi(self, PolygonComplexityDialogBase):
        PolygonComplexityDialogBase.setObjectName(_fromUtf8("PolygonComplexityDialogBase"))
        PolygonComplexityDialogBase.setEnabled(True)
        PolygonComplexityDialogBase.resize(400, 376)
        self.button_box = QtGui.QDialogButtonBox(PolygonComplexityDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 320, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.convCheckbox = QtGui.QCheckBox(PolygonComplexityDialogBase)
        self.convCheckbox.setEnabled(True)
        self.convCheckbox.setGeometry(QtCore.QRect(60, 180, 271, 26))
        self.convCheckbox.setObjectName(_fromUtf8("convCheckbox"))
        self.amplCheckbox = QtGui.QCheckBox(PolygonComplexityDialogBase)
        self.amplCheckbox.setEnabled(True)
        self.amplCheckbox.setGeometry(QtCore.QRect(60, 210, 241, 26))
        self.amplCheckbox.setObjectName(_fromUtf8("amplCheckbox"))
        self.freqCheckbox = QtGui.QCheckBox(PolygonComplexityDialogBase)
        self.freqCheckbox.setEnabled(True)
        self.freqCheckbox.setGeometry(QtCore.QRect(60, 240, 241, 26))
        self.freqCheckbox.setObjectName(_fromUtf8("freqCheckbox"))
        self.complCheckbox = QtGui.QCheckBox(PolygonComplexityDialogBase)
        self.complCheckbox.setEnabled(True)
        self.complCheckbox.setGeometry(QtCore.QRect(40, 120, 241, 26))
        self.complCheckbox.setAutoFillBackground(False)
        self.complCheckbox.setChecked(True)
        self.complCheckbox.setObjectName(_fromUtf8("complCheckbox"))
        self.label = QtGui.QLabel(PolygonComplexityDialogBase)
        self.label.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(PolygonComplexityDialogBase)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 221, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.inputLayer = QtGui.QComboBox(PolygonComplexityDialogBase)
        self.inputLayer.setGeometry(QtCore.QRect(40, 50, 281, 29))
        self.inputLayer.setObjectName(_fromUtf8("inputLayer"))
        self.cnessCheckbox = QtGui.QCheckBox(PolygonComplexityDialogBase)
        self.cnessCheckbox.setEnabled(True)
        self.cnessCheckbox.setGeometry(QtCore.QRect(40, 90, 241, 26))
        self.cnessCheckbox.setAutoFillBackground(False)
        self.cnessCheckbox.setChecked(True)
        self.cnessCheckbox.setObjectName(_fromUtf8("cnessCheckbox"))
        self.vertCheckbox = QtGui.QCheckBox(PolygonComplexityDialogBase)
        self.vertCheckbox.setEnabled(True)
        self.vertCheckbox.setGeometry(QtCore.QRect(60, 270, 241, 26))
        self.vertCheckbox.setObjectName(_fromUtf8("vertCheckbox"))

        self.retranslateUi(PolygonComplexityDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), PolygonComplexityDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), PolygonComplexityDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(PolygonComplexityDialogBase)

    def retranslateUi(self, PolygonComplexityDialogBase):
        PolygonComplexityDialogBase.setWindowTitle(_translate("PolygonComplexityDialogBase", "PolygonComplexity", None))
        self.convCheckbox.setText(_translate("PolygonComplexityDialogBase", "Deviation from the convex hull [CV]", None))
        self.amplCheckbox.setText(_translate("PolygonComplexityDialogBase", "Amplitude of the vibration [AP]", None))
        self.freqCheckbox.setText(_translate("PolygonComplexityDialogBase", "Frequency of the vibration [FQ]", None))
        self.complCheckbox.setText(_translate("PolygonComplexityDialogBase", "Calculate complexity [CP]", None))
        self.label.setText(_translate("PolygonComplexityDialogBase", "Select layer", None))
        self.label_2.setText(_translate("PolygonComplexityDialogBase", "Include intermediary parameters:", None))
        self.cnessCheckbox.setText(_translate("PolygonComplexityDialogBase", "Calculate compactness [CS]", None))
        self.vertCheckbox.setText(_translate("PolygonComplexityDialogBase", "Number of vertices [vert]", None))

