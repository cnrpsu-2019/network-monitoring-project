import requests

base_uri = 'http://172.31.0.102'
user = '5910110573'
password = 'Test123**'
rest_path = '/data/InventoryDetails'
url = base_uri + rest_path
response = requests.request('GET', url, auth=(user, password), verify=False)
print(response.text)
