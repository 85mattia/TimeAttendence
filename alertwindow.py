from views.alertwindowui import Ui_AlertWindow
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import QtCore, QtWidgets

class AlertWindow(QDialog, Ui_AlertWindow):

    

	def __init__(self, parent=None, text="Alert", showCancelButton=True, showOkButton=True, actionOnOkButton=None):
		super(AlertWindow, self).__init__(parent)
		self.setupUi(self)
		self.buttonCancel.setVisible(showCancelButton)
		self.buttonOk.setVisible(showOkButton)
		self.label.setText(text)
		self.action = actionOnOkButton
		self.showFullScreen()
		
		
	@QtCore.pyqtSlot()
	def okPressed(self):
	    self.close()
	    if self.action is not None:
	        self.action()
	    
	@QtCore.pyqtSlot()
	def cancelPressed(self):
	    self.close()
        
