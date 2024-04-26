import pytest
from project.src.jeu.Not import Not
from project.src.jeu.Phrase import Phrase
from project.src.jeu.Personnage import Personnage
from project.src.jeu.Caracteristique import Caracteristique

class TestQuestion: 
    
    def setup_method(self,method):
        self.n = Not()

        
        self.p1 = Personnage()
        self.p1.description.append(Caracteristique("Prenom", "Bob"))
        
        self.p2 = Personnage()
        self.p2.description.append(Caracteristique("Prenom", "John"))
        
        #print("\n")
        
    def test_ajouter(self):
        assert len(self.n.composantEnfant) == 0
        self.n.add_question(Phrase("Prenom","John"))
        assert len(self.n.composantEnfant) == 1
        
    def test_ajouter_trop(self):
        self.n.add_question(Phrase("Prenom","John"))
        
        with pytest.raises(IndexError):
            self.n.add_question(Phrase("test","test"))
        
    def test_evaluer(self):
        self.n.add_question(Phrase("Prenom","John"))
                
        assert self.n.evaluer(self.p1)
        assert not (self.n.evaluer(self.p2))
        
    @classmethod
    def teardown_class(cls):
        foo = Not()
        foo.add_question(Phrase("Lunettes","True"))
        
        print("\n")
        print(foo)