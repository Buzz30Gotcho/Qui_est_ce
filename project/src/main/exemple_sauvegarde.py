from project.src.generateur.generateur import Generateur
from project.src.generateur.perso import Perso
from jeu.src.SaveMethod import sauvegarder

def main():
    gen = Generateur()
    gen.creer_nouvelle_attribut("cheveux", True)
    gen.creer_nouvelle_attribut("yeux", True)
    
    gen.all_attributs[0].add_valeur("noir")
    gen.all_attributs[0].add_valeur("blanc")
    
    gen.all_attributs[1].add_valeur("bleu")
    gen.all_attributs[1].add_valeur("vert")
    
    gen.liste_perso.append(Perso("Girafe.png", "Girafe"))
    
    sauvegarder(gen, "sauvegarde_generateur", "ressources/sauvegarde/generateur/")
    
main()