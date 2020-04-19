#lists of ap mac address each floor
floor01_mac_list = ['bc:16:f5:98:8:0','68:3b:78:e1:8e:c0','68:3b:78:e1:94:20','f4:4e:5:a2:a1:d0',
                    'dc:8c:37:4c:2e:e0','f4:4e:5:b5:24:b0']

floor02_mac_list = ['88:1d:fc:a:f1:20','88:1d:fc:6:3f:b0','70:10:5c:b1:a4:d0','a0:e0:af:3d:c7:80',
                   'f4:4e:5:a2:a1:10','f4:4e:5:b5:65:90']

floor03_mac_list = ['a0:3d:6f:31:b7:e0','f4:4e:5:df:4e:f0','f4:4e:5:db:f0:40','70:10:5c:b1:9e:d0',
                    '68:3b:78:e1:93:0','68:3b:78:e1:93:80','68:3b:78:e9:47:40']

floor04_mac_list = ['a0:e0:af:22:6e:70','a0:3d:6f:31:b7:f0','a0:3d:6f:31:b7:d0','a0:e0:af:95:9c:40',
                   'a0:3d:6f:dd:2d:70']

#all ap mac addresses in building

buildingMacList = floor01_mac_list + floor02_mac_list + floor03_mac_list + floor04_mac_list

#ssid name list
ssidname_list = ['CoEIoT','CoEWiFi','TrueMove H','AIS SMART Login','PSU WiFi 5GHz','PSU WiFi 802.1x']

building_ap_dict = {'AP108-R300': 'R300 Info Lab',
 'AP109-R404': 'R404',
 'AP110-R311': 'R311, Robot Bldg.',
 'AP111-R405': 'R405 Robotic Lab',
 'AP112-R400': 'R400 Staff Office',
 'AP2-7-R020-153': 'Robot Auditorium Robot Bldg.',
 'AP2-8-R020-154': 'Robot Auditorium Robot Bldg.',
 'AP201-R411': 'R411',
 'AP204-R100': 'R100',
 'AP205-R207': 'R207 Common Room',
 'AP206-R204': 'R204 Network Security Lab',
 'AP208-R211': 'R211 WIG Research Lab',
 'AP209-R302-1': 'R302 CNR Lab',
 'AP210-R302-2': 'R302-CNR-Meeting-Room',
 'AP211-Shop': 'CoE Workshop Flr01',
 'AP212-IDL': 'IDL, Flr04',
 'AP213-R202': 'R400 Staff Office',
 'AP214-R205': 'CoE General Office',
 'AP215-R409': 'R409, Robot Bldg.',
 'AP216-R101': 'R101, Robot Bldg.',
 'AP217-FL01-W': 'Floor01-West-Activity-Area',
 'AP218-FL01-E': 'Floor01-East-Activity-Area',
 'AP219-R303': 'R303, Robot Bldg.',
 'AP220-R301B': 'R301B, Robot Bldg.',
 'AP221-R301A': 'R301A, Robot Bldg.',
 'AP222-R201': 'R201, Robot Bldg.',
 'AP223-R200': 'R200, Robot Bldg.',
 'AP3-46-R010-146': 'R010-Robot Exhibition Hall Robot Bldg.'}