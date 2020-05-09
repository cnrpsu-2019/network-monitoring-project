import Secret
import os
import requests
import subprocess
import time
from datetime import datetime

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
		print('Error , Please try again')

def main():
	if(checkPing() == False):
		print('NOT LOGIN !!')
		login() # Call login() function
	else:
		print('Already Loged in!!') 

if __name__ == '__main__':
    main() ## Main Function