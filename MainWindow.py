# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(726, 639)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mainTabs = QtGui.QTabWidget(self.centralwidget)
        self.mainTabs.setObjectName(_fromUtf8("mainTabs"))
        self.searchTab = QtGui.QWidget()
        self.searchTab.setObjectName(_fromUtf8("searchTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.searchTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.modelGroupBox = QtGui.QGroupBox(self.searchTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelGroupBox.sizePolicy().hasHeightForWidth())
        self.modelGroupBox.setSizePolicy(sizePolicy)
        self.modelGroupBox.setObjectName(_fromUtf8("modelGroupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.modelGroupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.modelGroupBox)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.vectorTab = QtGui.QWidget()
        self.vectorTab.setObjectName(_fromUtf8("vectorTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.vectorTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.vectorSearchLayout = QtGui.QHBoxLayout()
        self.vectorSearchLayout.setObjectName(_fromUtf8("vectorSearchLayout"))
        self.vectorSearchLineEdit = QtGui.QLineEdit(self.vectorTab)
        self.vectorSearchLineEdit.setObjectName(_fromUtf8("vectorSearchLineEdit"))
        self.vectorSearchLayout.addWidget(self.vectorSearchLineEdit)
        self.vectorSearchPushButton = QtGui.QPushButton(self.vectorTab)
        self.vectorSearchPushButton.setObjectName(_fromUtf8("vectorSearchPushButton"))
        self.vectorSearchLayout.addWidget(self.vectorSearchPushButton)
        self.verticalLayout_3.addLayout(self.vectorSearchLayout)
        self.vectorSimilarityGroupBox = QtGui.QGroupBox(self.vectorTab)
        self.vectorSimilarityGroupBox.setObjectName(_fromUtf8("vectorSimilarityGroupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.vectorSimilarityGroupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.innerProductRadioButton = QtGui.QRadioButton(self.vectorSimilarityGroupBox)
        self.innerProductRadioButton.setChecked(True)
        self.innerProductRadioButton.setObjectName(_fromUtf8("innerProductRadioButton"))
        self.horizontalLayout_2.addWidget(self.innerProductRadioButton)
        self.diceRadioButton = QtGui.QRadioButton(self.vectorSimilarityGroupBox)
        self.diceRadioButton.setObjectName(_fromUtf8("diceRadioButton"))
        self.horizontalLayout_2.addWidget(self.diceRadioButton)
        self.cosRadioButton = QtGui.QRadioButton(self.vectorSimilarityGroupBox)
        self.cosRadioButton.setObjectName(_fromUtf8("cosRadioButton"))
        self.horizontalLayout_2.addWidget(self.cosRadioButton)
        self.jaccardRadioButton = QtGui.QRadioButton(self.vectorSimilarityGroupBox)
        self.jaccardRadioButton.setObjectName(_fromUtf8("jaccardRadioButton"))
        self.horizontalLayout_2.addWidget(self.jaccardRadioButton)
        self.verticalLayout_3.addWidget(self.vectorSimilarityGroupBox)
        self.tabWidget.addTab(self.vectorTab, _fromUtf8(""))
        self.booleanTab = QtGui.QWidget()
        self.booleanTab.setObjectName(_fromUtf8("booleanTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.booleanTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.booleanSearchLayout = QtGui.QHBoxLayout()
        self.booleanSearchLayout.setObjectName(_fromUtf8("booleanSearchLayout"))
        self.booleanSearchLineEdit = QtGui.QLineEdit(self.booleanTab)
        self.booleanSearchLineEdit.setObjectName(_fromUtf8("booleanSearchLineEdit"))
        self.booleanSearchLayout.addWidget(self.booleanSearchLineEdit)
        self.booleanSearchPushButton = QtGui.QPushButton(self.booleanTab)
        self.booleanSearchPushButton.setObjectName(_fromUtf8("booleanSearchPushButton"))
        self.booleanSearchLayout.addWidget(self.booleanSearchPushButton)
        self.verticalLayout_4.addLayout(self.booleanSearchLayout)
        self.booleanNoteLabel = QtGui.QLabel(self.booleanTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.booleanNoteLabel.sizePolicy().hasHeightForWidth())
        self.booleanNoteLabel.setSizePolicy(sizePolicy)
        self.booleanNoteLabel.setObjectName(_fromUtf8("booleanNoteLabel"))
        self.verticalLayout_4.addWidget(self.booleanNoteLabel)
        self.tabWidget.addTab(self.booleanTab, _fromUtf8(""))
        self.matchingScoreTab = QtGui.QWidget()
        self.matchingScoreTab.setObjectName(_fromUtf8("matchingScoreTab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.matchingScoreTab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.matchingScoreSearchLayout = QtGui.QHBoxLayout()
        self.matchingScoreSearchLayout.setObjectName(_fromUtf8("matchingScoreSearchLayout"))
        self.matchingScoreSearchLineEdit = QtGui.QLineEdit(self.matchingScoreTab)
        self.matchingScoreSearchLineEdit.setObjectName(_fromUtf8("matchingScoreSearchLineEdit"))
        self.matchingScoreSearchLayout.addWidget(self.matchingScoreSearchLineEdit)
        self.matchingScoreSearchPushButton = QtGui.QPushButton(self.matchingScoreTab)
        self.matchingScoreSearchPushButton.setObjectName(_fromUtf8("matchingScoreSearchPushButton"))
        self.matchingScoreSearchLayout.addWidget(self.matchingScoreSearchPushButton)
        self.verticalLayout_5.addLayout(self.matchingScoreSearchLayout)
        self.tabWidget.addTab(self.matchingScoreTab, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.modelGroupBox)
        self.ResultsGroupBox = QtGui.QGroupBox(self.searchTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultsGroupBox.sizePolicy().hasHeightForWidth())
        self.ResultsGroupBox.setSizePolicy(sizePolicy)
        self.ResultsGroupBox.setObjectName(_fromUtf8("ResultsGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.ResultsGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.resultsTableWidget = QtGui.QTableWidget(self.ResultsGroupBox)
        self.resultsTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultsTableWidget.setObjectName(_fromUtf8("resultsTableWidget"))
        self.resultsTableWidget.setColumnCount(2)
        self.resultsTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.resultsTableWidget)
        self.clearResultsPushButton = QtGui.QPushButton(self.ResultsGroupBox)
        self.clearResultsPushButton.setObjectName(_fromUtf8("clearResultsPushButton"))
        self.verticalLayout_2.addWidget(self.clearResultsPushButton)
        self.verticalLayout.addWidget(self.ResultsGroupBox)
        self.mainTabs.addTab(self.searchTab, _fromUtf8(""))
        self.extraTab = QtGui.QWidget()
        self.extraTab.setObjectName(_fromUtf8("extraTab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.extraTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.loadInverseFileGroupBox = QtGui.QGroupBox(self.extraTab)
        self.loadInverseFileGroupBox.setObjectName(_fromUtf8("loadInverseFileGroupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.loadInverseFileGroupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.loadInverseFileLineEdit = QtGui.QLineEdit(self.loadInverseFileGroupBox)
        self.loadInverseFileLineEdit.setObjectName(_fromUtf8("loadInverseFileLineEdit"))
        self.horizontalLayout_4.addWidget(self.loadInverseFileLineEdit)
        self.loadInveseFilePushButton = QtGui.QPushButton(self.loadInverseFileGroupBox)
        self.loadInveseFilePushButton.setObjectName(_fromUtf8("loadInveseFilePushButton"))
        self.horizontalLayout_4.addWidget(self.loadInveseFilePushButton)
        self.verticalLayout_6.addWidget(self.loadInverseFileGroupBox)
        self.saveInverseFileGroupBox = QtGui.QGroupBox(self.extraTab)
        self.saveInverseFileGroupBox.setEnabled(False)
        self.saveInverseFileGroupBox.setObjectName(_fromUtf8("saveInverseFileGroupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.saveInverseFileGroupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.saveInverseFileFieldLayout = QtGui.QHBoxLayout()
        self.saveInverseFileFieldLayout.setObjectName(_fromUtf8("saveInverseFileFieldLayout"))
        self.saveInverseFileLineEdit = QtGui.QLineEdit(self.saveInverseFileGroupBox)
        self.saveInverseFileLineEdit.setObjectName(_fromUtf8("saveInverseFileLineEdit"))
        self.saveInverseFileFieldLayout.addWidget(self.saveInverseFileLineEdit)
        self.saveInveseFilePushButton = QtGui.QPushButton(self.saveInverseFileGroupBox)
        self.saveInveseFilePushButton.setObjectName(_fromUtf8("saveInveseFilePushButton"))
        self.saveInverseFileFieldLayout.addWidget(self.saveInveseFilePushButton)
        self.saveInverseFileGeneratePushButton = QtGui.QPushButton(self.saveInverseFileGroupBox)
        self.saveInverseFileGeneratePushButton.setObjectName(_fromUtf8("saveInverseFileGeneratePushButton"))
        self.saveInverseFileFieldLayout.addWidget(self.saveInverseFileGeneratePushButton)
        self.verticalLayout_7.addLayout(self.saveInverseFileFieldLayout)
        self.saveInvefrseFileChoiceLayout = QtGui.QHBoxLayout()
        self.saveInvefrseFileChoiceLayout.setObjectName(_fromUtf8("saveInvefrseFileChoiceLayout"))
        self.saveInverseFileTfIdfRadioButton = QtGui.QRadioButton(self.saveInverseFileGroupBox)
        self.saveInverseFileTfIdfRadioButton.setChecked(True)
        self.saveInverseFileTfIdfRadioButton.setObjectName(_fromUtf8("saveInverseFileTfIdfRadioButton"))
        self.saveInvefrseFileChoiceLayout.addWidget(self.saveInverseFileTfIdfRadioButton)
        self.saveInverseFileFrequencyRadioButton = QtGui.QRadioButton(self.saveInverseFileGroupBox)
        self.saveInverseFileFrequencyRadioButton.setObjectName(_fromUtf8("saveInverseFileFrequencyRadioButton"))
        self.saveInvefrseFileChoiceLayout.addWidget(self.saveInverseFileFrequencyRadioButton)
        self.verticalLayout_7.addLayout(self.saveInvefrseFileChoiceLayout)
        self.verticalLayout_6.addWidget(self.saveInverseFileGroupBox)
        self.mainTabs.addTab(self.extraTab, _fromUtf8(""))
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.mainTabs.addTab(self.settingsTab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.mainTabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 37))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Projet de recherche d\'informations", None))
        self.modelGroupBox.setTitle(_translate("MainWindow", "Modèle", None))
        self.vectorSearchLineEdit.setPlaceholderText(_translate("MainWindow", "Votre requête", None))
        self.vectorSearchPushButton.setText(_translate("MainWindow", "Rechercher", None))
        self.vectorSimilarityGroupBox.setTitle(_translate("MainWindow", "Fonction de similarité", None))
        self.innerProductRadioButton.setText(_translate("MainWindow", "Produit interne", None))
        self.diceRadioButton.setText(_translate("MainWindow", "Dice", None))
        self.cosRadioButton.setText(_translate("MainWindow", "Cosinus", None))
        self.jaccardRadioButton.setText(_translate("MainWindow", "Jaccard", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vectorTab), _translate("MainWindow", "Vectoriel", None))
        self.booleanSearchLineEdit.setPlaceholderText(_translate("MainWindow", "Votre requête", None))
        self.booleanSearchPushButton.setText(_translate("MainWindow", "Rechercher", None))
        self.booleanNoteLabel.setText(_translate("MainWindow", "<html><head/><body><p>Les opérateurs booléen : &amp; (et), | (ou), ~ (non).</p><p>Les parenthèses peuvent être utilisées pour indiquer la priorité.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booleanTab), _translate("MainWindow", "Booléen", None))
        self.matchingScoreSearchLineEdit.setPlaceholderText(_translate("MainWindow", "Votre requête", None))
        self.matchingScoreSearchPushButton.setText(_translate("MainWindow", "Rechercher", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.matchingScoreTab), _translate("MainWindow", "Matching score", None))
        self.ResultsGroupBox.setTitle(_translate("MainWindow", "Résultats", None))
        item = self.resultsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Document", None))
        item = self.resultsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Score", None))
        self.clearResultsPushButton.setText(_translate("MainWindow", "Effacer", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.searchTab), _translate("MainWindow", "Recherche", None))
        self.loadInverseFileGroupBox.setTitle(_translate("MainWindow", "Charger un fichier inverse", None))
        self.loadInverseFileLineEdit.setPlaceholderText(_translate("MainWindow", "Chemin du fichier", None))
        self.loadInveseFilePushButton.setText(_translate("MainWindow", "Sélectionner", None))
        self.saveInverseFileGroupBox.setTitle(_translate("MainWindow", "Sauvegarder un fichier inverse", None))
        self.saveInverseFileLineEdit.setPlaceholderText(_translate("MainWindow", "Chemin du fichier", None))
        self.saveInveseFilePushButton.setText(_translate("MainWindow", "Sélectionner", None))
        self.saveInverseFileGeneratePushButton.setText(_translate("MainWindow", "Générer", None))
        self.saveInverseFileTfIdfRadioButton.setText(_translate("MainWindow", "Tf-Idf", None))
        self.saveInverseFileFrequencyRadioButton.setText(_translate("MainWindow", "Fréquence", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.extraTab), _translate("MainWindow", "Fichier inverse", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.settingsTab), _translate("MainWindow", "Paramètres", None))

