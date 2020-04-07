from influxdb import InfluxDBClient

# host = 'localhost'
# port = 8086
# username = 'sabaszx'
# password = 'admin'
# dbName = 'snmptrapd'

host = 'localhost'
port = 8086
username = 'root'
password = 'root'
dbName = 'test'

dbClient = InfluxDBClient(host,port,username,password,dbName, ssl=False, verify_ssl=False)
dbClient.switch_database('trapEvent')

def countUser(topic,username,ssid,floor,receive):
    json_body = [{
                "measurement": str(topic),
                "tags": {
                    "username":str(username),
                    "ssid": str(ssid),
                    "apname":str(apname)},
                "fields": {
                    "value": receive}
                    }
                ]
    print(json_body)