import re
import MacList


def listDuplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)


def compileMacPattern(receive):
    pattern = re.compile(r'(?:[0-9a-f]:?){12}')
    # now there's only list of mac addresses
    resultMac = re.findall(pattern, str(receive))
    return resultMac


def extractSpecific(path, keyword):
    output = ''
    with open(path, 'r') as f:
        for line in f:
            line = line.rstrip()
            if re.search(keyword, line):
                output += line
    f.close()
    return output


def client_mac(path):
    raw_mac = extractSpecific(path, 'MacAddress')
    pure_mac = compileMacPattern(raw_mac)
    # differenciate between client and ap mac_address
    client_mac = list(set(pure_mac) - set(MacList.buildingMacList))

    return client_mac  # return unique mac addresses
