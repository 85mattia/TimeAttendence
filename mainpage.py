from views.mainpage import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from wifimanager import WifiManager
from datetime import datetime
from cardreadermanager import CardReader
from datamanager import DataManager
from restapiserver import runServer
import threading


class MainPage(QDialog, Ui_Dialog):

    wifiManager = WifiManager()
    cardReader = CardReader()
    currentStatus = "IN"
    dataManager = DataManager()
    wifiTimer = 0
    forzature = []
    tickTimer = QTimer()
    adminTimer = QTimer()
    restApiIsRunning = False

    def __init__(self, parent=None, tab=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget = tab
        self.labelInOut.setText("IN")
        self.wifiLabel.setText("")

    def clock(self):
        now = datetime.now()
        self.labelOrario.setText(now.strftime("%H:%M:%S"))
        self.wifiTimer += 1
        if self.wifiTimer > 5:
            self.wifiTimer = 0
            h = self.wifiLabel.height()
            w = self.wifiLabel.width()
            gate = self.wifiManager.getGateway()
            if gate == None:
                self.wifiLabel.setPixmap(QPixmap())
                self.restApiIsRunning = False
            else:
                if self.restApiIsRunning == False:
                    self.restApiIsRunning = True
                    thread = threading.Thread(target = self.runRestApi)
                    thread.daemon = True
                    thread.start()
                if gate[3] == "wlan0":
                    db = self.wifiManager.getWifiPower()
                    if db > -45:
                        self.wifiPixMap = QPixmap("images/wifi-4.png")
                    elif db > -60:
                        self.wifiPixMap = QPixmap("images/wifi-3.png")
                    elif db > -70:
                        self.wifiPixMap = QPixmap("images/wifi-2.png")
                    elif db > -80:
                        self.wifiPixMap = QPixmap("images/wifi-1.png")
                    else:
                        self.wifiPixMap = QPixmap("images/wifi-0.png")
                else:
                    self.wifiPixMap = QPixmap("images/ethernet.png")
                self.wifiLabel.setPixmap(self.wifiPixMap.scaled(w,h,QtCore.Qt.KeepAspectRatio))
         
    def runRestApi(self):
        runServer()
        
    @QtCore.pyqtSlot()
    def menuPressed(self):
        allUsers = self.dataManager.getAllData()["users"]
        f = [d for d in allUsers if d["admin"]=="1"]
        if len(f) > 0:
            self.tickTimer.stop()
            self.labelOrario.setText("Admin ?")
            self.adminTimer.timeout.connect(self.adminTimerTimeout)
            self.tickTimer.start(5000)
        else:
            self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
            
    def adminTimerTimeout(self):
        self.adminTimer.stop()
        self.clock()
        self.tickTimer.timeout.connect(self.clock)
        self.tickTimer.start(200)

    def showEvent(self, event):
        self.adminTimer.stop()
        self.tickTimer.timeout.connect(self.clock)
        self.tickTimer.start(200)
        self.cardReader.delegate = self
        self.currentStatus = self.dataManager.getLastStatus()
        self.lastTypeId = self.dataManager.getLastTypeId()
        self.labelInOut.setText(self.currentStatus)
        self.labelMessage.setText("")
        self.labelType.setText(self.dataManager.getTypeName(self.lastTypeId))
        self.setFocus()

    def hideEvent(self, event):
        self.cardReader.delegate = None

    def cardPassed(self, cardStr):
        users = self.dataManager.getUsers({"cardCode": cardStr})
        if len(users) == 1:
            user = users[0]
            if self.adminTimer.isActive():
                if user["admin"] == 1:
                    self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabWidget.menuPage))
                else:
                    self.adminTimerTimeout()
                return
            try:
                indexForzature = self.forzature.index(user["name"])
            except:
                indexForzature = None
            if user["lastStatus"] != self.currentStatus or indexForzature != None:
                try:
                    self.forzature.pop(indexForzature)
                except:
                    pass
                self.dataManager.saveNewLog(
                    {
                        "userId": user["objectId"],
                        "datetime": datetime.now().isoformat(),
                        "status": self.currentStatus,
                        "objectId": self.dataManager.random_string(6),
                        "downloaded": "0",
                        "typeId": self.lastTypeId
                    }
                )
                self.labelMessage.setText(
                    user["name"] + " logged " + self.currentStatus
                )
            else:
                self.labelMessage.setText(
                    "ERROR: " + user["name"] + " is already"
                    " logged " + self.currentStatus
                )
                self.forzature.append(user["name"])
        else:
            if self.adminTimer.isActive():
                self.adminTimerTimeout()
            self.labelMessage.setText("User Not Found !")
        t = threading.Timer(4, self.labelTimer)
        t.start()

    def labelTimer(self):
        self.labelMessage.setText("")

    @QtCore.pyqtSlot()
    def inPressed(self):
        self.currentStatus = "IN"
        self.labelInOut.setText("IN")
        self.dataManager.saveLastStatus("IN")

    @QtCore.pyqtSlot()
    def outPressed(self):
        self.currentStatus = "OUT"
        self.labelInOut.setText("OUT")
        self.dataManager.saveLastStatus("OUT")
