#import modules
import Extract
import createFiles
import time
import ExportToDB

def harvest_user():
	status = Extract.extractSpecific(createFiles.realFile,'Event').split('Event')[-1]
	prev_mac = Extract.client_mac(createFiles.realFile)[-1]
	time.sleep(10) #sleep for 10 secs
	curr_mac = Extract.client_mac(createFiles.realFile)[-1]
	total_user = 0
	try:
		if curr_mac == prev_mac:
			time.sleep(5) #snooze for 5 secs
		elif curr_mac != prev_mac:
			if status is 'Associate':
				total_user = total_user + 1
			elif status is 'Disassociate':
				total_user = total_user - 1

		ExportToDB.harvest_user(total_user)
		time.sleep(5) #delayed for 5 mins
		total_user = 0
	except e:
		print(e)