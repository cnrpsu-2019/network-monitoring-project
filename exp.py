import datetime
import re

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
            filtered = input.translate("<UNKNOWN>","")
            #final result
            Result  = filtered           
            output.write(Result + "\n")
           

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
