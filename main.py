import subprocess
import collections
import filterString
import createFiles
import B612

def main(): #this shit is receive, filter string and write into a local server
    output = open( createFiles.path + createFiles.fileName, 'a') #write into local server
    while True:
        try:
            input_raw = input()
            result = filterString.filter_string(input_raw)
            #write to local serever
            output.write(result + '\n')
        except EOFError:
            break
            output.close
        finally:
            subprocess.call(['sed','-i','/.*SessionID.*/d',createFiles.path + createFiles.fileName])
            B612.seek_and_destroy()
            
if __name__ == '__main__':
    main()
