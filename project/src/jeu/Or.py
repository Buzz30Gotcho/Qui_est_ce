from project.src.jeu.PhraseComplexe import PhraseComplexe

class Or(PhraseComplexe):
    def __init__(self):
        self.composantEnfant = []

    def nb_elem_max(self):
        return 2
    
    def get_nom(self):
        return "Or"

    def __str__(self):
        return "("+self.composantEnfant[0].__str__() + " | " + self.composantEnfant[1].__str__()+")"

#faire des tests pour savoir si """    resultat_Question(SELF.FIRSTQUESTION) """ 
#appelle bien la fonction qui correspond au type de self.firstQuestion

    def evaluer(self, lePersoAEval):
        """Vérifie que le personnage passé en paramètre correspond à au moins une de ses questions enfants.
            
            Parameters
            ----------
            lePersoAEval : Personnage
                le personnage qui est comparé à la question
            
            Returns
            ----------
            bool
                True ssi le personnage répond True a au moins une des questions enfants
        """    
        if self.composantEnfant[0].evaluer(lePersoAEval):
            return True
        elif self.composantEnfant[1].evaluer(lePersoAEval):
            return True
        return False
    