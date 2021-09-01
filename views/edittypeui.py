# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edittypeui.ui'
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
        self.labelTitle = QtWidgets.QLabel(Page)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Page)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameField = QtWidgets.QLineEdit(Page)
        self.nameField.setObjectName("nameField")
        self.horizontalLayout.addWidget(self.nameField)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelMessage = QtWidgets.QLabel(Page)
        self.labelMessage.setStyleSheet("QLabel{\n"
"color:rgb(212, 0, 0);\n"
"}")
        self.labelMessage.setObjectName("labelMessage")
        self.verticalLayout.addWidget(self.labelMessage)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonMakeCurrent = QtWidgets.QPushButton(Page)
        self.buttonMakeCurrent.setStyleSheet("QPushButton{\n"
"    background-color:rgb(80, 255, 255);\n"
"}")
        self.buttonMakeCurrent.setObjectName("buttonMakeCurrent")
        self.horizontalLayout_3.addWidget(self.buttonMakeCurrent)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonRemove = QtWidgets.QPushButton(Page)
        self.buttonRemove.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 73, 73);\n"
"}")
        self.buttonRemove.setObjectName("buttonRemove")
        self.horizontalLayout_2.addWidget(self.buttonRemove)
        self.pushButton = QtWidgets.QPushButton(Page)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(100, 255, 100);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Page)
        self.pushButton_2.clicked.connect(Page.exitPressed)
        self.pushButton.clicked.connect(Page.savePressed)
        self.buttonMakeCurrent.clicked.connect(Page.makeCurrentPressed)
        self.buttonRemove.clicked.connect(Page.removePressed)
        QtCore.QMetaObject.connectSlotsByName(Page)

    def retranslateUi(self, Page):
        _translate = QtCore.QCoreApplication.translate
        Page.setWindowTitle(_translate("Page", "Form"))
        self.labelTitle.setText(_translate("Page", "TextLabel"))
        self.label.setText(_translate("Page", "Name :"))
        self.labelMessage.setText(_translate("Page", "TextLabel"))
        self.buttonMakeCurrent.setAccessibleName(_translate("Page", "blueBackground"))
        self.buttonMakeCurrent.setText(_translate("Page", "Make Current"))
        self.pushButton_2.setText(_translate("Page", "<--"))
        self.buttonRemove.setText(_translate("Page", "Remove"))
        self.pushButton.setText(_translate("Page", "Save"))

