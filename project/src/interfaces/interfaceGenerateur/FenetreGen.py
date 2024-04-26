from tkinter import *

from tkinter.messagebox import *

from project.src.interfaces.interfaceGenerateur.CadreToutesLesImagesGen import CadreToutesLesImagesGen
from project.src.interfaces.interfaceGenerateur.CadreImagePersoGen import CadreImagePersoGen


from project.src.interfaces.interfaceGenerateur.FenetreDefPerso import FenetreDefPerso
from project.src.interfaces.interfaceGenerateur.FenetreListeAttributs import FenetreListeAttributs

from project.src.interfaces.interfaceGenerateur.FenetreConfigurationPlateau import FenetreConfigurationPlateau
from project.src.generateur.generateur import Generateur

from project.src.interfaces.bibliotheque.ToplevelPopUp import ToplevelPopUp

from project.src.bibliotheque.SaveMethod import sauvegarder


import os
from PIL import Image
from tkinter.ttk import *
import tkinter.font




class FenetreGen(Tk):
    def __init__(self, gen):

        Tk.__init__(self)

        ToplevelPopUp.generateur = gen
        ToplevelPopUp.fenetreGen = self
        
        CadreImagePersoGen.fenetreGen = self
        CadreToutesLesImagesGen.fenetreGen = self

        self.generateur = gen
        self.metadonnees = {}

        self.style = Style(self)
        # self.font = Font(self, size=20)



        self.defaultFont = tkinter.font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Helvetica",
                                   size=16)


        cadreTop = Frame(self)

        boutonPersonnalisationPlateau = Button(cadreTop, text="Personnalisation\nPlateau", command=self.creerFenetrePersonnalisationPlateau)
        boutonPersonnalisationPlateau.grid(row=0, column=0, padx=30, pady=25)

        configurationAttribut = Button(cadreTop, text = "configuration\nAttribut", command = self.creerFenListeAttr)
        configurationAttribut.grid(row=0, column=1, padx=30, pady=25)

        cadreTop.pack(pady=30)
        


        self.cadrePlateau = None





        self.metadonnees = {"images" : self.generateur.path,\
                            "ligne" : self.generateur.nbLignes,\
                            "colonne" : self.generateur.nbColonnes,\
                            "largeurImage" :self.generateur.largeurImage,\
                            "hauteurImage" : self.generateur.hauteurImage,\
                            "espacementPhoto" : self.generateur.espacementPhoto,\
                            "tailleMaxHauteurImage" : self.generateur.tailleImage}

        
        #c'est la premiere fois que son générateur est ouvert
        if self.metadonnees["largeurImage"] == 0:
            size = (Image.open(gen.path + os.listdir(gen.path)[0])).size
            print(size)

            self.metadonnees["largeurImage"] = size[0]
            self.metadonnees["hauteurImage"] = size[1]

            self.generateur.largeurImage = size[0]
            self.generateur.hauteurImage = size[1]

        
        #on crée l'ancien cadre
        self.creation_CadreToutesLesImages()

        #on coche les anciens persos cochés
        self.cocherPersoRendusIdentiques()

        #on met un filtre vert sur ceux qui sont bons
        if self.generateur.all_attributs:
            for perso in self.generateur.liste_perso:
                if perso.est_complete():
                    self.cadrePlateau.dicoPerso_Frame[perso].dessinerFiltreVert()

    


        


        boutonGenererJson = Button(self, text="Générer fichier JSON", command=self.verification)
        boutonGenererJson.pack(side="bottom", pady=30)


        self.protocol("WM_DELETE_WINDOW", self.quitter)
        

    
    def creation_CadreToutesLesImages(self):
        if self.cadrePlateau != None:
            self.cadrePlateau.destroy()
            self.cadrePlateau = None

        self.cadrePlateau = CadreToutesLesImagesGen(self, self.metadonnees)
        self.cadrePlateau.pack(pady=20)


        #----------------------------------------- modifier avec self.generateur.path
        self.cadrePlateau.ajouter_perso(self.generateur.liste_perso, self.generateur.path)

        


    #on crée la fenetre pour definir les attributs d'un perso
    def modifierAttrPerso(self, cadreImgPersoGen):
        #il faut ouvrir une fenetre defperso et faut empecher de pouvoir rajouter/enlever des attributs
        if self.generateur.all_attributs:


            fenetreModifAttrPerso = FenetreDefPerso(self, cadreImgPersoGen)

            
            self.wait_window(fenetreModifAttrPerso)
            self.grab_set()
        
            self.lift()

            self.cadrePlateau.croixSurPersoSimilaire(cadreImgPersoGen.perso)

        else:
            showinfo("pas d'attribut", "Veuillez d'abord définir des attributs\n avant de définir les personnages")



    
    #on crée la fenetre qui va lister les attributs pour définir les attributs
    def creerFenListeAttr(self):

        fenetreListeAttr = FenetreListeAttributs(self)
        self.grab_release()
       
        self.wait_window(fenetreListeAttr)
        self.grab_set()
        
        del fenetreListeAttr
        self.lift()


    def verification(self):
        message = ""

        for perso in self.generateur.liste_perso:
            if not perso.est_complete():
                message = "Des persos sont incomplets.\nVeuillez les définir"

        if self.generateur.nb_perso_max() < len(self.generateur.liste_perso):
            message = "Le nombre actuel d'attribut ne permet pas de couvrir tous les persos\n Veuillez en ajouter, ou ajouter des valeurs"
        
        elif self.generateur.get_perso_similaire():
            message= "Des persos sont identiques.\nVeuillez les définir autrement"

        elif self.cadrePlateau == None:
            message = "Le plateau doit être visible"

        #tout va bien, étrangement
        if message == "":  
            

            listeAttributsSupp = self.generateur.supp_attr_dans_perso_qui_ont_une_seul_valeur()
            if listeAttributsSupp:
                chainesAttrSupp = "\n\n"
                for attrSupp in listeAttributsSupp:
                    chainesAttrSupp += attrSupp.nom + "\n"
                showinfo ("Attributs supprimés", "Les attribut suivants ne permettaient pas de différencier\n deux persos et ont donc été supprimés:" + chainesAttrSupp )

            self.generateur.generer_fichier_json()
            sauvegarder(self.generateur, "sauvegarde_generateur", "ressources/sauvegarde/generateur/")
            showinfo("Sauvegarde réussie","Le fichier json a été généré dans le dossier :\n/ressources/JSON/")
            self.destroy()

        
        else:
            showinfo("Erreur", message)

       


    #si on supprime une valeur ou un attribut ça peut rendre des persos identiques
    def cocherPersoRendusIdentiques(self):
        
        if len(self.generateur.all_attributs) != 0:
            listePersosAcocher = self.generateur.get_perso_similaire()
            
            for perso in listePersosAcocher:
                if perso.est_complete():
                    self.cadrePlateau.dicoPerso_Frame[perso].dessiner_croix()
            

        else:
            for perso in self.generateur.liste_perso:
                self.cadrePlateau.dicoPerso_Frame[perso].effacer_croix()

    



    def creerFenetrePersonnalisationPlateau(self):

        fenetrePersonnalisation = FenetreConfigurationPlateau(self)
        self.grab_release()
       
        self.wait_window(fenetrePersonnalisation)
        self.grab_set()
        
        del fenetrePersonnalisation
        self.lift()




    def quitter(self):
        if askquestion("Quitter", "Voulez-vous sauvegarder et reprendre plus tard?\n(Cela pourrait écraser une ancienne sauvegarde)") == "yes":
            sauvegarder(self.generateur, "sauvegarde_generateur", "ressources/sauvegarde/generateur/")

        self.destroy()