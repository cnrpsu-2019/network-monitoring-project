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
read = open('/home/bass/receive/' + fileName, 'r')

line = read.readlines()

# Read config file
config_file = open('/home/bass/config.yaml', 'r')
config = yaml.load(config_file, yaml.SafeLoader)

# parsing SNMP stuff
trap = {}
trap['mac_addr'] = None
trap['ap'] = None
trap['description'] = []
trap['description_dict'] = {}
for line in line[2:]:
    if trap['ap'] is None:
        if "APName" in line:
            trap['ap'] = line.split(" ")[1].strip()
            continue
    if trap['description'] is None:
        if "ClientUsername" in line:
            varbind = line.strip().split(" ", 1)
            trap['description_dict'][varbind[0]] = varbind[1]
            trap['description'] = varbind[1].strip()
            continue
    trap['description'].append(line.strip().replace(" ", "="))
    varbind = line.strip().split(" ", 1)
    trap['description'][varbind[0]] = varbind[1]

# preparing data for influxdb
# putting combined mesrsage into the one measurement for all taps
datapoints = []
if config.get('all', None) is not None:
    if config['all'].get('measurement', None) is not None:
        if config['all'].get('permit', None) is not None:
            for rule in config['all']['permit']:
                if rule in trap['oid']:
                    datapoints.append(get_all_traps_influx_datapoint(config, trap))
        elif config['all'].get('deny', None) is not None:
            for rule in config['all']['deny']:
                if rule in trap['oid']:
                    break
            else:
                # if deny rule is not match
                datapoints.append(get_all_traps_influx_datapoint(config, trap))
        else:
            # no permit or deny rules, so permit everything
            datapoints.append(get_all_traps_influx_datapoint(config, trap))

if datapoints != [] and config.get('influxdb', None) is not None:
    dbclients = []
    for server in config['influxdb'].get('server', []):
        dbclient = InfluxDBClient(host=server['ip'], port=server['port'], username=server['user'], password=server['pass'], database=server['db'])
        dbclients.append(dbclient)
    if dbclients != []:
        for dbclient in dbclients:
            dbclient.write_points(datapoints)