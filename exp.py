import datetime
import re

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
            filter5th = filter4th.replace("SNMPv2-MIB::snmpTrapOID.0", "Trap event:"+ strnow +" ==>" )
            filter6th = filter5th.replace("CISCO-LWAPP-RRM-MIB::", "")
            filter7th = filter6th.replace("CISCO-LWAPP-RRM-MIB::", "")
            filter8th = filter7th.replace("CISCO-LWAPP-WLAN-MIB::", "")
            filter9th = filter8th.replace("CISCO-LWAPP-ROGUE-MIB::", "")
            

            #filter more details
            clientIPFilter = filter9th.replace("cldcClientByIpAddressType.0", "IP address type:")
            clientUsername = clientIPFilter.replace("cldcClientUsername.", "Client username:")
            clientSSID = clientUsername.replace("cldcClientSSID.0", "Client SSID:")
            clientMACAddr = clientSSID.replace("cldcApMacAddress.", "AP MAC address:")
            clientSessionID = clientMACAddr.replace("cldcClientSessionID.", "Client session ID:")
            clApName = clientSessionID.replace("cLApName.", "AP name: ")
            
            bsnStationAPMacAddr = clApName.replace("bsnStationAPMacAddr.0", "AP MAC address:")
            bsnStationAPIfSlotId = bsnStationAPMacAddr.replace("bsnStationAPIfSlotId.0", "AP slot ID:")
            bsnStationReasonCode = bsnStationAPIfSlotId.replace("bsnStationReasonCode.0", "Reason code:")
            bsnUserIpAddress = bsnStationReasonCode.replace("bsnUserIpAddress.0", "Client IP address:")
            bsnStationUserName = bsnUserIpAddress.replace("bsnStationUserName.0", "Client username:")
            bsnStationMacAddress = bsnStationUserName.replace("bsnStationMacAddress.0", "Client MAC address:")
            bsnAPName = bsnStationMacAddress.replace("bsnAPName.0", "AP Name:")
            cldcClientByIpAddress = bsnAPName.replace("cldcClientByIpAddress.0", "Client by IP address:")
            
            #Rogue
            cLApSysMacAddress = cldcClientByIpAddress.replace("cLApSysMacAddress.0", "System rogue AP MAC address:")
            cLApName = cLApSysMacAddress.replace("cLApName.0", "Rogue AP name:")
            cLApRogueApMacAddress = cLApName.replace("cLApRogueApMacAddress.0", "Rogue AP MAC address:")
            cLApEthernetIfSlotId = cLApRogueApMacAddress.replace("cLApEthernetIfSlotId.0", "Slot ID:")
            cLApDot11IfType = cLApEthernetIfSlotId.replace("cLApDot11IfType.0", "Type:")
            cLApRogueDetectedChannel = cLApDot11IfType.replace("cLApRogueDetectedChannel.0 Wrong Type (should be Gauge32 or Unsigned32):", "Detected channel:")
            cLApRSSI = cLApRogueDetectedChannel.replace("cLApRSSI.0", "RSSI:")
            cLApSNR = cLApRSSI.replace("cLApSNR.0","SNR:")
            cLApRogueAPOnWiredNetwork = cLApSNR.replace("cLApRogueAPOnWiredNetwork.0", "Rogue AP on wired network:")
            cLApAdhocRogue = cLApRogueAPOnWiredNetwork.replace("cLApAdhocRogue.0", "Rogue Adhoc:")
            cLApRogueApSsid = cLApAdhocRogue.replace("cLApRogueApSsid.0", "Rogue SSID:")
            cLApRogueClassType = cLApRogueApSsid.replace("cLApRogueClassType.0", "Class type:")
            cLApRogueMode = cLApRogueClassType.replace("cLApRogueMode.0", "Rogue mode:")
            cLApRogueIsClassifiedByRule = cLApRogueMode.replace("cLApRogueIsClassifiedByRule.0", "Is classified by rule?:")
            cLApSeverityScore = cLApRogueIsClassifiedByRule.replace("cLApSeverityScore.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity score:")
            cLApRuleName = cLApSeverityScore.replace("cLApRuleName.0", "Rule name:")
            cLApRogueClassifiedApMacAddress = cLApRuleName.replace("cLApRogueClassifiedApMacAddress.0", "Classified rogue AP MAC address:")
            cLApRogueClassifiedRSSI = cLApRogueClassifiedApMacAddress.replace("cLApRogueClassifiedRSSI.0", "Classified rogue AP RSSI:")

            cLApDot11IfSlotId = cLApRogueClassifiedRSSI.replace("cLApDot11IfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32)", "AP interface slot ID:")
            cldcClientSSID = cLApDot11IfSlotId.replace("cldcClientSSID.", "Client SSID:")
            bsnAPDot3MacAddress = cldcClientSSID.replace("bsnAPDot3MacAddress.", "AP MAC address:")
            bsnAPIfSlotId = bsnAPDot3MacAddress.replace("bsnAPIfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "AP interface slot ID:")
            cldcClientIPAddress = bsnAPIfSlotId.replace("cldcClientIPAddress.0","Client IP address:")

            cldcClientMacAddress = cldcClientIPAddress.replace("cldcClientMacAddress.0", "Client MAC address:")
            cldcIfType = cldcClientMacAddress.replace("cldcIfType.0", "Client interface type:")
            
            clrRrmApTransmitPowerLevel = cldcIfType.replace("clrRrmApTransmitPowerLevel.0", "Controller AP power level:")
            clrRrmTimeStamp = clrRrmApTransmitPowerLevel.replace("clrRrmTimeStamp.0 Wrong Type (should be Timeticks)","Controller AP timestamp:")
            clrRrmClientType = clrRrmTimeStamp.replace("clrRrmClientType.0","Controller AP client type:")
            clrRrmRssiHistogramLength = clrRrmClientType.replace("clrRrmRssiHistogramLength.0 Wrong Type (should be Gauge32 or Unsigned32)", "RSSI histogram length:")
            clrRrmRssiHistogramMaxIndex = clrRrmRssiHistogramLength.replace("clrRrmRssiHistogramMaxIndex.0","RSSI histogram max:")
            clrRrmRssiHistogramMinIndex = clrRrmRssiHistogramMaxIndex.replace("clrRrmRssiHistogramMinIndex.0","RSSI histogram min:")
            clrRrmRssiHistogramValues = clrRrmRssiHistogramMinIndex.replace("clrRrmRssiHistogramValues.0","RSSI histogram values:")
            clrRrmNeighborApCount = clrRrmRssiHistogramValues.replace("clrRrmNeighborApCount.0 Wrong Type (should be Gauge32 or Unsigned32)","Controller neighbor AP count: ")
            clrRrmNeighborApMacAddress = clrRrmNeighborApCount.replace("clrRrmNeighborApMacAddress.0", "Neighbor AP MAC address:")
            clrRrmNeighborApRssi = clrRrmNeighborApMacAddress.replace("clrRrmNeighborApRssi.0", "Neighbor AP RSSI:")
            clrRrmNeighborApIfType = clrRrmNeighborApRssi.replace("clrRrmNeighborApIfType.0", "Neighbor AP interface type:")
            cLWlanChdEnable = clrRrmNeighborApIfType.replace("cLWlanChdEnable.2","WLAN channel enable:")

            bsnAuthFailureUserType = cLWlanChdEnable.replace("bsnAuthFailureUserType.0", "User type:")
            bsnAuthFailureUserName = bsnAuthFailureUserType.replace("bsnAuthFailureUserName.0","Username:")

            bsnRogueAPDot11MacAddress = bsnAuthFailureUserName.replace("bsnRogueAPDot11MacAddress.0","(Dot11)Rogue AP MAC address:")
            bsnRogueAPAirespaceAPMacAddress = bsnRogueAPDot11MacAddress.replace("bsnRogueAPAirespaceAPMacAddress.0", "(Airespace)Rogue AP MAC address")
            bsnRogueAPAirespaceAPSlotId = bsnRogueAPAirespaceAPMacAddress.replace("bsnRogueAPAirespaceAPSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Rogue AP slot ID:")
            bsnRogueAPRadioType = bsnRogueAPAirespaceAPSlotId.replace("bsnRogueAPRadioType.0", "Rogue AP radio type:")
            bsnRogueAPAirespaceAPMacAddress = bsnRogueAPRadioType.replace("bsnRogueAPAirespaceAPMacAddress.0","(Airespace)Rogue AP MAC address:")

            bsnImpersonatedAPMacAddr = bsnRogueAPAirespaceAPMacAddress.replace("bsnImpersonatedAPMacAddr.0", "AP MAC address:")
            bsnImpersonatingSourceMacAddr = bsnImpersonatedAPMacAddr.replace("bsnImpersonatingSourceMacAddr.0","AP Source MAC adress:")

            cLRogueClientTotalDetectingAPs = bsnImpersonatingSourceMacAddr.replace("cLRogueClientTotalDetectingAPs.0", "Total rogue AP:")
            cLRogueClientFirstReported = cLRogueClientTotalDetectingAPs.replace("cLRogueClientFirstReported.0","First report:")
            cLRogueClientLastReported = cLRogueClientFirstReported.replace("cLRogueClientLastReported.0","Last report:")
            cLRogueClientGatewayMac = cLRogueClientLastReported.replace("cLRogueClientGatewayMac.0","Rogue gateway MAC address:")
            bsnAPIfType = cLRogueClientGatewayMac.replace("bsnAPIfType.0","AP interface type:")
            bsnStationBlacklistingReasonCode = bsnAPIfType.replace("bsnStationBlacklistingReasonCode.0", "Blacklisted reason:")
            
            #remaining filter
            filter10th = bsnAPIfType.replace("CISCO-LWAPP-SI-MIB::", "")
            cLSiIdrDeviceId = filter10th.replace("cLSiIdrDeviceId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device ID:")
            cLSiIdrDeviceType = cLSiIdrDeviceId.replace("cLSiIdrDeviceType.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device type:")
            cLSiIdrAffectedChannels = cLSiIdrDeviceType.replace("cLSiIdrAffectedChannels.0 Wrong Type (should be OCTET STRING):", "Affected channels:")
            cLSiIdrSeverity = cLSiIdrAffectedChannels.replace("cLSiIdrSeverity.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity:")
            cLSiIdrClusterId = cLSiIdrSeverity.replace("cLSiIdrClusterId.0", "Cluster ID:") 
            cLSiAlarmClear = cLSiIdrClusterId.replace("cLSiAlarmClear.0", "Alarm clear:")
            cLSiIdrPreviousClusterId = cLSiAlarmClear.replace("cLSiIdrPreviousClusterId.0", "Previous cluster ID:")

            #rogue Ap
            bsnRogueAPAirespaceAPName = cLSiIdrPreviousClusterId.replace("bsnRogueAPAirespaceAPName.0", "Rogue AP name:")
            modApname = bsnRogueAPAirespaceAPName.replace("AP Name: .","AP name:")
            modUsername  = modApname.replace("Client username:0", "Client username:")
            cLLastDetectingRadioMACAddress = modUsername.replace("cLLastDetectingRadioMACAddress.0", "Last detecting radio MAC address:") 
            modApname0 = cLLastDetectingRadioMACAddress.replace("AP Name:0", "AP name:")

            cLWlanChdEnable = modApname0.replace("cLWlanChdEnable.1", "Wlan channel enable:")
            cLApDot11IfSlotId2 = cLWlanChdEnable.replace("cLApDot11IfSlotId.0","AP interface slot ID:")
            
            convertsingle = cLApDot11IfSlotId2.replace("'","0")
            #final result
            Result  = convertsingle
            
            output.write(Result + "\n")
           

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
