import datetime

now = datetime.datetime.now()
strnow = now.strftime("%X") #current time
#log file date
fileDate = now.strftime("%d-%b-%Y") #day-month-year
path = '/home/bass/receive/'
fileName = "trapd-" + fileDate + ".log"

realFile = path + fileName
sampleFile = 'example.log'