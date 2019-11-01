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
            #lines = sys.stdin.readlines(result)

            #client = InfluxDBClient('localhost',8086,'sabaszx','admin','snmptrapd')

            trap['ApName'] = None
            trap['UptimeInstance'] = None
            trap['varbinds'] = []
            trap['varbinds_dict'] = {}
            for line in lines[2:]:
                if trap['UptimeInstance'] is None:
                    if "UptimeInstance" in line:
                        trap['UptimeInstance'] = line.split(" ")[1].strip()
                        continue
                if trap['oid'] is None:
                    if "snmpTrapOID" in line:
                        varbind = line.strip().split(" ", 1)
                        trap['varbinds_dict'][varbind[0]] = varbind[1]
                        trap['ApName'] = varbind[1].strip()
                        continue
                trap['varbinds'].append(line.strip().replace(" ", "="))
                varbind = line.strip().split(" ", 1)
                trap['varbinds_dict'][varbind[0]] = varbind[1]


            # preparing data for influxdb
            # putting combined mesrsage into the one measurement for all taps
            datapoints = []
            if config.get('all', None) is not None:
                if config['all'].get('measurement', None) is not None:
                    if config['all'].get('permit', None) is not None:
                        for rule in config['all']['permit']:
                            if rule in trap['ApName']:
                                datapoints.append(get_all_traps_influx_datapoint(config, trap))
                    elif config['all'].get('deny', None) is not None:
                        for rule in config['all']['deny']:
                            if rule in trap['ApName']:
                                break
                        else:
                            # if deny rule is not match
                            datapoints.append(get_all_traps_influx_datapoint(config, trap))
                    else:
                        # no permit or deny rules, so permit everything
                        datapoints.append(get_all_traps_influx_datapoint(config, trap))
            

            
            # export to influxdb
            if datapoints != [] and config.get('influxdb', None) is not None:
                dbclients = []
                for server in config['influxdb'].get('server', []):
                    dbclient = InfluxDBClient(host=server['172.30.232.250'], port=server['8086'], username=server['sabaszx'], password=server['admin'], database=server['snmptrapd'])
                    dbclients.append(dbclient)
                if dbclients != []:
                    for dbclient in dbclients:
                        dbclient.write_points(datapoints)
           
            output.write(result + '\n')
       
        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
