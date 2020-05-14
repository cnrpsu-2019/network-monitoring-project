#import modules
import Extract
import createFiles
import time
import ExportToDB

def harvest_user(): #collect user by mac address
    status = Extract.extractSpecific(createFiles.realFile,'Event').split('Event')[-1].strip()
    curr_mac = Extract.client_mac(createFiles.realFile) #collect all mac addresses
    bucket = []
    bucket.append(curr_mac)
    total_user = int(len(bucket))
    ExportToDB.harvest_user(total_user)
