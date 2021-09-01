from views.settingpageui import Ui_Page
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui
from datamanager import DataManager


class SettingPage(QWidget, Ui_Page):
	
	typeModel = QtGui.QStandardItemModel()
	dataManager = DataManager()

	def __init__(self, parent=None, tab=None):
		super(SettingPage, self).__init__(parent)
		self.setupUi(self)
		self.tabWidget = tab
		
	def showEvent(self, event):
		self.updateTypeTable()
		self.fieldDeviceName.setText(self.dataManager.getDeviceName())
		
	def updateTypeTable(self):
		self.allTypes = self.dataManager.getAllData()["types"]
		self.listView.setModel(self.typeModel)
		self.typeModel.clear()
		for t in self.allTypes:
			self.typeModel.appendRow(QtGui.QStandardItem(t["name"]))
	
	@QtCore.pyqtSlot()
	def savePressed(self):
		if self.fieldDeviceName.text() == "":
			return
		if self.fieldDeviceName.text() == self.dataManager.getDeviceName():
			self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
		else:
			self.dataManager.saveDeviceName(self.fieldDeviceName.text())
			self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
			
	@QtCore.pyqtSlot()
	def exitPressed(self):
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
		
	@QtCore.pyqtSlot()
	def plusPressed(self):
		self.tabWidget.editType.typeToEdit = None
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.editType))
		
	@QtCore.pyqtSlot()	
	def selectionChanged(self):
		if len(self.listView.selectionModel().selectedIndexes()) == 1:
			name = self.listView.selectedIndexes()[0].data()
			allTypes = self.dataManager.getAllData()["types"]
			f = [d for d in allTypes if d["name"]==name]
			if len(f) == 1:
				index = allTypes.index(f[0])
				self.tabWidget.editType.typeToEdit = allTypes[index]
				self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.editType))
		
	@QtCore.pyqtSlot()
	def noTypePressed(self):
		self.dataManager.setNoType()
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.mainPage))
