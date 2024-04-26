from ast import dump
import pickle
import os
from jeu.src.Caracteristique import Caracteristique
q= Caracteristique("sexe","femme")
d= Caracteristique("sexe","homme")
s = {"question":q,"carac":d}

cwd = os.getcwd()
print(cwd)
with open("Sauvegarde/donnee.pickel","rb") as file:
    # pickle.dump(s,file)
    # pickle.dump(d,file)
    var = pickle.load(file)
    # var2 = pickle.load(file)

for i in var:
    print(i.value())

