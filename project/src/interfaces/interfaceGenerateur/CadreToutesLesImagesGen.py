from project.src.interfaces.interfaceGenerateur.CadreImagePersoGen import CadreImagePersoGen
from project.src.interfaces.bibliotheque.CadreToutesLesImages import CadreToutesLesImages #pour hériter




class CadreToutesLesImagesGen(CadreToutesLesImages):

    fenetreGen = None

    def __init__(self, parent, metadonnees):
        
        
        CadreToutesLesImages.__init__(self, parent, metadonnees)
        


    def ajouter_perso(self, listePerso, cheminVersFichier ): #normalement y aura le nom du fihier dans le perso (je crois)
        

        for indice in range(len(listePerso)):
        #on garde le "numero" du perso, où il est situé sur le canvas
            cadreOuOnGrid=self.cadrePasDerniereLigne
            if indice // self.nbrColonne == self.nbrLigne-1:
                cadreOuOnGrid = self.cadreDerniereLigne


            self.dicoPerso_Frame[listePerso[indice]] = CadreImagePersoGen(cadreOuOnGrid, cheminVersFichier + listePerso[indice].fichier, listePerso[indice])

            self.dicoPerso_Frame[listePerso[indice]].grid(row = indice // self.nbrColonne, column= indice % self.nbrColonne, padx=self.decalageEntrePhoto, pady = self.decalageEntrePhoto, sticky="we")


    def croixSurPersoSimilaire(self, perso):
        
        #on s'assure que le perso est effectivemnt rempli, i.e. le mec a pas fermé la fenetre sans valider
        if perso.est_complete():

            #on décoche les personnages qui sont plus identiques
            listePersosCoches = self.__class__.fenetreGen.generateur.get_perso_similaire()

            for persoGen in self.__class__.fenetreGen.generateur.liste_perso:
                if persoGen.est_complete() and persoGen not in listePersosCoches:
                    self.dicoPerso_Frame[persoGen].dessinerFiltreVert()


            #on coche les personnages qui deviennent identiques
            listePerso = self.__class__.fenetreGen.generateur.comparer_perso_aux_restes(perso)

            if listePerso:
                self.dicoPerso_Frame[perso].dessiner_croix()
                for persoIdentique in listePerso:
                    self.dicoPerso_Frame[persoIdentique].dessiner_croix()
                    

    def enleverFiltreVert(self):
        for cadreImgPersoGen in self.dicoPerso_Frame.values():
            cadreImgPersoGen.effacerFiltreVert()

    
