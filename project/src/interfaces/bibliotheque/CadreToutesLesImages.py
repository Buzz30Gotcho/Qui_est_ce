from tkinter import Frame

from project.src.interfaces.bibliotheque.CadreImagePerso import CadreImagePerso
from project.src.jeu.Personnage import Personnage


class CadreToutesLesImages(Frame):

    


    def __init__(self, parent, metadonnees):
        
        
        Frame.__init__(self, parent, background="#B2B2B2" )


        
        
        
        self.calculerLargeur(metadonnees["hauteurImage"], metadonnees["tailleMaxHauteurImage"], metadonnees["largeurImage"])



        self.dicoPerso_Frame = {}

        self.nbrColonne = metadonnees["colonne"]
        self.nbrLigne = metadonnees["ligne"]

        self.decalageEntrePhoto = metadonnees["espacementPhoto"]



        CadreImagePerso.hauteurImage = metadonnees["tailleMaxHauteurImage"]


        self.cadrePasDerniereLigne = Frame(self, background="#B2B2B2")
        self.cadreDerniereLigne = Frame(self, background="#B2B2B2")

        self.cadrePasDerniereLigne.pack()
        self.cadreDerniereLigne.pack(fill="y")

        
    def calculerLargeur(self, hauteurImage, tailleMaxHauteurImage, largeurImage):
        ratioDivision = hauteurImage / tailleMaxHauteurImage
        nouvelleLargeurImage = round( largeurImage / ratioDivision)
        CadreImagePerso.largeurImage = nouvelleLargeurImage

        

    def ajouter_perso(self, listePerso, cheminVersFichier ): #normalement y aura le nom du fihier dans le perso (je crois)
        

        for indice in range(len(listePerso)):
        #on garde le "numero" du perso, où il est situé sur le canvas
            cadreOuOnGrid=self.cadrePasDerniereLigne
            if indice // self.nbrColonne == self.nbrLigne-1:
                cadreOuOnGrid = self.cadreDerniereLigne


            self.dicoPerso_Frame[listePerso[indice]] = CadreImagePerso(cadreOuOnGrid, cheminVersFichier + listePerso[indice].description[0].valeur, listePerso[indice])

            self.dicoPerso_Frame[listePerso[indice]].grid(row = indice // self.nbrColonne, column= indice % self.nbrColonne, padx=self.decalageEntrePhoto, pady = self.decalageEntrePhoto, sticky="we")


                

    