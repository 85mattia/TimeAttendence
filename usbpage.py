from logging import log
from views.usbpageui import Ui_Page
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore
from datamanager import DataManager
import csv
import psutil
from datetime import datetime
import json
from alertwindow import AlertWindow


class UsbPage(QWidget, Ui_Page):

    dataManager = DataManager()
    data = []

    def __init__(self, parent=None, tab=None):
        super(UsbPage, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget = tab

    @QtCore.pyqtSlot()
    def backPressed(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))

    @QtCore.pyqtSlot()
    def downloadAllPressed(self):
        self.createCsv(allLogs=True)

    @QtCore.pyqtSlot()
    def downloadNewPressed(self):
        self.createCsv(allLogs=False)

    @QtCore.pyqtSlot()
    def comboActivated(self):
        print("")
        # print(self.comboBoxUsb.currentIndex())

    def createCsv(self, allLogs=True):
        allData = self.dataManager.getAllData()
        allTypes = allData["types"]
        logs = allData["logs"]
        allUsers = allData["users"]
        if allLogs == False:
            logs = [d for d in logs if d["downloaded"] == "0"]
        filename = datetime.now().strftime("/logs_%d-%m-%Y_%H-%M-%S.csv")
        try:
            with open(
                str(
                    self.comboBoxUsb.itemText(self.comboBoxUsb.currentIndex())
                    + filename
                ),
                "w",
            ) as f:
                self.progressBar.setMaximum(len(logs))
                self.progressBar.setValue(0)
                self.progressBar.setVisible(True)
                writer = csv.writer(f)
                writer.writerow(["Name", "ID", "Card", "Time", "Stat", "Type"])
                logs = sorted(
                    logs,
                    key=lambda k: datetime.fromisoformat(k["datetime"]),
                    reverse=True,
                )
                for i, log in enumerate(logs):
                    users = [d for d in allUsers if d["objectId"] == log["userId"]]
                    if len(users) == 1:
                        name = users[0]["name"]
                        uid = users[0]["id"]
                        cardId = users[0]["cardCode"]
                        dtime = datetime.fromisoformat(log["datetime"]).strftime(
                            "%d/%m/%Y %H:%M:%S"
                        )
                        types = [d for d in allTypes if d["objectId"]==log["typeId"]]
                        if len(types) == 1:
                            typeName = types[0]["name"]
                        else:
                            typeName = ""
                        writer.writerow([name, uid, cardId, dtime, log["status"],typeName])
                        self.progressBar.setValue(self.progressBar.value() + 1)
                        allData["logs"][i]["downloaded"] = "1"
            with open("data.json", "r+") as f:
                f.seek(0)
                json.dump(allData, f, indent=4)
                f.truncate()
            self.progressBar.setVisible(False)
            self.alert = AlertWindow(text="Csv Saved !", showCancelButton=False)
            self.alert.show()
        except EnvironmentError:
            self.alert = AlertWindow(text="Usb Device Error !", showCancelButton=False)
            self.alert.show()

    @QtCore.pyqtSlot()
    def scanPressed(self):
        self.scanUsb()

    def scanUsb(self):
        self.partitions = psutil.disk_partitions()
        self.comboBoxUsb.clear()
        if len(self.partitions) == 0:
            self.comboBoxUsb.addItem("No Devices")
        else:
            for p in self.partitions:
                self.comboBoxUsb.addItem(p.mountpoint)

    def showEvent(self, event):
        self.scanUsb()
        self.progressBar.setVisible(False)
