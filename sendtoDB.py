import datetime
import re
import string
# import yaml
import sys
import Filterx

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString     

def main():
    running = True
    now = datetime.datetime.now()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    readFile = open('/home/bass/trap-receiver/' + fileName, 'r')
    
    while running:
        try:
            readInput = readFile.read()
            filtered = readInput.replace("<UNKNOWN>","" )
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)
            wrongtypeRemove = replaceMultiple(showDate, Filterx.wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"
            #outstr
            outstr  = weirdRemove.translate(None, bad_chars)
            result = replaceMultiple(outstr,Filterx.bad_list,' ')
               
        except EOFError:
            running = False
    print(result + '\n')
    readInput.close()
if __name__ == '__main__':
    main()