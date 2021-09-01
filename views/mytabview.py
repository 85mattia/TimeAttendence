
from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5 import QtCore, QtGui, uic
from mainpage import MainPage
from menupage import MenuPage
from logspage import LogsPage
from userspage import UsersPage
from settingpage import SettingPage
from edituserpage import EditUserPage
from usbpage import UsbPage
from edittypepage import EditTypePage




class MyTabView(QTabWidget, QWidget):
	
	app = None
	
	def __init__(self, parent=None):
		super(MyTabView, self).__init__(parent)
		#self.setDocumentMode(True)
		self.setTabsClosable(True)
		self.mainPage = MainPage(tab=self)
		self.menuPage = MenuPage(tab=self)
		self.logsPage = LogsPage(tab=self)
		self.usersPage = UsersPage(tab=self)
		self.settingPage = SettingPage(tab=self)
		self.editUserPage = EditUserPage(tab=self)
		self.usbPage = UsbPage(tab=self)
		self.editType = EditTypePage(tab=self)
		self.addTab(self.mainPage, "home")
		self.addTab(self.menuPage, "menu")
		self.addTab(self.logsPage, "logs")
		self.addTab(self.usersPage, "users")
		self.addTab(self.settingPage, "setting")
		self.addTab(self.editUserPage, "edituser")
		self.addTab(self.usbPage, "usb")
		self.addTab(self.editType,"editType")
		#self.tabBar().setTabVisible(0, False)
		#for n in range(self.count()):
			#self.setTabEnabled(n, False)
	
		
