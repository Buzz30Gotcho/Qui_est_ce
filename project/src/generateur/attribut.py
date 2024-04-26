class Attribut:

    def __init__(self, nom:str, choix_multiple:bool):
        self.nom=nom
        self.choix_multiple=choix_multiple
        self.domaine_valeur=set()
        
    def add_valeur(self,val:str):
        self.domaine_valeur.add(val)
        
    def __str__(self):
        return f"{self.nom} {self.domaine_valeur.__str__()} choix_multiple={self.choix_multiple}"
    
    def possibilites(self):
        return 2**len(self.domaine_valeur)-1 if self.choix_multiple else len(self.domaine_valeur)
