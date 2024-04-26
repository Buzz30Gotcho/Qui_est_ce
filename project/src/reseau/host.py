# coding: utf-8

# Définition d'un serveur réseau rudimentaire
# # Ce serveur attend la connexion d'un client, pour entamer un dialogue avec lui

import json
import os
import socket, sys


from project.src.interfaces.interfaceJeu.InterfaceJeuReseau import InterfaceJeuReseau

from project.src.reseau.jeuReseau import JeuReseau


HOST = ''    # ça cible la machine elle même de faire ça (à ne pas modifier donc)
PORT = 52001   # de préférence une valeur supérieure à 1024 


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

        
"""

argv 0 : guest.py
     1 : fichier json
     2 : pseudo

"""
print(sys.argv)

if len(sys.argv) != 3:
    raise Exception("mauvais nombre d'arguments")

mySocket, connexion = initialisation_serveur()

#envoie avec quel fichier json jouer
connexion.send(sys.argv[1].encode())

#on réception le pseudo du guest
msgClientPseudo = connexion.recv(1024).decode()

#on envoie le pseudo du host
connexion.send(sys.argv[2].encode())

print("...lecture du fichier")
a_file = open(f"ressources/JSON/{sys.argv[1]}", "r", encoding='utf-8')
lignes = a_file.read()

print("...converstion du string en dictionaire")
j = json.loads(lignes)

jeu = JeuReseau(connexion, j["metadonnees"])
jeu.remplissage_planche(j["possibilites"])

print(f"{jeu =}")
print(f"{jeu.planche=}")


# print(f"{jeu.recevoir_message()=}")
fen = InterfaceJeuReseau(jeu, msgClientPseudo)

fen.style.theme_use("clam")

fen.title("Qui-est-ce? (serveur)")



fen.launch()
# msg = ""
#
# while msg != "fin":
#     msg = connexion.recv(1024).decode()
#     print(f"{msg}")

# print(f"{connexion.recv(1024).decode()=}")

# connexion.send("bien reçu".encode())


# 6) Fermeture de la connexion :
# connexion.send("Au revoir !".encode())
print ("Connexion interrompue.")
connexion.close()

print("Fermeture du socket.")
mySocket.close()

sys.exit(0)

# state = 0
# # file descriptors r, w for reading and writing
# r, w = os.pipe()
# r2, w2 = os.pipe()
#
#
# pid = os.fork()
# if pid == 0 :
#     #child
#     print("Child>", f"mon pid : {pid}")
#     os.close(r)
#     os.close(w2)
#     w = os.fdopen(w, 'w')
#     # print(type(r2))
#     r2 = os.fdopen(r2)
#     jeu = JeuReseau(r2, w)
#     # print(type(r2))
#
#
#     # if state == 0:
#         # w.write("ClashRoyale")
#     # elif state == 1:
#         # w.write("Valkyrie")
#
#
#
#     f = fenetre(jeu)
#     # jeu.envoyer_message("Test")
#
#
#
#
#     # s = r2.read()
#
#
#     r2.close()
#     w.close()
# else : #parent
#     print("Parent>", f"pid de l'enfant : {pid}")
#
#     os.close(w)
#     os.close(r2)
#     r = os.fdopen(r)
#     w2 = os.fdopen(w2,'w')
#
#     mySocket, connexion = initialisation_serveur()
#
#     s = ""
#     # while s != "stop":
#     s = r.read()
#     connexion.send(s.encode())
#
#
#     # 6) Fermeture de la connexion :
#     # connexion.send("Au revoir !".encode())
#     print ("Connexion interrompue.")
#     connexion.close()
#
#     print("Fermeture du socket.")
#     mySocket.close()
#
#     sys.exit(0)
