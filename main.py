#!/usr/bin/env python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from views.mainwindowui import Ui_MainWindow



"""
sudo apt-get install python3-pyqt5
sudo pip3 install keyboard
sudo pip3 install psutil
sudo pip3 install flask
"""


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, app=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.menuPage.app = app
        for w in self.children():
            print(type(w).__name__)
        
    def closeEvent(self, event):
        print("close")


with open("stylesheet.css", "r") as file:
    styleStr = file.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(styleStr)
    win = Window(app=app)
    win.show()
    app.exec_()
