from influxdb import InfluxDBClient
#edit later
json_body = [
    {
        "measurement": "floor_01",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]

client = InfluxDBClient('localhost',8086,'sabaszx','admin','snmptrapd')
