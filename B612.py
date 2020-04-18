import createFiles
import Extract
import ExportToDB
import MacList
import collections
import re

def uptime_instance():
    #uptime instance
    uptime = Extract.extractSpecific(createFiles.realFile,'UpTimeInstance').replace('UpTimeInstance','')
    pattern = re.compile(r'(?:[0-9]:?){6}')
    uptime_non_zero = re.findall(pattern,uptime) #filter 0 out
    #pick last element in list
    lastet_uptime = uptime_non_zero[-1]

    ExportToDB.uptime_instance(lastet_uptime)

def active_user_cummulate():
    username_ext = Extract.username_extract(whole_file).replace('Username','').split()
    unique_users = int(len(list(set(username_ext))) * 0.85)
    #send to database
    ExportToDB.active_users_coarse(unique_users)