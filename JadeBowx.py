from influxdb import InfluxDBClient
dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verify_ssl=False)
dbClient.switch_database('trapEvent')

def countUserAssociate():
        json_body = [{
                    "measurement": "client_user",
                    "tags": {
                        "user": "user_associate",
                    "type": "associate"},
                    "fields": {
                        "item": 1}
                        }
                    ]
        dbClient.write_points(json_body)
def countUserDauth():
        json_body = [{
                "measurement": "client_user",
                "tags": {
                    "user": "user_deauthenticate",
                "type": "deauthenticate"},
                "fields": {
                    "item": 1}
                    }
                ]
        dbClient.write_points(json_body)

def count802():
        json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "PSU Wifi 802.1x",
                "type": "known_ssid"},
                "fields": {
                    "item": 1}
                    }
                ]
        dbClient.write_points(json_body)
def countPSU5Ghz():
            json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "PSU Wifi 5Ghz",
                "type": "known_ssid"},
                "fields": {
                    "item": 1}
                    }
                ] 
            dbClient.write_points(json_body)
def countTruemove():
            json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "TrueMove H",
                "type": "known_ssid"},
                "fields": {
                    "item": 1}
                    }
                ]
            dbClient.write_points(json_body)
def countCoeIot():
            json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "CoEIIoT",
                "type": "known_ssid"},
                "fields": {
                    "item": 1}
                    }
                ]
            dbClient.write_points(json_body)
def countCoeWifi():
            json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "CoEWiFi",
                "type": "known_ssid"},
                "fields": {
                    "item": 1}
                    }
                ]
            dbClient.write_points(json_body)
def countRogue():
            json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "unknown",
                "type": "others"},
                "fields": {
                    "item": 1}
                    }
                ]
            dbClient.write_points(json_body)
