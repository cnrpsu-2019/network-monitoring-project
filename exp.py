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

            filter = input.translate("<UNKNOWN>","")            
          
            filter.translate("DISMAN-EVENT-MIB::sysUpTimeInstance", "System Uptime (Day:Hour:Minutes:Second):")
            filter.translate("AIRESPACE-WIRELESS-MIB::", "")
            filter.translate("CISCO-LWAPP-DOT11-CLIENT-MIB::", "")

            filter.translate("CISCO-LWAPP-AP-MIB::", "")
            filter.translate("SNMPv2-MIB::snmpTrapOID.0", "Trap event:"+ strnow +" ==>" )
            filter.translate("CISCO-LWAPP-RRM-MIB::", "")
            filter.translate("CISCO-LWAPP-RRM-MIB::", "")
            filter.translate("CISCO-LWAPP-WLAN-MIB::", "")
            filter.translate("CISCO-LWAPP-ROGUE-MIB::", "")
            filter.translate("CISCO-LWAPP-SI-MIB::", "")
            
            
            filter.translate("cldcClientByIpAddressType.0", "IP address type:")
            filter.translate("cldcClientUsername.", "Client username:")
            filter.translate("cldcClientSSID.0", "Client SSID:")
            filter.translate("cldcApMacAddress.", "AP MAC address:")
            filter.translate("cldcClientByIpAddress.0", "Client by IP address:")
            filter.translate("cldcClientSessionID.", "Client session ID:")
            filter.translate("cldcClientIPAddress.0","Client IP address:")
            filter.translate("cldcClientMacAddress.0", "Client MAC address:")
            filter.translate("cldcIfType.0", "Client interface type:")
            filter.translate("cldcClientSSID.", "Client SSID:")

           
            filter.translate("bsnUserIpAddress.0", "Client IP address:")
            filter.translate("bsnStationAPMacAddr.0", "AP MAC address:")
            filter.translate("bsnStationAPIfSlotId.0", "AP slot ID:")
            filter.translate("bsnStationReasonCode.0", "Reason code:")
            filter.translate("bsnStationUserName.0", "Client username:")
            filter.translate("bsnStationMacAddress.0", "Client MAC address:")
            filter.translate("bsnStationBlacklistingReasonCode.0", "Blacklisted reason:")


            filter.translate("bsnAPName.0", "AP Name:")
            filter.translate("bsnAPIfType.0","AP interface type:")
            filter.translate("bsnAPDot3MacAddress.", "AP MAC address:")
            filter.translate("bsnAPIfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "AP interface slot ID:")
            filter.translate("bsnAuthFailureUserType.0", "User type:")
            filter.translate("bsnAuthFailureUserName.0","Username:")

            filter.translate("bsnRogueAPDot11MacAddress.0","(Dot11)Rogue AP MAC address:")
            filter.translate("bsnRogueAPAirespaceAPMacAddress.0", "(Airespace)Rogue AP MAC address")
            filter.translate("bsnRogueAPAirespaceAPSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Rogue AP slot ID:")
            filter.translate("bsnRogueAPRadioType.0", "Rogue AP radio type:")
            filter.translate("bsnRogueAPAirespaceAPMacAddress.0","(Airespace)Rogue AP MAC address:")
            filter.translate("bsnRogueAPAirespaceAPName.0", "Rogue AP name:")

            filter.translate("bsnImpersonatedAPMacAddr.0", "AP MAC address:")
            filter.translate("bsnImpersonatingSourceMacAddr.0","AP Source MAC adress:")
            
            
            filter.translate("cLApName.", "AP name: ")
            filter.translate("cLApSysMacAddress.0", "System rogue AP MAC address:")
            filter.translate("cLApName.0", "AP name:")
            filter.translate("cLApEthernetIfSlotId.0", "Slot ID:")
            filter.translate("cLApRSSI.0", "RSSI:")
            filter.translate("cLApSNR.0","SNR:")
            
            filter.translate("cLApAdhocRogue.0", "Rogue Adhoc:")
            filter.translate("cLApRogueApMacAddress.0", "Rogue AP MAC address:")
            filter.translate("cLApRogueDetectedChannel.0 Wrong Type (should be Gauge32 or Unsigned32):", "Detected channel:")
            filter.translate("cLApRogueAPOnWiredNetwork.0", "Rogue AP on wired network:")
            filter.translate("cLApRogueApSsid.0", "Rogue SSID:")
            filter.translate("cLApRogueClassType.0", "Class type:")
            filter.translate("cLApRogueMode.0", "Rogue mode:")
            filter.translate("cLApRogueIsClassifiedByRule.0", "Is classified by rule?:")
            filter.translate("cLApRogueClassifiedApMacAddress.0", "Classified rogue AP MAC address:")
            filter.translate("cLApRogueClassifiedRSSI.0", "Classified rogue AP RSSI:")
            filter.translate("cLApSeverityScore.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity score:")
            filter.translate("cLApRuleName.0", "Rule name:")
           
            filter.translate("cLApDot11IfSlotId.0","AP interface slot ID:")
            filter.translate("cLApDot11IfType.0", "Type:")
            filter.translate("cLApDot11IfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32)", "AP interface slot ID:")
            
            
            
            
            filter.translate("clrRrmApTransmitPowerLevel.0", "Controller AP power level:")
            filter.translate("clrRrmTimeStamp.0 Wrong Type (should be Timeticks)","Controller AP timestamp:")
            filter.translate("clrRrmClientType.0","Controller AP client type:")
            filter.translate("clrRrmRssiHistogramLength.0 Wrong Type (should be Gauge32 or Unsigned32)", "RSSI histogram length:")
            filter.translate("clrRrmRssiHistogramMaxIndex.0","RSSI histogram max:")
            filter.translate("clrRrmRssiHistogramMinIndex.0","RSSI histogram min:")
            filter.translate("clrRrmRssiHistogramValues.0","RSSI histogram values:")
            filter.translate("clrRrmNeighborApCount.0 Wrong Type (should be Gauge32 or Unsigned32)","Controller neighbor AP count: ")
            filter.translate("clrRrmNeighborApMacAddress.0", "Neighbor AP MAC address:")
            filter.translate("clrRrmNeighborApRssi.0", "Neighbor AP RSSI:")
            filter.translate("clrRrmNeighborApIfType.0", "Neighbor AP interface type:")

            filter.translate("cLWlanChdEnable.1", "Wlan channel enable:")
            filter.translate("cLWlanChdEnable.2","WLAN channel enable:")

            

            filter.translate("cLRogueClientTotalDetectingAPs.0", "Total rogue AP:")
            filter.translate("cLRogueClientFirstReported.0","First report:")
            filter.translate("cLRogueClientLastReported.0","Last report:")
            filter.translate("cLRogueClientGatewayMac.0","Rogue gateway MAC address:")
            
            
        
            filter.translate("cLSiIdrDeviceId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device ID:")
            filter.translate("cLSiIdrDeviceType.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device type:")
            filter.translate("cLSiIdrAffectedChannels.0 Wrong Type (should be OCTET STRING):", "Affected channels:")
            filter.translate("cLSiIdrSeverity.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity:")
            filter.translate("cLSiIdrClusterId.0", "Cluster ID:") 
            filter.translate("cLSiAlarmClear.0", "Alarm clear:")
            filter.translate("cLSiIdrPreviousClusterId.0", "Previous cluster ID:")

            
            
            filter.translate("AP Name: .","AP name:")
            filter.translate("Client username:0", "Client username:")
            filter.translate("cLLastDetectingRadioMACAddress.0", "Last detecting radio MAC address:") 
            filter.translate("AP Name:0", "AP name:")

            filter.translate("'","")
            filter.translate("...","")
            filter.translate("..","")
            filter.translate("=","")
            filter.translate("^","")
            filter.translate("]","")
            filter.translate("[","")
            filter.translate(".Z.","")
            filter.translate("o1","")
            filter.translate("\\","")
            filter.translate("Q","")
            filter.translate("$","")
            filter.translate("hT.","")
            filter.translate(".Nj.","")
            filter.translate(".N","")
            filter.translate("<","")
            filter.translate(".g?","")
            filter.translate("?","")
            filter.translate(":f ", ":")
            
            filter.translate(".N.","")
            filter.translate(".NN.","")
            filter.translate("D-","")
            filter.translate("-","")
            filter.translate("_","")
            filter.translate(".s","")
            filter.translate("}","")
            
            filter.translate("@","")
            filter.translate(".A","")
            filter.translate("p.","")
            filter.translate("Z.","")
            filter.translate(".lc","")
            filter.translate(".Ni.","")
            filter.translate("&","")
             
            #final result
            Result  = filter            
            output.write(Result + "\n")
           

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
