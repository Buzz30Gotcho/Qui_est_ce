import pytest
from project.src.jeu.Or import Or
from project.src.jeu.Phrase import Phrase
from project.src.jeu.Personnage import Personnage
from project.src.jeu.Caracteristique import Caracteristique

class TestOr: 
    
    @classmethod
    def setup_class(cls):
        cls.o = Or()
        
        cls.p1 = Personnage()
        cls.p1.description.append(Caracteristique("Prenom", "Bob"))
        cls.p1.description.append(Caracteristique("Chauve", "True"))
        
        cls.p2 = Personnage()
        cls.p2.description.append(Caracteristique("Prenom", "John"))
        cls.p2.description.append(Caracteristique("Chauve", "False"))
        
        cls.p3 = Personnage()
        cls.p3.description.append(Caracteristique("Prenom", "Pierre"))
        cls.p3.description.append(Caracteristique("Chauve", "False"))
        
        assert len(cls.o.composantEnfant) == 0
        cls.o.add_question(Phrase("Prenom","John"))
        assert len(cls.o.composantEnfant) == 1
        cls.o.add_question(Phrase("Chauve", "True"))
        assert len(cls.o.composantEnfant) == 2

        print("\n")
        print(cls.o)      
        
    def test_ajouter_trop(self):    
        with pytest.raises(IndexError):
            self.o.add_question(Phrase("test","test"))
    
    def test_evaluer(self):
        assert self.o.evaluer(self.p1)
        assert self.o.evaluer(self.p2)
        
        assert not (self.o.evaluer(self.p3))