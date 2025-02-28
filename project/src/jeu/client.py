# coding: utf-8



 # Définition d'un client réseau rudimentaire
 # Ce client dialogue avec un serveur ad hoc

import socket, sys
HOST = '192.168.1.18' #il faut mettre l'adresse IP du SERVEUR ici
PORT = 50000

 # 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) envoi d'une requête de connexion au serveur :
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print ("La connexion a échoué.")
    sys.exit()    
print ("Connexion établie avec le serveur.")    



# 3) Dialogue avec le serveur :
msgServeur = mySocket.recv(1024).decode()

while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    print ("S>", msgServeur)
    msgClient = input()
    mySocket.send(msgClient.encode())
    msgServeur = mySocket.recv(1024).decode()

# 4) Fermeture de la connexion :
print ("Connexion interrompue.")
mySocket.close()