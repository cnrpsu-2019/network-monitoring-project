import Filterx

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return  mainString

def filter_string(input_raw):    
    #filter weird string sction
    filtered = input_raw.replace("<UNKNOWN>","" )
    wrongtypeRemove = replaceMultiple(filtered, Filterx.wronglist, '')
    timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
    hideMIB = replaceMultiple(timestamp, Filterx.mibList, '')
    event = hideMIB.replace("snmpTrapOID","Event")
    prefixRemove = replaceMultiple(event, Filterx.prefixList, '')
    weirdRemove = replaceMultiple(prefixRemove, Filterx.weirdList, ' ')
    bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"
    outstr  = replaceMultiple(weirdRemove,bad_chars,'') #outstr - write log files into local server
    result = replaceMultiple(outstr,Filterx.bad_list,' ')   

    return result
