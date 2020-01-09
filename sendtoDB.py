import datetime
from influxdb import InfluxDBClient

def setData(host='172.30.232.250', port=8086):
    user = 'sabaszx'
    passwd = 'admin'
    dbname = 'trapEvent'
    json_body = [
            {
                "measurement":"ex",
                "tags":{
                    "tag1":"val1"
                    }
                "fields":{
                    "field1":"val1"
                    }
                }]
    client = InfluxDBClient(host, port, user, passwd, dbname)
    
