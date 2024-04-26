from project.src.jeu.PhraseComplexe import PhraseComplexe

class And(PhraseComplexe):
    def __init__(self):
        self.composantEnfant = []
        
    def __str__(self):
        return "("+self.composantEnfant[0].__str__() + " & " + self.composantEnfant[1].__str__()+")"
        
    def nb_elem_max(self):
        return 2
    
    def get_nom(self):
        return "And"
    
    def evaluer(self, lePersoAEval):
        if self.composantEnfant[0].evaluer(lePersoAEval):
            if self.composantEnfant[1].evaluer(lePersoAEval):
                return True
        return False