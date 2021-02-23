#Omer Erbilgin
#Basic DDOS protection for vps

import os
import time

#config

#the maximum connection 
max = 100

#list of blocked ip addresses
blockedIpAddresses = []

#the connection num from a specific address
connectionNum = []

#list of connected ip addresses
ipList = []

#refresh rate
rRate = 3

while True:

#open file
    file = open('blockedIPs.txt','a')

#netstat
    netStatPrint = os.popen("netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r")

#set list
    ii = netStatPrint.read()
    l = list(ii.split())

#check connections from ip addresses
    for i in range(len(l)):
        if i % 2 == 0:
            connectionNum.append(l[i])
        else:
            ipList.append(l[i])
    for i, j in enumerate(connectionNum):
        if int(j) > max:
            if ipList[i] != '127.0.0.1' and ipList[i] not in blockedIpAddresses:
                print('%s blocked because of causing %d connections' % (ipList[i], int(j)))
                os.system(str('ufw insert 2 deny from %s' % ipList[i]))
                os.system(str('ufw reload'))
                blockedIpAddresses.append(ipList[i])
                file.write(ipList[i] + '\n')
    file.close()
    time.sleep(rRate)
