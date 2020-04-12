# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]

# %%
import createFiles
import Extract
import ExportToDB
import MacList
import collections
import re
import filterString

def seek_and_destroy():
    # seek ssid name by open files and count
    #psu wifi
    psu_802 = Extract.extractSpecific(createFiles.realFile,'SSID PSU WiFi 802.1x').replace('SSID',' ').count('PSU WiFi 802.1x')
    # psu wifi 5GHz
    psu_5g = Extract.extractSpecific(createFiles.realFile,'SSID PSU WiFi 5GHz').replace('SSID',' ').count('PSU WiFi 5GHz')
    # ais smart login
    ais_smart_login = Extract.extractSpecific(createFiles.realFile,'SSID AIS SMART Login').replace('SSID',' ').count('AIS SMART Login')
    # truemove h
    truemove_h = Extract.extractSpecific(createFiles.realFile,'SSID TrueMove H').replace('SSID',' ').count('TrueMove H')
    # coe wifi
    coe_wifi = Extract.extractSpecific(createFiles.realFile,'SSID CoEWiFi').replace('SSID',' ').count('CoEWiFi')
    # coe iot
    coe_iot = Extract.extractSpecific(createFiles.realFile,'SSID CoEIoT').replace('SSID',' ').count('CoEIoT')
    # whole username
    user_name = Extract.extractSpecific(createFiles.realFile,'Username').replace('Username','').split()
    # unique username and reduce error
    unique_name = int((len(list(set(user_name)))) * 0.85)

    #uptime instance
    uptime = Extract.extractSpecific(createFiles.realFile,'UpTimeInstance').replace('UpTimeInstance','')
    pattern = re.compile(r'(?:[0-9]:?){6}')
    uptime_non_zero = re.findall(pattern,uptime) #filter 0 out
    #pick last element in list
    lastet_uptime = uptime_non_zero[-1]

    #rogue ap detected
    rougue_ap_detected = Extract.extractSpecific(createFiles.sampleFile,'Event ApRogueDetected').replace('Event','').count('ApRogueDetected')

    #export to db part
    ExportToDB.countUser(unique_name)
    ExportToDB.count_ssid(MacList.ssidname_list[0],coe_iot)
    ExportToDB.count_ssid(MacList.ssidname_list[1],coe_wifi)
    ExportToDB.count_ssid(MacList.ssidname_list[2],truemove_h)
    ExportToDB.count_ssid(MacList.ssidname_list[3],ais_smart_login)
    ExportToDB.count_ssid(MacList.ssidname_list[4],psu_5g)
    ExportToDB.count_ssid(MacList.ssidname_list[5],psu_802)
    ExportToDB.uptime_instance(lastet_uptime)

    ExportToDB.countSoething('rogue_ap_detected','rogue',rougue_ap_detected)

