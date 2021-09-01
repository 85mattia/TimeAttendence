from views.userspageui import Ui_Page
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore
from datamanager import DataManager
import time

class UsersPage(QWidget, Ui_Page):

	dataManager = DataManager()
	data = []

	def __init__(self, parent=None, tab=None):
		super(UsersPage, self).__init__(parent)
		self.setupUi(self)
		self.tabWidget = tab
		
	def showEvent(self, event):
		self.createTable()
		
	
	def createTable(self):
	    self.tableWidget.selectionModel().clear()
	    self.tableWidget.setRowCount(len(self.data))
	    self.data = self.dataManager.getUsers()
	    self.tableWidget.setRowCount(len(self.data))
	    for r in range(len(self.data)):
	        for c in range(self.tableWidget.columnCount()):
	            header = self.tableWidget.horizontalHeaderItem(c).text()
	            if header == "ID":
	                self.tableWidget.setItem(r , c, QTableWidgetItem(self.data[r]["id"]))
	            elif header == "Name":
	                self.tableWidget.setItem(r , c, QTableWidgetItem(self.data[r]["name"]))
		
	@QtCore.pyqtSlot()
	def exitPressed(self):
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
		
	@QtCore.pyqtSlot()
	def newUserPressed(self):
	    self.tabWidget.editUserPage.userToEdit = None
	    self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.editUserPage))
	
	@QtCore.pyqtSlot()
	def selectionChanged(self):
	    if len(self.tableWidget.selectedIndexes()) == 0:
	        return
	    row = self.tableWidget.selectedIndexes()[0].row()
	    time.sleep(0.3)
	    self.tabWidget.editUserPage.userToEdit = self.data[row]
	    self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.editUserPage))
	    