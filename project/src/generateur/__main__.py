# -*- coding: utf-8 -*-

"""Générateur de Qui-est-ce ?

Ce script lance une interface tkinter permettant de créer un fichier json."

ce fichier json décrit les différent personnages.

python3.8 ou plus récent
Des modules extérieurs sont requis.
    -tkinter
    -Pillow
"""

import os
import sys
import json

from project.src.generateur.generateur import Generateur
from project.src.interfaces.interfaceGenerateur.FenetreGen import FenetreGen
from project.src.bibliotheque.SaveMethod import charger


if __name__ == '__main__':
    print(len(sys.argv))
    print(sys.argv)
    
    gen = None

    nbrArgument = len(sys.argv) - (1 if sys.argv[-1] == "-windows" else 0)
    print(nbrArgument)

    if nbrArgument == 2:
        
         
        if sys.argv[1] == "-save":
            gen = charger("sauvegarde_generateur", "./ressources/sauvegarde/generateur/")
        else:
            # pass
            gen = Generateur(sys.argv[1])
    
    elif nbrArgument == 3 and sys.argv[1] == "-m":

        fichierJson = open("ressources/JSON/"+sys.argv[2], "r", encoding='utf-8')
        lignes = fichierJson.read()

        j = json.loads(lignes)

        gen = Generateur(j["metadonnees"]["images"])

        gen.charge_Fichier_Json(j)

    
    
    fen = FenetreGen(gen)
    if sys.argv[-1] != "-windows":
        fen.style.theme_use("clam")
    fen.mainloop()


















    
    
    