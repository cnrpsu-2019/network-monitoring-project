import datetime

def main():
    running = True
    now = datetime.datetime.now()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/trap-receiver/' + fileName, 'a')
    
    while running:
        try:
            input = raw_input()
            unknowToTimestmp = input.replace("<UNKNOWN>","") #1st filter - remove <UNKNOWN>
            #2nd filter - sysUptime
            sysUp = unknowToTimestmp.replace("DISMAN-EVENT-MIB::sysUpTimeInstance", "System Uptime (Day:Hour:Minutes:Second):")
            filterAire = sysUp.replace("AIRESPACE-WIRELESS-MIB::", " ")
            filterLwapp = filterAire.replace("CISCO-LWAPP-DOT11-CLIENT-MIB::", " ")
            #4th filter
            filter4th = filterLwapp.replace("CISCO-LWAPP-AP-MIB::", " ")
            filter5th = filter4th.replace("SNMPv2-MIB::snmpTrapOID.0", "Trap Event at : " + strnow + " ==>" )
            filter6th = filter5th.replace("CISCO-LWAPP-RRM-MIB::", " ")
            filter7th = filter6th.replace("CISCO-LWAPP-RRM-MIB::", " ")
            filter8th = filter7th.replace("CISCO-LWAPP-WLAN-MIB::", " ")
            filter9th = filter8th.replace("CISCO-LWAPP-ROGUE-MIB::", " ")
            #filter10th = filter9th.replace("CISCO-LWAPP-ROGUE-MIB::", " ")

            #filter more details
            clientIPFilter = filter9th.replace("cldcClientByIpAddressType", "IP Address Type:")
            clientUsername = clientIPFilter.replace("cldcClientUsername", "Client Username:")
            clientSSID = clientUsername.replace("cldcClientSSID", "Client SSID:")
            clientMACAddr = clientSSID.replace("cldcApMacAddress", "AP MAC Address:")
            clientSessionID = clientMACAddr.replace("cldcClientSessionID", "Client Session ID:")
            clApName = clientSessionID.replace("cLApName", "Access Point Name: ")
            

            #write final message into file
            output.write( clApName + "\n")

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
