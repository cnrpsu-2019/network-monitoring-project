import re

def main():
    readTest = open('example.log','r')
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}') #compile mac address pattern xx:xx:xx:xx:xx:xx
    txt = readTest.read() #raw txt files

    resultMac = re.findall(pattern, txt) #now there's only list of mac addresses
    print(resultMac)
    #close file
    readTest.close()
if __name__ == "__main__":
    main() 
    
#add mac address to regcognize use