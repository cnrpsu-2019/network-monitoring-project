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
ap_fl01 = {"ap01":"AP3-46-R010-146","ap02":"AP218-FL01-E","ap03":"AP217-FL01-W","ap04":"AP204-R100","ap05":"AP216-R101","ap06":"AP211-Shop"}
ap_fl02 = {"ap01":"AP2-7-R020-153","ap02":"AP2-8-R020-154","ap03":"AP213-R202","ap04":"AP214-R203","ap05":"AP206-R204","ap06":"AP205-R207"}
ap_fl03 = {"ap01":"AP108-R300","ap02":"AP209-R302-1","ap03":"AP210-R302-2","ap04":"AP110-R311","ap05":"AP221-R301A","ap06":"AP220-R301B","ap07":"AP219-R303"}
ap_fl04 = {"ap01":"AP112-R400","ap02":"AP109-R404","ap03":"AP212-IDL","ap04":"AP111-R405","ap05":"AP215-R409"}

all_ap = [ap_fl01, ap_fl02, ap_fl03, ap_fl04]
print(ap_fl01)
while running:
    try:
        line = readfile.read()
        if not line:
            time.sleep(1)
<<<<<<< HEAD
        print(line)
        #print(len(line_split))
        known_ssid_list = ["PSU WiFi 802.1x","PSU WiFi 5GHz","TrueMove H","CoEIoT","CoEWiFi"]
         #json_body = [{"measurement":"client_event","tags":{"event":"Deauthenticate","type":"Informational_fail"},"fields":{"item": 1}}]
=======
        
>>>>>>> 37dca75ddc7c83c94bcc560342ee0317a0854dde
    except EOFError:
        running = False
readfile.close()
