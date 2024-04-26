from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

from project.src.interfaces.interfaceJeu.CadreToutesLesImagesJeu import CadreToutesLesImagesJeu


class InterfaceJeu(Tk)  :

    
    def __init__(self, jeu):

        Tk.__init__(self)

        
        self.style = Style(self)
        self.style.configure('TLabel', font=('Helvetica', 15))
        self.style.configure('TButton', font=('Helvetica', 15), padding=3)
        # self.style.configure('To')


        
        self.jeu = jeu #on garde une référence de jeu (on va en avoir besoin mdr)
        
        self.title("Qui-est-ce?")

       

        self.menubar= Menu(self)
        self.config(menu=self.menubar)


        self.cadreLePlusHaut = Frame(self)
        self.cadreLePlusHaut.pack()


        self.cadreToutesLesPhotos = CadreToutesLesImagesJeu(self.cadreLePlusHaut, self.jeu, self)
        self.cadreToutesLesPhotos.pack()

        
             
        


    def partie_terminee(self, message):
        
        

        self.cadrePartieTerminee = Frame(self.cadreLePlusHaut)
        self.cadrePartieTerminee.pack()

        

        messagePartieTerminee = Label(self.cadrePartieTerminee, text = message)
        messagePartieTerminee.grid(row = 0, column=0, columnspan=2,  pady=15)


        boutonRejouer = Button(self.cadrePartieTerminee, text="Rejouer", command= self.nouvellePartie)
        boutonRejouer.grid( row=1, column=0, pady=20, padx=20)
        boutonQuitter = Button(self.cadrePartieTerminee, text="Quitter", command=exit)
        boutonQuitter.grid( row=1, column=1, pady=20, padx=20)

        self.supprimerBoutonMenubar("Abandonner")

        





    def abandon(self):
        if askquestion("Abandonner", "Voulez vous vraiment abandonner?") == "yes":

            
            texte= "Dommage le personnage mystère était : " + self.jeu.joueur.personnage_mystere.nom

            self.partie_terminee(texte)


    def nouvellePartie(self, PasPremierePartie = True ):

        if PasPremierePartie: #au debut d'une premiere partie je dois pas reset le jeu
            self.jeu.reset()
            self.cadrePartieTerminee.destroy()


        self.menubar.insert_command(1, label="Abandonner", command = self.abandon)

    def supprimerBoutonMenubar(self, nomBouton):
        nbrDeEntries = self.menubar.index("end")

        for i in range(1, nbrDeEntries+1):
            if self.menubar.entrycget(i, "label") == nomBouton:
                self.menubar.delete(i)
                break


