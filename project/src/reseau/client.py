# coding: utf-8



# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc
import json
import socket, sys
HOST = '172.24.94.139' #il faut mettre l'adresse IP du SERVEUR ici
PORT = 50000

def main():
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
    
    j = json.loads(msgServeur)
    print("S> ", type(j), j)
    
    j["config"]["j2"] = '{ "nom" : "Romain", perso_mystere : "Archer"}'
    
    mySocket.send(json.dumps(j).encode())
    
    msgServeur = mySocket.recv(1024).decode()
    print("C> ", msgServeur)
    
    # 4) Fermeture de la connexion :
    print ("Connexion interrompue.")
    mySocket.close()
    
state = 0
main()
    

