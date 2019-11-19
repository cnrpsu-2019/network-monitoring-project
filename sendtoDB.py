import datetime
import time
from influxdb import InfluxDBClient
#print(line)
running = True
now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"
readfile = open('/home/bass/receive/' + fileName, 'r')
#line = readfile.read()

dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verify_ssl=False)
dbClient.create_database('trapEvent')

#print('Database created, go check in shell')

dbClient.switch_database('trapEvent')
#a = dbClient.get_list_measurements()

print(dbClient.get_list_users())
#print(dbClient.get_list_measurements())

while running:
    try:
        line = readfile.read()
        if not line:
            time.sleep(1)
        
    except EOFError:
        running = False
readfile.close()
