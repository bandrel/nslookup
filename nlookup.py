__author__ = 'jubi'
import socket
import sys


with open(sys.argv[1]) as file:
        for line in file:
            try:
                host,empty,ip = socket.gethostbyaddr(line.strip('\r\n'))
                print host + '\t' + ip[0]
            except:
                print "none found for %s" % line.strip('\r\n')
                pass




