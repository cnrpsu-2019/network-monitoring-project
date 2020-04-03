from influxdb import InfluxDBClient

dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verify_ssl=False)
dbClient.switch_database('trapEvent')

#count number
def countAIS(receive):
    json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "AIS Smart Login",
                "type": "known_ssid"},
                "fields": {
                    "item": receive}
                    }
                ]
    dbClient.write_points(json_body)

def count802(receive):
        json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "PSU Wifi 802.1x",
                "type": "known_ssid"},
                "fields": {
                    "item": receive}
                    }
                ]
        dbClient.write_points(json_body)

def countPSU5Ghz(receive):
            json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "PSU Wifi 5Ghz",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ] 
            dbClient.write_points(json_body)

def countTruemove(receive):
            json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "TrueMove H",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)

def countCoeIot(receive):
            json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "CoEIIoT",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)

def countCoeWifi(receive):
            json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "CoEWifi",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)

def countOthers(receive):
        json_body = [{
                "measurement": "countSSID",
                "tags": {
                    "SSIDName": "Unknown",
                "type": "unknown_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
        dbClient.write_points(json_body)

def countClient(receive):
            json_body = [{
                "measurement": "number_of_client",
                "tags": {
                    "SSIDName": "number",
                "type": "number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)