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
    B612.uptime_instance()