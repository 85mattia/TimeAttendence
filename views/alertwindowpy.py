# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/TimeAttendence2/views/alertwindowui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlertWindow(object):
    def setupUi(self, AlertWindow):
        AlertWindow.setObjectName("AlertWindow")
        AlertWindow.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(AlertWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AlertWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCancel = QtWidgets.QPushButton(AlertWindow)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.buttonOk = QtWidgets.QPushButton(AlertWindow)
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout.addWidget(self.buttonOk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AlertWindow)
        self.buttonCancel.clicked.connect(AlertWindow.cancelPressed)
        self.buttonOk.clicked.connect(AlertWindow.okPressed)
        QtCore.QMetaObject.connectSlotsByName(AlertWindow)

    def retranslateUi(self, AlertWindow):
        _translate = QtCore.QCoreApplication.translate
        AlertWindow.setWindowTitle(_translate("AlertWindow", "Alert"))
        self.label.setText(_translate("AlertWindow", "TextLabel"))
        self.buttonCancel.setText(_translate("AlertWindow", "Cancel"))
        self.buttonOk.setText(_translate("AlertWindow", "Ok"))

