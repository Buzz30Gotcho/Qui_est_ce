from project.src.jeu.Joueur import Joueur
from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Personnage import Personnage
from project.src.jeu.Phrase import Phrase

class TestJoueur:

    @classmethod
    def setup_class(cls):
        list1 = []
        list1.append(Caracteristique("fichier", "/jeu/jeu/fred.jpeg"))
        list1.append(Caracteristique("prenom", "Fred"))
        
        cls.perso1 = Personnage(list1)
        Personnage.path_directory = "./dir/jeu"

        
        
        cls.j1 = Joueur("Fred")
        cls.j1.personnage_mystere = cls.perso1
        
        print("\n")
        print(cls.j1)
        print("son personnage mystère: " + cls.j1.personnage_mystere.__str__())
        
    # def test_str(self):
    #     assert self.j1.__str__() == "Fred" #test nul
        
    def test_question(self):
        q = Phrase("prenom","Fred")
        
        assert len(self.j1.get_historique()) == 0
        assert self.j1.poser_question(q)
        assert self.j1.get_historique()[0][0] == q
        assert self.j1.get_historique()[0][1] == True
        assert len(self.j1.get_historique()) == 1
        