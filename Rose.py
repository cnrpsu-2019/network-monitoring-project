#import modules
import Extract
import createFiles
import time
import ExportToDB

def harvest_user(): #collect user by mac address
	status = Extract.extractSpecific(createFiles.realFile,'Event').split('Event')[-1].strip()
	curr_mac = Extract.client_mac(createFiles.realFile)[-1].strip()
	prev_mac = Extract.client_mac(createFiles.realFile)[-2].strip()
	bucket = []
	total_user = 0
	
	if curr_mac is not prev_mac:
		if status is 'Associate':
			bucket.append(curr_mac)
		elif status is 'Disassociate':
			if bucket is not []:
				bucket.pop()
	
	total_user = int(len(bucket))
	ExportToDB.harvest_user(total_user)