import datetime
import time
import re

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"

def readUPS():
    with open('/var/log/client_logs/172.30.254.201/UPS.log',"r") as clientLog:
        for line in clientLog:
            if 'UPS: No longer on battery power.' in line:
                print('no longer on battery power')

def testRead():
    test = open('/home/bass/receive/' + fileName)
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
