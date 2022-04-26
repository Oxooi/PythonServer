#-*- coding:utf-8
#!/usr/bin/env python

import socket
host = raw_input("Entrez l'IP : ")
port = 80
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Creation of the socket
print("Socket Fait")
print("Connexion a l'host distant")
s.connect((host,port))                                  #Connection to the host 
print("Connexion faite")