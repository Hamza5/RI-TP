# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocumentPropertiesDialog.ui'
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

class Ui_DocumentDialog(object):
    def setupUi(self, DocumentDialog):
        DocumentDialog.setObjectName(_fromUtf8("DocumentDialog"))
        DocumentDialog.resize(733, 332)
        self.formLayout = QtGui.QFormLayout(DocumentDialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.documentNumberLabel = QtGui.QLabel(DocumentDialog)
        self.documentNumberLabel.setObjectName(_fromUtf8("documentNumberLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.documentNumberLabel)
        self.documentNumberLineEdit = QtGui.QLineEdit(DocumentDialog)
        self.documentNumberLineEdit.setReadOnly(True)
        self.documentNumberLineEdit.setObjectName(_fromUtf8("documentNumberLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.documentNumberLineEdit)
        self.documentTitleLabel = QtGui.QLabel(DocumentDialog)
        self.documentTitleLabel.setObjectName(_fromUtf8("documentTitleLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.documentTitleLabel)
        self.documentTitleLineEdit = QtGui.QLineEdit(DocumentDialog)
        self.documentTitleLineEdit.setReadOnly(True)
        self.documentTitleLineEdit.setObjectName(_fromUtf8("documentTitleLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.documentTitleLineEdit)
        self.documentSummaryLabel = QtGui.QLabel(DocumentDialog)
        self.documentSummaryLabel.setObjectName(_fromUtf8("documentSummaryLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.documentSummaryLabel)
        self.documentSummaryPlainTextEdit = QtGui.QPlainTextEdit(DocumentDialog)
        self.documentSummaryPlainTextEdit.setReadOnly(True)
        self.documentSummaryPlainTextEdit.setObjectName(_fromUtf8("documentSummaryPlainTextEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.documentSummaryPlainTextEdit)
        self.closeButtonBox = QtGui.QDialogButtonBox(DocumentDialog)
        self.closeButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.closeButtonBox.setObjectName(_fromUtf8("closeButtonBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.closeButtonBox)

        self.retranslateUi(DocumentDialog)
        QtCore.QObject.connect(self.closeButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DocumentDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DocumentDialog)

    def retranslateUi(self, DocumentDialog):
        DocumentDialog.setWindowTitle(_translate("DocumentDialog", "Propriétés du document - Recherche d\'informations", None))
        self.documentNumberLabel.setText(_translate("DocumentDialog", "N°", None))
        self.documentTitleLabel.setText(_translate("DocumentDialog", "Titre", None))
        self.documentSummaryLabel.setText(_translate("DocumentDialog", "Résumé", None))

