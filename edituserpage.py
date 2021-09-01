from views.edituserui import Ui_Page
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from alertwindow import AlertWindow
from views.alertwindowui import  Ui_AlertWindow
from datamanager import DataManager
import time
from cardreadermanager import CardReader

class EditUserPage(QWidget, Ui_Page):

    userToEdit = None
    dataManager = DataManager()
    cardReader = CardReader()
    
    def __init__(self, parent=None, tab=None):
        super(EditUserPage, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget = tab
		
    @QtCore.pyqtSlot()
    def exitPressed(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
	    
    @QtCore.pyqtSlot()
    def savePressed(self):
        admin = "0"
        if self.checkBoxAdmin.isChecked():
            admin = "1"
        if self.validateFields() == False:
        	return
        if self.userToEdit == None:
        	newUser = {"name":self.fieldName.text(), "cardCode":self.lineEditCardCode.text(), "id":str(self.spinBoxId.value()),"admin":admin,"lastStatus":"OUT", "objectId":str(self.dataManager.random_string(6))}
        	self.dataManager.addUser(newUser)
        else:
        	newUser = {"name":self.fieldName.text(), "cardCode":self.lineEditCardCode.text(), "id":str(self.spinBoxId.value()),"admin":admin,"lastStatus":self.userToEdit["lastStatus"], "objectId":self.userToEdit["objectId"]}
        	self.dataManager.editUser(user=newUser)
        self.alert = AlertWindow(text="Saved Successful.", showCancelButton=False)
        self.alert.show()
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.usersPage))
        
    def validateFields(self):
        allUsers = self.dataManager.getUsers()
        if self.userToEdit != None:
        	r = [d for d in allUsers if d["objectId"]==self.userToEdit["objectId"]]
        	if len(r) == 1:
        		allUsers.remove(r[0])
        if self.fieldName.text() == "":
            self.alert = AlertWindow(text="Missed name Field", showCancelButton=False)
            self.alert.show()
            return False
        if self.lineEditCardCode.text() == "":
            self.alert = AlertWindow(text="Missed CardCode Field", showCancelButton=False)
            self.alert.show()
            return False
        r = [d for d in allUsers if d["name"]==self.fieldName.text()]
        if len(r) != 0:
            self.alert = AlertWindow(text="Name " + self.fieldName.text() + " already exist.", showCancelButton=False)
            self.alert.show()
            return False
        r = [d for d in allUsers if d["id"]==str(self.spinBoxId.value())]
        if len(r) != 0:
            self.alert = AlertWindow(text="ID " + str(self.spinBoxId.value()) +  " already exist.", showCancelButton=False)
            self.alert.show()
            return False
        r = [d for d in allUsers if d["cardCode"]==self.lineEditCardCode.text()]
        if len(r) != 0:
            self.alert = AlertWindow(text="Card Code " + self.lineEditCardCode.text() + " already exist.", showCancelButton=False)
            self.alert.show()
            return False
        return True
        
	    
    @QtCore.pyqtSlot()
    def showLogsPressed(self):
    	if self.userToEdit == None:
    		return
    	self.tabWidget.logsPage.currentUser = self.userToEdit
    	self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.logsPage))
    	
        
    @QtCore.pyqtSlot()
    def readCardPressed(self):
    	self.lineEditCardCode.setText("")
    	if self.buttonRead.isChecked():
    		self.cardReader.delegate = self
    		self.lineEditCardCode.setPlaceholderText("Scan Card ...")
    		self.lineEditCardCode.setFocus()
    	else :
    		self.lineEditCardCode.setPlaceholderText("Card Code")
	    
    @QtCore.pyqtSlot()
    def deletePressed(self):
        self.alert = AlertWindow(text="Remove " + self.fieldName.text() + " and all Logs ?", actionOnOkButton=self.removeConfirmed)
        self.alert.show()
    
    def removeConfirmed(self):
    	self.dataManager.removeUser(self.userToEdit)
    	time.sleep(0.3)
    	self.alert = AlertWindow(text="User Removed.", showCancelButton=False)
    	self.alert.show()
    	self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.usersPage))
        
	    
    @QtCore.pyqtSlot()
    def generatePressed(self):
        self.spinBoxId.setValue(self.generateId())
        
    def generateId(self):
        allUser = self.dataManager.getUsers()
        max = 0
        for user in allUser:
            n = int(user["id"])
            if n > max:
                max = n
        return max+1
        
    def cardPassed(self, cardStr):
    	if self.buttonRead.isChecked():
    		self.lineEditCardCode.setText(cardStr)
    		self.buttonRead.setChecked(False)
        
	    
    def showEvent(self, event):
    	if self.userToEdit is None:
    		self.buttonDelete.setVisible(False)
    		self.labelTitle.setText("New User")
    		self.buttonShowLogs.setVisible(False)
    		self.fieldName.setText("")
    		self.lineEditCardCode.setText("")
    		self.checkBoxAdmin.setChecked(False)
    		self.spinBoxId.setValue(self.generateId())
    		self.lineEditCardCode.setText("")
    		self.lineEditCardCode.setPlaceholderText("Card Code")
    	else:
    		self.buttonDelete.setVisible(True)
    		self.labelTitle.setText("Edit User")
    		self.buttonShowLogs.setVisible(True)
    		self.fieldName.setText(self.userToEdit["name"])
    		self.lineEditCardCode.setText(self.userToEdit["cardCode"])
    		if self.userToEdit["admin"] == "1":
    			self.checkBoxAdmin.setChecked(True)
    		else:
    			self.checkBoxAdmin.setChecked(False)
    		self.spinBoxId.setValue(int(self.userToEdit["id"]))
    		
    def hideEvent(self, event):
        self.cardReader.delegate = None
