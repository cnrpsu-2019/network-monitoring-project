from influxdb import InfluxDBClient
import JadeBowx
import datetime
import Filterx
import time

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"    
output = open('/home/bass/receive/' + fileName, 'a')

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return  mainString
def writeToLocal():
    while True:
        try:
            rawInput = raw_input()
            filtered = rawInput.replace("<UNKNOWN>","")
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)
            wrongtypeRemove = replaceMultiple(showDate, Filterx.wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"
            #outstr - write log files into local server
            outstr = weirdRemove.translate(None, bad_chars)
            result = replaceMultiple(outstr,Filterx.bad_list,' ')
            #write to local
            output.write(result + '\n')
        except EOFError:
            break
    output.close()
    
def sendToDB():
    while True:
        JadeBowx.readLog()
        JadeBowx.prepareDB('sabaszx','admin')
        if 'UserName' or 'StationUsername' in line:
            JadeBowx.countUser() 
if __name__ == '__main__':
    writeToLocal()
