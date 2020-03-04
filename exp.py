from influxdb import InfluxDBClient
import time
import datetime
import Filterx
import JadeBowx
import re

#import yaml
dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verify_ssl=False)
dbClient.switch_database('trapEvent')

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return  mainString

def main():
    running = True
    now = datetime.datetime.now()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/receive/' + fileName, 'a')
    readfile = open('/home/bass/receive/' + fileName, 'r')
    while running:
        try:
            input_raw = input()
            #filter weird string sction
            filtered = input_raw.replace("<UNKNOWN>","" )
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)

            #filter out lookoup from Filterx  module 
            wrongtypeRemove = replaceMultiple(showDate, Filterx.wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"

            outstr  = replaceMultiple(weirdRemove,bad_chars,'')
            #outstr - write log files into local server
            result = replaceMultiple(outstr,Filterx.bad_list,' ')

            #write to local
            output.write(result + '\n')
            #export to db
            line = readfile.read()
            if not line:
                time.sleep(1)
            #associate users
            PatternAssociate = ['Associate', 'Sessiontrap''MovedToRunState','Username']
            for patterns in PatternAssociate:
                if re.search(patterns, line):
                    JadeBowx.countUserAssociate()
                    print('associated')
                    time.sleep(1)

            PatternDeauth = ['StationDeauthenticate', 'Disassociate','Deauthenticate']
            for patterns in PatternDeauth:
                if re.search(patterns, line):
                    JadeBowx.countUserDauth()
                    time.sleep(1)

            # ap each floor list
            floor_01_list = ['AP3-46-R010-146','AP218-FL01-E','AP217-FL01-W','AP204-R100','AP216-R101','AP211-Shop']
            floor_02_list = ['AP2-7-R020-153','AP2-8-R020-154','AP213-R202','AP214-R203','AP206-R204','AP205-R207']
            floor_03_list = ['AP108-R300','AP209-R302-1','AP209-R302-2','AP110-R311','AP221-R301A','AP221-R301B','AP219-R303']
            floor_04_list = ['AP112-R400','AP109-R404','AP212-IDL','AP111-R405','AP215-R409']
            rogue_list = ['RogueAPRemoved','RogueClientDetected','ApRogueDetected']

            for patterns in floor_01_list:
                if re.search(patterns, line):
                    JadeBowx.countFloor01()
                    print('floor1')
                    time.sleep(1)

            for patterns in floor_02_list:
                if re.search(patterns, line):
                    JadeBowx.countFloor02()
                    print('floor2')
                    time.sleep(1)
                    
            for patterns in floor_03_list:
                if re.search(patterns, line):
                    JadeBowx.countFloor03()
                    print('floor3')
                    time.sleep(1)

            for patterns in floor_04_list:
                if re.search(patterns,line):
                    JadeBowx.countFloor04()
                    print('floor4')
                    time.sleep(1)
                        
            if 'CoEWiFi' in line:
                JadeBowx.countCoeWifi()
                print('CoE WiFi')
                time.sleep(1)

            if 'PSU WiFi 802.1x' in line:
                JadeBowx.count802()
                print('802.1x')
                time.sleep(1)

            if 'PSU WiFi 5GHz' in line:
                JadeBowx.countPSU5Ghz()
                print('PSU 5ghz')
                time.sleep(1)

            if 'TrueMove H' in line:
                JadeBowx.countTruemove()
                print('truemove')
                time.sleep(1)

            if  'CoEIoT' in line:
                JadeBowx.countCoeIot()
                print('coeiot')
                time.sleep(1)

            for patterns in rogue_list:
                if re.search(patterns, line):
                    JadeBowx.countRogue()
                    print('others')
                    time.sleep(1)

            #Ap event
            #floor 01
            if 'AP3-46-R010-146' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP3-46-R010-146","floor":"01","macAddr":"bc:16:f5:98:8:0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP218-FL01-E' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP218-FL01-E","floor":"01","macAddr":"24:fb:65:65:9a:4f"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP217-FL01-W' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP217-FL01-W","floor":"01","macAddr":"68:3b:78:e1:94:20"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP204-R100' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP204-R100","floor":"01","macAddr":"f4:4e:5:a2:a1:d0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP216-R101' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP216-R101","floor":"01","macAddr":"dc:8c:37:4c:2e:e0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP211-Shop' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP211-Shop","floor":"01","macAddr":"f4:4e:5:b5:24:b0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)

            #floor 02
            if 'AP2-7-R020-153' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP2-7-R020-153","floor":"02","macAddr":"88:1d:fc:a:f1:20"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP2-8-R020-154' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP2-8-R020-154","floor":"02","macAddr":"88:1d:fc:6:3f:b0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP213-R202' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP213-R202","floor":"02","macAddr":"70:10:5c:b1:a4:d0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP214-R203' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP214-R203","floor":"02","macAddr":"a0:e0:af:3d:c7:80"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP206-R204' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP206-R204","floor":"02","macAddr":"f4:4e:5:a2:a1:10"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP205-R207' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP205-R207","floor":"02","macAddr":"f4:4e:5:b5:65:90"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)

            #floor03
            if 'AP108-R300' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP108-R300","floor":"03","macAddr":"a0:3d:6f:31:b7:e0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP209-R302-1' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP209-R302-1","floor":"03","macAddr":"f4:4e:5:df:4e:f0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP210-R302-2' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP210-R302-2","floor":"03","macAddr":"f4:4e:5:db:f0:40"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP110-R311' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP110-R311","floor":"03","macAddr":"70:10:5c:b1:9e:d0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP221-R301A' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP221-R301A","floor":"03","macAddr":"68:3b:78:e1:93:80"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP220-R301B' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP220-R301B","floor":"03","macAddr":"68:3b:78:e1:93:0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP219-R303' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP219-R303","floor":"03","macAddr":"68:3b:78:e9:47:40"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)

            #floor4
            if 'AP112-R400' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP112-R400","floor":"04","macAddr":"a0:e0:af:22:6e:70"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP109-R404' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP109-R404","floor":"04","macAddr":"a0:3d:6f:31:b7:f0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP212-IDL' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP212-IDL","floor":"04","macAddr":"a0:3d:6f:31:b7:d0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP111-R405' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP111-R405","floor":"04","macAddr":"a0:e0:af:95:9c:40"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)
            if 'AP215-R409'in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP215-R409","floor":"04","macAddr":"70:10:5c:b1:a4:d0"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                time.sleep(1)

        except EOFError:
            running = False
    output.close()

if __name__ == '__main__':
    main()
