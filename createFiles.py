import datetime

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y") #day-month-year
path = '/home/bass/receive/'
fileName = "trapd-" + fileDate + ".log"


sampleFile = 'trapd-05-Apr-2020.log'