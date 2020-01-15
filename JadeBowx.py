import datetime
import Filterx
import time
from influxdb import InfluxDBClient

class Jadebowx:
    def readLog():
        now = datetime.datetime.now()
        strnow = now.strftime("%X") #current time
        #log file date
        fileDate = now.strftime("%d-%b-%Y")
        fileName = "trapd-" + fileDate + ".log"
        readfile = open('/home/bass/receive/' + fileName, 'r')
        #export to db
        line = readfile.read()
        if not line:
            time.sleep(1)
    def prepareDB(username, password): 
        dbClient = InfluxDBClient('localhost', 8086, username, password, 'trapEvent', ssl=False, verify_ssl=False)
        dbClient.create_database('trapEvent')
        #print('Database created, go check in shell')
        dbClient.switch_database('trapEvent')
    def countUser():
        pass
    def countEvent():
        pass
