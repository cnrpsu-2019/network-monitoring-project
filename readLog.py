import datetime
import time
import re

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#loggt file date

fileDate = now.strftime("%d-%b-%Y")
def readUPS():
    with open('/var/log/client_logs/172.30.254.201/UPS.log',"r") as clientLog:
        print(clientLog.read())

def testRead():
#    test = open('/home/bass/receive/' + fileName)
    with open('/var/log/client_logs/syslog/snmptrapd.log','r') as test:
        while True:
            try:
                line = test.read()
                if not line:
                    time.sleep(1)
                print(line + '\n')
            except EOFError:
                break
    test.close()

if __name__ == '__main__':
    testRead()
    readUPS()
