from tkinter import Frame, Canvas, Menu
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk




from project.src.interfaces.bibliotheque.CadreImagePerso import CadreImagePerso


class CadreImagePersoJeu(CadreImagePerso):

    #seront modifés par CadreToutesLesImages

    
    jeu = None
    fenetreJeu = None



    def __init__(self, parent, cheminFichierPhoto, perso):

        CadreImagePerso.__init__(self, parent, cheminFichierPhoto, perso)

        
        

        self.canvasImagePerso.bind("<Button-1>", self.dessiner_enlever_croix)
        self.canvasImagePerso.bind("<Button-2>", self.menuContextuelChoisirPerso) #pour macOS
        self.canvasImagePerso.bind("<Button-3>", self.menuContextuelChoisirPerso)

        
        

    
    #cette fonction sera appelée au clic souris (je suis obligé)
    def dessiner_enlever_croix(self, evt): #dessine la croix et la rajoute à la dicoCroix pour pouvoir la supprimer plus tard


        if self.imageCroix != None: #si y a déjà une croix, on la supprime

            self.effacer_croix()

            
        else:  # si y a deja une ligne rouge, et donc une croix

            self.dessiner_croix()
            
    


    def menuContextuelChoisirPerso(self, event):
        menu = Menu(self, tearoff=0)
        menu.add_command(label= "Chosir ce personnage", command= self.accuserPerso)

        try: 
            menu.tk_popup(event.x_root, event.y_root) 
        finally: 
            menu.grab_release()

    
    def accuserPerso(self):
        if self.jeu.accuser(self.perso):
            texte="Bravo! Vous avez trouvé le personnage mystère!"

            self.__class__.fenetreJeu.partie_terminee(texte)
        
        else:
            showinfo("Pas le bon personnage", "Il ne s'agit pas du personnage : "+self.perso.nom)

