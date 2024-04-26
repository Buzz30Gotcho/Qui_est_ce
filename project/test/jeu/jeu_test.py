from project.src.jeu.PhraseComplexe import PhraseComplexe
from project.src.jeu.Joueur import Joueur
from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Personnage import Personnage
from project.src.jeu.Phrase import Phrase
from project.src.jeu.And import And
from project.src.jeu.Not import Not
from project.src.jeu.Or import Or
from project.src.jeu.Jeu import Jeu



class TestJeu:

    @classmethod
    def setup_class(cls):
        #Création des personnages
        Personnage.path_directory = "./dir/jeu"
        
        cls.perso1 = Personnage()
        cls.perso1.description.append(Caracteristique("fichier", "/jeu/jeu/dog.jpeg"))
        cls.perso1.description.append(Caracteristique("espece", "dog"))
        
        cls.perso2 = Personnage()
        cls.perso2.description.append(Caracteristique("fichier", "/jeu/jeu/cat.jpeg"))
        cls.perso2.description.append(Caracteristique("espece", "cat"))

        cls.perso3 = Personnage()
        cls.perso3.description.append(Caracteristique("fichier", "/jeu/jeu/fat_dog.jpeg"))
        cls.perso3.description.append(Caracteristique("espece", "dog"))
        
        cls.perso4 = Personnage()
        cls.perso4.description.append(Caracteristique("fichier", "/jeu/jeu/black_cat.jpeg"))
        cls.perso4.description.append(Caracteristique("espece", "cat"))
        
        cls.perso5 = Personnage()
        cls.perso5.description.append(Caracteristique("fichier", "/jeu/jeu/white_cat.jpeg"))
        cls.perso5.description.append(Caracteristique("espece", "cat"))
        
        #Création des joueurs
        cls.j1 = Joueur("Fred")
        cls.j1.personnage_mystere = cls.perso1
        
        #Creation du jeu
        cls.jeu = Jeu()
        
        cls.jeu.planche.append(cls.perso1) 
        cls.jeu.planche.append(cls.perso2)
        cls.jeu.planche.append(cls.perso3)
        cls.jeu.planche.append(cls.perso4)
        cls.jeu.planche.append(cls.perso5)
        
        cls.jeu.set_joueur(cls.j1)

        cls.jeu.modeFacile = True
        
        #print("\n")
    
    def setup_method(self,method):
        self.jeu.indice_joueur = 0
        
    def test_set_joueur(self):
        
        assert type(self.jeu.joueur) == Joueur
        assert self.jeu.joueur == self.j1
        assert self.jeu.joueur.jeu == self.jeu
             
    def test_accuser(self):
        #j1 pense que le personnage mystère est un chien (perso1)
        assert self.jeu.accuser(self.perso1)
        assert not self.jeu.accuser(self.perso2)
        
    def test_evaluer(self):
        assert self.jeu.evaluer(Phrase("espece", "dog")) #Fred:Est-ce que le personnage mystère est un chien ?
        assert not self.jeu.evaluer(Phrase("espece", "cow")) #Fred:Est-ce que le personnage mystère est une vache ?

    def test_calcule_MapAttributsDomaine(self):
        dict_correct = {}

        dict_correct["fichier"] = {"/jeu/jeu/dog.jpeg","/jeu/jeu/fat_dog.jpeg","/jeu/jeu/cat.jpeg","/jeu/jeu/black_cat.jpeg","/jeu/jeu/white_cat.jpeg"}
        dict_correct["espece"] = {"dog","cat"}
        # print(dict_correct)
        
        answer = self.jeu.calcule_MapAttibutsDomaine()
        
        print(answer)
        
        
        assert len(answer) == 2
        assert len(answer["espece"]) == 2
        assert len(answer["fichier"]) == 5
        assert  answer == dict_correct # Est-ce-que le dictionnaire des caractéristiques existants est bien correct
        

        
        

    def test_list_invalides(self):
        # création des questions 
        Q_simple = Phrase("espece","dog")
        
        Q_not = Not()
        Q_not.add_question(Q_simple)

        Q_and = And()
        Q_or = Or()
        Q_and.add_question(Q_simple) ; Q_and.add_question(Q_simple)
        Q_or.add_question(Q_simple) ; Q_or.add_question(Q_simple)
        # création des réponses corrects en fonction des quesitons
        list_correct_simple = {self.perso2, self.perso4, self.perso5}
        list_correct_not = [self.perso1,self.perso3]
        list_correct_complexe = [self.perso2]
        # vérification
        assert self.jeu.get_perso_invalide(Q_simple) == list_correct_simple
        # assert self.jeu.get_perso_invalide(Q_not) == list_correct_not
        # assert self.jeu.get_perso_invalide(Q_or) == list_correct_complexe
        # assert self.jeu.get_perso_invalide(Q_and) == list_correct_complexe

