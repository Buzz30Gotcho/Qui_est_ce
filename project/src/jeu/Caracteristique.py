class Caracteristique:
    def __init__(self, attribut, valeur):
        self.attribut = attribut
        self.valeur = valeur

    def __eq__(self, caracteristique):
        return (self.attribut == caracteristique.attribut) & (self.valeur == caracteristique.valeur)
    
    def __str__(self):
        return " (" + self.attribut + " : " + self.valeur + ") "
    
    def to_dict(self):
        return {"attribut":self.attribut,"valeur":self.valeur}
    