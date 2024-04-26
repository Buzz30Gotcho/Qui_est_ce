from project.src.jeu.Phrase import Phrase
from project.src.jeu.Joueur import Joueur
from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Jeu import Jeu

"""
TODO
-> transformer les fct° de jeu utilisé en méthode de classe
-> enlever l'instance de jeu
"""

class Bot(Joueur):
    """
    Attributes
    ----------
    nom : str
        "Beep"
    historique : List<Question>
    personnage_mystere : Personnage
        Le personnage devant être deviné ce joueur (self)
    suspects : set<Personnage>
        Ensemble des personnages qui pourraient correspondre au personnage mystère
    map_attr_to_val : Dict<string,set<string>>
        clé : les attributs que possedent les suspects ; valeur : ensemble de valeurs que les suspects ont
    """
    
    def __init__(self, jeu:Jeu):
        Joueur.__init__(self, "Beep")
        self.jeu = jeu
        
        self.stop = False
        
        self.suspects = set()
        for perso in jeu.planche:
            self.suspects.add(perso)
            
        self.map_Attr_Val = jeu.calcule_MapAttibutsDomaine(jeu.planche)
        
    def __str__(self):
        s = super().__str__()
        
        s += f"\n    Les suspects : {len(self.suspects)}\n"
        # for p in self.suspects:
        #     print("    -", p.nom)
        s += "".join(list(map(lambda perso : f"        - {perso.nom} -> {perso.__str__()}\n", self.suspects)))
        s += self.map_Attr_Val.__str__() if len(self.map_Attr_Val) != 0 else "{empty}"
        return s
    
    def choisir_question_suivante(self) -> Phrase:    
        #choix de la caractéristque partagé par le plus de monde
        max = 0
        meilleurC = None
        for attribut in self.map_Attr_Val:
            for valeur in self.map_Attr_Val[attribut]:
                #l'ensemble des personnages ayant tel caractéristiques parmit l'ensemble des personnage suspects
                set_perso = self.jeu.get_perso_avec(Caracteristique(attribut,valeur), self.suspects)
                
                if len(set_perso) > max:
                    max = len(set_perso)
                    meilleurC = Caracteristique(attribut,valeur)
        
        q = Phrase(meilleurC.attribut, meilleurC.valeur)
        # q.caracteristique = meilleurC
        # print(q)
        return q
    
    def mise_a_jour(self, q:Phrase, reponse:bool) -> None:
        """Met a jour attributs de la classe en fonction de la réponse à la question poser
        
        Parameters
        ----------
        b : bool
            la réponse a la question que Bot pose
        """
        
        #on élimine de la liste des suspects les personnages qui ont répondu négativement à la question
        if reponse:
            list_perso = set(filter(lambda un_perso: not un_perso.correspond(q.caracteristique), self.suspects))
        else:
            list_perso = set(filter(lambda un_perso: un_perso.correspond(q.caracteristique), self.suspects))
        print("Perso à éliminer : ")
        print("".join(list(map(lambda perso : f"        - {perso.nom} -> {perso.__str__()}\n", list_perso))))
        
        self.suspects = self.suspects - list_perso
        assert self.personnage_mystere in self.suspects, "Le personnage mystère ne fait pas partie des suspects"
        self.liste_persos_coches = list(filter(lambda un_perso: un_perso not in self.suspects, self.jeu.planche))
        
        
        #maj de map_Attr_Val
        self.map_Attr_Val = self.jeu.calcule_MapAttibutsDomaine(self.suspects)


        # supression des clé qui renvoient vers des ensembles à 1 elem
        cle_a_suppr = []
        for key, value in self.map_Attr_Val.items():
            if len(value) == 1:
                cle_a_suppr.append(key)
                pass
        for i in range(len(cle_a_suppr)):
            del self.map_Attr_Val[cle_a_suppr[i]]
            
    def poser_question_tout_seul(self):
        if self.stop:
            raise Exception(f"j'ai trouvé mon perso mystère: {self.personnage_mystere.nom}")
        
        une_question = self.choisir_question_suivante()
        reponse = self.poser_question(une_question)
        print(f"{une_question}? -> {reponse}")
        self.mise_a_jour(une_question, reponse)
        
        
        return une_question, reponse

    
    