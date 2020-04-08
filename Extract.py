import re

def listDuplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

def compileMacPattern(receive):
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    resultMac = re.findall(pattern, str(receive)) #now there's only list of mac addresses
    return resultMac

def extractSpecific(path, keyword):
    output = ''
    with open(path,'r') as f:
        for line in f:
            line = line.rstrip()
            if re.search(keyword, line):
              output += line.replace(keyword,'')
    f.close()
    return output