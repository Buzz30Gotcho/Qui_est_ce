from project.src.generateur.generateur import Generateur



gen = Generateur("ressources/img/")

    
gen.creer_nouvelle_attribut("cheveux", True)
gen.all_attributs[0].add_valeur("noir")
gen.all_attributs[0].add_valeur("blond")
gen.all_attributs[0].add_valeur("roux")
gen.all_attributs[0].add_valeur("rose")

gen.creer_nouvelle_attribut("yeux", False)
gen.all_attributs[1].add_valeur("noir")
gen.all_attributs[1].add_valeur("noisette")
gen.all_attributs[1].add_valeur("vert")
gen.all_attributs[1].add_valeur("bleu")


gen.liste_perso[0].ajouter("cheveux","noir")
gen.liste_perso[0].ajouter("cheveux","blond")
gen.liste_perso[0].ajouter("yeux","noir")

gen.liste_perso[1].ajouter("cheveux","blond")
gen.liste_perso[1].ajouter("yeux","noir")

gen.liste_perso[2].ajouter("cheveux","roux")
gen.liste_perso[2].ajouter("yeux","noir")

gen.liste_perso[3].ajouter("cheveux","roux")
gen.liste_perso[3].ajouter("yeux","noir")

gen.liste_perso[4].ajouter("cheveux","rose")
gen.liste_perso[4].ajouter("yeux","noir")

gen.liste_perso[5].ajouter("cheveux","noir")
gen.liste_perso[5].ajouter("yeux","noisette")


for p in gen.liste_perso:
    print(p)
print(f"{len(gen.liste_perso)} au total")
print()

print("La girafe est complété ? ", gen.liste_perso[0].est_complete())
print()

for attr in gen.all_attributs:
    print(attr)
    print(f"{attr.possibilites()} possibilites")
    print()
print()
    
    
# taille = 19
#
# ligne = 5
# col = 5
#
#
# res = (ligne*col) % taille
# print(res)
# print(res >= ligne, res >= col)

gen.hauteurImage = 100
gen.largeurImage = 100

gen.nbColonnes = 2
gen.nbLignes = 2
print("2x2 ", gen.a_bonne_taille())

gen.nbColonnes = 3
gen.nbLignes = 2
print("3x2 ", gen.a_bonne_taille(), "taille parfaite")

gen.nbColonnes = 6
gen.nbLignes = 2
print("3x3 ", gen.a_bonne_taille())
print()

print(f"{gen.nb_perso_max()} combinaison possible")
print(f"sufisant pour convrir tout nos perso ?  {gen.nb_perso_max() > len(gen.liste_perso)}")

gen.generer_fichier_json()




