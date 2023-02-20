# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_output.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.backButton = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphics/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(30, 30))
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)

        self.forwardButton = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphics/forward.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.forwardButton.setIcon(icon)
        self.forwardButton.setIconSize(QtCore.QSize(30, 30))
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout.addWidget(self.forwardButton)

        self.refreshButton = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphics/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setIconSize(QtCore.QSize(30, 30))        
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)

        self.addressBar = QtWidgets.QLineEdit(Form)
        self.addressBar.setFixedHeight(40)
        self.addressBar.setObjectName("addressBar")
        self.horizontalLayout.addWidget(self.addressBar)

        self.searchBar = QtWidgets.QLineEdit(Form)
        self.searchBar.setFixedHeight(40)
        self.searchBar.setMaximumWidth(300)
        self.searchBar.setPlaceholderText("Search")
        self.searchBar.setObjectName("searchBar")
        self.horizontalLayout.addWidget(self.searchBar)

        self.searchSelection = QtWidgets.QComboBox(Form)
        self.searchSelection.setFixedHeight(40)
        self.searchSelection.setObjectName("searchSelection")
        self.searchSelection.addItem(QtGui.QIcon("Graphics/google.png"), "")
        self.searchSelection.addItem(QtGui.QIcon("Graphics/bing.png"), "")
        self.searchSelection.addItem(QtGui.QIcon("Graphics/yahoo.png"), "")
        self.searchSelection.addItem(QtGui.QIcon("Graphics/duckduckgo.png"), "")
        self.horizontalLayout.addWidget(self.searchSelection)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.webView = QtWebEngineWidgets.QWebEngineView(Form)
        self.webView.setObjectName("webView")

        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyQtWebBrowser"))
        self.backButton.setText(_translate("Form", "Back"))
        self.forwardButton.setText(_translate("Form", "Forward"))
        self.refreshButton.setText(_translate("Form", "Refresh"))

from PyQt6 import QtWebEngineWidgets
