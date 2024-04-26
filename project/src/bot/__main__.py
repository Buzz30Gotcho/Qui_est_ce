from random import random
import json
import sys



from project.src.interfaces.interfaceJeu.InterfaceJeuBot import InterfaceJeuBot



from project.src.bot.jeuVSOrdi import JeuVSOrdi
from project.src.jeu.Joueur import Joueur

from project.src.bibliotheque.SaveMethod import charger


def chargerPartie(nom_joueur:str, path:str, choixModeFacile:bool):
    
    print("Lecture du fichier")
    a_file = open("./ressources/JSON/"+path, "r", encoding='utf-8')
    lignes = a_file.read()
    
    print("Converstion du string en dictionaire")
    j = json.loads(lignes)
    # print(j)
    
    print("Initialisation")
    jeu = JeuVSOrdi(j["metadonnees"], choixModeFacile)
    jeu.remplissage_planche(j["possibilites"])
    
    print("Création d'un joueur humain")
    jeu.set_joueur(Joueur(nom_joueur))
    jeu.joueur.personnage_mystere = jeu.planche[int(random()*len(jeu.planche))]
    
    print("Création d'une IA très intélligente")
    jeu.set_un_bot()
    jeu.ordi.personnage_mystere = jeu.planche[int(random()*len(jeu.planche))] # on choisit son perso mystère qu'il doit deviner
    print(jeu)
    print()

    return jeu

    
    assert not jeu.ordi == None
    assert not jeu.joueur == None

    #le jeu est créé, on le passe à l'interface
    
    nb_question = 0
    while len(jeu.ordi.suspects) != 1 :
        print(f"Tour de boucle i={nb_question}")
        jeu.ordi.poser_question_tout_seul()
        print(jeu.ordi, end="\n\n")
        nb_question += 1
        
    print(f"trouvé en {nb_question} questions")
    assert len(jeu.ordi.historique) != 1
    assert len(jeu.ordi.liste_persos_coches) == len(jeu.planche) - 1
    
    print(f"Les persos cochés ({len(jeu.ordi.liste_persos_coches)}):")
    for p in jeu.ordi.liste_persos_coches:
        print(f"    {p.nom}")
    print()
        
    print(f"Historique du bot:")
    for q in jeu.ordi.historique:
        print(f"{q[0]}? -> {q[1]}")
    
"""


argv =  0 le fichier
        1 le pseudo du joueur
        2 le chemin du json
        3 anciennePartie
        4 -windows
"""

jeu=None

if sys.argv[3] == "True":

    jeu = charger(sys.argv[1])

else:
    #si c'est une nouvelle partie
    jeu = chargerPartie(sys.argv[1], sys.argv[2], False)



fenetreJeu = InterfaceJeuBot(jeu)

if sys.argv[4] != "-windows":
    fenetreJeu.style.theme_use("clam")

fenetreJeu.mainloop()

print("c'est fini")
exit()

    
