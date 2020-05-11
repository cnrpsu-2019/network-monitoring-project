import subprocess
import filterString
import createFiles
import ExportToDB
import Extract
import B612
import AutoLogin
import Rose

def main():
    running = True
    output = open(createFiles.realFile,'a')
    while running:
        try:
            raw_input = input() #receive input
            #replace string
            result = filterString.filter_string(raw_input)
            #write to local server
            output.write(result +'\n')
           
        except EOFError:
            running = False
    output.close()
    # subprocess.call(['sed','-i','/.*SessionID.*/d',createFiles.realFile])

if __name__ == '__main__':
    main()
    #login into outside world
    AutoLogin.check_and_login()
    
    B612.uptime_instance()
    B612.rogue_ssid_detected()
    B612.activity_users()
    B612.deauth_users()
    #Rose.harvest_user()
