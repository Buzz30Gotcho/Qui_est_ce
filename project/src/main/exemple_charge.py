# from project.src.generateur.generateur import Generateur
from jeu.src.SaveMethod import charger

def main():
    
    g = charger("sauvegarde_generateur", "ressources/sauvegarde/generateur/")
    
    

    print(g)
    
    for attr in g.all_attributs:
        print(attr.nom, end=" : ")
        
        print("{ ", end="")
        for val in attr.domaine_valeur:
            print(val, end=" ")
        print("}")
    
    for p in g.liste_perso:
        print(p.nom)
main()