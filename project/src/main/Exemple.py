from jeu.src.Jeu import Jeu
from jeu.src.Personnage import Personnage
from jeu.src.Caracteristique import Caracteristique
from jeu.src.Joueur import Joueur
import json
import sys
from random import random
from jeu.src.Or import Or

from jeu.src.Phrase import Phrase

if __name__ == '__main__':
    print("Lecture du fichier")
    a_file = open(sys.argv[1], "r")
    lignes = a_file.read()
    
    print("Converstion du string en dictionaire")
    j = json.loads(lignes)
    # print(j)
    
        
    jeu = Jeu()
    Personnage.path_directory = j["metadonnees"]["images"]
    # print(Personnage.path_directory)
    print("Création des personnages")
    jeu.remplissage_planche(j["possibilites"])
    for perso in jeu.planche:
        print("    ", perso.nom, perso, perso.image)
    print("\n")

    
    print("Création Joueur")
    j1 = Joueur("Tony")
    random_int = int(random()*len(jeu.planche))
    j1.personnage_mystere = jeu.planche[random_int]
    jeu.add_joueur(j1)
    print(j1,end="\n\n")
    
    """Créer une question"""
    q = Or()
    q.add_question(Phrase("cheveux", "noir"))
    q.add_question(Phrase("cheveux", "blond"))
    print(f"question : {q}?")
    
    """Poser une question"""
    rep = jeu.joueur.poser_question(q)
    print(f"réponse : {rep}", end="\n\n")
    
    """Pour choisir les questions"""
    print("map")
    dico = jeu.calcule_MapAttibutsDomaine()
    print(dico)
    
    """L'historique"""
    print("historique")
    for q in j1.get_historique():
        print("    ",q)
    print()
    
    
    """Accuser"""
    print("accuser")
    rep = j1.personnage_mystere == jeu.planche[5]
    print(f"Est-ce-que le 5e personnage est le personnage mystère que j1 doit trouver ? : {rep}")
    
    
    