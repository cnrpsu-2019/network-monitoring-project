#!/usr/bin/python
import sys
import yaml
from influxdb import InfluxDBClient

def get_all_traps_influx_datapoint(config, trap):
    pass

# Read config file
config_file = open('./config.yaml', 'r')
config = yaml.load(config_file, yaml.SafeLoader)

lines = sys.stdin.readlines()

# Parsing input from snmptrapd
# parsing DNS name and IP
trap = {}
trap['host_dns'] = lines[0].strip()
socket = lines[1]
trap['host_ip'] = socket[socket.find('[') + 1:socket.find(']')]

# parsing SNMP stuff
trap['oid'] = None
trap['sysuptime'] = None
trap['varbinds'] = []
trap['varbinds_dict'] = {}

for line in lines[2:]:
    if trap['sysuptime'] is None:
        if "sysUpTime" in line:
            trap['sysuptime'] = line.split(" ")[1].strip()
            continue
    if trap['oid'] is None:
        if "snmpTrapOID" in line:
            varbind = line.strip().split(" ", 1)
            trap['varbinds_dict'][varbind[0]] = varbind[1]
            trap['oid'] = varbind[1].strip()
#            logger.debug("OID: %s" % trap['oid'])
            continue
    trap['varbinds'].append(line.strip().replace(" ", "="))
    varbind = line.strip().split(" ", 1)
    trap['varbinds_dict'][varbind[0]] = varbind[1]
datapoints = []

# processing for each type of traps according to the mappings configuration
cfg_mappings = config.get('mappings', None)
if cfg_mappings is not None:
    mapping = cfg_mappings.get(trap['oid'], None)
    if mapping is not None:
        oid_datapoint = {}
        oid_datapoint['measurement'] = mapping['measurement']
        oid_datapoint['tags'] = {}
        oid_datapoint['tags'].update({ config['all']['tags'].get('host_dns', 'host_dns'): trap['host_dns'] })
        oid_datapoint['tags'].update({ config['all']['tags'].get('host_ip', 'host_ip'): trap['host_ip'] })
        oid_datapoint['fields'] = {}
        for varbind in trap['varbinds_dict'].keys():
            for element in mapping['tags']:
                if element in varbind:
                    oid_datapoint['tags'].update({ element : trap['varbinds_dict'][varbind] })
            for element in mapping['fields']:
                if element in varbind:
                    oid_datapoint['fields'].update({ element: trap['varbinds_dict'][varbind] })

# export to influxdb
if datapoints != [] and config.get('influxdb', None) is not None:
    dbclients = []
    for server in config['influxdb'].get('server', []):
        dbclient = InfluxDBClient(host=server['ip'], port=server['port'], username=server['user'], password=server['pass'], database=server['db'])
        dbclients.append(dbclient)
    if dbclients != []:
        for dbclient in dbclients:
            dbclient.write_points(datapoints)

