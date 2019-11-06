import yaml
import sys
import datetime
import exp

def get_all_traps_influx_datapoint(config, trap):
    varbinds = ", ".join(trap['description'])
    datapoint = {
        "measurement" : config['all']['measurement'],
        "tags": {
            config['all']['tags'].get('ap', 'ap'): trap['ap'],
            config['all']['tags'].get('event', 'event'): trap['event'],
            config['all']['tags'].get('mac_addr', 'mac_addr'): trap['mac_addr']
        },
        "fields" : {
            "description" : varbinds
        }
    }
    return datapoint

running = True
now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"
read = open('/home/bass/receive/' + fileName, 'r+')

line = read.readlines()

# parsing SNMP stuff
trap = {}
trap['mac_addr'] = None
trap['sysuptime'] = None
trap['description'] = []
trap['description_dict'] = {}
for line in line[2:]:
    if trap['sysuptime'] is None:
        if "sysUpTime" in line:
            trap['sysuptime'] = line.split(" ")[1].strip()
            continue
    if trap['description'] is None:
        if "snmpTrapOID" in line:
            varbind = line.strip().split(" ", 1)
            trap['description_dict'][varbind[0]] = varbind[1]
            trap['description'] = varbind[1].strip()
            continue
    trap['description'].append(line.strip().replace(" ", "="))
    varbind = line.strip().split(" ", 1)
    trap['description'][varbind[0]] = varbind[1]
