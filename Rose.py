#import modules
import Extract, createFiles, time, ExportToDB
import sched as sc

schedule = sc.scheduler(time.time, time.sleep)
status = Extract.extractSpecific(createFiles.realFile,'Event').split('Event')[-1].strip()

'''
def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    s.enter(60, 1, do_something, (sc,))
    scheduler.enter(delay, priority, action, argument=(), kwargs={}) 
s.enter(60, 1, do_something, (s,))
s.run()

'''

def harvest(): #collect user by mac address
    curr_mac = Extract.client_mac(createFiles.realFile) #collect all mac addresses 
    total_user = int(len(curr_mac))
    ExportToDB.harvest_user(total_user)

if __name__ == '__main__':
    schedule.enter(300,1,harvest())
    schedule.enter(100,1,harvest())