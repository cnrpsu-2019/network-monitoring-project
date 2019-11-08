import datetime
import time
from influxdb import InfluxDBClient

running = True
now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"
readfile = open('/home/bass/receive/' + fileName, 'r')
#line = readfile.read()

#print(line)

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
        #client event
        if 'SessionTrap' in line:
            json_body = [{"measurement": "client_event","tags": {"event": "SessionTrap","type": "Informational"},"fields": {"item": 1}}]
            dbClient.write_points(json_body)
        if 'MovedToRunState' in line:
           json_body = [{"measurement": "client_event","tags": {"event":"MovedToRunState","type":"Informational"},"fields":{"item": 1}}]
           dbClient.write_points(json_body)
        if 'AssociateFail' in line:
            json_body = [{"measurement":"client_event","tags":{"event":"AssociateFail","type":"Informational_fail"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        #client.write(['interface,path=address,elementss=link value=3'],{'db':'yourdb'},204,'line')
        if 'Deauthenticate' in line:
            json_body = [{"measurement":"client_event","tags":{"event":"Deauthenticate","type":"Informational_fail"},"fields":{"item": 1}}]
        if 'Blacklisted' in line:
            json_body = [{"measurement":"client_event","tags":{"event":"Blacklisted","type":"Informational_blacklisted"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        #Ap event
        if 'AP3-46-R010-146' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP3-46-R010-146","floor":"01","macAddr":"bc:16:f5:98:8:0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP218-FL01-E' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP218-FL01-E","floor":"01","macAddr":"24:fb:65:65:9a:4f"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP217-FL01-W' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP217-FL01-W","floor":"01","macAddr":"68:3b:78:e1:94:20"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP204-R100' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP204-R100","floor":"01","macAddr":"f4:4e:5:a2:a1:d0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP216-R101' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP216-R101","floor":"01","macAddr":"dc:8c:37:4c:2e:e0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP211-Shop' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP211-Shop","floor":"01","macAddr":"f4:4e:5:b5:24:b0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'RogueAPRemoved' in line:
            json_body = [{"measurement":"ap_event_rogue","tags":{"event":"RogueAPRemoved","type":"Informational_rogue"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'ApRogueDetected' in line:
            json_body = [{"measurement":"ap_event_rogue","tags":{"event":"ApRogueDetected","type":"Informational_rogue"},"fields":{"item": 1}}]
        print(line)
        #json_body = [{"measurement":"client_event","tags":{"event":"Deauthenticate","type":"Informational_fail"},"fields":{"item": 1}}]
    except EOFError:
        running = False

readfile.close()
