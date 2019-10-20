import datetime
now = datetime.datetime.now()
fileDate = now.strftime("%d-%b-%Y")
fileName = "trapd-" + fileDate + ".log"
output = open('/home/bass/trap-receiver/' + fileName, 'r')
output.readline()
