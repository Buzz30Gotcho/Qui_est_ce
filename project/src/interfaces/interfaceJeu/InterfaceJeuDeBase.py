from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
import os

from project.src.interfaces.bibliotheque.InterfaceJeu import InterfaceJeu
from project.src.interfaces.interfaceJeu.CadreToutesLesImagesJeu import CadreToutesLesImagesJeu
from project.src.interfaces.interfaceJeu.CadreInterractions import CadreInterractions
from project.src.interfaces.interfaceJeu.ScrollableFrame import ScrollableFrame

from project.src.bibliotheque.SaveMethod import sauvegarder

class InterfaceJeuDeBase(InterfaceJeu)  :

    
    


    def __init__(self, jeu):

        InterfaceJeu.__init__(self, jeu)

        
        self.cadreHistorique = ScrollableFrame(self)

        self.nouvellePartie(False)


        self.laPartieEstTerminee = False
        

            



    def afficher_historique(self):
        if self.cadreHistorique.winfo_ismapped() != 1:
            self.supprimerBoutonMenubar("Historique des Questions")
            self.supprimerBoutonMenubar("Abandonner")
            self.menubar.add_command(label="Plateau de Jeu", command=self.afficher_plateau_jeu)
            self.cadreLePlusHaut.pack_forget()
            self.cadreHistorique.pack()

            
            for question in self.jeu.joueur.get_historique():
                cadreQuestionHistorique = Label(self.cadreHistorique.scrollable_frame, text="Question :   " + question[0].__str__()+"\n        Réponse : "+str(question[1]))
                cadreQuestionHistorique.pack(pady=20, padx=40)


    def afficher_plateau_jeu(self):
        if self.cadreLePlusHaut.winfo_ismapped() != 1:
            self.supprimerBoutonMenubar("Plateau de Jeu")

            if not self.laPartieEstTerminee:
                self.menubar.add_command( label="Abandonner", command = self.abandon)

            self.menubar.add_command(label="Historique des Questions", command=self.afficher_historique)
            self.cadreHistorique.pack_forget()
            self.cadreLePlusHaut.pack()

            for cadreHistoriqueQuestion in self.cadreHistorique.scrollable_frame.winfo_children():
                cadreHistoriqueQuestion.destroy()
    


    def sauvegarderQuitter(self):
        if askquestion("Sauvegarder et Quitter", "Voulez vous sauvegarder et quitter la partie?") == "yes":

            #on enregistre la position des cases cochées dans joueur
            self.jeu.joueur.liste_persos_coches = self.cadreToutesLesPhotos.get_liste_persos_coches()
            self.jeu.sauvegarderPartie()
            exit()
    


    def partie_terminee(self, message):

        self.cadreScrollableInterraction.destroy()


        self.laPartieEstTerminee=True

        self.cadreToutesLesPhotos.stopClicDroit()

        self.supprimerBoutonMenubar("Sauvegarder et Quitter")
        
        
        super().partie_terminee(message)

        


        #on supprime la sauvegarde, prck on enregistre pas une partie finie
        try :
            os.remove("ressources/sauvegarde/jeu/" + self.jeu.joueur.nom + ".pickle") #on supprime la partie pour pas relancer une partie déjà terminée
        except: # si y a pas de sauvegarde, bah y a pas de sauvegarde mdr
            pass


    def nouvellePartie(self, PasPremierePartie = True ):

        self.laPartieEstTerminee=False

        super().nouvellePartie(PasPremierePartie)

        self.creationCadreInterraction()
        self.cadreToutesLesPhotos.nouvellePartie()


        if not PasPremierePartie:
            self.menubar.add_command(label="Historique des Questions", command=self.afficher_historique)
        self.menubar.insert_command(1, label="Sauvegarder et Quitter", command = self.sauvegarderQuitter)



    def creationCadreInterraction(self):
        #création du cadre pour poser les questions, valider, connecteurs logiques etc

        self.cadreScrollableInterraction = ScrollableFrame(self.cadreLePlusHaut)
        self.cadreInterraction = CadreInterractions(self.cadreScrollableInterraction.scrollable_frame, self.jeu, self)
        self.cadreInterraction.pack(fill='x', pady=15)
        self.cadreScrollableInterraction.pack(fill="x")
        



