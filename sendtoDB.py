import yaml
import sys
import datetime
import exp
import string

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
read = open('/home/bass/receive/' + fileName, 'r')

line = read.read()
print(line)

# Read config file
config_file = open('/home/bass/config.yaml', 'r')
config = yaml.load(config_file, yaml.SafeLoader)
print('yaml file loaded')

trap = {}
trap['event'] = lines[0].strip()
socket = lines[1]
trap['event'] = socket[socket.find('Event') + 1:socket.find('Event')]

print(str(trap['event']))
