# coding: utf-8

from project.src.interfaces.interfaceJeu.InterfaceJeuReseau import InterfaceJeuReseau

from project.src.reseau.jeuReseau import JeuReseau


# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc
import json
import socket, sys
from project.src.interfaceReseau.testInterface import fenetre
# HOST = '172.24.95.68' #il faut mettre l'adresse IP du SERVEUR ici
PORT = 52001

from project.src.reseau.jeuReseau import JeuReseau

def f(adresse_ip:str, pseudo):
    # 1) création du socket :
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2) envoi d'une requête de connexion au serveur :
    try:
        mySocket.connect((adresse_ip, PORT))
    except socket.error:
        print ("La connexion a échoué.")
        sys.exit()    
    print ("Connexion établie avec le serveur.")    
    
    
    # 3) Dialogue avec le serveur :

    #reception fichier json
    msgServeurFichierJson = mySocket.recv(1024).decode()
    print("S> ", type(msgServeurFichierJson), msgServeurFichierJson)


    #envoi pseudo joueur guest:
    mySocket.send(pseudo.encode())


    #reception pseudo joueur host:
    msgServeurPseudo = mySocket.recv(1024).decode()

    
    print("...lecture du fichier")
    a_file = open(f"ressources/JSON/{msgServeurFichierJson}", "r", encoding='utf-8')
    lignes = a_file.read()
    
    print("...converstion du string en dictionaire")
    j = json.loads(lignes)
    
    jeu = JeuReseau(mySocket, j["metadonnees"])
    jeu.remplissage_planche(j["possibilites"])
    print(f"{jeu=}")

    # 3bis) Plus de dialogue
    fen = InterfaceJeuReseau(jeu, msgServeurPseudo)

    fen.title("Qui-est-ce? (client)")

    fen.style.theme_use("clam")

    fen.launch()
    
    
    # 4) Fermeture de la connexion :
    print ("Connexion interrompue.")
    mySocket.close()
    
state = 0

"""

argv 0 : guest.py
     1 : adress ip
     2 : pseudo

"""




def main():
    print(sys.argv)
    if len(sys.argv) != 3:
        raise Exception("mauvais nombre d'arguments")
    else:        
        print(f"{sys.argv[1]=}")
        f(sys.argv[1], sys.argv[2])
    
main()


