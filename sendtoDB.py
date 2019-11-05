import datetime
import string
from influxdb import InfluxDBClient
import time

def main():
    running = True
    now = datetime.datetime.today()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    toReadData = open('/home/bass/receive/' + fileName, 'r')

    client = InfluxDBClient('localhost',8090,'sabaszx','admin','snmptrapd',use_udp=True)
    #client.switch_database('snmptrapd')
    #series = []
    while running:
        try:
            #reading file continuously
            line = toReadData.readline()
            json_body = [
                    {
                        "measurement":"trap_daemon",
                        "tags":{
                            "InterfaceID":""
                        },
                        "time": int(now.strftime('%s')),
                        "fields":{
                            "MACAddress":"",
                            "Username":"",
                            "Event":"",
                            "ApName":"",
                            }
                        }
                    ]
            if not line:
                time.sleep(1)
            print('before parsing')
            if 'ApIfSlotId' in line:
                payload = line.split()
                json_body["tags"]["InterfaceID"] = int(payload[1])
                print(payload[1])
            if 'Event' in line:
                payload = line.split()
                json_body["fields"]["Event"] = payload[1]
                print(payload[1])
            if 'ApName' in line:
                payload = line.split()
                json_body["fields"]["APName"] = payload[1]
                print(payload[1])
            if 'ApMacAddress' in line:
                payload = line.split()
                json_body["fields"]["MACAddress"] = payload[1]
                print(payload[1])
            if 'ClientUsername' in line:
                payload = line.split()
                json_body["fields"]["Username"] = payload[1]
                print(payload[1])
            try:
                print('in block try')
                if protocol == json:
                    client.write(json_body)
            except:
                print('error')

            #reset values
            #json_body["tags"]["InterfaceID"] = ""
            #json_body["fields"]["Event"] = ""
            #json_body["fields"]["APName"] = ""
            #json_body["fields"]["MACAddress"] = ""
            #json_body["fields"]["Username"] = ""
            
        except EOFError:
            running = False
    toReadData.close()

if __name__ == '__main__':
    main()
