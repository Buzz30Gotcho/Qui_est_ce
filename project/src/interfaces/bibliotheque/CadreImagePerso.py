from tkinter import Frame, Canvas, Menu
from PIL import Image, ImageTk


class CadreImagePerso(Frame):

    #seront modifés par CadreToutesLesImages
    cheminImageCroix = "ressources/img/filtrePhoto/croix.png"

    largeurImage = 0 
    hauteurImage = 0



    def __init__(self, parent, cheminFichierPhoto, perso):

        Frame.__init__(self, parent, width=self.__class__.largeurImage, height=self.__class__.hauteurImage, highlightthickness=2, highlightcolor="black", takefocus=1 )

        
        self.perso = perso

        self.canvasImagePerso = Canvas(self, width = self.__class__.largeurImage, height = self.__class__.hauteurImage)
        self.canvasImagePerso.pack()



        #on doit garder les références sinon ça affiche pas
        self.imageCroix = None
        self.imagePerso = None

        self.dessiner_perso(cheminFichierPhoto)

        

        self.bind("<Enter>", self.donner_focus)
        

        
        

    def donner_focus(self, event):
        self.focus_set()

        

    


    def dessiner_perso(self, cheminFichierPhoto ):
        imagePIL = Image.open(cheminFichierPhoto)
        imagePIL = imagePIL.resize(( self.__class__.largeurImage   , self.__class__.hauteurImage ) ,Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imagePIL)

    
        self.imagePerso = image

        self.canvasImagePerso.create_image( 0, 0,  anchor="nw",   image=image)
        

    
    def dessiner_croix(self):
        if self.imageCroix == None:
            imagePIL = Image.open(self.__class__.cheminImageCroix)
            imagePIL = imagePIL.resize(( self.__class__.largeurImage   , self.__class__.hauteurImage ) ,Image.ANTIALIAS)
            image = ImageTk.PhotoImage(imagePIL)

            self.imageCroix = image

            self.canvasImagePerso.create_image( 0, 0,  anchor="nw",   image=image)
            
        
    def effacer_croix(self):
        if self.imageCroix != None:
            self.canvasImagePerso.delete(self.imageCroix)
            self.imageCroix = None
