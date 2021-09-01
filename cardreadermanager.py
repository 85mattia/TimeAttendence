import keyboard
import time

class CardReader(object):

    delegate = None
    __instance = None
    currentStr = ""
    lastTime = time.time()
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CardReader,cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):      
        if(self.__initialized): return
        self.__initialized = True
        self.initConfig()
        
    def initConfig(self):
        self.currentStr = ""
        keyboard.on_press(self.keyPressed)
        
    def keyPressed(self, event):
        if event.time - self.lastTime > 0.1:
            self.currentStr = ""
        self.lastTime = event.time
        if event.name == "enter":
            if self.delegate != None:
                self.delegate.cardPassed(self.currentStr)
            self.currentStr = ""
        else:
            self.currentStr = self.currentStr + event.name
        
