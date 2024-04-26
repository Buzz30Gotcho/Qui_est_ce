import json

from project.src.bot.jeuVSOrdi import JeuVSOrdi
from project.src.jeu.Joueur import Joueur

def main():
    
    print("Lecture du fichier")
    a_file = open("./ressources/JSON/ClashRoyale.json", "r")
    lignes = a_file.read()
    
    print("Converstion du string en dictionaire")
    j = json.loads(lignes)
    # print(j)
    
    print("Initialisation")
    jeu = JeuVSOrdi()
    jeu.remplissage_planche(j["possibilites"])
    
    print("Création d'un joueur humain")
    jeu.set_joueur(Joueur("Tony"))
    jeu.joueur.personnage_mystere = jeu.planche[5]
    
    print("Création d'une IA très intélligente")
    jeu.set_un_bot()
    jeu.ordi.personnage_mystere = jeu.planche[0] # on choisit son perso mystère qu'il doit deviner
    print(jeu)
    print()
    
    assert not jeu.ordi == None
    assert not jeu.joueur == None
    
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
    
    
    
main()