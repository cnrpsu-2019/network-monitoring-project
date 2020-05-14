#!/usr/bin/python3

#import modules
import Extract
import createFiles
import time
import ExportToDB
import schedule
import sys

sys.path.append('/home/bass/.local/lib/python3.8/site-packages/schedule')

def harvest_user(): #collect user by mac address
	status = Extract.extractSpecific(createFiles.realFile,'Event').split('Event')[-1].strip()
	curr_mac = Extract.client_mac(createFiles.realFile) #collect all mac addresses
	bucket = []
	bucket.append(curr_mac)
	total_user = int(len(bucket))
	ExportToDB.harvest_user(total_user)

schedule.every(5).minutes.do(harvest_user)

while True:
	schedule.run_pending()
	time.sleep(1)
