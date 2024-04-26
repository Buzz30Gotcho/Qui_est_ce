from project.src.jeu.Question import Question

class Joueur:
    """
    Une classe pour représenter un joueur.
    
    Attributes
    ----------
    nom : str
        nom du joueur
    historique : List<Question>
        une liste de Question poser par ce joueur
    personnage_mystere : Personnage
        Le personnage devant être deviné ce joueur (self)
    """
    def __init__(self, nom:str):
        self.nom = nom
        self.historique = []
        self.personnage_mystere = None
        self.jeu = None

        #cet attribut sera modifié à chaque sauvegarde
        self.liste_persos_coches = []
            

        
    def __str__(self) -> str:
        return self.nom + " | " + self.personnage_mystere.nom + " -> " + self.personnage_mystere.__str__()

    def get_historique(self):
        return self.historique
        
        
    def poser_question(self, q:Question, test=False) -> bool:
        """Pose une question q à self.

        Args:
            q (Question): la question posé
            test (bool): True si la question q a été validé, False si le mode facile est activé et le joueur "test" la question
                (default is False)
        
        Returns:
            bool: la réponse à la question q, True ssi le personnage mystère correspond à q (True)
        """

        resultat = q.evaluer(self.personnage_mystere)

        if not test: #si c'est juste pour savoir le nombre de persos que le joueur élimine avec cette question
            self.historique.append([q,resultat])
        
        return resultat

    
