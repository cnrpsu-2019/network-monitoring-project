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
            if result == 'UDP: 172.30.232.2:32768-172.30.232.250:162': #coe wlc
                coe_wlc = Extract.extractSpecific(createFiles.realFile,'UpTimeInstance').replace('UpTimeInstance','').split()[-2]
                ExportToDB.uptime_wlc('172.30.232.2 - CoE',coe_wlc)
            elif result == 'UDP: 172.31.253.2:32769-172.30.232.250:162': #eng psu
                eng_psu = Extract.extractSpecific(createFiles.realFile,'UpTimeInstance').replace('UpTimeInstance','').split()[-2]
                ExportToDB.uptime_wlc('172.30.253.2 - EnG',eng_psu)

            output.write(result +'\n')
        except EOFError:
            running = False
    output.close()

if __name__ == '__main__':
    main()
    AutoLogin.check_and_login()  #login into outside world    
    B612.rogue_ssid_detected()
    B612.activity_users()
    B612.deauth_users()
    B612.eng_users_details()