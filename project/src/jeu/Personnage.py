from project.src.jeu.Caracteristique import Caracteristique

class Personnage:
    """
    Une classe pour représenter un personnage.
    
    Attributes
    ----------
    description : List<Caracteristique>
        une liste de caracteristique décrivant ce personnage
    """
    
    
    #attribut statique

    def __init__(self, list_caracteristique=None):
        self.description = [] if list_caracteristique is None else list_caracteristique
        self.image = ""
        self.nom = ""

    def __eq__(self, o) :#a modifier
        """Vérifie si self est égale à p en comparant toutes les caractéristiques de p à toutes celles de self.
        """
        if o is self: #comparaison d'adresse
            return True
        
        if not type(o) == Personnage: #même type ?
            return False
        
        if not len(self.description) == len(o.description): #même nombre de caracteristiques
            return False
        
        for i in range(len(self.description)):
            if not self.description[i] == o.description[i]:
                return False
        
        return True
    
    def __hash__(self):
        return hash(self.image + self.nom)

    
    def __str__(self):
        s = "{"
        for une_caracteristique in self.description:
            s += une_caracteristique.__str__() + ", "
        return s.rstrip(", ") + "}"

    
    def get_caracteristique(self) :
        return self.description

    
    def correspond(self, caracteristique:Caracteristique) :
        """Prend une caractéristique et retourne vrai si et seulement si la caractéristique donnée décrit ce personnage
        
        Parameters
        ----------
        caracteristique : Caracteristique
            La caracteristique qui est dans ce personnage ou pas
        
        Returns
        ----------
        bool
            True si la caracteristique correspond à la description de ce personnage, False sinon
        """
        
        for une_caracteristique in self.description:
            if (une_caracteristique.attribut == caracteristique.attribut) & (une_caracteristique.valeur == caracteristique.valeur) :
                return True
        ### fin de la boucle for ###
        return False
    
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < len(self.description):
            x = self.a
            self.a += 1
            return self.description[x]
        else:
            raise StopIteration
    
    
    
    