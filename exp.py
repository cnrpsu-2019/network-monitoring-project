from influxdb import InfluxDBClient
import time
import datetime
import Filterx
import JadeBowx
import re

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

    dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verify_ssl=False)
    dbClient.create_database('trapEvent')

    #print('Database created, go check in shell')
    dbClient.switch_database('trapEvent')

    while running:
        try:
            input = raw_input()
            #filter weird string sction
            filtered = input.replace("<UNKNOWN>","" )
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)

            #filter out lookoup from Filterx  module 
            wrongtypeRemove = replaceMultiple(showDate, Filterx.wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"

            #outstr - write log files into local server
            outstr  = weirdRemove.translate(None, bad_chars)
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

            PatternDeauth = ['StationDeauthenticate', 'Disassociate','Deauthenticate']
            for patterns in PatternDeauth:
                if re.search(patterns, line):
                    JadeBowx.countUserDauth()

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

        except EOFError:
            running = False
    output.close()

if __name__ == '__main__':
    main()
