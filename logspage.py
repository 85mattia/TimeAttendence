from views.logspageui import Ui_Page
from datamanager import DataManager
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QBrush, QColor
from datetime import datetime, date
from alertwindow import AlertWindow


class LogsPage(QWidget, Ui_Page):

    dataManager = DataManager()
    currentUser = None

    def __init__(self, parent=None, tab=None):
        super(LogsPage, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget = tab
        h = self.tableWidget.horizontalHeader()
        h.setSectionResizeMode(0, QHeaderView.Stretch)
        h.setSectionResizeMode(1, QHeaderView.Stretch)
        h.setSectionResizeMode(2, QHeaderView.Fixed)
        h.setSectionResizeMode(3, QHeaderView.Stretch)
        h.setSectionResizeMode(4, QHeaderView.Stretch)
        self.tableWidget.setShowGrid(False)

    def showEvent(self, event):
        if self.currentUser == None:
            self.labelTitle.setText("All Logs")
            self.createTable()
        else:
            self.labelTitle.setText(self.currentUser["name"] + " Logs")
            self.createTable({"objectId": self.currentUser["objectId"]})

    def createTable(self, forUser=None):
        self.buttonDeleteSelected.setVisible(False)
        self.tableWidget.selectionModel().clear()
        self.allData = self.dataManager.getAllData()
        if forUser == None:
            self.allLogs = self.allData["logs"]
        else:
            self.allLogs = [
                d for d in self.allData["logs"] if d["userId"] == forUser["objectId"]
            ]
        self.allLogs = sorted(
            self.allLogs,
            key=lambda k: datetime.fromisoformat(k["datetime"]),
            reverse=True,
        )
        self.tableWidget.setRowCount(len(self.allLogs))
        for r in range(len(self.allLogs)):
            users = [
                d
                for d in self.allData["users"]
                if d["objectId"] == self.allLogs[r]["userId"]
            ]
            logTypeName = ""
            if self.allLogs[r]["typeId"] != "":
                t = [d for d in self.allData["types"] if d["objectId"]==self.allLogs[r]["typeId"]]
                if len(t) == 1:
                    logTypeName = t[0]["name"]
            if len(users) == 1:
                user = users[0]
                for c in range(self.tableWidget.columnCount()):
                    header = self.tableWidget.horizontalHeaderItem(c).text()
                    if self.allLogs[r]["downloaded"] == "1":
                        brush = QBrush(QColor(130, 130, 130))
                    else:
                        brush = QBrush(QColor(0, 0, 0))
                    if header == "ID":
                        self.tableWidget.setItem(r, c, QTableWidgetItem(user["id"]))
                        self.tableWidget.item(r,c).setForeground(brush)
                    elif header == "Name":
                        self.tableWidget.setItem(r, c, QTableWidgetItem(user["name"]))
                        self.tableWidget.item(r,c).setForeground(brush)
                    elif header == "Time":
                        time = datetime.fromisoformat(self.allLogs[r]["datetime"])
                        self.tableWidget.setItem(
                            r, c, QTableWidgetItem(time.strftime("%d/%m/%Y  %H:%M:%S"))
                        )
                        self.tableWidget.item(r,c).setForeground(brush)
                    elif header == "Type":
                        self.tableWidget.setItem(
                            r, c, QTableWidgetItem(logTypeName)
                        )
                        self.tableWidget.item(r,c).setForeground(brush)
                    elif header == "Stat":
                        self.tableWidget.setItem(
                            r, c, QTableWidgetItem(self.allLogs[r]["status"])
                        )
                        self.tableWidget.item(r,c).setForeground(brush)

    @QtCore.pyqtSlot()
    def selectedChanged(self):
        if len(self.tableWidget.selectedIndexes()) == 0:
            self.buttonDeleteSelected.setVisible(False)
        else:
            self.buttonDeleteSelected.setVisible(True)

    @QtCore.pyqtSlot()
    def deleteDownloadedPressed(self):
        self.alert = AlertWindow(text="Delete All Downloaded Logs ?", actionOnOkButton=self.deleteDownloadedConfirm)
        self.alert.show()
        
    def deleteDownloadedConfirm(self):
        self.dataManager.deleteLogs([d for d in self.allLogs if d["downloaded"]=="1"])
        self.showEvent(event=None)
    
    @QtCore.pyqtSlot()
    def deletePressed(self):
        if len(self.tableWidget.selectedIndexes()) == 0:
	        return
        row = self.tableWidget.selectedIndexes()[0].row()
        urerId = self.allLogs[row]["userId"]
        users = [d for d in self.allData["users"] if d["objectId"] == urerId]
        if len(users) == 1:
            user = users[0]
            self.alert = AlertWindow(
                text="Delete Log  "
                + self.allLogs[row]["status"]
                + " "
                + datetime.fromisoformat(self.allLogs[row]["datetime"]).strftime(
                    "%d/%m/%Y  %H:%M:%S"
                )
                + " ?",
                actionOnOkButton=self.saveConfirmed,
            )
            self.alert.show()

    def saveConfirmed(self):
        row = self.tableWidget.selectedIndexes()[0].row()
        logToDel = self.allLogs[row]
        self.dataManager.deleteLogs([logToDel])
        self.alert = AlertWindow(text="Log Deleted !", showCancelButton=False)
        self.alert.show()
        self.showEvent(event=None)

    @QtCore.pyqtSlot()
    def deleteAllLogsPressed(self):
        self.alert = AlertWindow(
            text="Delete all Logs ?", actionOnOkButton=self.delAllConfirmed
        )
        self.alert.show()

    def delAllConfirmed(self):
        self.dataManager.deleteAllLogs()
        self.showEvent(event=None)

    @QtCore.pyqtSlot()
    def exitPressed(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
