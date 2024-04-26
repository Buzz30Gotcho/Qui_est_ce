from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from project.src.interfaces.bibliotheque.ToplevelPopUp import ToplevelPopUp


class FenModifAttr(ToplevelPopUp):

    def __init__(self, parent, attribut):

        ToplevelPopUp.__init__(self, parent)
        self.minsize(None, 600)

        self.attribut = attribut

        self.labelNomAttribut = Label(self, text="Attribut : "+self.attribut.nom)
        self.labelNomAttribut.pack(pady=20)


        self.frameVisuValeurs = Frame(self)

        self.frameModifValeur = Frame(self)
        self.frameModifValeur.pack(fill="x")

        self.frameAjoutValeur = Frame(self)

        self.sceneVisuValeurs()







    def sceneVisuValeurs(self):
        

        # -------- on enleve la frame modifvaleur ------
        for widget in self.frameModifValeur.winfo_children():
            widget.destroy()

        for widget in self.frameAjoutValeur.winfo_children():
            widget.destroy()

        self.frameModifValeur.pack_forget()
        self.frameAjoutValeur.pack_forget()

        #--------------------------------------------

        labelValeurPossible = Label(self.frameVisuValeurs, text = "\nValeur Possibles\n")
        labelValeurPossible.grid(row=0, columnspan = 2, pady=20)

        for valeur in self.attribut.domaine_valeur:
            

            labelValeur = Label(self.frameVisuValeurs, text = valeur, cursor="hand2", font=('Arial', '18', 'bold underline'))

            labelValeur.bind("<Button-1>", self.menuContextuelModifSuppr)
            labelValeur.grid(columnspan=2, padx=10)

        boutonModifierNomAttr= Button(self.frameVisuValeurs, text="Modifier\nnom attribut", command= lambda : self.sceneModifValeur("", True))
        boutonModifierNomAttr.grid(row=len(self.attribut.domaine_valeur)+1, column=0,  pady=30, padx=30)
        
        boutonAjouterValeur= Button(self.frameVisuValeurs, text="Ajouter\nValeur", command= self.sceneAjoutValeur)
        boutonAjouterValeur.grid(row=len(self.attribut.domaine_valeur)+1, column=1,  pady=30, padx=30)
        
    

        boutonValiderQuitter = Button(self.frameVisuValeurs, text="OK", command=self.destroy )
        boutonValiderQuitter.grid(row=len(self.attribut.domaine_valeur)+2, column=0, columnspan=2,  pady=10)

        self.frameVisuValeurs.pack()

    

    def menuContextuelModifSuppr(self, event):
        chaineValeur = (event.widget)["text"]
        menu = Menu(self, tearoff=0)
        menu.add_command(label= "Modifier", command= lambda chaine = chaineValeur :  self.sceneModifValeur(chaine))
        menu.add_command(label= "Supprimer", command= lambda chaine = chaineValeur : self.suppressionValeur(chaine))

        try: 
            menu.tk_popup(event.x_root, event.y_root) 
        finally: 
            menu.grab_release()
    


    def sceneModifValeur(self, chaineValeur, modifNomAttr=False ):


        # -------- on enleve la frame visuValeur ------
        for widget in self.frameVisuValeurs.winfo_children():
            widget.destroy()

        self.frameVisuValeurs.pack_forget()

        #--------------------------------------------

        message = "Veuillez entrer un nouveau nom \npour la valeur : " + chaineValeur if not modifNomAttr else "Veuillez entrer le nouveau nom\nde l'attribut : "+self.attribut.nom
        labelNouvelleChaine = Label(self.frameModifValeur, text = message)

        labelNouvelleChaine.grid(row=0, column=0, columnspan=2, pady=20)

        self.entryNouvelleValeur = Entry(self.frameModifValeur, width=20)
        self.entryNouvelleValeur.grid(row=1, column=0, columnspan=2,pady=10)

        boutonAnnuler = Button(self.frameModifValeur, text="Annuler", command=self.sceneVisuValeurs)
        boutonAnnuler.grid(row=2, column=0, padx=20)

        if modifNomAttr:
            boutonOK = Button(self.frameModifValeur, text="OK", command=self.modificationNom)
        else:
            boutonOK = Button(self.frameModifValeur, text="OK", command= lambda chaineNewVal= chaineValeur : self.modificationValeur(chaineNewVal))

        boutonOK.grid(row=2, column=1, padx=20)
        self.frameModifValeur.pack(fill="x")




    def sceneAjoutValeur(self):

        # -------- on enleve la frame visuValeur ------
        for widget in self.frameVisuValeurs.winfo_children():
            widget.destroy()

        self.frameVisuValeurs.pack_forget()

        #--------------------------------------------

        labelNouvelleChaine = Label(self.frameAjoutValeur, text = "Veuillez entrer un nom\npour la nouvelle valeur")
        labelNouvelleChaine.grid(pady=20, row=0, column=0, columnspan=2)

        self.entryNouvelleValeur = Entry(self.frameAjoutValeur, width=20)
        self.entryNouvelleValeur.grid(row=1, column=0, columnspan=2, pady=10)

        boutonAnnuler = Button(self.frameAjoutValeur, text="Annuler", command=self.sceneVisuValeurs)
        boutonAnnuler.grid(row=2, column=0, padx=20)

        
        boutonOK = Button(self.frameAjoutValeur, text="OK", command=self.ajoutValeur)
        boutonOK.grid(row=2, column=1, padx=20)

        self.frameAjoutValeur.pack()


    def ajoutValeur(self):
        if self.nomValeurOK(self.entryNouvelleValeur.get()):
            self.attribut.add_valeur(self.entryNouvelleValeur.get())
            self.sceneVisuValeurs()




    def modificationValeur(self, ancienneValeur):

        nouveauNom = self.entryNouvelleValeur.get()

        if self.nomValeurOK(nouveauNom):
            self.__class__.generateur.modif_valeur(ancienneValeur, nouveauNom, self.attribut)
            self.sceneVisuValeurs()


    def modificationNom(self):

        nouveauNom = self.entryNouvelleValeur.get()
        if self.nomAttributOK(nouveauNom):
    
            self.__class__.generateur.modif_attribut(nouveauNom, self.attribut)
            self.sceneVisuValeurs()

            self.labelNomAttribut.config(text="Attribut : "+self.attribut.nom)
        

    
    def suppressionValeur(self, chaineValeur):
        
        # self.attributes("-disabled", True)
        self.grab_release()
        
        #la suppression de la valeur entrainera la suppression de l'attribut
        if len(self.attribut.domaine_valeur) == 2:
            if askquestion("Supprimer Valeur", "Supprimer cette valeur donnera un attribut à une valeur\nCette action supprimera définitevement l'attribut : "+self.attribut.nom+"\nContinuer? :" ) == "yes":
                self.__class__.generateur.supp_valeur(chaineValeur, self.attribut)
                self.__class__.fenetreGen.cocherPersoRendusIdentiques()
                self.destroy()

        else:

            if askquestion("Supprimer Valeur", "Supprimer une valeur peut amener à rendre des perso identiques.\n Voulez vous vraiment supprimer " + chaineValeur + "?") == "yes":
                #la méthode est pas prete mdr
                self.__class__.generateur.supp_valeur(chaineValeur, self.attribut)
                
                for widget in self.frameVisuValeurs.winfo_children():
                    if widget["text"] == chaineValeur:
                        widget.destroy()
                        break

            # self.attributes("-disabled", False)
            self.grab_set()
            self.lift()



    def nomAttributOK(self, nomAttr):
        self.grab_release()
        # self.attributes("-disabled", True)
        success = True

        
        if nomAttr == "":
            showinfo("Mauvais nom", "Veuillez entrer un nom svp")
            success = False
        else:
            try:
                self.__class__.generateur.verif_nom(nomAttr)
            except NameError:
                showinfo("Mauvais nom", "Ce nom d'attribut est déjà pris.\nVeuillez entrer un autre nom.")
                success = False

        # self.attributes("-disabled", False)
        self.grab_set()
        self.lift()

        return success



    def nomValeurOK(self, nomValeur):
        # self.attributes("-disabled", True)
        self.grab_release()
        success = True

        
        if nomValeur == "":
            showinfo("Mauvais nom", "Veuillez entrer un nom svp")
            success = False
        else:
            if nomValeur in self.attribut.domaine_valeur:
                success = False
                showinfo("Mauvais nom", "Cette valeur existe déjà.\nVeuillez entrer un autre nom")


        # self.attributes("-disabled", False)
        self.grab_set()
        self.lift()

        return success

        


    # showinfo("Mauvais nombre de ligne/colonne", message)

