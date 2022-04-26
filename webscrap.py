#-*- coding:utf-8
#!/usr/bin/env python

import socket
from time import sleep
host = raw_input("Enter the IP or URL : ")
req = raw_input("Enter the name of the page :")
port = 80
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Creation of the socket
print("The socket has been created")
print("Connection to the distant host")
sleep(1)
s.connect((host,port))                                  #Connection to the host 
print("Connection established")
s.send("GET /" + req + " HTML/1.1\r\n\r\n")             #Send a request to grab the page
while 1:
    data=s.recv(128)                                    #Grab the answer 
    print(data)                                         #Print the answer
    if(data == ""):
        break
s.close()                                               #Close the socket