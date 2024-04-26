from project.src.jeu.Question import Question

class PhraseComplexe(Question):
    def __init__(self):
        raise NotImplementedError("Classe abstraite")
    
    def add_question(self, q:Question):
        if len(self.composantEnfant) >= self.nb_elem_max():
            raise IndexError(type(self).__name__ + " doit contenir " + str(self.nb_elem_max()) + " élément(s)")
        else:
            self.composantEnfant.append(q)
        
    def nb_elem_max(self):
        raise NotImplementedError("Méthode abstraite")
    
    def get_nom(self):
        raise NotImplementedError("Méthode abstraite")
    
    def to_dict(self):
        d = dict()
        d["type"] = self.get_nom()
        d["content"] = dict()
        
        for i in range(self.nb_elem_max()) : 
            d["content"][i] = self.composantEnfant[i].to_dict()
            
        return d