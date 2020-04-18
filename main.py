import subprocess
import filterString
import createFiles
import ExportToDB
import Extract
import B612

def main():
    running = True
    output = open(createFiles.realFile,'a')
    while running:
        try:
            raw_input = input() #receive input
            #replace string
            result = filterString.filter_string(raw_input)

            username_ext = Extract.username_extract(result).replace('Username','').split()
            unique_users = int(len(list(set(username_ext))) * 0.85)
            ExportToDB.active_users_coarse(unique_users)
            
            #extract username
            #write to local
            output.write(result +'\n')
           
        except EOFError:
            running = False
    output.close()
    subprocess.call(['sed','-i','/.*SessionID.*/d',createFiles.realFile])

if __name__ == '__main__':
    main()
    B612.seek_and_destroy()
