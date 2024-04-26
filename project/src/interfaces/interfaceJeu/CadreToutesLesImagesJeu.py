from tkinter import Frame

from project.src.interfaces.interfaceJeu.CadreImagePersoJeu import CadreImagePersoJeu
from project.src.interfaces.bibliotheque.CadreToutesLesImages import CadreToutesLesImages #pour hériter

from project.src.jeu.Personnage import Personnage



class CadreToutesLesImagesJeu(CadreToutesLesImages):

    


    def __init__(self, parent, jeu, fenetreJeu):
        
        


        self.jeu = jeu
        metadonnees = self.jeu.metadonnees

        CadreImagePersoJeu.jeu = jeu
        CadreImagePersoJeu.fenetreJeu = fenetreJeu
        
        
        CadreToutesLesImages.__init__(self, parent, metadonnees)

        self.ajouter_perso(self.jeu.planche, jeu.metadonnees["images"])
        
        


    def cocher(self, liste_personnes_eliminees):
        for personnage in liste_personnes_eliminees:
            self.dicoPerso_Frame[personnage].dessiner_croix()


    def remettreClicGauche(self):
        for cadreImagePerso in self.dicoPerso_Frame.values():
            cadreImagePerso.canvasImagePerso.bind("<Button-1>", cadreImagePerso.dessiner_enlever_croix)
    
    def stopClicDroit(self): #pour éviter qu'on réaccuse un perso quand le partie est finie
        for cadreImagePerso in self.dicoPerso_Frame.values():
            cadreImagePerso.canvasImagePerso.unbind("<Button-2>")
            cadreImagePerso.canvasImagePerso.unbind("<Button-3>")
            cadreImagePerso.canvasImagePerso.unbind("<Button-1>")


    def effacerCroixTouteLaGrille(self):
        for cadreImagePerso in self.dicoPerso_Frame.values():
            cadreImagePerso.effacer_croix() # on décoche forcément tout quand une nouvelle partie se lance

            cadreImagePerso.canvasImagePerso.bind("<Button-1>", cadreImagePerso.dessiner_enlever_croix)
            cadreImagePerso.canvasImagePerso.bind("<Button-2>", cadreImagePerso.menuContextuelChoisirPerso)
            cadreImagePerso.canvasImagePerso.bind("<Button-3>", cadreImagePerso.menuContextuelChoisirPerso)

    def nouvellePartie(self):
        self.effacerCroixTouteLaGrille()
        
        self.cocher(self.jeu.joueur.liste_persos_coches)
    

    def get_liste_persos_coches(self):
        liste_persos_coches = []
        for perso, cadreImagePerso in self.dicoPerso_Frame.items():
            if cadreImagePerso.imageCroix != None:
                liste_persos_coches.append(perso)
        return liste_persos_coches


    def ajouter_perso(self, listePerso, cheminVersFichier ): #normalement y aura le nom du fihier dans le perso (je crois)
        

        for indice in range(len(listePerso)):
        #on garde le "numero" du perso, où il est situé sur le canvas
            cadreOuOnGrid=self.cadrePasDerniereLigne
            if indice // self.nbrColonne == self.nbrLigne-1:
                cadreOuOnGrid = self.cadreDerniereLigne


            self.dicoPerso_Frame[listePerso[indice]] = CadreImagePersoJeu(cadreOuOnGrid, cheminVersFichier + listePerso[indice].image, listePerso[indice])

            self.dicoPerso_Frame[listePerso[indice]].grid(row = indice // self.nbrColonne, column= indice % self.nbrColonne, padx=self.decalageEntrePhoto, pady = self.decalageEntrePhoto, sticky="we")

            
            

