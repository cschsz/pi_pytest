# call with "python scanner.py SSH"
import socket
import sys

plist = [21, 22, 25, 80, 110]

#----------------------------[checkip]
def interpret(data, prot):
    if prot in data:
        return "Protocoll " + prot + " found"
    else:
        return data

#----------------------------[checkip]
def checkip(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip, port))
        erg = s.recv(1024)
        return erg 
    except Exception, e:
        print ip + ":" + str(port) +  " - " + str(e)
        return

#----------------------------[main]
def checkparm():
    if len(sys.argv) != 2:
        print "parameter missing"
        return 1
    return 0

#----------------------------[main]
def main():
    if checkparm() != 0:
        return

    print "running"

    done = 0
    for x in range(105,107):
        ip = "192.168.1." + str(x)
        for port in plist:
            erg = checkip(ip, port)
            if erg:
                erg = interpret(erg, sys.argv[1])
                print ip + ":" + str(port) + " - " + erg
                done = 1
                break

            if done:
                break

#----------------------------[]
if __name__ == "__main__":
    main()
