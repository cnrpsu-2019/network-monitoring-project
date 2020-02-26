import datetime
import time
import re
from influxdb import InfluxDBClient

#loggt file date
now = datetime.datetime.now()
strnow = now.strftime("%X") #current time

dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verify_ssl=False)
dbClient.switch_database('trapEvent')

fileDate = now.strftime("%d-%b-%Y")

def readUPS():
    with open('/var/log/client_logs/172.30.254.201/UPS.log',"r") as clientLog:
        while True:
            try:
                json_body = [{
                    "measurement": "ssid_count",
                    "tags": {
                        "SSIDName": "unknown",
                    "type": "others"},
                    "fields": {
                        "item": 1}
                        }
                    ]
                dbClient.write_points(json_body)
            except EOFError:
                break
        print(clientLog.read())
    clientLog.close()

def testRead():
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
#    testRead()
    readUPS()
