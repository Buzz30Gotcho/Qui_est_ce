from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *



from project.src.interfaces.interfaceGenerateur.ZoneDeTexte import ZoneDeTexte
from project.src.interfaces.bibliotheque.ToplevelPopUp import ToplevelPopUp


class FenetreAddAttribut(ToplevelPopUp):

    

    def __init__(self, parent):
        ToplevelPopUp.__init__(self, parent)
        self.transient(parent)

        ZoneDeTexte.fenetreAddAttribut = self

        # Creation des frames   
        self.framePrincipale = Frame(self)
        self.frameListeValeur = Frame(self.framePrincipale)

        # Creation des labels
        labelNomAttribut = Label(self.framePrincipale,text="Entrez le nom de l'attribut :")
        labelChoixMultiple = Label(self.framePrincipale,text="Possibilité de choix multiple :")
        labelValeurAttribut = Label(self.framePrincipale,text="Entrez les valeurs possibles de votre attribut :")

        # Creation des entry --------- A MODIFIER
        self.entryNomAttribut = Entry(self.framePrincipale)
        self.listEntryValeur = [Entry(self.frameListeValeur), Entry(self.frameListeValeur)]



        # Creation des boutons et checkbox ---------- A MODIFIER 
        boutonValider = Button(self.framePrincipale, text="Valider", command=self.ajoutAttribut)
        boutonAjouter = Button(self.framePrincipale, text="Ajouter une valeur",command=self.add_entry)


        self.AttrMultiple = IntVar()
        checkBox = Checkbutton(self.framePrincipale, variable=self.AttrMultiple)

        # Packing des labels et des boutons
        labelNomAttribut.grid(row=0,column=0, pady=25)
        labelChoixMultiple.grid(row=1,column=0, pady=25)
        labelValeurAttribut.grid(row=2,column=0, pady=25)

        self.entryNomAttribut.grid(row=0,column=1, pady=25)
        checkBox.grid(row=1,column=1, pady=25)
        self.listEntryValeur[0].pack(pady=7, anchor="w")
        self.listEntryValeur[1].pack(pady=5, anchor="w")

        
        boutonAjouter.grid(row=2,column=1, pady=25)
        boutonValider.grid(row=4,columnspan=2, pady=15)

        self.frameListeValeur.grid(row=3,columnspan=2, pady=30)
        self.framePrincipale.pack()


        

    # ----------Methode d'ajout d'un entry dans listEntryValeurAttribut----------
    def add_entry(self):
        nouvelleEntry = ZoneDeTexte(self.frameListeValeur)
        self.listEntryValeur.append(nouvelleEntry)
        nouvelleEntry.pack(pady=5)


        
    # ---------------------------------------------------------------------------

    def supprimerAttr(self, objASuppr):
        objASuppr.destroy()
        del (self.listEntryValeur[self.listEntryValeur.index(objASuppr)])
        


    def ajoutAttribut(self):
        self.grab_release()
        # self.attributes("-disabled", True)

        success = True
        listeValeur=[]

        if self.entryNomAttribut.get() == "":
            success = False
            showinfo("Nom invalide", "Veuillez entrer un nom svp")

        


        else:
            try:
                self.__class__.generateur.verif_nom(self.entryNomAttribut.get())
            except NameError:
                success = False
                showinfo("Nom invalide", "ce nom correspond déjà à un autre attribut.\nVeuillez changer de nom")



        #pour l'instant ça passe
        if success:
            for entry in self.listEntryValeur:
                valeur = entry.get()


                if success:

                    if valeur in listeValeur:
                        showinfo("Noms Valeurs invalides", "deux valeurs ont le même nom.\nVeuillez à ce que toutes les valeurs ont des noms différents")
                        success = False
                    if success:
                        if valeur == "":
                            showinfo("Noms Valeurs invalides", "Veuillez compléter tous les champs svp")
                            success = False
            
                        listeValeur.append(valeur)

        if success:
            multiple = False if self.AttrMultiple.get() == 0 else True
            
            self.__class__.generateur.creer_nouvelle_attribut(self.entryNomAttribut.get(), multiple)

            for valeur in listeValeur:
                self.__class__.generateur.all_attributs[-1].add_valeur(valeur)
            
            
            self.destroy()


        else:
            self.grab_set()
            self.lift()
            


# root = Tk()
# test = FenetreAddAttribut(root)

# root.mainloop()

