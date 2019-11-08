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
        #floor 01
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
        #floor 02
        if 'AP2-7-R020-153' in line:
             json_body = [{"measurement":"ap_event","tags":{"name":"AP2-7-R020-153","floor":"02","macAddr":"88:1d:fc:a:f1:20"},"fields":{"item": 1}}]
             dbClient.write_points(json_body)
        if 'AP2-8-R020-154' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP2-8-R020-154","floor":"02","macAddr":"88:1d:fc:6:3f:b0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP213-R202' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP213-R202","floor":"02","macAddr":"70:10:5c:b1:a4:d0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP214-R203' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP214-R203","floor":"02","macAddr":"a0:e0:af:3d:c7:80"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP206-R204' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP206-R204","floor":"02","macAddr":"f4:4e:5:a2:a1:10"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP205-R207' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP205-R207","floor":"02","macAddr":"f4:4e:5:b5:65:90"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        #floor03
        if 'AP108-R300' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP108-R300","floor":"03","macAddr":"a0:3d:6f:31:b7:e0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP209-R302-1' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP209-R302-1","floor":"03","macAddr":"f4:4e:5:df:4e:f0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP210-R302-2' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP210-R302-2","floor":"03","macAddr":"f4:4e:5:db:f0:40"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP110-R311' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP110-R311","floor":"03","macAddr":"70:10:5c:b1:9e:d0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP221-R301A' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP221-R301A","floor":"03","macAddr":"68:3b:78:e1:93:80"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP220-R301B' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP220-R301B","floor":"03","macAddr":"68:3b:78:e1:93:0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP219-R303' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP219-R303","floor":"03","macAddr":"68:3b:78:e9:47:40"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        #floor4
        if 'AP112-R400' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP112-R400","floor":"04","macAddr":"a0:e0:af:22:6e:70"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP109-R404' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP109-R404","floor":"04","macAddr":"a0:3d:6f:31:b7:f0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP212-IDL' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP212-IDL","floor":"04","macAddr":"a0:3d:6f:31:b7:d0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP111-R405' in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP111-R405","floor":"04","macAddr":"a0:e0:af:95:9c:40"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        if 'AP215-R409'in line:
            json_body = [{"measurement":"ap_event","tags":{"name":"AP215-R409","floor":"04","macAddr":"70:10:5c:b1:a4:d0"},"fields":{"item": 1}}]
            dbClient.write_points(json_body)
        #rogue ap event
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
