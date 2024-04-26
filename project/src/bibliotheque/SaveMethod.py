import pickle

# ---------------Une nouvelle sauvegarde supprime les donnees de l'ancienne sauvegarde---------------
def sauvegarder(obj, nom_fichier, path_arg="./ressources/sauvegarde/jeu/"):
    path = path_arg + nom_fichier + ".pickle"
    try:
        with open(path, "wb") as file:
            pickle.dump(obj,file)
            print("----------Sauvegarde reussie----------")
    except: print("----------Sauvegarde echouee----------")
# ---------------------------------------------------------------------------------------------------



def charger(nom_fichier, path_arg="./ressources/sauvegarde/jeu/"):
    path = path_arg + nom_fichier + ".pickle"
    print(path)
    try:
        with open(path, "rb") as file:
            data = pickle.load(file)
            print("------Charge complete !------")
            return data
    except: 
        print("------No saved data detected !------")