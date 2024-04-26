# coding: utf-8

# Définition d'un serveur réseau rudimentaire
# # Ce serveur attend la connexion d'un client, pour entamer un dialogue avec lui

import json
import os
import socket, sys

HOST = ''    # ça cible la machine elle même de faire ça (à ne pas modifier donc)
PORT = 50000   # de préférence une valeur supérieure à 1024 


def initialisation_serveur():
    # 1) création du socket :   (demande d'allocation de boite réseau si j'ai bien compris)
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2) liaison du socket à une adresse précise :
    try:
        mySocket.bind((HOST, PORT))
    except socket.error:
        print ("La liaison du socket à l'adresse choisie a échoué.")
        sys.exit()
    
    # 3) Attente de la requête de connexion d'un client :
    print ("Serveur prêt, en attente de requêtes ...")
    mySocket.listen(1)
    
    # 4) Etablissement de la connexion :
    connexion, adresse = mySocket.accept() #bloquant
    print ("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    
    return mySocket, connexion

        



state = 0
# file descriptors r, w for reading and writing
r, w = os.pipe()
r2, w2 = os.pipe()

pid = os.fork()
if pid == 0 :
    #child
    print("Child>", f"mon pid : {pid}")
    os.close(r)
    os.close(w2)
    w = os.fdopen(w, 'w')
    r2 = os.fdopen(r2)
    print("Child>", "Child writing")
    w.write("(yeux:noir)?")
    w.close()
    print("Child>", "Child reading")
    s = r2.read()
    print("text =", s)
    print("Child>", "Child closing")
else : #parent
    print("Parent>", f"pid de l'enfant : {pid}")
    
    mySocket, connexion = initialisation_serveur()
    
    # 5) Dialogue avec le client :
    connexion.send('{"config" : { "fichierJSON" :  "Json.json", "j1" : { "nom" : "Tony", "perso_mystere" : "Gobelin"} } }'.encode())
    msgClient = connexion.recv(1024).decode()

    j = json.loads(msgClient)
    print("C> ", type(j), j)


    # This is the parent process 
    # Closes file descriptor w
    os.close(w)
    os.close(r2)
    r = os.fdopen(r)
    w2 = os.fdopen(w2,'w')
    print("Parent>", "Parent reading")
    s = r.read()
    print("text =", s)
    print("Parent>", "Parent respondig")
    w2.write("Message reçu")
    connexion.send(s.encode())
    #parsing du text reçu

    # 6) Fermeture de la connexion :
    # connexion.send("Au revoir !".encode())
    print ("Connexion interrompue.")
    connexion.close()
            
    print("Fermeture du socket.")
    mySocket.close()

    sys.exit(0)
