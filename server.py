#--*-- coding:utf-8 --*--
#!/usr/bin/env python

import socket,time

host = socket.gethostbyname(socket.gethostname())   #Define the default network interfce
print(host)
port= 1234

print("Création du serveur...")
time.sleep(1)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation of the socket
s.bind((host,port))                                 #Binding the host & port
time.sleep(1)
print("En attentes de connexion")
s.listen(1)                                         #Listening for connections
client,adresse=s.accept()                           #Define the 'client & adres' variable to the connection socket
print(adresse)
print( "une connexion s'est effectuee depuis "),
print( client.getpeername())                        #Print the client informations
client.close()                                      #Close the client socket
s.close()                                           #Close the socket