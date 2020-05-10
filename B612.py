import createFiles
import Extract
import ExportToDB
import MacList
import collections
import re

def uptime_instance():
    #uptime instance
    uptime = Extract.extractSpecific(createFiles.realFile,'UpTimeInstance').replace('UpTimeInstance','')
    pattern = re.compile(r'(?:[0-9]:?){6}')
    uptime_non_zero = re.findall(pattern,uptime) #filter 0 out
    #pick last element in list
    lastet_uptime = uptime_non_zero[-1]
    ExportToDB.uptime_instance(lastet_uptime)

def rogue_ssid_detected():
    # ApRogueMode
    rogue_detected = Extract.extractSpecific(createFiles.realFile,'ApRogueDetected').replace('ApRogueDetected','').split()[-1]
    rogue_mode = Extract.extractSpecific(createFiles.realFile,'ApRogueMode').replace('ApRogueMode','').split()[-1]
    rogue_apname_last = Extract.extractSpecific(createFiles.realFile,'APName').replace('APName','').split()[-1]
    rogue_ssid = Extract.extractSpecific(createFiles.realFile,'ApRogueApSsid').split('ApRogueApSsid')[-1]
    rogue_detected_ch = Extract.extractSpecific(createFiles.realFile,'ApRogueDetectedChannel').split('ApRogueDetectedChannel')[-1]
    rogue_mac_address = Extract.extractSpecific(createFiles.realFile,'ApRogueApMacAddress').split('ApRogueApMacAddress')[-1]
    rogue_rssi = Extract.extractSpecific(createFiles.realFile,'ApRSSI').split('ApRSSI')[-1]
    ExportToDB.ssid_rogue_detected(rogue_mode,rogue_ssid,rogue_apname_last,rogue_detected_ch,rogue_mac_address,rogue_rssi)

def activity_users():
    apname_last = Extract.extractSpecific(createFiles.realFile,'APName').replace('APName','').split()[-1]
    ssid = Extract.extractSpecific(createFiles.realFile,'SSID').split('SSID')[-1]
    user_name = Extract.extractSpecific(createFiles.realFile,'Username').split('Username')[-1]
    mac_address = Extract.extractSpecific(createFiles.realFile,'MacAddress').split('MacAddress')[-1]
    ip_address = Extract.extractSpecific(createFiles.realFile,'IPAddress').split('IPAddress')[-1]
    if mac_address is not '0:0:0:0:0:0':
        ExportToDB.send_to_db(mac_address,ip_address,apname_last,ssid,user_name)

def deauth_users():
    apname_last = Extract.extractSpecific(createFiles.realFile,'APName').replace('APName','').split()[-1]
    reason_code = Extract.extractSpecific(createFiles.realFile,'ReasonCode').split('ReasonCode')[-1]
    user_ip_address = Extract.extractSpecific(createFiles.realFile,'UserIpAddress').split('UserIpAddress')[-1]
    user_name = Extract.extractSpecific(createFiles.realFile,'UserName').split('UserName')[-1]
    mac_address = Extract.extractSpecific(createFiles.realFile,'MacAddress').split('MacAddress')[-1]
    if mac_address is not '0:0:0:0:0:0':
        ExportToDB.disassociate_users(mac_address,user_ip_address,apname_last,reason_code,user_name) 