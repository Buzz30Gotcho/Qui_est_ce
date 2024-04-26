from tkinter import *
from tkinter.messagebox import askquestion
from tkinter.ttk import *


from project.src.interfaces.interfaceGenerateur.FenModifAttr import FenModifAttr
from project.src.interfaces.interfaceGenerateur.FenetreAddAttribut import FenetreAddAttribut

from project.src.interfaces.bibliotheque.ToplevelPopUp import ToplevelPopUp

class FenetreListeAttributs(ToplevelPopUp):


# Création de la fenetre
    def __init__(self, parent):
        ToplevelPopUp.__init__(self, parent)

        self.minsize(None, 600)

        # Création des zones de texte 
        labelEntete = Label(self, text = "Liste des attributs :")
        labelEntete.pack(pady=20, padx=50)

        # création d'une liste qui contient la liste des attributs sous forme de label
        self.listeLabelAttributs = []


        # Création du frame qui contiendra tous les labels
        self.frameListeAttributs = Frame(self)
        self.frameListeAttributs.pack(pady=20)


        self.actualiserListe()

        # -----------------fin de la création du listeLabelAttributs-------------- 

        # Création des boutons
        boutonAddAttribut = Button(self, text="Ajouter un attribut", command=self.creerFenDefAttr)
        boutonValider = Button(self, text="Valider", command=self.destroy)

        # Ajout des labels et des boutons dans la frame principale


        

        boutonAddAttribut.pack( pady=20)
        boutonValider.pack(pady=20)

        



    def ClicAttribut(self, event):

        nomAttr = event.widget["text"]

        menu = Menu(self, tearoff=0)
        menu.add_command(label= "Modifier Attribut", command= lambda chaine = nomAttr :  self.modifierAttribut(chaine))
        menu.add_command(label= "Supprimer Attribut", command= lambda chaine = nomAttr : self.supprimerAttribut(chaine))

        try: 
            menu.tk_popup(event.x_root, event.y_root) 
        finally: 
            menu.grab_release()

    
        
    def actualiserListe(self):

        for widget in self.frameListeAttributs.winfo_children():
            widget.destroy()

        for attribut in self.__class__.generateur.all_attributs:
            labelAttribut = Label(self.frameListeAttributs, text = attribut.nom, cursor="hand2", font=('Arial', '18', 'bold underline'))
            labelAttribut.pack(pady=5)
            labelAttribut.bind("<Button-1>", self.ClicAttribut)
            self.listeLabelAttributs.append(labelAttribut)
        
                # y a plus d'attribut faut enlever les filtres verts
        if len(self.__class__.generateur.all_attributs) == 0 and self.__class__.fenetreGen.cadrePlateau != None:
            for perso in self.generateur.liste_perso:
                self.__class__.fenetreGen.cadrePlateau.dicoPerso_Frame[perso].effacerFiltreVert()

    

    
    def supprimerAttribut(self, nomAttr):
        # attributASuppr = ToplevelPopUp.getAttributFromNom(nomAttr)
        
        
        # self.attributes("-disabled", True)
        self.grab_release()
        
        if askquestion("Supression Attribut", "Voulez vous vraiment supprimer l'attribut : " + nomAttr + "?\nCette question peut rendre deux persos identiques") == "yes":
            self.__class__.generateur.supp_attribut(ToplevelPopUp.getAttributFromNom(nomAttr))
            self.actualiserListe()
            self.__class__.fenetreGen.cocherPersoRendusIdentiques()

        # self.attributes("-disabled", False)
        self.grab_set()
        self.lift()
    

    
    def modifierAttribut(self, nomAttr):

        attribut = ToplevelPopUp.getAttributFromNom(nomAttr)

        fenetreModifAttribut = FenModifAttr(self, attribut)
        self.popupFenetre(fenetreModifAttribut)
        self.actualiserListe()


        

    #on crée la fenetre pour définir les attributs
    def creerFenDefAttr(self):
        compteur = len(self.__class__.generateur.all_attributs)
        fenetreListeAttr = FenetreAddAttribut(self)
        self.popupFenetre(fenetreListeAttr)
        
        #l'user a bien ajouté un attribut
        if compteur < len(self.__class__.generateur.all_attributs):
            if self.__class__.fenetreGen.cadrePlateau != None:
                self.__class__.fenetreGen.cadrePlateau.enleverFiltreVert()
            self.actualiserListe()


        

