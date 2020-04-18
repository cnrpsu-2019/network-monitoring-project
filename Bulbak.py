from influxdb import InfluxDBClient
import Secret

#build class
class Bulbak(self):
    #influxdb for local tests
    # host = 'localhost'
    # port = 8086
    # username = 'root'
    # password = 'root'
    # dbName = 'test'
    
    dbClient = InfluxDBClient(Secret.host,Secret.port,Secret.username,Secret.password,Secret.dbName, ssl=False, verify_ssl=False)
    dbClient.switch_database(Secret.dbName)

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

    def count_client(self):
        print(json_body)
