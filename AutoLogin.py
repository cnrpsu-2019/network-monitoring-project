import Secret
import os
import requests
import subprocess
import time
from datetime import datetime

PSU_URL = 'https://cp-xml-40g.psu.ac.th:6082/php/uid.php'

def checkPing():
	host_ip = '1.1.1.1' #Check ping res by Cloudflare Public DNS server
	try:
		output = subprocess.check_output("ping -c 1 -W 3 {}".format(host_ip), shell=True)
	except Exception as e:
		return False
	return True

def login():
	headers = {'User-Agent': 'PSU Auto Login'}
	payload = {
		'username' : Secret.std_id,
		'password' : Secret.std_password,
		'login': 'Login'
	}
	
	s = requests.Session()
	get_login = s.get(PSU_URL)
	cookies = dict(get_login.cookies)
	#print(get_login.headers)
	
	post_login = s.post(PSU_URL, headers=headers, data=payload, cookies=cookies)
	#print(post_login.text)
	time.sleep(5) ## Sleep 5s.

	if(checkPing() == True):
		print('Log in successful !!')
	else:
		print('Error , Please try again and do it yourself')

def check_and_login():
	if(checkPing() == False):
		print('NOT LOGIN !!')
		login() # Call login() function
		# time.sleep(14400) #sleep for 4 hours !
	else:
		print('Already Loged in!!') 
