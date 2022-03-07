from ast import parse
import platform    # For getting the operating system name
import subprocess
from unicodedata import decimal
from time import sleep  # For executing a shell command

def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    #return subprocess.call(command) == 0
    """
    gopal@LX1E2-GPATIL:/mnt/c/Users/gpatil$ ping -c 1 google.com
    PING google.com (172.217.9.206) 56(84) bytes of data.
    64 bytes from iad30s14-in-f14.1e100.net (172.217.9.206): icmp_seq=1 ttl=57 time=81.0 ms

    --- google.com ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 81.049/81.049/81.049/0.000 ms    
    """
    p = subprocess.Popen(command, stdout = subprocess.PIPE)
    result = p.communicate()[0]
    #print(result)
    i1 = result.index(b'rtt min/')
    #print("index 1" , i1)
    s= b'rtt min/avg/max/mdev ='
    i2 = result.index(b' ms')
    #print("index 2" , i2)
    a = result[i1 + len(s):]
    #print(a)
    a2=a.split(b'/')
    #print(a2)
    #print(a2[1])
    return float(a2[1])
    

def getAvg(arr):
    print(arr) # comment this line to not printing array values 
    total = 0.0
    n=0
    for x in arr:
        if x > 0:
            n += 1
            total += x
    
    if n > 0:
        return total / n
    return 0.0

min1Max = 6
min5Max = 5
min1arr = [0] * min1Max
min5arr = [0] * min5Max
min1 = 0
min5 = 0
x = 1
try:
    while True:
    #explicit break after 1000 rounds
        if x > 1000:
            break
            
        x += 1
        #get current latency 
        avg = ping("www.google.com")
      
        min1 %= min1Max 
        min1arr[min1] = avg
        # 1 minute array - store average of 10 seconds in each index from 0-6 for 1 minutes
        avg1 = getAvg(min1arr)

        # 5 minutes array - store average of 1 minute in each index from 0-4 for 5 minutes
        min5 %= min5Max 
        min5arr[min5] = avg1
        
        avg5 = getAvg(min5arr)

        min5 += 1
        min1 += 1

        #display current latency, 1 minute average latency and 5 minutes average latency
        print("Current latency: ", avg, " 1 minutes average: ", avg1, " 5 minutes average: ", avg5, "  .....Press \"Ctrl + C\" to exit")
        
        #delay for 10 seconds 
        sleep(2)

#press any key to exit the loop
except KeyboardInterrupt:
    pass
