import datetime
import re
import string
#import yaml
import sys
import Filterx
from influxdb import InfluxDBClient

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString

def get_all_traps_influx_datapoint(config, trap):
    varbinds = ", ".join(trap['varbinds'])
    datapoint = {
        "measurement" : config['all']['measurement'],
        "tags": {
            config['all']['tags'].get('ApName', 'ApName'): trap['ApName'],
            config['all']['tags'].get('SSID', 'SSID'): trap['SSID'],
        },
        "fields" : {
            "varbinds" : varbinds
        }
    }
    return datapoint

 # Read config file
 #   config_file = open('./config.yaml', 'r')
    #config = yaml.load(config_file, yaml.SafeLoader)

def main():
    running = True
    now = datetime.datetime.now()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/receive/' + fileName, 'a')

   
    
    while running:
        try:
            input = raw_input()
            filtered = input.replace("<UNKNOWN>","" )
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)
        
            wrongtypeRemove = replaceMultiple(showDate, Filterx.wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"
            #outstr
            outstr  = weirdRemove.translate(None, bad_chars)
            result = replaceMultiple(outstr,Filterx.bad_list,' ')
           
           
            output.write(result + '\n')
       
        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
