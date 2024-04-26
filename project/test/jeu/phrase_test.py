'''
Created on 7 févr. 2022

@author: tony
'''
from project.src.jeu.Phrase import Phrase
from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Personnage import Personnage


class TestPhrase:

    @classmethod
    def setup_class(cls):
        cls.p = Phrase("Chapeau","True")
        print("\n")
        print(cls.p)
        
        
    
    def test_evaluer(self):
        liste = []
        liste.append(Caracteristique("Chapeau","True"))
        liste.append(Caracteristique("Cheveux","True"))
        perso = Personnage(liste)
        
        assert self.p.evaluer(perso)