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
            clientIPFilter = filter9th.replace("cldcClientByIpAddressType.0", "IP Address Type:")
            clientUsername = clientIPFilter.replace("cldcClientUsername.", "Client Username:")
            clientSSID = clientUsername.replace("cldcClientSSID.", "Client SSID:")
            clientMACAddr = clientSSID.replace("cldcApMacAddress.", "AP MAC Address:")
            clientSessionID = clientMACAddr.replace("cldcClientSessionID.", "Client Session ID:")
            clApName = clientSessionID.replace("cLApName.", "Access Point Name: ")
            
            bsnStationAPMacAddr = clApName.replace("bsnStationAPMacAddr.0", "Access Point MAC Address:")
            bsnStationAPIfSlotId = bsnStationAPMacAddr.replace("bsnStationAPIfSlotId.0", "Access Point Slot ID:")
            bsnStationReasonCode = bsnStationAPIfSlotId.replace("bsnStationReasonCode.0", "Reason:")
            bsnUserIpAddress = bsnStationReasonCode.replace("bsnUserIpAddress.0", "Client IP Address:")
            bsnStationUserName = bsnUserIpAddress.replace("bsnStationUserName.0", "CLient Username:")
            bsnStationMacAddress = bsnStationUserName.replace("bsnStationMacAddress.0", "Client MAC Address:")
            bsnAPName = bsnStationMacAddress.replace("bsnAPName.0", "Access Point Name:")
            cldcClientByIpAddress = bsnAPName.replace("cldcClientByIpAddress.0", "Client by IP Address:")
            
            #Rogue
            cLApSysMacAddress = cldcClientByIpAddress.replace("cLApSysMacAddress.0", "System rogue AP MAC Address:")
            cLApName = cLApSysMacAddress.replace("cLApName.0", "Rogue AP name:")
            cLApRogueApMacAddress = cLApName.replace("cLApRogueApMacAddress.0", "Rogue AP MAC Address:")
            cLApEthernetIfSlotId = cLApRogueApMacAddress.replace("cLApEthernetIfSlotId.0", "Slot ID:")
            cLApDot11IfType = cLApEthernetIfSlotId.replace("cLApDot11IfType.0", "Type:")
            cLApRogueDetectedChannel = cLApDot11IfType.replace("cLApRogueDetectedChannel.0", "Detected Channel:")
            cLApRSSI = cLApRogueDetectedChannel.replace("cLApRSSI.0", "RSSI:")
            cLApSNR = cLApRSSI.replace("cLApSNR.0","SNR:")
            cLApRogueAPOnWiredNetwork = cLApSNR.replace("cLApRogueAPOnWiredNetwork.0", "Rogue AP on wired Network:")
            cLApAdhocRogue = cLApRogueAPOnWiredNetwork.replace("cLApAdhocRogue.0", "Rogue Adhoc:")
            cLApRogueApSsid = cLApAdhocRogue.replace("cLApRogueApSsid.0", "Rogue SSID:")
            cLApRogueClassType = cLApRogueApSsid.replace("cLApRogueClassType.0", "Class Type:")
            cLApRogueMode = cLApRogueClassType.replace("cLApRogueMode.0", "Rogue Mode:")
            cLApRogueIsClassifiedByRule = cLApRogueMode.replace("cLApRogueIsClassifiedByRule.0", "Is Classified by rule?:")
            cLApSeverityScore = cLApRogueIsClassifiedByRule.replace("cLApSeverityScore.0", "Severity score:")
            cLApRuleName = cLApSeverityScore.replace("cLApRuleName.0", "Rule name:")
            cLApRogueClassifiedApMacAddress = cLApRuleName.replace("cLApRogueClassifiedApMacAddress.0", "Classified rogue AP MAC Address:")
            cLApRogueClassifiedRSSI = cLApRogueClassifiedApMacAddress.replace("cLApRogueClassifiedRSSI.0", "Classified rogue AP RSSI:")

            cLApDot11IfSlotId = cLApRogueClassifiedRSSI.replace("cLApDot11IfSlotId.0", "AP interface Slot ID:")
            cldcClientSSID = cLApDot11IfSlotId.replace("cldcClientSSID.", "Client SSID:")

            finalResult  = cldcClientSSID

            #write final message into file
            output.write( finalResult + "\n")

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
