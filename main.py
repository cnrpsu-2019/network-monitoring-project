import subprocess
import filterString
import createFiles
import ExportToDB
import Extract
import B612
import AutoLogin

def main():
    running = True
    output = open(createFiles.realFile,'a')
    while running:
        try:
            raw_input = input() #receive input
            #replace string
            result = filterString.filter_string(raw_input)
            #write to local server
            if result is 'UDP: 172.30.232.2:32768-172.30.232.250:162': #coe wlc
                ExportToDB.uptime_wlc('172.30.232.2 - CoE',B612.uptime_instance)
            elif result is 'UDP: 172.31.253.2:32769-172.30.232.250:162': #eng psu
                ExportToDB.uptime_wlc('172.30.253.2 - EnG',B612.uptime_instance)

            output.write(result +'\n')
        except EOFError:
            running = False
    output.close()

if __name__ == '__main__':
    main()
    #login into outside world
    AutoLogin.check_and_login()    
    # B612.uptime_instance()
    B612.rogue_ssid_detected()
    B612.activity_users()
    B612.deauth_users()
