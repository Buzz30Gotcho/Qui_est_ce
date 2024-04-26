from project.src.jeu.Caracteristique import Caracteristique
from project.src.jeu.Personnage import Personnage
from project.src.jeu.Joueur import Joueur
from project.src.jeu.Question import Question
from project.src.bibliotheque.SaveMethod import sauvegarder
from random import random


class Jeu(object):
    
    def __init__(self, metadonnees=None, modeFacile=False):
        #attributs
        self.joueur = None
        self.planche = [] #ensembles des personnages
        self.modeFacile = modeFacile


        if metadonnees is not None:
            self.metadonnees = metadonnees
            self.metadonnees["modeFacile"] = self.modeFacile
            
    def __str__(self):
        s = ""
            
        s = s + ""
        s += "Jeu :\n"
        s += f"{self.modeFacile = }\n"
        s += "self.planche = \n" 
        s += "".join(list(map(lambda perso : f"    {perso.nom} -> {perso.__str__()}\n", self.planche)))
        s += f"J1 = {self.joueur.__str__()}\n"
        
        return s
            

    def remplissage_planche(self, posibilites):
        
        for indice in posibilites:
            un_perso = Personnage()

            for attribut, valeurs in posibilites[indice].items():
                if attribut == "fichier":
                    un_perso.image = valeurs[0]
                elif attribut == "nom":
                    un_perso.nom = valeurs[0]
                else:
                    for valeur in valeurs:
                        un_perso.description.append(Caracteristique(attribut,valeur))

            self.planche.append(un_perso)
            
    def get_set_all_attributs(self):
        all_attributs = set()
        
        for perso in self.planche:
            for carac in perso.get_caracteristique():
                all_attributs.add(carac.attribut)
            
        return all_attributs
    
    
    
    def set_joueur(self,j:Joueur):
        self.joueur = j
        j.jeu = self
    
    def reset(self):
        #choix d'un nouveau personnage mystere
        
        self.joueur.historique = []
        self.joueur.personnage_mystere = self.planche[int(random()*len(self.planche))]
        self.joueur.liste_persos_coches = []

    def accuser(self, perso_accuse: Personnage, j:Joueur=None) -> bool:
        """Pendant le tour du joueur j, j essaie de deviner son personnage mystère
        """    
        j = self.joueur if j == None else j
        return j.personnage_mystere == perso_accuse
    
    def evaluer(self, q:Question, test:bool = False, j:Joueur = None) -> bool:
        """Pendant le tour du joueur j, j pose ça question et on renvoie la réponse directement
            
            Parameters
            ----------
            q : Question
                la question poser par le joueur courant
            test : bool
                est-ce que le joueur veut valider la question ou veut "tester" la question (pour vérifier combien de personnages seront éliminés)
            
            Returns
            ----------
            bool
                True ssi le personnage mystère correspond à la question
        """    
        j = self.joueur if j == None else j
        return j.poser_question(q, test)
        
    """
        Methodes développés pour le mode FACILE
    """
    """
        Methodes utilitaires au mode FACILE
    """
    """
        Main methode mode FACILE
    """


    
    def calcule_MapAttibutsDomaine(self, list_perso=None) -> dict:
        """Renvoie un dictionnaire des attribus associés à leurs valeurs. dict<str, set<str>>
                        
            Returns
            ----------
            dict[str, set[str]]
                attribut -> {val-1, val-2, val3-, ..., val-n}
        """    
        
        if list_perso == None:
            list_perso = self.planche
        
        map_Attr_Val = dict()
        for perso in list_perso:
            for carac in perso:
                if carac.attribut not in map_Attr_Val:
                    map_Attr_Val[carac.attribut] = set()
                map_Attr_Val[carac.attribut].add(carac.valeur)
        
        return map_Attr_Val

    def get_perso_invalide(self, q: Question, j: Joueur = None) -> set:
        """Renvoie une liste des personnages répondant False à la question q.
            

            
            Parameters
            ----------
            q : Question
                la question à poser à tous les personnages
            
            Returns
            ----------
            list[Personnage]
                list de Personnage
        """    
        ensemble_invalides = set()
        
        j = self.joueur if j == None else j

        #on veut savoir ce que repond le perso mystere pour voir quels personnages seront éliminés des sus
        reponsePersoMystere = j.poser_question(q, True)

        for perso in self.planche:
            
            if q.evaluer(perso) != reponsePersoMystere:
                ensemble_invalides.add(perso)
        return ensemble_invalides
    
    
    
    ###########################################    
    ### Extentions : Algorithme de décision ###
    ###########################################
    
    def get_perso_avec(self, c:Caracteristique, S:set) -> set:
        """Recherche les personnages qui ont la caracteristique c et appartienent à l'ensemble S"""
        result = set()
        for perso in self.planche:
            if (perso.correspond(c)) and (perso in S):
                result.add(perso)
                
        return result



    def sauvegarderPartie(self):
        
        sauvegarder(self, self.joueur.nom)
   
