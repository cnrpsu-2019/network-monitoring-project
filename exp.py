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

            
          
            input.replace("DISMAN-EVENT-MIB::sysUpTimeInstance", "System Uptime (Day:Hour:Minutes:Second):")
            input.replace("AIRESPACE-WIRELESS-MIB::", "")
            input.replace("CISCO-LWAPP-DOT11-CLIENT-MIB::", "")

            input.replace("CISCO-LWAPP-AP-MIB::", "")
            input.replace("SNMPv2-MIB::snmpTrapOID.0", "Trap event:"+ strnow +" ==>" )
            input.replace("CISCO-LWAPP-RRM-MIB::", "")
            input.replace("CISCO-LWAPP-RRM-MIB::", "")
            input.replace("CISCO-LWAPP-WLAN-MIB::", "")
            input.replace("CISCO-LWAPP-ROGUE-MIB::", "")
            input.replace("CISCO-LWAPP-SI-MIB::", "")
            
            
            input.replace("cldcClientByIpAddressType.0", "IP address type:")
            input.replace("cldcClientUsername.", "Client username:")
            input.replace("cldcClientSSID.0", "Client SSID:")
            input.replace("cldcApMacAddress.", "AP MAC address:")
            input.replace("cldcClientByIpAddress.0", "Client by IP address:")
            input.replace("cldcClientSessionID.", "Client session ID:")
            input.replace("cldcClientIPAddress.0","Client IP address:")
            input.replace("cldcClientMacAddress.0", "Client MAC address:")
            input.replace("cldcIfType.0", "Client interface type:")
            input.replace("cldcClientSSID.", "Client SSID:")

           
            input.replace("bsnUserIpAddress.0", "Client IP address:")
            input.replace("bsnStationAPMacAddr.0", "AP MAC address:")
            input.replace("bsnStationAPIfSlotId.0", "AP slot ID:")
            input.replace("bsnStationReasonCode.0", "Reason code:")
            input.replace("bsnStationUserName.0", "Client username:")
            input.replace("bsnStationMacAddress.0", "Client MAC address:")
            input.replace("bsnStationBlacklistingReasonCode.0", "Blacklisted reason:")


            input.replace("bsnAPName.0", "AP Name:")
            input.replace("bsnAPIfType.0","AP interface type:")
            input.replace("bsnAPDot3MacAddress.", "AP MAC address:")
            input.replace("bsnAPIfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "AP interface slot ID:")
            input.replace("bsnAuthFailureUserType.0", "User type:")
            input.replace("bsnAuthFailureUserName.0","Username:")

            input.replace("bsnRogueAPDot11MacAddress.0","(Dot11)Rogue AP MAC address:")
            input.replace("bsnRogueAPAirespaceAPMacAddress.0", "(Airespace)Rogue AP MAC address")
            input.replace("bsnRogueAPAirespaceAPSlotId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Rogue AP slot ID:")
            input.replace("bsnRogueAPRadioType.0", "Rogue AP radio type:")
            input.replace("bsnRogueAPAirespaceAPMacAddress.0","(Airespace)Rogue AP MAC address:")
            input.replace("bsnRogueAPAirespaceAPName.0", "Rogue AP name:")

            input.replace("bsnImpersonatedAPMacAddr.0", "AP MAC address:")
            input.replace("bsnImpersonatingSourceMacAddr.0","AP Source MAC adress:")
            
            
            input.replace("cLApName.", "AP name: ")
            input.replace("cLApSysMacAddress.0", "System rogue AP MAC address:")
            input.replace("cLApName.0", "AP name:")
            input.replace("cLApEthernetIfSlotId.0", "Slot ID:")
            input.replace("cLApRSSI.0", "RSSI:")
            input.replace("cLApSNR.0","SNR:")
            
            input.replace("cLApAdhocRogue.0", "Rogue Adhoc:")
            input.replace("cLApRogueApMacAddress.0", "Rogue AP MAC address:")
            input.replace("cLApRogueDetectedChannel.0 Wrong Type (should be Gauge32 or Unsigned32):", "Detected channel:")
            input.replace("cLApRogueAPOnWiredNetwork.0", "Rogue AP on wired network:")
            input.replace("cLApRogueApSsid.0", "Rogue SSID:")
            input.replace("cLApRogueClassType.0", "Class type:")
            input.replace("cLApRogueMode.0", "Rogue mode:")
            input.replace("cLApRogueIsClassifiedByRule.0", "Is classified by rule?:")
            input.replace("cLApRogueClassifiedApMacAddress.0", "Classified rogue AP MAC address:")
            input.replace("cLApRogueClassifiedRSSI.0", "Classified rogue AP RSSI:")
            input.replace("cLApSeverityScore.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity score:")
            input.replace("cLApRuleName.0", "Rule name:")
           
            input.replace("cLApDot11IfSlotId.0","AP interface slot ID:")
            input.replace("cLApDot11IfType.0", "Type:")
            input.replace("cLApDot11IfSlotId.0 Wrong Type (should be Gauge32 or Unsigned32)", "AP interface slot ID:")
            
            
            
            
            input.replace("clrRrmApTransmitPowerLevel.0", "Controller AP power level:")
            input.replace("clrRrmTimeStamp.0 Wrong Type (should be Timeticks)","Controller AP timestamp:")
            input.replace("clrRrmClientType.0","Controller AP client type:")
            input.replace("clrRrmRssiHistogramLength.0 Wrong Type (should be Gauge32 or Unsigned32)", "RSSI histogram length:")
            input.replace("clrRrmRssiHistogramMaxIndex.0","RSSI histogram max:")
            input.replace("clrRrmRssiHistogramMinIndex.0","RSSI histogram min:")
            input.replace("clrRrmRssiHistogramValues.0","RSSI histogram values:")
            input.replace("clrRrmNeighborApCount.0 Wrong Type (should be Gauge32 or Unsigned32)","Controller neighbor AP count: ")
            input.replace("clrRrmNeighborApMacAddress.0", "Neighbor AP MAC address:")
            input.replace("clrRrmNeighborApRssi.0", "Neighbor AP RSSI:")
            input.replace("clrRrmNeighborApIfType.0", "Neighbor AP interface type:")

            input.replace("cLWlanChdEnable.1", "Wlan channel enable:")
            input.replace("cLWlanChdEnable.2","WLAN channel enable:")

            

            input.replace("cLRogueClientTotalDetectingAPs.0", "Total rogue AP:")
            input.replace("cLRogueClientFirstReported.0","First report:")
            input.replace("cLRogueClientLastReported.0","Last report:")
            input.replace("cLRogueClientGatewayMac.0","Rogue gateway MAC address:")
            
            
        
            input.replace("cLSiIdrDeviceId.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device ID:")
            input.replace("cLSiIdrDeviceType.0 Wrong Type (should be Gauge32 or Unsigned32):", "Device type:")
            input.replace("cLSiIdrAffectedChannels.0 Wrong Type (should be OCTET STRING):", "Affected channels:")
            input.replace("cLSiIdrSeverity.0 Wrong Type (should be Gauge32 or Unsigned32):", "Severity:")
            input.replace("cLSiIdrClusterId.0", "Cluster ID:") 
            input.replace("cLSiAlarmClear.0", "Alarm clear:")
            input.replace("cLSiIdrPreviousClusterId.0", "Previous cluster ID:")

            
            
            input.replace("AP Name: .","AP name:")
            input.replace("Client username:0", "Client username:")
            input.replace("cLLastDetectingRadioMACAddress.0", "Last detecting radio MAC address:") 
            input.replace("AP Name:0", "AP name:")

            input.replace("'","")
            input.replace("...","")
            input.replace("..","")
            input.replace("=","")
            input.replace("^","")
            input.replace("]","")
            input.replace("[","")
            input.replace(".Z.","")
            input.replace("o1","")
            input.replace("\\","")
            input.replace("Q","")
            input.replace("$","")
            input.replace("hT.","")
            input.replace(".Nj.","")
            input.replace(".N","")
            input.replace("<","")
            input.replace(".g?","")
            input.replace("?","")
            input.replace(":f ", ":")
            
            input.replace(".N.","")
            input.replace(".NN.","")
            input.replace("D-","")
            input.replace("-","")
            input.replace("_","")
            input.replace(".s","")
            input.replace("}","")
            
            input.replace("@","")
            input.replace(".A","")
            input.replace("p.","")
            input.replace("Z.","")
            input.replace(".lc","")
            input.replace(".Ni.","")
            input.replace("&","")
            input.replace("<UNKNOWN>","") 

            
           
            
          

            #final result
            Result  = input            
            output.write(Result + "\n")
           

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
