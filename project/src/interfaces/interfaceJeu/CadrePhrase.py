from tkinter import Button, Menu
from tkinter.ttk import *
import tkinter

from project.src.jeu.Phrase import Phrase
from project.src.interfaces.interfaceJeu.CadreQuestion import CadreQuestion



class CadrePhrase(CadreQuestion):
    """Cadre qui contiendra une seule question et la possibilité d'en ajouter d'autres"""

    dicoAttrVal = {}



#faut prendre en parametre 
    def __init__( self, parent ):    

        #Construit le cadre qui contiendra la liste déroulante attribut, valeur, le connecteur logique etc
        CadreQuestion.__init__(self, parent)

        self.boutonAttribut = Menubutton(self, width=4, text="Attribut")
        

        self.menuAttribut = Menu(self.boutonAttribut)
        for texte in list(self.__class__.dicoAttrVal.keys()):
            self.menuAttribut.add_command(label=texte, command=lambda string=texte : self.changementAttribut(string))

        self.boutonAttribut["menu"] = self.menuAttribut


        #le pack faudra jouer avec les coordonnées du parent hein

        self.boutonAttribut.config(width=15) 
        self.boutonAttribut.pack(side="left", padx=10, pady=5)




        self.boutonValeur = Menubutton(self, width=4, text="Valeur", state="disabled")

        

        self.menuValeur = Menu(self.boutonValeur)
        self.boutonValeur["menu"] = self.menuValeur


        self.boutonValeur.config(width=15) 
        self.boutonValeur.pack(side="left", padx=10, pady=5)



        self.boutonSupprimerQuestion = Button(self, text="x", command=self.supprimer_phrase)
        self.boutonSupprimerQuestion.pack(padx=10, side="left", pady=5)
        self.boutonSupprimerQuestion.config(width=1)



    def supprimer_phrase(self):

        self.master.supprimer_question(self)


    def changementAttribut(self, string):
        self.boutonAttribut["text"] = string

        self.menuValeur.delete(0,"end")

        self.boutonValeur.configure(state="normal")

        for valeur in self.__class__.dicoAttrVal[string]:
                self.menuValeur.add_command(label=valeur, command=lambda chaineValeur = valeur : self.boutonValeur.configure(text=chaineValeur))
    


        

    #def choisirPerso(self, perso): #normalement je reçois un personnage, pas une string mais bon...
        



    def transformationEnQuestion(self):
        valeurDeLattr = self.boutonValeur["text"]

        if valeurDeLattr != "Valeur":
            return Phrase(self.boutonAttribut["text"], valeurDeLattr) #on retourne une instance de phrase avec
        else:
            raise Exception
        
        
        



    

        




    