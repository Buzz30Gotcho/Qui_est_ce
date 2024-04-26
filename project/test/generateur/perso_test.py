from project.src.generateur.perso import Perso

class TestPerso:

    @classmethod
    def setup_class(cls):
        cls.p = Perso("Archer.jpg","Archer")

        assert type(cls.p.description) == dict, "description devrait être un dictionnaire"
        assert cls.p.description == {}, "la description devrait être vide après l'initialisation"
        assert len(cls.p.description.keys()) == 0, "la description devrait ne pas avoir de clé après l'initialisation"
        

    def setup_method(self,method):
        self.p = Perso("Archer.jpg","Archer")
    
    def test_ajouter_attribut(self):
        self.p.ajouter_attribut("cheveux")
        
        assert "cheveux" in self.p.description, "il manque une clé/attribut dans la description"
        assert len(self.p.description.keys()) == 1, "il devrait y avoir un seul attribut dans la description"        
        assert type(self.p.description["cheveux"]) == set, "l'ensemble associé à une clé doit être un ensemble"
        assert len(self.p.description["cheveux"]) == 0, "l'ensemble associé à la clé \"cheveux\" doit être de taille 0 après un ajout d'attribut"
        
    def test_ajouter_valeurs(self):
        self.p.ajouter_attribut("cheveux")
        self.p.ajouter("cheveux",{"brun","blanc"})
        
        expected = {"cheveux" : {"brun","blanc"}}
        answer = self.p.description
    
        assert len(self.p.description) == 1, "description n'a pas la bonne taille"
        assert "brun" in answer["cheveux"], "problème avec l'ajout dans domaine"
        assert "blanc" in answer["cheveux"]
        assert len(self.p.description["cheveux"]) == 2
        assert answer == expected, "la réponse attendu est différente de la réponse reçu"
        
    def test_ajouter__une_valeur(self):
        self.p.ajouter_attribut("cheveux")
        self.p.ajouter("cheveux",{"brun"})
        self.p.ajouter("cheveux",{"brun"})
        
        expected = {"cheveux" : {"brun"}}
        answer = self.p.description
    
        assert len(self.p.description) == 1, "description n'a pas la bonne taille"
        assert "brun" in answer["cheveux"], "problème avec l'ajout dans domaine"
        assert answer == expected, "la réponse attendu est différente de la réponse reçu"
        
        
    def test_est_complete(self):
        self.p.ajouter_attribut("cheveux")
        assert not self.p.est_complete()
        
        self.p.ajouter("cheveux", "rose")
        assert self.p.est_complete()


