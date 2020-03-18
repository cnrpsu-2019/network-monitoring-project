import re
import datetime
import time

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
path = '/home/bass/receive/'
fileDate = now.strftime("%d-%b-%Y")
fileName = path + 'trapd-' + fileDate + '.log'
sample = 'example.log'

def main():
    readTest = open(fileName,'r')
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}') #compile mac address pattern xx:xx:xx:xx:xx:xx
    txt = readTest.read() #raw txt files
    while True:
        try:
            resultMac = re.findall(pattern, txt) #now there's only list of mac addresses
            if not resultMac:
                time.sleep(1)
            print(resultMac)
        except EOFError:
            break
        finally:
            #close file
            readTest.close()
if __name__ == "__main__":
    main() 
    
#add mac address to regcognize use
