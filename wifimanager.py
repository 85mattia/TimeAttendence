import subprocess
import argparse
import requests
import socket
import os

class WifiManager():

    parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
    
    
    def getGateway(self):
        gw = os.popen("ip -4 route show default").read().split()
        if gw == "":
            return None
        if len(gw) < 11:
            return None
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2], 0))
        ipaddr = s.getsockname()[0]
        gateway = gw[2]
        host = socket.gethostname()
        dev = gw[4]
        return ipaddr, gateway, host, dev
        
    def getWifiPower(self):
        self.parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
        args = self.parser.parse_args()
        cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True, stdout=subprocess.PIPE)
        for line in cmd.stdout:
            if "Signal level" in str(line,"utf-8"):
                db = int(str(line,"utf-8").split()[3].replace("level=",""))
                return db
                
        
    def internetOn(self):
        url = "http://www.google.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            return False
