# -*- coding: utf-8 -*-

"""Qui-est-ce ?

Ce script lance une instance du jeu de plateau "Qui-est-ce?"

Un fichier json décrivant les différent personnages doit être prêt ainsi que sa banque d'image.

python3.8 ou plus récent
Des modules extérieurs sont requis.
    -tkinter
    -Pillow
"""

import os
import sys
import json
from random import random

from project.src.interfaces.interfaceJeu.InterfaceJeuDeBase import InterfaceJeuDeBase
from project.src.interfaces.interfaceJeu.ChoixModeJeu import ChoixModeJeu

from project.src.jeu.Jeu import Jeu
from project.src.jeu.Joueur import Joueur
from project.src.bibliotheque.SaveMethod import charger

########################################################################################
def creer_partie(nom_joueur:str, path:str, choixModeFacile:bool):

    print("...lecture du fichier")
    a_file = open("ressources/JSON/"+path, "r", encoding='utf-8')
    lignes = a_file.read()
    
    print("...converstion du string en dictionaire")
    j = json.loads(lignes)
    
    ################################################
    
    # 1 - création instance Jeu
    print("...instanciation d'un jeu")
    jeu = Jeu(j["metadonnees"], choixModeFacile)
    

    
    # 2 - faut créer les personnages dans l'objet jeu
    print("...création des personnages")
    jeu.remplissage_planche(j["possibilites"])
    
    
    
    # 3 - on crée le(s) joueur(s)
    print("...création d'un joueur")
    j1 = Joueur(nom_joueur)
    random_int = int(random()*len(jeu.planche))
    j1.personnage_mystere = jeu.planche[random_int]
    jeu.set_joueur(j1)
    print(j1,end="\n\n")


    # 4 - Une fois que tous les persos, tous les joueurs sont créés
    # on appelle une méthode de jeu pour créer l'interface
    # print("...lancement de l'interface")
    # jeu.creation_interface_graphique()
    return jeu
    

    
    

def main():
    #on créé l'objet pour lancer le menu
    configPartie = ChoixModeJeu()

    if sys.argv[-1] != "-windows":
        configPartie.style.theme_use("clam")
    
    #on lance la fenetre
    configPartie.mainloop()
    

    if configPartie.modeJeu == "JeuDeBase":

        jeu = None
        if configPartie.anciennePartie: #le mec charge son ancienne partie
            jeu = charger(configPartie.pseudoJoueur)
        else:
            #on recup les attributs
            jeu = creer_partie(configPartie.pseudoJoueur, configPartie.fichierJson, configPartie.modeFacile)
        del(configPartie)

        fenetreJeu = InterfaceJeuDeBase(jeu) #création ET lancement de l'interface graphique

        
        if sys.argv[-1] != "-windows":
            fenetreJeu.style.theme_use("clam")

        fenetreJeu.mainloop()
        
        print("Fin...")
        os._exit(1)
    ##################################################################################################    


    elif configPartie.modeJeu == "Bot":
        if sys.argv[-1] != "-windows":
            os.system("python3 ./project/src/bot/__main__.py \"" + configPartie.pseudoJoueur +"\" "+configPartie.fichierJson +" "+str(configPartie.anciennePartie) + " " + "-linux")
        else:
            os.system("py ./project/src/bot/__main__.py \"" + configPartie.pseudoJoueur +"\" "+configPartie.fichierJson +" "+str(configPartie.anciennePartie) + " " + "-windows")


    elif configPartie.modeJeu == "Reseau":
        
        if configPartie.heberger:
            if sys.argv[-1] != "-windows":
                os.system("python3 ./project/src/reseau/host.py " + configPartie.fichierJson + " \"" + configPartie.pseudoJoueur +"\"")
            else:
                os.system("py ./project/src/reseau/host.py " + configPartie.fichierJson + " \"" + configPartie.pseudoJoueur +"\"")

        else:
            if sys.argv[-1] != "-windows":
                os.system("python3 ./project/src/reseau/guest.py " + configPartie.adresseIP + " \"" + configPartie.pseudoJoueur + "\"")
            else:
                os.system("py ./project/src/reseau/guest.py " + configPartie.adresseIP + " \"" + configPartie.pseudoJoueur +"\"")




if __name__ == '__main__':
    main()



