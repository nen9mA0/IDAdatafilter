import re
import getopt
import sys

myinput = []
data = []
regex = "\\bdb\s+[0-9A-F]+h?"
numregex = "(db\s+)([0-9A-F]+)"
pystringstyle = False

def replace():
    if pystringstyle == True:
        for i in range(0,len(data)):
            data[i] = re.sub("0x","\\x",data[i])
        print "".join(data)
        exit(0)

def isdata(line):
    try:
        cache = re.search(regex,line).group()
    except:
        return False
    return True

def isstack(line):
    myregex = "(v[0-9A-F]+\s+=\s+)([0-9A-Fx]+)u?;"
    try:
        cache = re.search(myregex,line).group()
    except:
        return False
    return True

def handledata(line):
    try:
        while line != "":
            cache = re.search(regex,line).group()
            if cache != None:
                myinput.append(cache)
            line = raw_input()
    except EOFError:
        pass

    n = 0
    for i in myinput:
        cache = pattern.match(i).group(2)
        if len(cache)>2:
            cache = cache[1:]
        elif len(cache)<2:
            cache = '0'+cache
        data.append("0x"+cache)
        n+=1

    replace()
    print ",".join(data)
    print "count:",n
    return 0

def handlestack(line):
    myregex = "(v[0-9A-F]+\s+=\s+)(-?[0-9A-Fx]+)u?;"
    try:
        while line != "":
            cache = re.search(myregex,line).group(2)
            if cache != None:
                myinput.append(cache)
            line = raw_input()
    except:
        pass

    replace()
    print ",".join(myinput)
    return 0


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'cph', ['cstyle', 'pystyle','help'])
    for key,value in opts:
        if key in ['-c','--cstyle']:
            pystringstyle = False
        if key in ['-p','--pystyle']:
            pystringstyle = True
        if key in ['-h','--help']:
            print "Usage:"
            print "-c  --cstyle\tcstyle"
            print "-p  --pystyle\tpystyle"
            exit(0)
    pattern = re.compile(numregex) 
    line = raw_input()
    if isdata(line) == True:
        handledata(line)
    elif isstack(line) == True:
        handlestack(line)