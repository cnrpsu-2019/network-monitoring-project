import datetime
import re
import string

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
    # strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/trap-receiver/' + fileName, 'a')
    
    while running:
        try:
            input = raw_input()
            filtered = input.replace("<UNKNOWN>","")
            dot0replace = filtered.replace(".0 ", ' ')
            wrongtypeRemove = dot0replace.replace("Wrong Type (should be Gauge32 or Unsigned32)","")
            mibList = ['CISCO-LWAPP-ROGUE-MIB::','AIRESPACE-WIRELESS-MIB::','CISCO-LWAPP-DOT11-CLIENT-MIB::','CISCO-LWAPP-AP-MIB::','CISCO-LWAPP-AP-MIB::']
            hideMIB = replaceMultiple(wrongtypeRemove, mibList, '')
            weirdList = ['.hx.F','..E.','.Tb','. ','.98y','.p.','.hx ','..o1','.XVM.','b.5.','.T','.Hn','.L','...0r','.A.','..A.','..0', '.gx.','.hx','.X','.i.','.W.g','.W','...j','.c ','.L','.    . ','.LkY ','... ','". ','"','..0','.p. ','.. ','. ','.M.',' : ','.c.q.','..p','..U','.hx','.pU.I','.H.0','v.','.. ','.j.','. ','.  ','..EB.M','Z','J','Q','..e.','..A.','..9.','.l.1.Fb','.p.','..x','..L.','.z.','..f','..N..j.','.i.', '.N.','.K','.h.','......','...','..','hx','wt','.o.']
            weirdRemove = replaceMultiple(hideMIB, weirdList, '')
            
            bad_chars = "/\\!$^&*|({)[}>_<]~+=#$%;`@?'"
            #rgx = re.compile('[%s]' % bad_chars)

            #final result
            result  = weirdRemove.translate(None, bad_chars)           
            output.write(result + "\n")

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
