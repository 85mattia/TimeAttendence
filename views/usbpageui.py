# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usbpageui.ui'
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBoxUsb = QtWidgets.QComboBox(Page)
        self.comboBoxUsb.setObjectName("comboBoxUsb")
        self.horizontalLayout.addWidget(self.comboBoxUsb)
        self.pushButton_4 = QtWidgets.QPushButton(Page)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(Page)
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(Page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(Page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(Page)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Page)
        self.pushButton_2.clicked.connect(Page.downloadNewPressed)
        self.pushButton.clicked.connect(Page.backPressed)
        self.comboBoxUsb.activated['int'].connect(Page.comboActivated)
        self.pushButton_3.clicked.connect(Page.downloadAllPressed)
        self.pushButton_4.clicked.connect(Page.scanPressed)
        QtCore.QMetaObject.connectSlotsByName(Page)

    def retranslateUi(self, Page):
        _translate = QtCore.QCoreApplication.translate
        Page.setWindowTitle(_translate("Page", "Form"))
        self.label.setText(_translate("Page", "Usb Download"))
        self.label_2.setText(_translate("Page", "Device :"))
        self.pushButton_4.setText(_translate("Page", "Scan"))
        self.pushButton_3.setText(_translate("Page", "Downlaod All Logs"))
        self.pushButton_2.setText(_translate("Page", "Downlaod New Logs"))
        self.pushButton.setText(_translate("Page", "<--"))

