import os, random, string
import json
import configparser

class DataManager(object):

    config = configparser.ConfigParser()
    __instance = None
    configFileName = "default.ini"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataManager, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.initConfig()

    def initConfig(self):
        if not os.path.exists("data.json"):
            with open("data.json", "w+") as f:
                baseJson = '{"users":[], "logs":[], "types":[]}'
                jsonData = json.loads(baseJson)
                f.write(json.dumps(jsonData, indent=4))
        if not os.path.exists(self.configFileName):
            with open(self.configFileName, "w+") as f:
                self.config["SETTING"] = {"laststatus": "OUT", "devicename": "Device 1", "lasttypeid":""}
                self.config.write(f)

    def getAllData(self):
        with open("data.json") as f:
            return json.load(f)
            
    def getDeviceName(self):
        return self.config["SETTING"]["devicename"]
        
    def saveDeviceName(self, name):
        with open(self.configFileName, "r+") as f:
            self.config["SETTING"]["devicename"] = name
            f.seek(0)
            self.config.write(f)
            f.truncate()
            
    def removeTypeIdFromLogs(self, typeId):
        with open("data.json", "r+") as f:
            jsonData = json.load(f)
            logsToEdit = [d for d in jsonData["logs"] if d["typeId"]==typeId]
            for log in logsToEdit:
                jsonData["logs"][jsonData["logs"].index(log)]["typeId"] = ""
            f.seek(0)
            json.dump(jsonData, f, indent=4)
            f.truncate()
            
    def deleteLogs(self, logs):
        with open("data.json", "r+") as f:
            jsonData = json.load(f)
            for l in logs:
                jsonData["logs"].remove(l)
            f.seek(0)
            json.dump(jsonData, f, indent=4)
            f.truncate()
            
            
    def saveLastTypeId(self, lastTypeId):
        with open(self.configFileName, "r+") as f:
            self.config["SETTING"]["lasttypeid"] = lastTypeId
            f.seek(0)
            self.config.write(f)
            f.truncate()
            
    def setNoType(self):
        with open(self.configFileName, "r+") as f:
            self.config.set("SETTING", "lasttypeid", "")
            f.seek(0)
            self.config.write(f)
            f.truncate()

    def getLastStatus(self):
        self.config.read(self.configFileName)
        last = self.config.get("SETTING", "laststatus")
        return last
        
    def getLastTypeId(self):
        self.config.read(self.configFileName)
        last = self.config.get("SETTING", "lasttypeid")
        return last
        
    def addType(self, name):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            allData["types"].append({"name":name, "objectId":self.random_string(6)})
            f.seek(0)
            json.dump(allData, f, indent=4)
            f.truncate()
            
    def editType(self, typeToEdit):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            objToEdit = [d for d in allData["types"] if d["objectId"]==typeToEdit["objectId"]]
            if len(objToEdit) == 1:
                indexToEdit = allData["types"].index(objToEdit[0])
                allData["types"][indexToEdit]["name"] = typeToEdit["name"]
                f.seek(0)
                json.dump(allData, f, indent=4)
                f.truncate()
    
    def getTypeName(self, typeId):
        types = self.getAllData()["types"]
        if typeId == "":
            return ""
        f = [d for d in types if d["objectId"]==typeId]
        if len(f) == 1:
            return f[0]["name"]
        else:
            return ""

    def saveLastStatus(self, stat):
        with open(self.configFileName, "r+") as f:
            self.config["SETTING"]["laststatus"] = stat
            f.seek(0)
            self.config.write(f)
            f.truncate()
            
    def getNode(self, node=None, filterDict=None):
        data = self.getAllData()
        if node != None and node in data:
            data = data[node]
            print(filterDict)
            if filterDict != None and filterDict != {}:
                try:
                    for k,v in filterDict.items():
                        data = [d for d in data if d[k]==v]
                    return data
                except KeyError:
                    return None
            else:
                return data
        else:
            return None
            
    def getObjectForId(self, node, row_id):
        return self.getNode(node, {"objectId":row_id})
        
    def addRow(self, node, rowToAdd):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            if not node in allData:
                return {"error" : "Not Found"}
            if not rowToAdd:
                return {"error":"the request is empty"}
            newRow = rowToAdd.copy()
            if not "objectId" in newRow:
                newRow["objectId"] = self.random_string(6)
            allData[node].append(newRow)
            f.seek(0)
            json.dump(allData, f, indent=4)
            f.truncate()
        return newRow
            
    def editRow(self, node, objectId, data):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            if not node in allData:
                return {"error" : "Not Found"}
            r = [d for d in allData[node] if d["objectId"]==objectId]
            if len(r) != 1:
                return {"error":"object not found"}
            print("data " + str(data))
            for k,v in allData[node][allData[node].index(r[0])].items():
                if k != "objectId" and k in data:
                    print("sono qua")
                    allData[node][allData[node].index(r[0])][k] = data[k]
                    print(allData[node][allData[node].index(r[0])])
            f.seek(0)
            json.dump(allData, f, indent=4)
            f.truncate()
        return r[0]
    
    def delete(self, node, objectId):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            if not node in allData:
                return {"error" : "Not Found"}
            r = [d for d in allData[node] if d["objectId"]==objectId]
            if len(r) != 1:
                return {"error":"object not found"}
            if node == "users":
                logs = [d for d in allData["logs"] if d["userId"]==objectId]
                for log in logs:
                    allData.remove(log)
            if node == "types":
                logs = [d for d in allData["logs"] if d["typeId"]==objectId]
                for log in logs:
                    allData["logs"][allData["logs"].index(log)]["typeId"] = ""
            allData[node].remove(r[0])
            f.seek(0)
            json.dump(allData, f, indent=4)
            f.truncate()
        return r[0]
        
    def importLogs(self,mode, edit=True):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            logsToExport = allData["logs"]
            if mode == "new":
                logsToExport = [d for d in allData["logs"] if d["downloaded"]=="0"]
            if edit == True:
                for log in logsToExport:
                    allData["logs"][allData["logs"].index(log)]["downloaded"] = "1"
                f.seek(0)
                json.dump(allData, f, indent=4)
                f.truncate()
        fullLogs = []
        for ind,log in enumerate(logsToExport):
            t = [d for d in allData["types"] if d["objectId"]==log["typeId"]]
            u = [d for d in allData["users"] if d["objectId"]==log["userId"]]
            if len(u) == 1:
                typeName = ""
                if len(t) == 1:
                    typeName = t[0]["name"]
                fullLogs.append({"Name": u[0]["name"],
                                    "UID": u[0]["id"],
                                    "DateTime": log["datetime"],
                                    "Status":log["status"],
                                    "logId" : log["objectId"],
                                    "downloaded" : log["downloaded"],
                                    "type":typeName})
        return {"logs":fullLogs}

    def getLogs(self, filterDict=None):
        with open("data.json") as f:
            jsonData = json.load(f)
            print(jsonData)
            if filter == None:
                return self.jsonData["logs"]

    def getUsers(self, filterDict=None):
        with open("data.json") as f:
            jsonData = json.load(f)
            if filterDict == None:
                return jsonData["users"]
            elif len(list(filterDict)) == 1:
                return [
                    d
                    for d in jsonData["users"]
                    if d[list(filterDict)[0]] == filterDict[list(filterDict)[0]]
                ]
            else:
                return []

    def addUser(self, newUser):
        with open("data.json", "r+") as f:
            jsonData = json.load(f)
            jsonData["users"].append(newUser)
            f.seek(0)
            json.dump(jsonData, f, indent=4)
            f.truncate()
            
    def removeType(self, objectId):
        with open("data.json", "r+") as f:
            jsonData = json.load(f)
            types = [d for d in jsonData["types"] if d["objectId"]==objectId]
            if len(types) == 1:
                jsonData["types"].pop(jsonData["types"].index(types[0]))
                f.seek(0)
                json.dump(jsonData, f, indent=4)
                f.truncate()
                return True
            else:
                return False

    def removeUser(self, user):
        with open("data.json", "r+") as f:
            jsonData = json.load(f)
            allUsers = jsonData["users"]
            r = [u for u in allUsers if u["objectId"] == user["objectId"]]
            if len(r) != 1:
                print("errore objectId non trovo user")
            else:
                del jsonData["users"][allUsers.index(r[0])]
                allLogs = jsonData["logs"]
                indexes = []
                for ind, log in enumerate(allLogs):
                    if log["userId"] == user["objectId"]:
                        indexes.append(ind)
                for ind in sorted(indexes, reverse=True):
                    del jsonData["logs"][ind]
                f.seek(0)
                json.dump(jsonData, f, indent=4)
                f.truncate()

    def deleteLogs(self, logsToDel):
        with open("data.json", "r+") as f:
            allData = json.load(f)
            for logToDel in logsToDel:
                del allData["logs"][allData["logs"].index(logToDel)]
            f.seek(0)
            json.dump(allData, f, indent=4)
            f.truncate()

    def editUser(self, user):
        with open("data.json", "r+") as f:
            jsonData = json.load(f)
            allUsers = jsonData["users"]
            r = [d for d in allUsers if d["objectId"] == user["objectId"]]
            if len(r) != 1:
                print("errore objectId")
            else:
                indexToEdit = allUsers.index(r[0])
                jsonData["users"][indexToEdit]["name"] = user["name"]
                jsonData["users"][indexToEdit]["cardCode"] = user["cardCode"]
                jsonData["users"][indexToEdit]["id"] = user["id"]
                jsonData["users"][indexToEdit]["admin"] = user["admin"]
                f.seek(0)
                json.dump(jsonData, f, indent=4)
                f.truncate()

    def saveNewLog(self, log):
        with open("data.json", "r+") as f:
            fullData = json.load(f)
            fullData["logs"].append(log)
            users = [d for d in fullData["users"] if d["objectId"] == log["userId"]]
            if len(users) == 1:
                user = users[0]
                if user["lastStatus"] != log["status"]:
                    ind = fullData["users"].index(user)
                    fullData["users"][ind]["lastStatus"] = log["status"]
                f.seek(0)
                json.dump(fullData, f, indent=4)
                f.truncate()
                return True
            else:
                return False

    def deleteAllLogs(self):
        with open("data.json", "r+") as f:
            allFile = json.load(f)
            allFile["logs"] = []
            f.seek(0)
            json.dump(allFile, f, indent=4)
            f.truncate()

    def random_string(self, length):
        return "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
        )
