import subprocess
import collections
import filterString
import createFiles

def main():
    output = open( createFiles.path + createFiles.fileName, 'a') #write into local server
    while True:
        try:
            input_raw = input()
            result = filterString.filter_string(input_raw)
            #write to local serever
            output.write(result + '\n')
        except EOFError:
            break
        finally:
            subprocess.call(['sed','-i','/.*SessionID.*/d',createFiles.path + createFiles.fileName])
            output.close
            
if __name__ == '__main__':
    main()