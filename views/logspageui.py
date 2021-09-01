# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logspageui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page(object):
    def setupUi(self, Page):
        Page.setObjectName("Page")
        Page.resize(552, 366)
        self.gridLayout = QtWidgets.QGridLayout(Page)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(Page)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.tableWidget = QtWidgets.QTableWidget(Page)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonDeleteSelected = QtWidgets.QPushButton(Page)
        self.buttonDeleteSelected.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 73, 73);\n"
"}")
        self.buttonDeleteSelected.setObjectName("buttonDeleteSelected")
        self.verticalLayout.addWidget(self.buttonDeleteSelected)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonExit = QtWidgets.QPushButton(Page)
        self.buttonExit.setObjectName("buttonExit")
        self.horizontalLayout.addWidget(self.buttonExit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Page)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 73, 73);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.buttonDeleteAll = QtWidgets.QPushButton(Page)
        self.buttonDeleteAll.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 73, 73);\n"
"}")
        self.buttonDeleteAll.setObjectName("buttonDeleteAll")
        self.horizontalLayout.addWidget(self.buttonDeleteAll)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Page)
        self.buttonExit.clicked.connect(Page.exitPressed)
        self.buttonDeleteSelected.clicked.connect(Page.deletePressed)
        self.buttonDeleteAll.clicked.connect(Page.deleteAllLogsPressed)
        self.tableWidget.itemSelectionChanged.connect(Page.selectedChanged)
        self.pushButton.clicked.connect(Page.deleteDownloadedPressed)
        QtCore.QMetaObject.connectSlotsByName(Page)

    def retranslateUi(self, Page):
        _translate = QtCore.QCoreApplication.translate
        Page.setWindowTitle(_translate("Page", "Form"))
        self.labelTitle.setText(_translate("Page", "Logs"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Page", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Page", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Page", "Stat"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Page", "Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Page", "Type"))
        self.buttonDeleteSelected.setText(_translate("Page", "Delete Selected"))
        self.buttonExit.setText(_translate("Page", "< --"))
        self.pushButton.setText(_translate("Page", "Delete Downloaded Logs"))
        self.buttonDeleteAll.setText(_translate("Page", "Delete All Logs"))

