'''
Created on 7 févr. 2022

@author: tony
'''
from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Personnage import Personnage


class TestCaracteristique:

    @classmethod
    def setup_class(cls):
        
        cls.perso1 = Personnage()
        cls.perso1.description.append(Caracteristique("fichier", "/jeu/jeu/romain.jpeg"))
        cls.perso1.description.append(Caracteristique("prenom", "Romain"))
        
        cls.perso2 = Personnage()
        cls.perso2.description.append(Caracteristique("fichier", "/jeu/jeu/laurent.jpeg"))
        cls.perso2.description.append(Caracteristique("prenom", "Laurent"))
        
        cls.perso3 = Personnage()
        cls.perso3.description.append(Caracteristique("fichier", "/jeu/jeu/laurent.jpeg"))
        cls.perso3.description.append(Caracteristique("prenom", "Tony"))
        
        Personnage.path_directory = "./dir/jeu"

        print("\n")
        print("perso1 : " + cls.perso1.__str__())
        print("perso2 : " + cls.perso2.__str__())
        print("perso3 : " + cls.perso3.__str__())
        
        print("Test" == "Test")
        
        
    
    def test_eq(self):
        assert (self.perso1 == self.perso2) == False
        assert (self.perso2 == self.perso3) == False
        assert (self.perso1 == self.perso3) == False
        
    def test_str(self):
        print(self.perso1.__str__())
        assert self.perso1.__str__() == "{ (fichier : /jeu/jeu/romain.jpeg) ,  (prenom : Romain)}"
        
    def test_path_directory(self):
        assert Personnage.path_directory == "./dir/jeu"
        
    def test_get_caracteristique(self):
        l = []
        l.append(Caracteristique("fichier", "/jeu/jeu/romain.jpeg"))
        l.append(Caracteristique("prenom", "Romain"))
        
        lc = self.perso1.get_caracteristique()
        
        assert len(lc) == len(l)
        for i in range(len(lc)):
            assert lc[i] == l[i]
    
    def test_correspond(self):
        assert self.perso1.correspond(Caracteristique("prenom","Romain"))
        assert self.perso1.correspond(Caracteristique("prenom","Tony")) == False 
        
    def test_init_sans_parametre(self):
        perso4 = Personnage()
        perso4.description.append(Caracteristique("nom", "abc"))
        
        perso5 = Personnage()
        perso5.description.append(Caracteristique("nom", "xyz"))
        
        assert not perso4.description == perso5.description
        
        
        
        
        
        
        
        
