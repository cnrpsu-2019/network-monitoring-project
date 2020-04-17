import createFiles
import Extract
import ExportToDB
import MacList
import collections
import re

def seek_and_destroy():
    #uptime instance
    uptime = Extract.extractSpecific(createFiles.realFile,'UpTimeInstance').replace('UpTimeInstance','')
    pattern = re.compile(r'(?:[0-9]:?){6}')
    uptime_non_zero = re.findall(pattern,uptime) #filter 0 out
    #pick last element in list
    lastet_uptime = uptime_non_zero[-1]

    ExportToDB.uptime_instance(lastet_uptime)