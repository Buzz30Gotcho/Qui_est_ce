from project.src.generateur.generateur import Generateur
from project.src.generateur.perso import Perso

class TestGenerateur:

    @classmethod
    def setup_class(cls):
        path = "ressources/img/Madagascar"
        gen = Generateur(path)
        
        assert len(gen.liste_perso) == 6
        assert len(gen.all_attributs) == 0
        
    def setup_method(self,method):
        path = "ressources/img/Madagascar"
        self.gen = Generateur(path)
        
    def test_creer_un_nouvel_attribut(self):
        self.gen.creer_nouvelle_attribut("cheveux", True)
        
        assert len(self.gen.all_attributs) == 1
    
    def test_get_perso_similaire(self):
        self.gen = Generateur()
        self.gen.liste_perso.append(Perso("Girafe.png", "Girafe"))
        self.gen.liste_perso.append(Perso("Zebre.png", "Zebre"))
        self.gen.liste_perso.append(Perso("Lion.png", "Lion"))
        
        self.gen.creer_nouvelle_attribut("cheveux", True)
        # self.gen.creer_nouvelle_attribut("yeux", False)
        # self.gen.creer_nouvelle_attribut("poils", True)
        
        self.gen.liste_perso[0].ajouter("cheveux", "noir")
        self.gen.liste_perso[1].ajouter("cheveux", "noir")
        self.gen.liste_perso[2].ajouter("cheveux", "noir")    
        
        
        answer = self.gen.get_perso_similaire()
        expected = []
        expected.append(self.gen.liste_perso[0])
        expected.append(self.gen.liste_perso[1])
        expected.append(self.gen.liste_perso[2])
        
        assert len(answer) == 3
        assert answer == expected
        
    def test_get_perso_pas_similaire(self):
        self.gen = Generateur()
        self.gen.liste_perso.append(Perso("Girafe.png", "Girafe"))
        self.gen.liste_perso.append(Perso("Zebre.png", "Zebre"))
        self.gen.liste_perso.append(Perso("Lion.png", "Lion"))
        
        self.gen.creer_nouvelle_attribut("cheveux", True)
        
        self.gen.liste_perso[0].ajouter("cheveux", "noir")
        self.gen.liste_perso[1].ajouter("cheveux", "blanc")
        self.gen.liste_perso[2].ajouter("cheveux", "gris")    
        
        
        answer = self.gen.get_perso_similaire()
        expected = []
        
        
        assert len(answer) == 0
        assert answer == expected
    
    def test_a_bonne_taille(self):
        self.gen.liste_perso = []
        
        for i in range(19):
            self.gen.liste_perso.append(Perso("test.jpg","test"))
            
        self.gen.nbColonnes = 5
        self.gen.nbLignes = 5
        assert self.gen.a_bonne_taille() == 19
        
        self.gen.nbColonnes = 4
        self.gen.nbLignes = 4
        assert self.gen.a_bonne_taille() == 19
        
        self.gen.nbColonnes = 5
        self.gen.nbLignes = 4
        assert self.gen.a_bonne_taille() == 0
        
    def test_nb_perso_max(self):
        self.gen.creer_nouvelle_attribut("cheveux", True)
        self.gen.creer_nouvelle_attribut("yeux", False)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc")
        
        self.gen.all_attributs[1].add_valeur("noisette")
        self.gen.all_attributs[1].add_valeur("noir")
        self.gen.all_attributs[1].add_valeur("vert")
        self.gen.all_attributs[1].add_valeur("bleu")
        
        assert self.gen.all_attributs[0].possibilites() == 15
        assert self.gen.all_attributs[1].possibilites() == 4
        
        assert self.gen.nb_perso_max() == 60

    def test_modif_attribut(self):

        self.gen.creer_nouvelle_attribut("cheveu", True)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc")
        
        girafe = Perso("Girafe.png", "Girafe")
        girafe.ajouter_attribut("cheveu")
        girafe.ajouter("cheveu","brun")

        zebre = Perso("Zebre.jpeg", "Zebre")
        zebre.ajouter_attribut("cheveu")
        zebre.ajouter("cheveu","noir")

        self.gen.liste_perso.append(zebre)
        self.gen.liste_perso.append(girafe)

        self.gen.modif_attribut("cheveux",self.gen.all_attributs[0])

        assert self.gen.all_attributs[0].nom == "cheveux"
        for p in self.gen.liste_perso:
            assert "cheveux" in p.description

    def test_modif_valeur(self):
        self.gen.creer_nouvelle_attribut("cheveux", True)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc")

        self.gen.liste_perso[0].ajouter("cheveux", {"roux"})

        self.gen.modif_valeur("roux", "couscous", self.gen.all_attributs[0])

        assert self.gen.all_attributs[0].domaine_valeur == {"brun","couscous","vert","blanc"}
        
        assert "couscous" in self.gen.liste_perso[0].description["cheveux"]
        assert not "couscous" in self.gen.liste_perso[1].description["cheveux"]
        assert not "couscous" in self.gen.liste_perso[2].description["cheveux"]
        assert not "couscous" in self.gen.liste_perso[3].description["cheveux"]
        assert not "couscous" in self.gen.liste_perso[4].description["cheveux"]
        assert not "couscous" in self.gen.liste_perso[5].description["cheveux"]

    def test_supp_valeur(self):
        self.gen.creer_nouvelle_attribut("cheveux", True)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc")        
        
        self.gen.liste_perso[0].ajouter("cheveux",{"brun"})

        self.gen.supp_valeur("brun" ,self.gen.all_attributs[0])

        assert len(self.gen.all_attributs) == 1
        assert len(self.gen.all_attributs[0].domaine_valeur) == 3
        assert len(self.gen.liste_perso[0].description["cheveux"]) == 0

    def test_supp_attribut(self):
        self.gen.creer_nouvelle_attribut("cheveux", True)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc")        
        
        self.gen.liste_perso[0].ajouter("cheveux",{"brun"})

        self.gen.supp_attribut(self.gen.all_attributs[0])

        assert len(self.gen.all_attributs) == 0
        assert "cheveux" not in self.gen.liste_perso[0].description
        
    def comparer_perso_aux_restes(self):
        self.gen.creer_nouvelle_attribut("cheveux", True)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc") 
        
        self.gen.liste_perso[0].ajouter("cheveux","brun")
        self.gen.liste_perso[1].ajouter("cheveux","roux")
        self.gen.liste_perso[2].ajouter("cheveux","vert")
        self.gen.liste_perso[3].ajouter("cheveux","blanc")
        self.gen.liste_perso[4].ajouter("cheveux","brun")
        self.gen.liste_perso[5].ajouter("cheveux","brun")
        
        answer = self.gen.comparer_perso_aux_restes(self.gen.liste_perso[0])
        
        expected = []
        expected.append(self.gen.liste_perso[4])
        expected.append(self.gen.liste_perso[5])
        
        assert answer == expected
        
    def test_supp_attr_dans_perso_qui_ont_une_seul_valeur(self):
        self.gen.creer_nouvelle_attribut("cheveux",True)
        self.gen.creer_nouvelle_attribut("yeux",False)
        
        self.gen.all_attributs[0].add_valeur("brun")
        self.gen.all_attributs[0].add_valeur("roux")
        self.gen.all_attributs[0].add_valeur("vert")
        self.gen.all_attributs[0].add_valeur("blanc")
        
        self.gen.all_attributs[1].add_valeur("bleu")
        self.gen.all_attributs[1].add_valeur("vert")
        self.gen.all_attributs[1].add_valeur("noisette") 
        
        self.gen.liste_perso[0].ajouter("cheveux",{"brun"})
        self.gen.liste_perso[1].ajouter("cheveux",{"roux"})
        self.gen.liste_perso[2].ajouter("cheveux",{"vert"})
        self.gen.liste_perso[3].ajouter("cheveux",{"blanc"})
        self.gen.liste_perso[4].ajouter("cheveux",{"brun"})
        self.gen.liste_perso[5].ajouter("cheveux",{"brun"})
        
        self.gen.liste_perso[0].ajouter("yeux",{"noisette"})
        self.gen.liste_perso[1].ajouter("yeux",{"noisette"})
        self.gen.liste_perso[2].ajouter("yeux",{"noisette"})
        self.gen.liste_perso[3].ajouter("yeux",{"noisette"})
        self.gen.liste_perso[4].ajouter("yeux",{"noisette"})
        self.gen.liste_perso[5].ajouter("yeux",{"noisette"})
        
        answer = self.gen.supp_attr_dans_perso_qui_ont_une_seul_valeur()
        print(answer)
        
        assert len(self.gen.liste_perso[0].description) == 1
        assert answer == ["yeux"]
        
    def test_get_nom_directory(self):
        
        path = "ressources/img/Madagascar"
        
        res = path.rsplit('/', 1)[-1]
        assert res == "Madagascar"
        
        
