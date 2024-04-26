
class Perso:
    def __init__(self,fichier,nom):
        self.description={}
        self.fichier=fichier
        self.nom=nom
        
    def __str__(self):
        return f"Perso: {self.fichier}, {self.nom}, {self.description}"
        
    def ajouter(self,attribut:str,nouvelle_valeur:set()): # je sais pas comment ajouter une valeur à un ensemble vide mdr, C'EST BON J'AI COMPRIS AAAAAA
        if attribut in self.description:
            reset={attribut:nouvelle_valeur}
            self.description.update(reset)# ajoute valeur à l'ensemble associé à attribut
        
    def retirer(self, attribut:str, valeur:str) -> None:
        """Supprime une valeur relié à attribut dans la description"""
        
        self.description[attribut].discard(valeur)
                       
    def est_complete(self):
        for v in self.description.values():
            if len(v)==0:
                    return False
            ### fin de la boucle for ###
        return True
                   
    def ajouter_attribut(self,attr:str):  
        self.description[attr]=set()
        
    def comparaison(self, p):
        """Requis : p de type Perso, sinon p.description n'existe pas et error"""
    
        return self.description == p.description    

