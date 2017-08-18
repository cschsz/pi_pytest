import socket

plist = [22, 4711]
done = 0

#----------------------------[main]
def connect(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        #print ip + " auf Port " + str(port) +  " nicht erreicht"
        return

#----------------------------[main]
print "running"
for x in range(105,107):
    ip = "192.168.1." + str(x)
    for port in plist:
        erg = connect(ip, port)
        if erg:
            print "Treffer auf " + ip + ":" + str(port)
            done = 1
            break
        if done:
            break

