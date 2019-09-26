import datetime

def main():
    running = True
    now = datetime.datetime.now()
    strnow = now.strftime("%X : ") #current time
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/trap-receiver/' + fileName, 'a')
    while running:
        try:
            input = raw_input()
            output.write(strnow + input.replace("<UNKNOWN>", "-------------------------------") + "\n")
        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
