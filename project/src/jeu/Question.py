"""faut que je vois si quand on créer la fonction on "connait"
déjà la réponse, en gros quand on instancie on vérifie en même
temps si la réponse est vraie ou fausse et on l'enregistre dans 
un attribut"""

class Question:
    def __init__(self):
        raise NotImplementedError("Classe abstraite")
    
    def get_nom(self):
        raise NotImplementedError("Méthode abstraite")
    
    def to_dict(self):
        raise NotImplementedError("Méthode abstraite")
    