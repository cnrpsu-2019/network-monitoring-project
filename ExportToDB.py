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
