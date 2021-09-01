from views.menupage import Ui_Page
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore


class MenuPage(QWidget, Ui_Page):
    
    app = None
    
    def __init__(self, parent=None, tab=None, app=None):
        super(MenuPage, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget = tab
        self.myApp = app

    @QtCore.pyqtSlot()
    def usersPressed(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.usersPage))

    @QtCore.pyqtSlot()
    def settingPressed(self):
        self.tabWidget.setCurrentIndex(
            self.tabWidget.indexOf(self.tabWidget.settingPage)
        )

    @QtCore.pyqtSlot()
    def logsPressed(self):
        self.tabWidget.logsPage.currentUser = None
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.logsPage))

    @QtCore.pyqtSlot()
    def exitPressed(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.mainPage))

    @QtCore.pyqtSlot()
    def usbPressed(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.usbPage))

    def showEvent(self, event):
        self.setFocus()
    
    @QtCore.pyqtSlot()
    def closeAppPressed(self):
        if self.app != None:
            self.myApp.quit()
