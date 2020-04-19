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

def active_user_cummulate():
    username_ext = Extract.extractSpecific(createFiles.realFile,'Username').replace('Username','').split()
    unique_users = int(len(list(set(username_ext))) * 0.85)
    #send to database
    ExportToDB.active_users_coarse(unique_users)

def rogue_ssid_detected():
    rogue_whole = Extract.extractSpecific(createFiles.realFile,'ApRogueApSsid').replace('ApRogueApSsid','')
    pattern = re.compile(r"(?:\w.?){10,}")
    result_ssid = re.findall(pattern,rogue_whole)
    unique_ssid_rogue = len(list(set(result_ssid)))
    ExportToDB.ssid_rogue_detected(unique_ssid_rogue)

def test_users():
    apname_last = Extract.extractSpecific(createFiles.realFile,'APName').replace('APName','').split()[-1]
    ssid = Extract.extractSpecific(createFiles.realFile,'SSID').split('SSID')[-1]
    user_name = Extract.extractSpecific(createFiles.realFile,'Username').split('Username')[-1]
    mac_address = Extract.extractSpecific(createFiles.realFile,'MacAddress').split('MacAddress')[-1]
    ip_address = Extract.extractSpecific(createFiles.realFile,'IPAddress').split('IPAddress')[-1]
    ExportToDB.send_to_db(mac_address,ip_address,apname_last,ssid,ip_address)