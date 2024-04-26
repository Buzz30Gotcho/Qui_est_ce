from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import threading
import os

from project.src.interfaces.bibliotheque.InterfaceJeu import InterfaceJeu
from project.src.interfaces.interfaceJeu.CadreToutesLesImagesJeu import CadreToutesLesImagesJeu
from project.src.interfaces.interfaceJeu.CadreInterractions import CadreInterractions
from project.src.interfaces.interfaceJeu.ScrollableFrame import ScrollableFrame

from project.src.bibliotheque.SaveMethod import sauvegarder

class InterfaceJeuReseau(InterfaceJeu)  :

    
    


    def __init__(self, jeu, pseudoJoueurEnFace):

        InterfaceJeu.__init__(self, jeu)

        self.cadreToutesLesPhotos.stopClicDroit()
        self.cadreToutesLesPhotos.remettreClicGauche()

        self.pseudoAutreJoueur = pseudoJoueurEnFace



        self.messagerie = Text(self.cadreLePlusHaut, state="disabled", height=5, width = 46, font=("Courier", 14), wrap="word")
        self.messagerie.pack(pady=40)

        labelEnvoyerMessage = Label(self.cadreLePlusHaut, text="Envoyer votre Message ici", font=("Courier", 11))
        labelEnvoyerMessage.pack()

        self.envoieMessage = Text(self.cadreLePlusHaut, height = 2, width=30, font =("Courier", 13), wrap="word")
        self.envoieMessage.pack(pady=15)

        self.envoieMessage.bind("<KeyRelease-Return>", self.envoyerMessage)


        self.boutonEnvoyerMessage = Button(self.cadreLePlusHaut, text="Envoyer", command=self.envoyerMessage)
        self.boutonEnvoyerMessage.pack(pady=15)


        self.messagerie.tag_config("Moi", foreground="blue")
        self.messagerie.tag_config("Jeu", foreground="red")
        self.messagerie.tag_config(self.pseudoAutreJoueur, foreground="green")


        self.messageServeur("Bienvenue sur le jeu Qui-est-ce?\n")
        self.messageServeur("Pour discuter avec " + self.pseudoAutreJoueur + ", envoyez votre message dans la zone de texte prévue à cet effet\n" )
        self.messageServeur("Bon Jeu !\n")

    def appuiSurEnvoyer(self, nomTag):
        
        nbr = len(self.pseudoAutreJoueur)
        if nomTag== "Jeu" or nomTag == "Moi":
            nbr = 4
        
        indexDerniereLigne = str(int(self.messagerie.index('end').split(".")[0] )-2)
        self.messagerie.tag_add(nomTag, indexDerniereLigne+".0" , indexDerniereLigne + "." +str(nbr))


    def envoyerMessage(self, eventonsenfiche=None):

        self.messagerie.config(state= "normal")


        texteAenvoyer = self.envoieMessage.get("1.0", "end")
        texteAenvoyer = texteAenvoyer[:texteAenvoyer.find("\n")]+"\n"

        

        self.jeu.envoyer_message(texteAenvoyer)

        
        self.messagerie.insert("end", "Moi>" + texteAenvoyer)
        self.appuiSurEnvoyer("Moi")


        self.envoieMessage.delete("1.0", "end")
        self.envoieMessage.mark_set("insert", "1.0")

        self.messagerie.see("end")
             
        self.messagerie.config(state= "disabled")



    def receptionMessage(self, message):
        self.messagerie.config(state= "normal")

        self.messagerie.insert("end", self.pseudoAutreJoueur + "> " + message)
        self.appuiSurEnvoyer(self.pseudoAutreJoueur)

        self.messagerie.see("end")

        self.messagerie.config(state= "disabled")


    def messageServeur(self, message):

        self.messagerie.config(state= "normal")

        self.messagerie.insert("end", "Jeu> " + message)
        self.appuiSurEnvoyer("Jeu")

        self.messagerie.see("end")

        self.messagerie.config(state= "disabled")


        


    def launch(self):
        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()
        
        self.mainloop()
            
        # le mec ferme la fenetre
        print("The system> Envoie du  signal pour terminer la discussion")
        self.jeu.envoyer_message("Goodbye!")
        
            
    def receive(self):
        msg = "foo"
        while True:
            try: 
                msg = self.jeu.recevoir_message()

                self.receptionMessage(msg)

                print(f"The other guy said> {msg}.")
                    
                if msg == "Goodbye!":
                    print(f"The system> Veuillez fermer la fenêtre.")
                    
                    self.jeu.envoyer_message("Goodbye!") # signal pour que l'autre s'arrête correctement
                     
                    break # fin du thread
            except:
                print("arret de la reception message")
                self.jeu.co.close()
                break # fin du thread
                


    def envoyerMsg(self):
        print(f"You say> {self.entryJsp.get()}")
        self.jeu.envoyer_message(self.entryJsp.get())
