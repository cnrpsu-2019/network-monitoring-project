import datetime
now = datetime.datetime.now()
strnow = now.strftime("%X") #current time

json_body_StationDeauthenticate = [
        {
            "measurement": "StationDeauthenticate",
            "tags": {
                "UserIpAddress": "",
                "StationAPMacAddr": ""
            },
            "time": strnow,
            "fields": {
                "APName": ""
            }
        }
    ]

json_body_StationDisassociate = [
        {
            "measurement": "StationDisassociate",
            "tags": {
                "UserIpAddress": "",
                "StationAPMacAddr": ""
            },
            "time": strnow,
            "fields": {
                "APName": ""
            }
        }
    ]

json_body_StationAsssociate = [
        {
            "measurement": "StationDeauthenticate",
            "tags": {
                "UserIpAddress": "",
                "StationAPMacAddr": ""
            },
            "time": strnow,
            "fields": {
                "APName": ""
            }
        }
    ]

json_body_ClientMovedToRunState = [
        {
            "measurement": "ClientMovedToRunState",
            "tags": {
                "ClientIPAddress": "",
                "ApMacAddress": ""
            },
            "time": strnow,
            "fields": {
                "ApName": "",
                "ClientSSID": ""
            }
        }
    ]

json_body_ClientSessionTrap = [
        {
            "measurement": "ClientSessionTrap",
            "tags": {
                "ClientByIpAddress": "",
                "ApMacAddress": ""
            },
            "time": strnow,
            "fields": {
                "ApName": "",
                "ClientSSID": ""
            }
        }
    ]

json_body_ApRogueDetected = [
        {
            "measurement": "ApRogueDetected",
            "tags": {
                "ApSysMacAddress": "",
                "ApMacAddress": ""
            },
            "time": strnow,
            "fields": {
                "ApName": "",
                "ApRSSI": "",
                "ApRuleName": ""
            }
        }
    ]

json_body_RogueClientDetected = [
        {
            "measurement": "RogueClientDetected",
            "tags": {
                "ClientMacAddress": "",
                "ApMacAddress": ""
            },
            "time": strnow,
            "fields": {
                "RogueClientTotalDetectingAPs": ""
            }
        }
    ]

json_body_RogueAPRemoved = [
        {
            "measurement": "RogueAPRemoved",
            "tags": {
                "RogueAPMacAddress": "",
                "RogueAPRadioType": ""
            },
            "time": strnow,
            "fields": {
                "RogueAPName": ""
            }
        }
    ]