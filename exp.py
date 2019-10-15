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
            filterAire = sysUp.replace("AIRESPACE-WIRELESS-MIB::", "")
            filterLwapp = filterAire.replace("CISCO-LWAPP-DOT11-CLIENT-MIB::", "")
            #4th filter
            filter4th = filterLwapp.replace("CISCO-LWAPP-AP-MIB::", "")
            filter5th = filter4th.replace("SNMPv2-MIB::snmpTrapOID.0", "Trap Event at : " + strnow + " ==>" )
            filter6th = filter5th.replace("CISCO-LWAPP-RRM-MIB::", "")
            filter7th = filter6th.replace("CISCO-LWAPP-RRM-MIB::", "")
            filter8th = filter7th.replace("CISCO-LWAPP-WLAN-MIB::", "")
            filter9th = filter8th.replace("CISCO-LWAPP-ROGUE-MIB::", "")
            

            #filter more details
            clientIPFilter = filter9th.replace("cldcClientByIpAddressType.0", "IP Address Type:")
            clientUsername = clientIPFilter.replace("cldcClientUsername.", "Client Username:")
            clientSSID = clientUsername.replace("cldcClientSSID.0", "Client SSID:")
            clientMACAddr = clientSSID.replace("cldcApMacAddress.", "AP MAC Address:")
            clientSessionID = clientMACAddr.replace("cldcClientSessionID.", "Client Session ID:")
            clApName = clientSessionID.replace("cLApName", "AP Name: ")
            
            bsnStationAPMacAddr = clApName.replace("bsnStationAPMacAddr.0", "AP MAC Address:")
            bsnStationAPIfSlotId = bsnStationAPMacAddr.replace("bsnStationAPIfSlotId.0", "AP Slot ID:")
            bsnStationReasonCode = bsnStationAPIfSlotId.replace("bsnStationReasonCode.0", "Reason Code:")
            bsnUserIpAddress = bsnStationReasonCode.replace("bsnUserIpAddress.0", "Client IP Address:")
            bsnStationUserName = bsnUserIpAddress.replace("bsnStationUserName.0", "CLient Username:")
            bsnStationMacAddress = bsnStationUserName.replace("bsnStationMacAddress.0", "Client MAC Address:")
            bsnAPName = bsnStationMacAddress.replace("bsnAPName.0", "AP Name:")
            cldcClientByIpAddress = bsnAPName.replace("cldcClientByIpAddress.0", "Client by IP Address:")
            
            #Rogue
            cLApSysMacAddress = cldcClientByIpAddress.replace("cLApSysMacAddress.0", "System rogue AP MAC Address:")
            cLApName = cLApSysMacAddress.replace("cLApName.0", "Rogue AP name:")
            cLApRogueApMacAddress = cLApName.replace("cLApRogueApMacAddress.0", "Rogue AP MAC Address:")
            cLApEthernetIfSlotId = cLApRogueApMacAddress.replace("cLApEthernetIfSlotId.0", "Slot ID:")
            cLApDot11IfType = cLApEthernetIfSlotId.replace("cLApDot11IfType.0", "Type:")
            cLApRogueDetectedChannel = cLApDot11IfType.replace("cLApRogueDetectedChannel.0 Wrong Type (should be Gauge32 or Unsigned32):", "Detected Channel:")
            cLApRSSI = cLApRogueDetectedChannel.replace("cLApRSSI.0", "RSSI:")
            cLApSNR = cLApRSSI.replace("cLApSNR.0","SNR:")
            cLApRogueAPOnWiredNetwork = cLApSNR.replace("cLApRogueAPOnWiredNetwork.0", "Rogue AP on wired Network:")
            cLApAdhocRogue = cLApRogueAPOnWiredNetwork.replace("cLApAdhocRogue.0", "Rogue Adhoc:")
            cLApRogueApSsid = cLApAdhocRogue.replace("cLApRogueApSsid.0", "Rogue SSID:")
            cLApRogueClassType = cLApRogueApSsid.replace("cLApRogueClassType.0", "Class Type:")
            cLApRogueMode = cLApRogueClassType.replace("cLApRogueMode.0", "Rogue Mode:")
            cLApRogueIsClassifiedByRule = cLApRogueMode.replace("cLApRogueIsClassifiedByRule.0", "Is Classified by rule?:")
            cLApSeverityScore = cLApRogueIsClassifiedByRule.replace("cLApSeverityScore.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity score:")
            cLApRuleName = cLApSeverityScore.replace("cLApRuleName.0", "Rule name:")
            cLApRogueClassifiedApMacAddress = cLApRuleName.replace("cLApRogueClassifiedApMacAddress.0", "Classified rogue AP MAC Address:")
            cLApRogueClassifiedRSSI = cLApRogueClassifiedApMacAddress.replace("cLApRogueClassifiedRSSI.0", "Classified rogue AP RSSI:")

            cLApDot11IfSlotId = cLApRogueClassifiedRSSI.replace("cLApDot11IfSlotId.0", "AP interface Slot ID:")
            cldcClientSSID = cLApDot11IfSlotId.replace("cldcClientSSID.", "Client SSID:")
            bsnAPDot3MacAddress = cldcClientSSID.replace("bsnAPDot3MacAddress.", "AP MAC Address:")
            bsnAPIfSlotId = bsnAPDot3MacAddress.replace("bsnAPIfSlotId. Wrong Type (should be Gauge32 or Unsigned32):", "AP interface slot ID:")
            cldcClientIPAddress = bsnAPIfSlotId.replace("cldcClientIPAddress.0","Client IP Address:")

            cldcClientMacAddress = cldcClientIPAddress.replace("cldcClientMacAddress.0", "Client MAC Address:")
            cldcIfType = cldcClientMacAddress.replace("cldcIfType.0", "Client interface type:")
            
            clrRrmApTransmitPowerLevel = cldcIfType.replace("clrRrmApTransmitPowerLevel.0", "Controller AP Power Level:")
            clrRrmTimeStamp = clrRrmApTransmitPowerLevel.replace("clrRrmTimeStamp.0","Controller AP timestamp:")
            clrRrmClientType = clrRrmTimeStamp.replace("clrRrmClientType.0","Controller AP client type:")
            clrRrmRssiHistogramLength = clrRrmClientType.replace("clrRrmRssiHistogramLength.0", "RSSI Histogram length:")
            clrRrmRssiHistogramMaxIndex = clrRrmRssiHistogramLength.replace("clrRrmRssiHistogramMaxIndex.0","RSSI histogram max:")
            clrRrmRssiHistogramMinIndex = clrRrmRssiHistogramMaxIndex.replace("clrRrmRssiHistogramMinIndex.0","RSSI histogram min:")
            clrRrmRssiHistogramValues = clrRrmRssiHistogramMinIndex.replace("clrRrmRssiHistogramValues.0","RSSI histogram values:")
            clrRrmNeighborApCount = clrRrmRssiHistogramValues.replace("clrRrmNeighborApCount.0","Controller Neighbor AP count: ")
            clrRrmNeighborApMacAddress = clrRrmNeighborApCount.replace("clrRrmNeighborApMacAddress.0", "Neighbor AP MAC Address:")
            clrRrmNeighborApRssi = clrRrmNeighborApMacAddress.replace("clrRrmNeighborApRssi.0", "Neighbor AP RSSI:")
            clrRrmNeighborApIfType = clrRrmNeighborApRssi.replace("clrRrmNeighborApIfType.0", "Neighbor AP interface type:")
            cLWlanChdEnable = clrRrmNeighborApIfType.replace("cLWlanChdEnable.2","WLAN channel enable:")

            bsnAuthFailureUserType = cLWlanChdEnable.replace("bsnAuthFailureUserType.0", "User type:")
            bsnAuthFailureUserName = bsnAuthFailureUserType.replace("bsnAuthFailureUserName.0","Username:")

            bsnRogueAPDot11MacAddress = bsnAuthFailureUserName.replace("bsnRogueAPDot11MacAddress.0","(Dot11)Rogue AP MAC Address:")
            bsnRogueAPAirespaceAPMacAddress = bsnRogueAPDot11MacAddress.replace("bsnRogueAPAirespaceAPMacAddress.0", "(Airespace)Rogue AP MAC Address")
            bsnRogueAPAirespaceAPSlotId = bsnRogueAPAirespaceAPMacAddress.replace("bsnRogueAPAirespaceAPSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Rogue AP slot ID:")
            bsnRogueAPRadioType = bsnRogueAPAirespaceAPSlotId.replace("bsnRogueAPRadioType.0", "Rogue AP radio type:")
            bsnRogueAPAirespaceAPMacAddress = bsnRogueAPRadioType.replace("bsnRogueAPAirespaceAPMacAddress.0","(Airespace)Rogue AP MAC Address:")

            bsnImpersonatedAPMacAddr = bsnRogueAPAirespaceAPMacAddress.replace("bsnImpersonatedAPMacAddr.0", "AP MAC Address:")
            bsnImpersonatingSourceMacAddr = bsnImpersonatedAPMacAddr.replace("bsnImpersonatingSourceMacAddr.0","AP Source MAC Adress:")

            cLRogueClientTotalDetectingAPs = bsnImpersonatingSourceMacAddr.replace("cLRogueClientTotalDetectingAPs.0", "Total rogue AP:")
            cLRogueClientFirstReported = cLRogueClientTotalDetectingAPs.replace("cLRogueClientFirstReported.0","First Report:")
            cLRogueClientLastReported = cLRogueClientFirstReported.replace("cLRogueClientLastReported.0","Last report:")
            cLRogueClientGatewayMac = cLRogueClientLastReported.replace("cLRogueClientGatewayMac.0","Rogue gateway MAC Address:")
            bsnAPIfType = cLRogueClientGatewayMac.replace("bsnAPIfType.0","AP interface type:")
            bsnStationBlacklistingReasonCode = bsnAPIfType.replace("bsnStationBlacklistingReasonCode.0", "Blacklisted reason:")
            
            #remaining filter
            filter10th = bsnAPIfType.replace("CISCO-LWAPP-SI-MIB::", "")
            cLSiIdrDeviceId = filter10th.replace("cLSiIdrDeviceId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device ID:")
            cLSiIdrDeviceType = cLSiIdrDeviceId.replace("cLSiIdrDeviceType.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device type:")
            cLSiIdrAffectedChannels = cLSiIdrDeviceType.replace("cLSiIdrAffectedChannels.0 Wrong Type (should be OCTET STRING):", "Affected Channels:")
            cLSiIdrSeverity = cLSiIdrAffectedChannels.replace("cLSiIdrSeverity.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity:")
            cLSiIdrClusterId = cLSiIdrSeverity.replace("cLSiIdrClusterId.0", "Cluster ID:") 
            cLSiAlarmClear = cLSiIdrClusterId.replace("cLSiAlarmClear.0", "Alarm Clear:")
            cLSiIdrPreviousClusterId = cLSiAlarmClear.replace("cLSiIdrPreviousClusterId.0", "Previous cluster ID:")

            #rogue Ap
            bsnRogueAPAirespaceAPName = cLSiIdrPreviousClusterId.replace("bsnRogueAPAirespaceAPName.0", "Rogue AP name:")
            modApname = bsnRogueAPAirespaceAPName.replace("AP Name: .","AP Name:")
            modUsername  = modApname.replace("Client Username:0", "Client Username:")
            cLLastDetectingRadioMACAddress = modUsername.replace("cLLastDetectingRadioMACAddress.0", "Last detecting radio MAC Address:") 
            modApname0 = cLLastDetectingRadioMACAddress.replace("AP Name:0", "AP Name:")

            cLWlanChdEnable = modApname0.replace("cLWlanChdEnable.1", "Wlan Channel Enable:")


            #remove weird characters
            hkxRemove = cLWlanChdEnable.replace("'H.k.x~'", "")
            opRemove = hkxRemove.replace("'.=o.-p'", "")
            atBRemove = opRemove.replace("'@..B..'","")
            niRemove = atBRemove.replace("'.N..i.'","")
            lbRemove = niRemove.replace("'..l.{.'", "")
            blankRemove = lbRemove.replace("'..... '", "")
            mRemove = blankRemove.replace("'..M...'","")
            psRemove = mRemove.replace("'p.\...'","")
            e01Remove = psRemove.replace("'.=o1..'", "")
            ctRemove = e01Remove.replace("'..c|.t'", "")
            bracketRemove = ctRemove.replace("'...[..'", "")
            enRemove = bracketRemove.replace("'`.En..'","")
            xvRemove = enRemove.replace("'X..@.v'","")
            atzRemove = xvRemove.replace("'@..Z.\'","")
            dotRemove = atzRemove.replace("'......'", "")
            qRemove = dotRemove.replace("'....Q.'", "")
            dollarRemove = qRemove.replace("'$.....'","")
            npRemove = dollarRemove.replace("'...np'", "")
            voRemove = npRemove.replace("'.vo..5'","")
            coRemove = voRemove.replace("'..co..'","")
            
            #final result
            finalResult  = dollarRemove


            #write final message into file
            output.write( finalResult + "\n")

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
