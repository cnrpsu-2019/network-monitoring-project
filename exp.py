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

            filter = input.replace("<UNKNOWN>","")            
          
            filter.replace("DISMAN-EVENT-MIB::sysUpTimeInstance", "System Uptime (Day:Hour:Minutes:Second):")
            filter.replace("AIRESPACE-WIRELESS-MIB::", "")
            filter.replace("CISCO-LWAPP-DOT11-CLIENT-MIB::", "")

            filter.replace("CISCO-LWAPP-AP-MIB::", "")
            filter.replace("SNMPv2-MIB::snmpTrapOID.0", "Trap event:"+ strnow +" ==>" )
            filter.replace("CISCO-LWAPP-RRM-MIB::", "")
            filter.replace("CISCO-LWAPP-RRM-MIB::", "")
            filter.replace("CISCO-LWAPP-WLAN-MIB::", "")
            filter.replace("CISCO-LWAPP-ROGUE-MIB::", "")
            filter.replace("CISCO-LWAPP-SI-MIB::", "")
            
            
            filter.replace("cldcClientByIpAddressType.0", "IP address type:")
            filter.replace("cldcClientUsername.", "Client username:")
            filter.replace("cldcClientSSID.0", "Client SSID:")
            filter.replace("cldcApMacAddress.", "AP MAC address:")
            filter.replace("cldcClientByIpAddress.0", "Client by IP address:")
            filter.replace("cldcClientSessionID.", "Client session ID:")
            filter.replace("cldcClientIPAddress.0","Client IP address:")
            filter.replace("cldcClientMacAddress.0", "Client MAC address:")
            filter.replace("cldcIfType.0", "Client interface type:")
            filter.replace("cldcClientSSID.", "Client SSID:")

           
            filter.replace("bsnUserIpAddress.0", "Client IP address:")
            filter.replace("bsnStationAPMacAddr.0", "AP MAC address:")
            filter.replace("bsnStationAPIfSlotId.0", "AP slot ID:")
            filter.replace("bsnStationReasonCode.0", "Reason code:")
            filter.replace("bsnStationUserName.0", "Client username:")
            filter.replace("bsnStationMacAddress.0", "Client MAC address:")
            filter.replace("bsnStationBlacklistingReasonCode.0", "Blacklisted reason:")


            filter.replace("bsnAPName.0", "AP Name:")
            filter.replace("bsnAPIfType.0","AP interface type:")
            filter.replace("bsnAPDot3MacAddress.", "AP MAC address:")
            filter.replace("bsnAPIfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "AP interface slot ID:")
            filter.replace("bsnAuthFailureUserType.0", "User type:")
            filter.replace("bsnAuthFailureUserName.0","Username:")

            filter.replace("bsnRogueAPDot11MacAddress.0","(Dot11)Rogue AP MAC address:")
            filter.replace("bsnRogueAPAirespaceAPMacAddress.0", "(Airespace)Rogue AP MAC address")
            filter.replace("bsnRogueAPAirespaceAPSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Rogue AP slot ID:")
            filter.replace("bsnRogueAPRadioType.0", "Rogue AP radio type:")
            filter.replace("bsnRogueAPAirespaceAPMacAddress.0","(Airespace)Rogue AP MAC address:")
            filter.replace("bsnRogueAPAirespaceAPName.0", "Rogue AP name:")

            filter.replace("bsnImpersonatedAPMacAddr.0", "AP MAC address:")
            filter.replace("bsnImpersonatingSourceMacAddr.0","AP Source MAC adress:")
            
            
            filter.replace("cLApName.", "AP name: ")
            filter.replace("cLApSysMacAddress.0", "System rogue AP MAC address:")
            filter.replace("cLApName.0", "AP name:")
            filter.replace("cLApEthernetIfSlotId.0", "Slot ID:")
            filter.replace("cLApRSSI.0", "RSSI:")
            filter.replace("cLApSNR.0","SNR:")
            
            filter.replace("cLApAdhocRogue.0", "Rogue Adhoc:")
            filter.replace("cLApRogueApMacAddress.0", "Rogue AP MAC address:")
            filter.replace("cLApRogueDetectedChannel.0 Wrong Type (should be Gauge32 or Unsigned32):", "Detected channel:")
            filter.replace("cLApRogueAPOnWiredNetwork.0", "Rogue AP on wired network:")
            filter.replace("cLApRogueApSsid.0", "Rogue SSID:")
            filter.replace("cLApRogueClassType.0", "Class type:")
            filter.replace("cLApRogueMode.0", "Rogue mode:")
            filter.replace("cLApRogueIsClassifiedByRule.0", "Is classified by rule?:")
            filter.replace("cLApRogueClassifiedApMacAddress.0", "Classified rogue AP MAC address:")
            filter.replace("cLApRogueClassifiedRSSI.0", "Classified rogue AP RSSI:")
            filter.replace("cLApSeverityScore.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity score:")
            filter.replace("cLApRuleName.0", "Rule name:")
           
            filter.replace("cLApDot11IfSlotId.0","AP interface slot ID:")
            filter.replace("cLApDot11IfType.0", "Type:")
            filter.replace("cLApDot11IfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32)", "AP interface slot ID:")
            
            
            
            
            filter.replace("clrRrmApTransmitPowerLevel.0", "Controller AP power level:")
            filter.replace("clrRrmTimeStamp.0 Wrong Type (should be Timeticks)","Controller AP timestamp:")
            filter.replace("clrRrmClientType.0","Controller AP client type:")
            filter.replace("clrRrmRssiHistogramLength.0 Wrong Type (should be Gauge32 or Unsigned32)", "RSSI histogram length:")
            filter.replace("clrRrmRssiHistogramMaxIndex.0","RSSI histogram max:")
            filter.replace("clrRrmRssiHistogramMinIndex.0","RSSI histogram min:")
            filter.replace("clrRrmRssiHistogramValues.0","RSSI histogram values:")
            filter.replace("clrRrmNeighborApCount.0 Wrong Type (should be Gauge32 or Unsigned32)","Controller neighbor AP count: ")
            filter.replace("clrRrmNeighborApMacAddress.0", "Neighbor AP MAC address:")
            filter.replace("clrRrmNeighborApRssi.0", "Neighbor AP RSSI:")
            filter.replace("clrRrmNeighborApIfType.0", "Neighbor AP interface type:")

            filter.replace("cLWlanChdEnable.1", "Wlan channel enable:")
            filter.replace("cLWlanChdEnable.2","WLAN channel enable:")

            

            filter.replace("cLRogueClientTotalDetectingAPs.0", "Total rogue AP:")
            filter.replace("cLRogueClientFirstReported.0","First report:")
            filter.replace("cLRogueClientLastReported.0","Last report:")
            filter.replace("cLRogueClientGatewayMac.0","Rogue gateway MAC address:")
            
            
        
            filter.replace("cLSiIdrDeviceId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device ID:")
            filter.replace("cLSiIdrDeviceType.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device type:")
            filter.replace("cLSiIdrAffectedChannels.0 Wrong Type (should be OCTET STRING):", "Affected channels:")
            filter.replace("cLSiIdrSeverity.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity:")
            filter.replace("cLSiIdrClusterId.0", "Cluster ID:") 
            filter.replace("cLSiAlarmClear.0", "Alarm clear:")
            filter.replace("cLSiIdrPreviousClusterId.0", "Previous cluster ID:")

            
            
            filter.replace("AP Name: .","AP name:")
            filter.replace("Client username:0", "Client username:")
            filter.replace("cLLastDetectingRadioMACAddress.0", "Last detecting radio MAC address:") 
            filter.replace("AP Name:0", "AP name:")

            filter.replace("'","")
            filter.replace("...","")
            filter.replace("..","")
            filter.replace("=","")
            filter.replace("^","")
            filter.replace("]","")
            filter.replace("[","")
            filter.replace(".Z.","")
            filter.replace("o1","")
            filter.replace("\\","")
            filter.replace("Q","")
            filter.replace("$","")
            filter.replace("hT.","")
            filter.replace(".Nj.","")
            filter.replace(".N","")
            filter.replace("<","")
            filter.replace(".g?","")
            filter.replace("?","")
            filter.replace(":f ", ":")
            
            filter.replace(".N.","")
            filter.replace(".NN.","")
            filter.replace("D-","")
            filter.replace("-","")
            filter.replace("_","")
            filter.replace(".s","")
            filter.replace("}","")
            
            filter.replace("@","")
            filter.replace(".A","")
            filter.replace("p.","")
            filter.replace("Z.","")
            filter.replace(".lc","")
            filter.replace(".Ni.","")
            filter.replace("&","")
             

            
           
            
          

            #final result
            Result  = filter            
            output.write(Result + "\n")
           

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
