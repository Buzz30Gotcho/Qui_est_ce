from project.src.jeu.Jeu import Jeu
# from jeu.src.Question import Question
# from project.src.reseau.parsing import parse_reponse
import json
import os
# from jeu.src.Personnage import Personnage

class JeuReseau(Jeu):
    
    def __init__(self, co, metadonnees=None):
        Jeu.__init__(self, metadonnees, False)
        
        self.co = co
        state = 0
        
        # print(type(self.fd_read))
        # print(type(self.fd_write))
            
    # def envoie_question(self, une_question:Question):
    #     s = une_question.to_dict().__str__()
    #     self.fd_write.write(s)
    #
    # def envoie_reponse(self, reponse:str):
    #     d = {"reponse":reponse}
    #     self.fd_write.write(d.__str__())
    #
    # def recevoir_reponse(self) -> str:
    #     rep_string = self.fd_read.read()
    #     rep_dict = json.loads(rep_string)
    #
    #     return parse_reponse(rep_dict)
    #
    #
    #
    # def envoie_accusation(self, un_personnage:Personnage):
    #     d = {"personnage":un_personnage.nom}
    #     self.fd_write.write(d.__str__())
    #
    # def envoie_accusation_reponse(self, message:str): 
        
    # def recevoir_accusation(self):
    #     s = self.fd_read.read()
    #
    #     d = json.load(s)
    #
    #     #parcours pour trouver le bon perso
    #     accuse = None
    #
    #     return 
    
    # def envoyer_nom_plateau(self, nom_plateau):
        # pass
        # d = dict()
        # d["nom_plateau"] = nom_plateau
        # self.fd_write.write(json.encoder(d).__str__)
    # def recevoir_nom_plateau(self, d:dict) -> str:
    #     pass
    
    def envoyer_choix_perso(self,nom:str):
        pass
    
    
    def envoyer_message(self, mess:str):
        self.co.send(mess.encode())
    
    def recevoir_message(self) -> str:
        return self.co.recv(1024).decode()


