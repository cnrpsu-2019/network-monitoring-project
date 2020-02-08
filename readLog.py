import datetime
import time
import re

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"

#json body each part
#json_body = 
#[{"measurement": "client_event",
#"tags": 
#    {"event": "SessionTrap",
#    "type": "Informational"},
#"fields": 
#    {"item": 1}}]

measurement_head = '[' + "measurement" + ':' 
measurement_name = '{measurement_name}'
tags_head = "tags" + ':'
tags_body01 = '{tags_1}'+ ':' 
tags_value01 = '{tag_value_1}'
fields = "fields" + ':'
fields_head = '{field_head}' + ':' 
fields_value01 = '{field_value_1}'+ ']'

json_body = measurement_head + measurement_name +',' +tags_head + tags_body01 + tags_value01 +','+ fields + fields_head + fields_value01

def readUPS():
    with open('/var/log/client_logs/172.30.254.201/UPS.log',"r") as clientLog:
        print(clientLog.read())

def testRead():
    test = open('/home/bass/receive/' + fileName)
    while True:
        try:
            line = test.read()
            if not line:
                time.sleep(1)
            if 'UpTimeInstance' in line:
                uptimeSlice = line[25:]
                print(json_body)
                print(uptimeSlice)
        except EOFError:
            break
    test.close()
if __name__ == '__main__':
    testRead()
#    readUPS()
