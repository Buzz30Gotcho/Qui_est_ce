from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import time
import os

from project.src.interfaces.interfaceJeu.InterfaceJeuDeBase import InterfaceJeuDeBase
from project.src.interfaces.interfaceJeu.CadreToutesLesImagesJeu import CadreToutesLesImagesJeu
from project.src.interfaces.interfaceJeu.CadreInterractions import CadreInterractions
from project.src.interfaces.interfaceJeu.ScrollableFrame import ScrollableFrame

from project.src.bibliotheque.SaveMethod import sauvegarder

class InterfaceJeuBot(InterfaceJeuDeBase)  :


    def __init__(self, jeu):

        InterfaceJeuDeBase.__init__(self, jeu)
        

        self.cadreSceneBot = Frame(self)

        self.cadreHistoriqueBot = ScrollableFrame(self)


        labelInfoBot = Label(self.cadreSceneBot, text="Que voulez-vous savoir à propos du bot?")
        labelInfoBot.grid(row=0, column=0, columnspan = 2, pady=30, padx=30)


        boutonHistoriqueBot = Button(self.cadreSceneBot, text="Hitorique\ndu Bot", command=self.afficher_historique_bot)
        boutonHistoriqueBot.grid(row=1, column=0, pady=20, padx=25)


        boutonGrilleBot = Button(self.cadreSceneBot, text="Grille du Bot", command =self.grilleBot)
        boutonGrilleBot.grid(row=1, column=1, pady=20, padx=25)


    def partie_terminee(self, message, botATrouveAvant=False):

        if botATrouveAvant:
            message = "Dommage, le bot a trouvé avant vous!\n Le personnage que vous deviez trouver était : " +self.jeu.joueur.personnage_mystere.nom
        
        
        super().partie_terminee(message)
        self.supprimerBoutonMenubar("Bot")

        
        
       

    def nouvellePartie(self, PasPremierePartie = True ):

        super().nouvellePartie(PasPremierePartie)
        self.menubar.add_command(label="Bot", command = self.sceneBot)
        self.cadreInterraction.boutonValider.config(command = self.enclencherBot)



    def afficher_plateau_jeu(self):
        super().afficher_plateau_jeu()
        if self.cadreToutesLesPhotos.winfo_ismapped() == 1:
            self.menubar.add_command( label="Abandonner", command = self.abandon)
            self.menubar.add_command(label="Historique des Questions", command=self.afficher_historique)
        if not self.laPartieEstTerminee:
            self.menubar.add_command(label="Bot", command = self.sceneBot)

    def afficher_historique(self):
        super().afficher_historique()
        self.supprimerBoutonMenubar("Bot")
        


    
    def sceneBot(self):
        
        self.jeu.joueur.liste_persos_coches = self.cadreToutesLesPhotos.get_liste_persos_coches()

        self.cadreLePlusHaut.pack_forget()

        self.cadreSceneBot.pack()

        self.supprimerBoutonMenubar("Historique des Questions")
        self.supprimerBoutonMenubar("Abandonner")
        self.supprimerBoutonMenubar("Bot")
        self.menubar.add_command(label="Retour Plateau", command=self.retourPlateauJeu)


    def grilleBot(self):
        self.cadreSceneBot.pack_forget()

        self.cadreLePlusHaut.pack()
        self.cadreScrollableInterraction.pack_forget()

        self.cadreToutesLesPhotos.effacerCroixTouteLaGrille()

        self.cadreToutesLesPhotos.cocher(self.jeu.ordi.liste_persos_coches)
        self.cadreToutesLesPhotos.stopClicDroit()




    def afficher_historique_bot(self):

        
        self.cadreSceneBot.pack_forget()
        self.cadreHistoriqueBot.pack()

        
        for question in self.jeu.ordi.get_historique():
            cadreQuestionHistorique = Label(self.cadreHistoriqueBot.scrollable_frame, text="Question :   " + question[0].__str__()+"\n        Réponse : "+str(question[1]))
            cadreQuestionHistorique.pack(pady=20, padx=40)

    
    def retourPlateauJeu(self):

        self.cadreSceneBot.pack_forget()


        self.cadreHistoriqueBot.pack_forget()
        for cadreHistoriqueQuestion in self.cadreHistorique.scrollable_frame.winfo_children():
                cadreHistoriqueQuestion.destroy()

        self.supprimerBoutonMenubar("Retour Plateau")


        self.cadreToutesLesPhotos.nouvellePartie()


        self.afficher_plateau_jeu()

        self.cadreScrollableInterraction.pack()


    def enclencherBot(self):
        if self.cadreInterraction.questionCorrecte() != None:
            self.cadreInterraction.envoyerQuestion()


            

            questionPoseeParBot, reponse = self.jeu.ordi.poser_question_tout_seul()


            fenBotReflechi = Toplevel(self)
            labelBotReflechi = Label(fenBotReflechi, text="Le Bot réfléchi...")
            labelBotReflechi.pack(padx=30, pady=30)

            self.update()
            fenBotReflechi.update()

            time.sleep(2)

            fenBotReflechi.destroy()


            
            
            showinfo("Bot", "Le bot a posé la question :\n" + questionPoseeParBot.__str__())

            #le bot a gagné mdr
            if len(self.jeu.ordi.suspects) == 1:
                self.partie_terminee("", True)



