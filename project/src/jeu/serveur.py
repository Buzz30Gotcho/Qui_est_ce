# coding: utf-8

 # Définition d'un serveur réseau rudimentaire
 # # Ce serveur attend la connexion d'un client, pour entamer un dialogue avec lui

import socket, sys

HOST = ''    # ça cible la machine elle même de faire ça (à ne pas modifier donc)
PORT = 50000   # de préférence une valeur supérieure à 1024 


 # 1) création du socket :   (demande d'allocation de boite réseau si j'ai bien compris)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2) liaison du socket à une adresse précise :
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print ("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    # 3) Attente de la requête de connexion d'un client :
    print ("Serveur prêt, en attente de requêtes ...")
    mySocket.listen(5)
    
    # 4) Etablissement de la connexion :
    connexion, adresse = mySocket.accept()
    print ("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    
    # 5) Dialogue avec le client :
    connexion.send("Vous êtes connecté au serveur Marcel. Envoyez vos messages.".encode())
    msgClient = connexion.recv(1024).decode()
    while 1:     #Lignes 54 à 60 : Cette nouvelle boucle sans fin maintient le dialogue jusqu'à ce que le client décide d'envoyer le mot « fin » ou une simple chaîne vide. Les écrans des deux machines afficheront chacune l'évolution de ce dialogue.
        print(msgClient) 
        if msgClient.upper() == "FIN" or msgClient =="":
            break
        msgServeur = input()
        connexion.send(msgServeur.encode())
        msgClient = connexion.recv(1024).decode()

    # 6) Fermeture de la connexion :
    connexion.send("Au revoir !")
    print ("Connexion interrompue.")
    connexion.close()

    ch = input("<R>ecommencer <T>erminer ? ")
    if ch.upper() =='T':
        break