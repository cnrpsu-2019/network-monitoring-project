#!/usr/bin/python3

import sys
<<<<<<< HEAD
import Filterx

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
 
    while running:
        try:
            read = raw_input()
            filtered = read.replace("<UNKNOWN>","" )
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)
        
            wrongtypeRemove = replaceMultiple(showDate, Filterx.wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"
            #outstr - write log files into local server
            outstr  = weirdRemove.translate(None, bad_chars)
            sameAp = outstr.replace("ApName", "APName")
            result = replaceMultiple(sameAp,Filterx.bad_list,' ')
            output.write(result+ '\n')
            
           
        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
=======
import logging
import logging.handlers
import yaml
import copy
from influxdb import InfluxDBClient

def get_all_traps_influx_datapoint(config, trap):
    varbinds = ", ".join(trap['varbinds'])
    datapoint = {
        "measurement" : config['all']['measurement'],
        "tags": {
            config['all']['tags'].get('event', 'event'): trap['event'],
            config['all']['tags'].get('apname', 'apname'): trap['apname']
        },
        "fields" : {
            "varbinds" : varbinds
        }
    }
    return datapoint


# logging part
logger = logging.getLogger("snmptrapd-influxdb-exporter")
logger.setLevel(logging.DEBUG)

f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

syslog_handler = logging.handlers.SysLogHandler()
syslog_handler.setFormatter(f_format)
logger.addHandler(syslog_handler)

#f_handler = logging.FileHandler('/var/log/snmptrapd-influxdb-exporter.log')
#f_handler.setLevel(logging.DEBUG)
#f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#f_handler.setFormatter(f_format)
#logger.addHandler(f_handler)

out_handler = logging.StreamHandler(sys.stdout)
out_handler.setFormatter(f_format)
logger.addHandler(out_handler)

# Read config file
config_file = open('/home/bass/config.yaml', 'r')
config = yaml.load(config_file, yaml.SafeLoader)

# adjust logging level from the config file 
numeric_level = getattr(logging, config.get("logging", "DEBUG").upper(), 10)
logger.setLevel(numeric_level)

logger.info("config: %s" % str(config))

lines = sys.stdin.readlines()

# Parsing input from snmptrapd

trap = {}
trap['event'] = lines[0].strip()
socket = lines[1]
trap['apname'] = socket[socket.find('[') + 1:socket.find(']')]
logger.debug("event: %s" % str(trap['event']))
logger.debug("apname: %s" % str(trap['apname']))

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
            logger.debug("OID: %s" % trap['oid'])
            continue
    trap['varbinds'].append(line.strip().replace(" ", "="))
    varbind = line.strip().split(" ", 1)
    trap['varbinds_dict'][varbind[0]] = varbind[1]
    logger.debug(line.strip())

logger.info("received trap: %s" % str(trap))

# preparing data for influxdb
# putting combined mesrsage into the one measurement for all taps
datapoints = []
if config.get('all', None) is not None:
    if config['all'].get('measurement', None) is not None:
        if config['all'].get('permit', None) is not None:
            for rule in config['all']['permit']:
                if rule in trap['oid']:
                    logger.debug("permit rule %s matching oid %s" % (rule, trap['oid']))
                    datapoints.append(get_all_traps_influx_datapoint(config, trap))
        elif config['all'].get('deny', None) is not None:
            for rule in config['all']['deny']:
                if rule in trap['oid']:
                    logger.debug("deny rule %s matching oid %s" % (rule, trap['oid']))
                    break
            else:
                # if deny rule is not match
                datapoints.append(get_all_traps_influx_datapoint(config, trap))
        else:
            # no permit or deny rules, so permit everything
            datapoints.append(get_all_traps_influx_datapoint(config, trap))
    else:
        logger.warning("configuration file missing 'all/measurement' part")
else:
    logger.warning("configuration file missing 'all' part")

# processing for each type of traps according to the mappings configuration
cfg_mappings = config.get('mappings', None)
if cfg_mappings is not None:
    mapping = cfg_mappings.get(trap['oid'], None)
    if mapping is not None:
        oid_datapoint = {}
        oid_datapoint['measurement'] = mapping['measurement']
        oid_datapoint['tags'] = {}
        oid_datapoint['tags'].update({ config['all']['tags'].get('event', 'event'): trap['event'] })
        oid_datapoint['tags'].update({ config['all']['tags'].get('apname', 'apname'): trap['apname'] })
        oid_datapoint['fields'] = {}
        for varbind in trap['varbinds_dict'].keys():
            for element in mapping['tags']:
                if element in varbind:
                    oid_datapoint['tags'].update({ element : trap['varbinds_dict'][varbind] })
            for element in mapping['fields']:
                if element in varbind:
                    oid_datapoint['fields'].update({ element: trap['varbinds_dict'][varbind] })
        logger.debug("add oid_datapoint %s" % (oid_datapoint))
        datapoints.append(copy.deepcopy(oid_datapoint))
    else:
        logger.debug("configuraton no mappings for trap %s" % (trap['oid']))
else:
    logger.info("configuration file missing 'mappings' part")

# export to influxdb
if datapoints != [] and config.get('influxdb', None) is not None:
    dbclients = []
    for server in config['influxdb'].get('server', []):
        dbclient = InfluxDBClient(host=server['ip'], port=server['port'], username=server['user'], password=server['pass'], database=server['db'])
        dbclients.append(dbclient)
    if dbclients != []:
        for dbclient in dbclients:
            dbclient.write_points(datapoints)

>>>>>>> 1b7698fc5d7a870e77fd46de001f741bbfac9aa7
