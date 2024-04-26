from project.src.generateur.attribut import Attribut

class TestAttribut:

    @classmethod
    def setup_class(cls):
        attr = Attribut("chapeau", False)

        assert type(attr.nom) == str
        assert type(attr.domaine_valeur) == set
        assert type(attr.choix_multiple) == bool

    def setup_method(self,method):
        self.un_attribut = Attribut("cheveux", True)
        self.deux_attribut = Attribut("yeux", False)

    def test_ajouter_valeur(self):
        self.un_attribut.add_valeur("blond")
    
        assert len(self.un_attribut.domaine_valeur) == 1, "domaine n'a pas la bonne taille"
        assert "blond" in self.un_attribut.domaine_valeur, "problème avec l'ajout dans domaine"
    
    def test_possiblites_choix_multiple(self):
        self.un_attribut.add_valeur("brun")
        self.un_attribut.add_valeur("roux")
        self.un_attribut.add_valeur("vert")
        self.un_attribut.add_valeur("blanc")
        
        assert self.un_attribut.possibilites() == 15
        
    def test_possiblites_pas_choix_multiple(self):
        self.deux_attribut.add_valeur("noisette")
        self.deux_attribut.add_valeur("noir")
        self.deux_attribut.add_valeur("vert")
        self.deux_attribut.add_valeur("bleu")
        
        assert self.deux_attribut.possibilites() == 4
