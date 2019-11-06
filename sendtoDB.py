import yaml
import sys
import datetime
import exp

def get_all_traps_influx_datapoint(config, trap):
    varbinds = ", ".join(trap['varbinds'])
    datapoint = {
        "measurement" : config['all']['measurement'],
        "tags": {
            config['all']['tags'].get('host_dns', 'host_dns'): trap['host_dns'],
            config['all']['tags'].get('host_ip', 'host_ip'): trap['host_ip'],
            config['all']['tags'].get('oid', 'oid'): trap['oid']
        },
        "fields" : {
            "varbinds" : varbinds
        }
    }
    return datapoint

running = True
now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"
read = open('/home/bass/receive/' + fileName, 'ar+')

line = read.readlines()