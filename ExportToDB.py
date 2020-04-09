from influxdb import InfluxDBClient

host = 'localhost'
port = 8086
username = 'sabaszx'
password = 'admin'
dbName = 'snmptrapd'

# host = 'localhost'
# port = 8086
# username = 'root'
# password = 'root'
# dbName = 'test'

dbClient = InfluxDBClient(host,port,username,password,dbName, ssl=False, verify_ssl=False)
dbClient.switch_database('snmptrapd')
# def countUser(topic='Unknown',username='Unnown',ssid='Unnown',floor='Unnown',apname='Unnown',value=0):

def countUser(value):
    json_body = [{
                "measurement": 'user_count',
                "tags": {
                    "type": 'user_associated',
                },
                "fields": {
                    "value": int(value)}
                    }
                ]
    print(json_body)
    dbClient.write_points(json_body)

def count_ssid(ssid_name,value):
    json_body = [{
                "measurement": 'ssid_count',
                "tags": {
                    "name": str(ssid_name),
                },
                "fields": {
                    "value": int(value)}
                    }
                ]
    print(json_body)
    dbClient.write_points(json_body)
