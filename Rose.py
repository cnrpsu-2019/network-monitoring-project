from influxdb import InfluxDBClient
import Secret
# import Extract


dbClient = InfluxDBClient(Secret.host,Secret.port,Secret.username,Secret.password,Secret.dbName, ssl=False, verify_ssl=False)
dbClient.switch_database(Secret.dbName)

# class Rose(self,mac_address,ip_address,ap_name,ssid,username):
    
#     def __init__(self):    
#         self.mac_address = mac_address 
#         self.ip_address = ip_address 
#         self.ap_name = ap_name 
#         self.ssid = ssid  
#         self.username = username 

def send_to_db(self,mac_address,ip_address,ap_name,ssid,username):
    
    tosend_body = [{
        "measurement": 'no_of_clients',
        "tags": {
            "type": 'active_users',
        },
        "fields": {
            "mac_address":mac_address,
            "ip_address":ip_address,
            "ap_name":ap_name, #this is how we identify floor
            "wlan_ssid":ssid,
            "username":username}
            }
        ]                
    dbClient.write_points(tosend_body)
