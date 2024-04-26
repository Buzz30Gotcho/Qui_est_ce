'''
Created on 7 févr. 2022

@author: tony
'''
from project.src.jeu.Caracteristique import Caracteristique


class TestCaracteristique:

    @classmethod
    def setup_class(cls):
        print("\n")
        cls.c1 = Caracteristique("cheveux","noir")
        print(TestCaracteristique.c1)
        
    
    
    def test_eq(self):
        assert self.c1 == Caracteristique("cheveux","noir")
        
    def test_str(self):
        assert self.c1.__str__() == " (cheveux : noir) "