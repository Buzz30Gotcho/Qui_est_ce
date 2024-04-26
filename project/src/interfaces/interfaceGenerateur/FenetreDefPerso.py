from tkinter import *
from tkinter.ttk import *

from project.src.interfaces.bibliotheque.CadreImagePerso import CadreImagePerso

from project.src.interfaces.bibliotheque.ToplevelPopUp import ToplevelPopUp


class FenetreDefPerso(ToplevelPopUp):



    def __init__(self, fenetreGen, cadreImgPersoGen ):
        
        self.cadreImagePersoGen = cadreImgPersoGen
        self.perso = cadreImgPersoGen.perso




        #servira de buffer pour perso.description
        self.dictionnaireAttrVal = (self.perso.description).copy()
        # for attr in self.__class__.generateur.all_attributs:
        #     nomattr = attr.nom
        #     self.dictionnaireAttrVal[nomattr] = []
        

        ToplevelPopUp.__init__(self, fenetreGen)
        self.transient(fenetreGen)
        #c'est l'attribut en cours, je pense ça sera plus simple à gérer
        self.indiceAttributEnCours = 0

        # Creation des frames
        cadrePresentation = Frame(self)
        cadrePresentation.pack()
        

        # Creation des label  ----------A MODIFIER
        labelEntete = Label(cadrePresentation, text="Selectionnez une valeur pour les attribut du perso")
        labelEntete.grid(row=0)

        imagePerso = CadreImagePerso(cadrePresentation, self.__class__.generateur.path + self.perso.fichier, self.perso)
        imagePerso.grid(row=1)

        labelEntete2 = Label(cadrePresentation, text=self.perso.nom) #faut mettre la taille hein
        labelEntete2.grid(row=2)




        cadreValeur = Frame(self)
        cadreValeur.pack()
        
        # création list box attribut



        self.labelNomAttribut = Label(cadreValeur, text = self.__class__.generateur.all_attributs[self.indiceAttributEnCours].nom)
        self.labelNomAttribut.grid(row=0, column=0, columnspan=2)

        cadreListBox = Frame(cadreValeur)
        



        yDefilB = Scrollbar(cadreListBox, orient='vertical')
        yDefilB.grid(row=0, column=1, sticky='ns')

        self.listBoxValeurs = Listbox(cadreListBox, yscrollcommand=yDefilB.set, activestyle="none", selectmode="multiple" , height=10)
        self.listBoxValeurs.grid(row=0, column=0, sticky='nsew')
        yDefilB['command'] = self.listBoxValeurs.yview

        self.listBoxValeurs.bind('<<ListboxSelect>>', self.boutonValiderNormal)

        cadreListBox.grid(row=1, column=0, columnspan=2)


        self.boutonAttributPrecedent = Button(cadreValeur, text="Attribut\nPrécédent", command= lambda i=-1 : self.chargerAttributDapres(i))
        

        self.boutonAttributSuivant = Button(cadreValeur, text="Attribut\nSuivant", command= lambda i=1 : self.chargerAttributDapres(i))


        self.boutonAttributSuivant.grid(row=2, column=1)


        self.boutonValider = Button(cadreValeur, text="Valider", state="disabled", command= self.validation)
        self.boutonValider.grid(row=3, column=0, columnspan=2)


        self.chargerAttributDapres(0)

        self.boutonValiderNormal(None)


    # l'utilisateur a cliqué sur précédent ou suivant : on enregistre ce qu'il a entré
    def changementAttribut(self):

        


        #on sélectionne l'attribut en cours de filling
        attributEnCours = self.__class__.generateur.all_attributs[self.indiceAttributEnCours]
        
        #on configure pour que tout corresponde à l'attribut en cours
        self.labelNomAttribut.config(text = attributEnCours.nom)

        self.listBoxValeurs.delete(0,"end")

        if attributEnCours.choix_multiple:
            self.listBoxValeurs.config(selectmode="multiple")
        else:
            self.listBoxValeurs.config(selectmode="single")


        for valeur in attributEnCours.domaine_valeur:
            self.listBoxValeurs.insert("end", valeur)

            #on sélectionne les attributs déjà sélectionnées avant
            if valeur in self.dictionnaireAttrVal[attributEnCours.nom]:
                self.listBoxValeurs.selection_set(self.listBoxValeurs.size()-1)
        
        



    def chargerAttributDapres(self, unOuMoinsUn):
        self.ajoutAttrPerso(unOuMoinsUn)
        self.indiceAttributEnCours += unOuMoinsUn
        self.changementAttribut()



        if self.indiceAttributEnCours == len(self.generateur.all_attributs)-1:
            self.boutonAttributSuivant.grid_forget()
        
        elif self.indiceAttributEnCours == len(self.generateur.all_attributs)-2:
            self.boutonAttributSuivant.grid(row=2, column=1)



        if self.indiceAttributEnCours == 1:
            self.boutonAttributPrecedent.grid(row=2, column=0)

        elif self.indiceAttributEnCours == 0:
            self.boutonAttributPrecedent.grid_forget()
        

    
    #ajoute ce que l'utilisateur a sélectionné dans un dictionnaire plus tard
    def ajoutAttrPerso(self, unOuMoinsUn):

        #si unOuMoinsUn vaut 0 ça veut dire qu'on "réouvre" le personnage
        if unOuMoinsUn != 0:
            attributEnCours = self.__class__.generateur.all_attributs[self.indiceAttributEnCours]


            #on supprime la ligne sinon ça garde ce qui avait avant et ça peut etre problematique
            self.dictionnaireAttrVal[attributEnCours.nom] = set()
            #on ajoute au dictionnaire les valeurs sélectionnées pour cet attribut là
            for i in self.listBoxValeurs.curselection():
                self.dictionnaireAttrVal[attributEnCours.nom].add(self.listBoxValeurs.get(i))

           
        
        


    def boutonValiderNormal(self, event):
        

        if self.listBoxValeurs.curselection() == ():
            self.boutonValider.config(state="disabled")

        #c'est le "dernier" set que je suis en train de remplir
        elif list(self.dictionnaireAttrVal.values()).count(set()) == 1 and self.dictionnaireAttrVal[self.labelNomAttribut["text"]] == set():
            self.boutonValider.config(state="normal")
        elif set() in self.dictionnaireAttrVal.values():
            self.boutonValider.config(state="disabled")
        else:
            self.boutonValider.config(state="normal")

        

    def validation(self):
        
        self.ajoutAttrPerso(1)

        #ajout de toutes les valeurs au perso
        for nomAttr, valeurs in self.dictionnaireAttrVal.items():
            self.perso.ajouter(nomAttr, valeurs)

        
        self.cadreImagePersoGen.dessinerFiltreVert()

        self.destroy()
        
        








# test = FenetreDefPerso(["Attribut1","Attributs2"])
# test.mainloop()