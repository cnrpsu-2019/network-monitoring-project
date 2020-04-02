import time
import datetime
import Filterx
import JadeBowx
import re
import subprocess
import collections

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y") #day-month-year
path = '/home/bass/receive/'
fileName = "trapd-" + fileDate + ".log"

#lists of ap mac address each floor
floor01_mac_list = ['bc:16:f5:98:8:0','68:3b:78:e1:8e:c0','68:3b:78:e1:94:20','f4:4e:5:a2:a1:d0',
                    'dc:8c:37:4c:2e:e0','f4:4e:5:b5:24:b0']

floor02_mac_list = ['88:1d:fc:a:f1:20','88:1d:fc:6:3f:b0','70:10:5c:b1:a4:d0','a0:e0:af:3d:c7:80',
                   'f4:4e:5:a2:a1:10','f4:4e:5:b5:65:90']

floor03_mac_list = ['a0:3d:6f:31:b7:e0','f4:4e:5:df:4e:f0','f4:4e:5:db:f0:40','70:10:5c:b1:9e:d0',
                    '68:3b:78:e1:93:0','68:3b:78:e1:93:80','68:3b:78:e9:47:40']

floor04_mac_list = ['a0:e0:af:22:6e:70','a0:3d:6f:31:b7:f0','a0:3d:6f:31:b7:d0','a0:e0:af:95:9c:40',
                   'a0:3d:6f:dd:2d:70']

#all ap mac addresses in building

buildingMacList = floor01_mac_list + floor02_mac_list + floor03_mac_list + floor04_mac_list

def listDuplicates(seq): 
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in seq if x in seen or seen_add(x) )
    # turn the set into a list (as requested)
    return list( seen_twice )

def findDuplicates(seq):
    result = ([item for item, count in collections.Counter(seq).items() if count > 1])
    return result 

def compileMacPattern(receive):
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    resultMac = re.findall(pattern, receive) #now there's only list of mac addresses
    return str(resultMac)

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return  mainString

def readAndInsertSSID():
    #extract specific line
    output = ''
    with open(path + fileName,'r') as f:
        for line in f:
            line = line.rstrip()
            if re.search('SSID', line):
                output += line.replace('SSID ','')
    f.close()
   
    #overAll ssids
    overall = int(output.count('TrueMove H')) + int(output.count('CoEWiFi')) + int(output.count('PSU WiFi 802.1x')) + int(output.count('PSU WiFi 5GHz')) + int(output.count('AIS SMART Login')) + int(output.count('CoEIoT')) 
    
    perTrue = 0
    perCoE  = 0
    perPsu  = 0
    per5G   = 0
    perAis  = 0
    perIot  = 0
    perOthers = 0

    #show percentage
    try:
        perTrue = (int(output.count('TrueMove H')) / overall) * 100
        perCoE = (int(output.count('CoEWiFi')) / overall) * 100
        perPsu = (int(output.count('PSU WiFi 802.1x')) / overall) * 100
        per5G = (int(output.count('PSU WiFi 5GHz')) / overall) * 100
        perAis = (int(output.count('AIS SMART Login')) / overall) * 100
        perIot = (int(output.count('CoEIoT')) / overall) * 100
        percenSum = perTrue + perCoE + perPsu + perAis + perIot + per5G
        perOthers = 100 - percenSum

    except ZeroDivisionError:
        overall = 0 
        
    #insert into database
    JadeBowx.count802(int(output.count('PSU WiFi 802.1x')))
    JadeBowx.countCoeIot(int(output.count('CoEIoT')))
    JadeBowx.countCoeWifi(int(output.count('CoEWiFi')))
    JadeBowx.countPSU5Ghz(int(output.count('PSU WiFi 5GHz')))
    JadeBowx.countTruemove(int(output.count('TrueMove H')))
    JadeBowx.countAIS(int(output.count('AIS SMART Login')))

    #insert percentage to present pie graph
    JadeBowx.percentage802(perPsu)
    JadeBowx.percentageCoeIot(perIot)
    JadeBowx.percentageCoeWifi(perCoE)
    JadeBowx.percentagePSU5Ghz(per5G)
    JadeBowx.percentageTruemove(perTrue)
    JadeBowx.percentageAIS(perAis)
    JadeBowx.percentageOthers(perOthers)

#read and insert
def readAndInsert():
    with open(path + fileName,'r') as readTest:
        #delete specific lines (session ID):
        macPattern = compileMacPattern(str(readTest)) #this return all mac addresses
        duplicateMac = listDuplicates(macPattern) # return dupliccated mac addresses (include ap)
        
        #return number of client addres
        clientMac = list(set(duplicateMac) - set(buildingMacList))
        toInsert = str(len(clientMac)) #result to be insert
        JadeBowx.countClient(toInsert)

    readTest.close

def main():
   
    output = open( path + fileName, 'a') #write into local server

    while True:
        try:
            input_raw = input()
            #filter weird string sction
            subprocess.call(['sed','-i','/.*SessionID.*/d',path + fileName])
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

        except EOFError:
            break
        finally:
            output.close
            
if __name__ == '__main__':
    main()
    readAndInsert()
    readAndInsertSSID()