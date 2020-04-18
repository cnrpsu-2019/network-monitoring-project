from influxdb import InfluxDBClient
import Secret

#influxdb for local tests
host = 'localhost'
port = 8086
username = 'root'
password = 'root'
dbName = 'test'

#test section
#dbClient = InfluxDBClient(host,port,username,password,dbName, ssl=False, verify_ssl=False)
#dbClient.switch_database('test')
#
dbClient = InfluxDBClient(Secret.host,Secret.port,Secret.username,Secret.password,Secret.dbName, ssl=False, verify_ssl=False)
dbClient.switch_database(Secret.dbName)
# dbClient = InfluxDBClient(host,port,username,password,dbName, ssl=False, verify_ssl=False)
# dbClient.switch_database('test')

dbClient = InfluxDBClient(Secret.host,Secret.port,Secret.username,Secret.password,Secret.dbName, ssl=False, verify_ssl=False)
dbClient.switch_database(Secret.dbName)

#func prototype
def count_client(self):
    json_body = [{
                "measurement": 'no_of_clients',
                "tags": {
                    "type": 'active_users',
                },
                "fields": {
                    "mac_address": self,
                    "ip_address": self,
                    "ap_name": self, #this is how we identify floor
                    "wlan_ssid":self,
                    "username":self}
                    }
                ]
    print(json_body)

def funcname(parameter_list):
    pass
    
#it works 
def uptime_instance(date_string):
    json_body = [{
                "measurement": 'uptime_instance',
                "tags": {
                    "name": 'uptime_instance',
                },
                "fields": {
                    "value": str(date_string)}
                    }
                ]
    print(json_body)
    # dbClient.write_points(json_body)
