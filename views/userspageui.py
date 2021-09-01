# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userspageui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page(object):
    def setupUi(self, Page):
        Page.setObjectName("Page")
        Page.resize(483, 433)
        self.gridLayout = QtWidgets.QGridLayout(Page)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Page)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Page)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonExit = QtWidgets.QPushButton(Page)
        self.buttonExit.setObjectName("buttonExit")
        self.horizontalLayout.addWidget(self.buttonExit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Page)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Page)
        self.buttonExit.clicked.connect(Page.exitPressed)
        self.pushButton.clicked.connect(Page.newUserPressed)
        self.tableWidget.itemSelectionChanged.connect(Page.selectionChanged)
        QtCore.QMetaObject.connectSlotsByName(Page)

    def retranslateUi(self, Page):
        _translate = QtCore.QCoreApplication.translate
        Page.setWindowTitle(_translate("Page", "Form"))
        self.label.setText(_translate("Page", "Users"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Page", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Page", "Name"))
        self.buttonExit.setText(_translate("Page", "< --"))
        self.pushButton.setText(_translate("Page", "New User"))

