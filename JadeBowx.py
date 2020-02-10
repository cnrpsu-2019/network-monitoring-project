from influxdb import InfluxDBClient
dbClient = InfluxDBClient('localhost', 8086, 'sabaszx', 'admin', 'trapEvent', ssl=False, verdefy_ssl=False)
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
                    "SSIDName": "PSU Wdefi 802.1x",
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
                    "SSIDName": "PSU Wdefi 5Ghz",
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
def countCoeWdefi():
            json_body = [{
                "measurement": "ssid_count",
                "tags": {
                    "SSIDName": "CoEWdefi",
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
#floor 01
def AP3_46_R010_146()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP3-46-R010-146","floor":"01","macAddr":"bc:16:f5:98:8:0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP218_FL01_E()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP218-FL01-E","floor":"01","macAddr":"24:fb:65:65:9a:4f"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP217_FL01_W() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP217-FL01-W","floor":"01","macAddr":"68:3b:78:e1:94:20"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP204_R100()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP204-R100","floor":"01","macAddr":"f4:4e:5:a2:a1:d0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP216_R101()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP216-R101","floor":"01","macAddr":"dc:8c:37:4c:2e:e0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP211_Shop() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP211-Shop","floor":"01","macAddr":"f4:4e:5:b5:24:b0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)

#floor 02
def AP2_7_R020_153() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP2-7-R020-153","floor":"02","macAddr":"88:1d:fc:a:f1:20"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP2_8_R020_154() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP2-8-R020-154","floor":"02","macAddr":"88:1d:fc:6:3f:b0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP213_R202() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP213-R202","floor":"02","macAddr":"70:10:5c:b1:a4:d0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP214_R203() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP214-R203","floor":"02","macAddr":"a0:e0:af:3d:c7:80"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP206_R204() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP206-R204","floor":"02","macAddr":"f4:4e:5:a2:a1:10"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP205_R207() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP205-R207","floor":"02","macAddr":"f4:4e:5:b5:65:90"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)

#floor03
def AP108_R300() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP108-R300","floor":"03","macAddr":"a0:3d:6f:31:b7:e0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP209_R302_1() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP209-R302-1","floor":"03","macAddr":"f4:4e:5:df:4e:f0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP210_R302_2() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP210-R302-2","floor":"03","macAddr":"f4:4e:5:db:f0:40"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP110_R311() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP110-R311","floor":"03","macAddr":"70:10:5c:b1:9e:d0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP221_R301A() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP221-R301A","floor":"03","macAddr":"68:3b:78:e1:93:80"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP220_R301B()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP220-R301B","floor":"03","macAddr":"68:3b:78:e1:93:0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP219_R303()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP219-R303","floor":"03","macAddr":"68:3b:78:e9:47:40"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
    
#floor4
def AP112_R400() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP112-R400","floor":"04","macAddr":"a0:e0:af:22:6e:70"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP109_R404()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP109-R404","floor":"04","macAddr":"a0:3d:6f:31:b7:f0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP212_IDL() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP212-IDL","floor":"04","macAddr":"a0:3d:6f:31:b7:d0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP111_R405() 
    json_body = [{"measurement":"ap_event","tags":{"name":"AP111-R405","floor":"04","macAddr":"a0:e0:af:95:9c:40"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)
def AP215_R409()
    json_body = [{"measurement":"ap_event","tags":{"name":"AP215-R409","floor":"04","macAddr":"70:10:5c:b1:a4:d0"},"fields":{"item": 1}}]
    dbClient.write_points(json_body)