from project.src.jeu.PhraseComplexe import PhraseComplexe
from project.src.jeu.Personnage import Personnage

#Bon en vrai je mets la classe mais je sais pas vraiment si y a besoin hein
class Not(PhraseComplexe):
    def __init__(self):
        self.composantEnfant = []
    
    def __str__(self):
        return "!(*vide*)" if len(self.composantEnfant)==0 else "!" + self.composantEnfant[0].__str__()
    
    def get_nom(self):
        return "Not"

    def nb_elem_max(self):
        return 1

    def evaluer(self, lePersoAEval:Personnage) -> bool:
        """Evalue si le personnage passé en paramètre NE correspond PAS à cette question.
            
            Parameters
            ----------
            lePersoAEval : Personnage
                le personnage qui est comparé à la question
            
            Returns
            ----------
            bool
                True ssi le personnage répond False aux questions enfants
        """    
        return not (self.composantEnfant[0].evaluer(lePersoAEval))