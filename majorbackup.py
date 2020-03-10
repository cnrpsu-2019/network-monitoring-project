from influxdb import InfluxDBClient
import time
import datetime
import Filterx
import JadeBowx
import re

#add macaddress to regcognize user

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
    now = datetime.datetime.now()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/receive/' + fileName, 'a') #write into local server
    readfile = open('/home/bass/receive/' + fileName, 'r') #read from local server that we wrote
    while True:
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

            #write to local serever
            output.write(result + '\n')

            #read files
            line = readfile.read()
            if not line:
                time.sleep(1)

            #associate users
            PatternAssociate = ['Associate', 'Sessiontrap','MovedToRunState','Username']
            for patterns in PatternAssociate:
                if re.search(patterns, line):
                    JadeBowx.countUserAssociate()
                    print('associated')
                    

            PatternDeauth = ['StationDeauthenticate', 'Disassociate','Deauthenticate']
            for patterns in PatternDeauth:
                if re.search(patterns, line):
                    JadeBowx.countUserDauth()
                     #sleep for 5 secs

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
                    

            for patterns in floor_02_list:
                if re.search(patterns, line):
                    JadeBowx.countFloor02()
                    print('floor2')
                    
                    
            for patterns in floor_03_list:
                if re.search(patterns, line):
                    JadeBowx.countFloor03()
                    print('floor3')
                    

            for patterns in floor_04_list:
                if re.search(patterns,line):
                    JadeBowx.countFloor04()
                    print('floor4')
                    
                        
            if 'CoEWiFi' in line:
                JadeBowx.countCoeWifi()
                print('CoE WiFi')
                

            if 'PSU WiFi 802.1x' in line:
                JadeBowx.count802()
                print('802.1x')
                

            if 'PSU WiFi 5GHz' in line:
                JadeBowx.countPSU5Ghz()
                print('PSU 5ghz')
                

            if 'TrueMove H' in line:
                JadeBowx.countTruemove()
                print('truemove')
            
            if  'CoEIoT' in line:
                JadeBowx.countCoeIot()
                print('coeiot')
            
            for patterns in rogue_list:
                if re.search(patterns, line):
                    JadeBowx.countRogue()
                    print('others')
            
            #Ap Event
            ##floor 01
            if 'AP3-46-R010-146' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP3-46-R010-146","floor":"01"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP218-FL01-E' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP218-FL01-E","floor":"01"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP217-FL01-W' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP217-FL01-W","floor":"01"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP204-R100' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP204-R100","floor":"01"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP216-R101' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP216-R101","floor":"01"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP211-Shop' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP211-Shop","floor":"01"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                

            #floor 02
            if 'AP2-7-R020-153' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP2-7-R020-153","floor":"02"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP2-8-R020-154' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP2-8-R020-154","floor":"02"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP213-R202' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP213-R202","floor":"02"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP214-R203' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP214-R203","floor":"02"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP206-R204' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP206-R204","floor":"02"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP205-R207' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP205-R207","floor":"02"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                

            #floor03
            if 'AP108-R300' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP108-R300","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP209-R302-1' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP209-R302-1","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP210-R302-2' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP210-R302-2","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP110-R311' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP110-R311","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP221-R301A' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP221-R301A","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP220-R301B' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP220-R301B","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP219-R303' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP219-R303","floor":"03"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                

            #floor4
            if 'AP112-R400' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP112-R400","floor":"04"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP109-R404' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP109-R404","floor":"04"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP212-IDL' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP212-IDL","floor":"04"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP111-R405' in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP111-R405","floor":"04"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                
            if 'AP215-R409'in line:
                json_body = [{"measurement":"ap_event","tags":{"name":"AP215-R409","floor":"04"},"fields":{"item": 1}}]
                dbClient.write_points(json_body)
                

        except EOFError:
            break

    output.close()

if __name__ == '__main__':
    main()
