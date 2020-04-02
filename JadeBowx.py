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

def percentageAIS(receive):
    json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "AIS Smart Login",
                "type": "known_ssid"},
                "fields": {
                    "item": receive}
                    }
                ]
    dbClient.write_points(json_body)


def percentage802(receive):
        json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "PSU Wifi 802.1x",
                "type": "known_ssid"},
                "fields": {
                    "item": receive}
                    }
                ]
        dbClient.write_points(json_body)

def percentagePSU5Ghz(receive):
            json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "PSU Wifi 5Ghz",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ] 
            dbClient.write_points(json_body)

def percentageTruemove(receive):
            json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "TrueMove H",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)

def percentageCoeIot(receive):
            json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "CoEIIoT",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)

def percentageCoeWifi(receive):
            json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "CoEWifi",
                "type": "known_ssid_number"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)

def percentageOthers(receive):
            json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "unknown_number",
                "type": "others"},
                "fields": {
                    "item": receive}
                    }
                ]
            dbClient.write_points(json_body)
            
def percentageAIS(receive):
    json_body = [{
                "measurement": "ssid_percentage",
                "tags": {
                    "SSIDName": "AIS Smart Login",
                "type": "known_ssid"},
                "fields": {
                    "item": receive}
                    }
                ]
    dbClient.write_points(json_body)

def countAIS(receive):
    json_body = [{
                "measurement": "ssid_percentage",
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
                "measurement": "ssid_count",
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
                "measurement": "ssid_count",
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
                "measurement": "ssid_count",
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
                "measurement": "ssid_count",
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
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "CoEWifi",
                "type": "known_ssid_number"},
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
