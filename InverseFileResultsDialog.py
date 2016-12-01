# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InverseFileResultsDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_InverseFileResultsDialog(object):
    def setupUi(self, InverseFileResultsDialog):
        InverseFileResultsDialog.setObjectName(_fromUtf8("InverseFileResultsDialog"))
        InverseFileResultsDialog.resize(618, 300)
        self.verticalLayout = QtGui.QVBoxLayout(InverseFileResultsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.inverseFileResultsTableWidget = QtGui.QTableWidget(InverseFileResultsDialog)
        self.inverseFileResultsTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.inverseFileResultsTableWidget.setObjectName(_fromUtf8("inverseFileResultsTableWidget"))
        self.inverseFileResultsTableWidget.setColumnCount(2)
        self.inverseFileResultsTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.inverseFileResultsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.inverseFileResultsTableWidget.setHorizontalHeaderItem(1, item)
        self.inverseFileResultsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.inverseFileResultsTableWidget)
        self.inverseFileResultsButtonBox = QtGui.QDialogButtonBox(InverseFileResultsDialog)
        self.inverseFileResultsButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.inverseFileResultsButtonBox.setObjectName(_fromUtf8("inverseFileResultsButtonBox"))
        self.verticalLayout.addWidget(self.inverseFileResultsButtonBox)

        self.retranslateUi(InverseFileResultsDialog)
        QtCore.QObject.connect(self.inverseFileResultsButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), InverseFileResultsDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(InverseFileResultsDialog)

    def retranslateUi(self, InverseFileResultsDialog):
        InverseFileResultsDialog.setWindowTitle(_translate("InverseFileResultsDialog", "Recherche d\'informations - Résultats", None))
        self.inverseFileResultsTableWidget.setSortingEnabled(True)
        item = self.inverseFileResultsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InverseFileResultsDialog", "Objet", None))
        item = self.inverseFileResultsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InverseFileResultsDialog", "Poids", None))

