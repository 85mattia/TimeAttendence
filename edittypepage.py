from views.edittypeui import Ui_Page
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui
from datamanager import DataManager
from alertwindow import AlertWindow

class EditTypePage(QWidget, Ui_Page):
	
	dataManager = DataManager()
	typeToEdit = None

	def __init__(self, parent=None, tab=None):
		super(EditTypePage, self).__init__(parent)
		self.setupUi(self)
		self.tabWidget = tab
	
	def showEvent(self,event):
		self.labelMessage.setText("")
		self.nameField.setFocus(True)
		if self.typeToEdit == None:
			self.labelTitle.setText("New Type")
			self.nameField.setText("")
			self.buttonMakeCurrent.setVisible(False)
			self.buttonRemove.setVisible(False)
		else:
			self.labelTitle.setText("Edit Type")
			self.nameField.setText(self.typeToEdit["name"])
			self.labelMessage.setText("")
			self.buttonMakeCurrent.setVisible(True)
			self.buttonRemove.setVisible(True)
	
	@QtCore.pyqtSlot()
	def exitPressed(self):
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.settingPage))
		
	@QtCore.pyqtSlot()
	def removePressed(self):
		self.alert = AlertWindow(text="Remove " + self.typeToEdit["name"] + " ?", actionOnOkButton=self.removeConfirm)
		self.alert.show()
		
	def removeConfirm(self):
		if self.dataManager.removeType(self.typeToEdit["objectId"]) == True:
			lastTypeId = self.dataManager.getLastTypeId()
			if lastTypeId == self.typeToEdit["objectId"]:
				self.dataManager.setNoType()
			self.dataManager.removeTypeIdFromLogs(self.typeToEdit["objectId"])
			self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.settingPage))
		else:
			self.labelMessage.setText("Error")
		
	@QtCore.pyqtSlot()
	def makeCurrentPressed(self):
		self.dataManager.saveLastTypeId(self.typeToEdit["objectId"])
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.mainPage))
		
	@QtCore.pyqtSlot()
	def savePressed(self):
		self.labelMessage.setText("")
		if self.nameField.text() == "":
			return
		types = self.dataManager.getAllData()["types"]
		if self.typeToEdit != None:
			types.pop(types.index(self.typeToEdit))
		r =[d for d in types if d["name"]==self.nameField.text()]
		if len(r) != 0:
			self.labelMessage.setText("Type Name Already Exist.")
			return
		if self.typeToEdit != None:
			self.dataManager.editType({"name":self.nameField.text(),"objectId":self.typeToEdit["objectId"]})
		else:
			self.dataManager.addType(self.nameField.text())
		self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.settingPage))
			
		

       
