import datetime
import json

def main():
    running = True
    now = datetime.datetime.now()
    #strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    input = open('/home/bass/trap-receiver/' + fileName, 'r')

    while running:
        try:
            print(input.readline)
        except EOFError:
            running = False
    input.close()
if __name__ == '__main__':
    main()
    
