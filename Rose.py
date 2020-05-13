#import modules
import Extract
import createFiles
import time
import ExportToDB
import datetime

def harvest_user(): #collect user by mac address
	status = Extract.extractSpecific(createFiles.realFile,'Event').split('Event')[-1].strip()
	curr_mac = Extract.client_mac(createFiles.realFile)[-1].strip()
	bucket = []
	bucket.append(curr_mac)
	total_user = int(len(bucket))
	ExportToDB.harvest_user(total_user)