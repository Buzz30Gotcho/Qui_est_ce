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

from project.src.interfaces.interfaceJeu.InterfaceJeuBot import InterfaceJeuBot
from project.src.interfaces.interfaceJeu.ChoixModeJeu import ChoixModeJeu

from project.src.jeu.Jeu import Jeu
from project.src.jeu.Joueur import Joueur
from project.src.bibliotheque.SaveMethod import charger

########################################################################################
def creer_partie():

    print("...lecture du fichier")
    a_file = open("ressources/JSON/"+ "Madagascar.json", "r", encoding='utf-8')
    lignes = a_file.read()
    
    print("...converstion du string en dictionaire")
    j = json.loads(lignes)
    
    ################################################
    
    # 1 - création instance Jeu
    print("...instanciation d'un jeu")
    jeu = Jeu(j["metadonnees"], False)
    

    
    # 2 - faut créer les personnages dans l'objet jeu
    print("...création des personnages")
    jeu.remplissage_planche(j["possibilites"])
    
    
    
    # 3 - on crée le(s) joueur(s)
    print("...création d'un joueur")
    j1 = Joueur("pseudonyme")
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
    # configPartie = ChoixModeJeu()

    # if sys.argv[-1] != "-windows":
    #     configPartie.style.theme_use("clam")
    
    #on lance la fenetre
    # configPartie.mainloop()
    
    jeu = None
    
    jeu = creer_partie()
    

    fenetreJeu = InterfaceJeuBot(jeu) #création ET lancement de l'interface graphique

    
    if sys.argv[-1] != "-windows":
        fenetreJeu.style.theme_use("clam")

    fenetreJeu.mainloop()
    
    print("Fin...")
    os._exit(1)
##################################################################################################    

if __name__ == '__main__':
    main()



