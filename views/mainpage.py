# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wifiLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiLabel.sizePolicy().hasHeightForWidth())
        self.wifiLabel.setSizePolicy(sizePolicy)
        self.wifiLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.wifiLabel.setObjectName("wifiLabel")
        self.horizontalLayout_2.addWidget(self.wifiLabel)
        self.labelInOut = QtWidgets.QLabel(Dialog)
        self.labelInOut.setStyleSheet("QLabel{\n"
"    \n"
"    font: 20pt \"Arial Black\";\n"
"}")
        self.labelInOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelInOut.setObjectName("labelInOut")
        self.horizontalLayout_2.addWidget(self.labelInOut)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.labelOrario = QtWidgets.QLabel(Dialog)
        self.labelOrario.setStyleSheet("QLabel{\n"
"    color:rgb(6, 75, 255);\n"
"    font: 60pt \"Arial\";\n"
"}")
        self.labelOrario.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOrario.setObjectName("labelOrario")
        self.verticalLayout.addWidget(self.labelOrario)
        self.labelMessage = QtWidgets.QLabel(Dialog)
        self.labelMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMessage.setObjectName("labelMessage")
        self.verticalLayout.addWidget(self.labelMessage)
        self.labelType = QtWidgets.QLabel(Dialog)
        self.labelType.setAlignment(QtCore.Qt.AlignCenter)
        self.labelType.setObjectName("labelType")
        self.verticalLayout.addWidget(self.labelType)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonIn = QtWidgets.QPushButton(Dialog)
        self.buttonIn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(100, 255, 100);\n"
"    min-height:70px;\n"
"font-size:25px;\n"
"}")
        self.buttonIn.setObjectName("buttonIn")
        self.horizontalLayout.addWidget(self.buttonIn)
        self.buttonMenu = QtWidgets.QPushButton(Dialog)
        self.buttonMenu.setObjectName("buttonMenu")
        self.horizontalLayout.addWidget(self.buttonMenu)
        self.buttonOut = QtWidgets.QPushButton(Dialog)
        self.buttonOut.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 73, 73);\n"
"min-height:70px;\n"
"font-size:25px;\n"
"}")
        self.buttonOut.setObjectName("buttonOut")
        self.horizontalLayout.addWidget(self.buttonOut)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonMenu.clicked.connect(Dialog.menuPressed)
        self.buttonIn.clicked.connect(Dialog.inPressed)
        self.buttonOut.clicked.connect(Dialog.outPressed)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.wifiLabel.setText(_translate("Dialog", "TextLabel"))
        self.labelInOut.setText(_translate("Dialog", "TextLabel"))
        self.labelOrario.setText(_translate("Dialog", "12:23:56"))
        self.labelMessage.setText(_translate("Dialog", "TextLabel"))
        self.labelType.setText(_translate("Dialog", "TextLabel"))
        self.buttonIn.setText(_translate("Dialog", "IN -->"))
        self.buttonMenu.setText(_translate("Dialog", "MENU"))
        self.buttonOut.setText(_translate("Dialog", "<-- OUT"))

