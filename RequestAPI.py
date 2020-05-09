import requests

base_uri = 'http://172.31.0.102'
user = '5910110573'
password = 'Test123**'
rest_path = '/webacs/loginAction.do?action=login&product=wcs&selectedCategory=en#pageId=mon_nav_searchClientAction_pageId&queryParams=statusString%3DAssociated%26securityPolicyStatus%3DYes%26connectionTypeString%3DWireless%20Client&forceLoad=true'

url = base_uri + rest_path
response = requests.request('GET', url, auth=(user, password), verify=False)
print(response.text)