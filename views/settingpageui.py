# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingpageui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page(object):
    def setupUi(self, Page):
        Page.setObjectName("Page")
        Page.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Page)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Page)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(Page)
        self.listView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Page)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(80, 255, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.fieldDeviceName = QtWidgets.QLineEdit(Page)
        self.fieldDeviceName.setObjectName("fieldDeviceName")
        self.horizontalLayout_3.addWidget(self.fieldDeviceName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Page)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(Page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Page)
        self.pushButton.clicked.connect(Page.exitPressed)
        self.pushButton_3.clicked.connect(Page.plusPressed)
        self.listView.clicked['QModelIndex'].connect(Page.selectionChanged)
        self.pushButton_4.clicked.connect(Page.noTypePressed)
        self.pushButton_2.clicked.connect(Page.savePressed)
        QtCore.QMetaObject.connectSlotsByName(Page)

    def retranslateUi(self, Page):
        _translate = QtCore.QCoreApplication.translate
        Page.setWindowTitle(_translate("Page", "Form"))
        self.label.setText(_translate("Page", "Types"))
        self.pushButton_3.setText(_translate("Page", "+"))
        self.pushButton_4.setText(_translate("Page", "Set No Type"))
        self.label_2.setText(_translate("Page", "Device Name:"))
        self.pushButton.setText(_translate("Page", "<--"))
        self.pushButton_2.setText(_translate("Page", "Save"))

