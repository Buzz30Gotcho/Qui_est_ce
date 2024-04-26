from tkinter import Frame, Canvas, Menu
from PIL import Image, ImageTk

from project.src.interfaces.bibliotheque.CadreImagePerso import CadreImagePerso


class CadreImagePersoGen(CadreImagePerso):

    
    filtreVertChemin = "ressources/img/filtrePhoto/Green_filter.png"


    fenetreGen = None



    def __init__(self, parent, cheminFichierPhoto, perso):

        CadreImagePerso.__init__(self, parent, cheminFichierPhoto, perso)

        self.filtreVert= None

        self.canvasImagePerso.bind("<Button-1>", self.modifierAttribut)
    
    def modifierAttribut(self, event): #(on s'en fiche de l'event hein)
        self.__class__.fenetreGen.modifierAttrPerso(self)


    def dessiner_croix(self):
        self.effacerFiltreVert()
        super().dessiner_croix()
    

    
    def dessinerFiltreVert(self):

        self.effacer_croix()

        if self.filtreVert == None:
            imagePIL = Image.open(self.__class__.filtreVertChemin)
            imagePIL = imagePIL.resize(( self.__class__.largeurImage   , self.__class__.hauteurImage ) ,Image.ANTIALIAS)
            image = ImageTk.PhotoImage(imagePIL)

            self.filtreVert = image

            self.canvasImagePerso.create_image( 0, 0,  anchor="nw",   image=image)
            

    def effacerFiltreVert(self):
        if self.filtreVert != None:
            self.canvasImagePerso.delete(self.filtreVert)
            self.filtreVert = None

        

    
        
    

    
            
    


