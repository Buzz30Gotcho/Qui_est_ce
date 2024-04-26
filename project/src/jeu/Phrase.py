from project.src.jeu.Question import Question
from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Personnage import Personnage

class Phrase(Question):
    def __init__(self, attribut:str, valeur:str):

        #Question.__init__(self, perso_Mystere)
        
        #jsp la différence avec caracteristique mdr
        self.caracteristique = Caracteristique(attribut, valeur)
        
    def __str__(self) -> str:
        return self.caracteristique.__str__()

    def evaluer(self, lePersoAEval:Personnage) -> bool :
        return lePersoAEval.correspond(self.caracteristique)
    
    def get_nom(self):
        return "Phrase"
    
    def to_dict(self):
        d = dict()
        d["type"] = self.get_nom()
        d["content"] = self.get_content()
        
        return d
    
    def get_content(self):
        return self.caracteristique.to_dict()
    
        
        #selectionne l'attribut en question dans l'objet perso à évaluer, et regarde si la valeur qui correspond c'est bien celle de la phrase
        #return self.perso_Mystere.caracteristiques[self.caracteristiques.attribut] == self.caracteristique.valeur
            

