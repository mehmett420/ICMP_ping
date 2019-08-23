import socket
import sys
import os

import time
s = socket.socket(socket.AF_INET, socket.SOCK_RAW,1)
ip = ("IP ADDRESS",3000)
s.bind(ip)
#rep = os.system("ping  "+ server_ip)
print("Connecting..")

while True:
    #time.sleep(2)
    data = s.recv(1024)
    if not data:

        break
    else:
        print(data)
        if "DONE" == data:
            break
            s.close()
