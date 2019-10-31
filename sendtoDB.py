from influxdb import InfluxDBClient
#edit later
client = InfluxDBClient('localhost',8086,'sabaszx','admin','snmptrapd')
client.switch_database('snmptrapd')

