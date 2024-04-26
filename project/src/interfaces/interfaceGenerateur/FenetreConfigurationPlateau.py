from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from project.src.interfaces.bibliotheque.ToplevelPopUp import ToplevelPopUp


class FenetreConfigurationPlateau(ToplevelPopUp):

    def __init__(self, parent):

        ToplevelPopUp.__init__(self, parent)



        self.ligne= StringVar()
        self.colonne= StringVar()
        self.espacementPhoto= StringVar()
        self.tailleImage= StringVar()



        #-------------------- On recharge les anciennes valeurs du générateur si jamais c'est une sauvegarde-----------
        self.ligne.set(self.__class__.generateur.nbLignes)
        self.colonne.set(self.__class__.generateur.nbColonnes)
        self.espacementPhoto.set(self.__class__.generateur.espacementPhoto)
        self.tailleImage.set(self.__class__.generateur.tailleImage)

        self.change_ligne(None)
        self.change_colonne(None)
        self.change_espacementPhoto(None)
        self.change_tailleImage(None)
        #  --------------------------------------------------------------------------------

            

# --------------------- création des entry et tout et tout -----------------




        #Cadre qui sera à gauche du frameTopGenerateur,  ce sera plus facile pour grid
        cadrePourLesEntry = Frame(self)


        # Création du bouton ligne
        labelNbrLigne = LabelFrame(cadrePourLesEntry, borderwidth=0, labelanchor="n", text = " Nombre de Ligne")
        self.entryNbrLigne = Entry(labelNbrLigne, textvariable=self.ligne)


        # Création du bouton colonne
        labelNbrColonne = LabelFrame(cadrePourLesEntry, borderwidth=0, labelanchor="n", text = "Nombre de Colonne")
        self.entryNbrColonne = Entry(labelNbrColonne, textvariable=self.colonne)



        # Création du bouton EspacementPhoto 
        labelEspacementPhoto = LabelFrame(cadrePourLesEntry, borderwidth=0, labelanchor="n", text = "Espacement des Cadres (en px)")
        self.entryEspacementPhoto = Entry(labelEspacementPhoto, textvariable=self.espacementPhoto)


        # Création du bouton tailleImage 
        labelTailleImage = LabelFrame(cadrePourLesEntry, borderwidth=0, labelanchor="n", text = "Hauteur de l'image (en px)")
        self.entryTailleImage = Entry(labelTailleImage, textvariable=self.tailleImage)



        self.boutonValider = Button(self, text= "Aperçu\nPlateau", command=self.clicSurApercu)




        #------------------ Packing des boutons et des frames -------------------- 

       


        cadrePourLesEntry.pack(pady=15)

        labelNbrLigne.grid(padx=25, pady=15, row=0, column=0)
        self.entryNbrLigne.pack()
        self.entryNbrLigne.bind("<FocusOut>", self.change_ligne)

        labelNbrColonne.grid(padx=25, pady=15,row=0, column=1)
        self.entryNbrColonne.pack()
        self.entryNbrColonne.bind("<FocusOut>", self.change_colonne)

        labelEspacementPhoto.grid(padx=25, pady=15,row=2, column=0)
        self.entryEspacementPhoto.pack()
        self.entryEspacementPhoto.bind("<FocusOut>", self.change_espacementPhoto)

        labelTailleImage.grid(padx=25, pady=15, row=2, column=1)
        self.entryTailleImage.pack()
        self.entryTailleImage.bind("<FocusOut>", self.change_tailleImage)


        self.boutonValider.pack(pady=15)




#




    def clicSurApercu(self):
        #fonction de generateur pour savoir si le nombre de colonne est bon etc
        # et SI c'est ok on instancie un nouveau cadreToutesLesImages ( faudrait que je vois si je le fais hériter aussi)
        

        #je suis obligé prck si le mec est en train de rentrer une entry et 
        #qu'il clic sur le bouton direct ça considère pas comme une perte de focus...
        self.change_ligne(1)
        self.change_colonne(1) #1 c'est une valeur arbitraire hein
        self.change_espacementPhoto(1)
        self.change_tailleImage(1)


        self.__class__.generateur.nbColonnes = int(self.colonne.get())
        self.__class__.generateur.nbLignes = int(self.ligne.get())

        success = self.__class__.generateur.a_bonne_taille()
        if success == 0:
            self.__class__.fenetreGen.creation_CadreToutesLesImages()
            self.destroy()

        else:
            message = "Il y a trop de ligne/colonne\nIl n'y a que " + str(success) + " personnages à couvrir"
            if (int(self.colonne.get()) * int(self.ligne.get())) < success:
                message = "Il n'y a pas assez de ligne/colonne\nIl y a " + str(success) + " personnages à couvrir"
            showinfo("Mauvais nombre de ligne/colonne", message)



        print("instanciation cadreToutesLesImages")



        



# -----------------  dès que l'utilisateur a rentré une valeur ça vérifie et met des bonnes valeurs si probleme

    def change_ligne(self, jsp):
        try:
            if int(self.ligne.get()) < 0:
                self.ligne.set(0)
        except ValueError:
            self.ligne.set(0)
        
        self.master.metadonnees["ligne"]= int(self.ligne.get())
        self.__class__.generateur.nbLignes = int(self.ligne.get())


        
    def change_colonne(self, jsp):
        try:
            if int(self.colonne.get()) < 0:
                self.colonne.set(0)
                
        except ValueError:
                self.colonne.set(0)
        
        self.master.metadonnees["colonne"]= int(self.colonne.get())
        self.__class__.generateur.nbColonnes = int(self.colonne.get())




    def change_espacementPhoto(self, jsp):
        try:
            if  int(self.espacementPhoto.get()) < 0 or int(self.espacementPhoto.get()) > 65:
                self.espacementPhoto.set(0)
                
        except ValueError:
            self.espacementPhoto.set(0)

        self.master.metadonnees["espacementPhoto"]= int(self.espacementPhoto.get())
        self.__class__.generateur.espacementPhoto = int(self.espacementPhoto.get())




    def change_tailleImage(self, jsp):
        try:
            
            if int(self.tailleImage.get()) < 10 or int(self.tailleImage.get()) > 200 :
                self.tailleImage.set(100)
                
        except ValueError:
            self.tailleImage.set(100)

        self.master.metadonnees["tailleMaxHauteurImage"]= int(self.tailleImage.get())
        self.__class__.generateur.tailleImage = int(self.tailleImage.get())


#---------------------------------------------

