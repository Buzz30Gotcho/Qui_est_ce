import tkinter.font
from tkinter import *
from tkinter.ttk import *

import socket
import sys
import os #pour le nom des fichiers de sauvegarde

from project.src.interfaces.interfaceJeu.ScrollableFrame import ScrollableFrame


class ChoixModeJeu(Tk)  :  #L'argument passé dans les parenthèses indique que notre classe interface hérite de la classe tk.Tk. Par ce mécanisme, nous héritons ainsi de toutes les méthodes et attributs de cette classe mère
    def __init__(self):     # constructeur de la fenetre principale

        Tk.__init__(self)



        #si on ferme la fenetre avant je veux pas que ça lance le jeu

        self.protocol("WM_DELETE_WINDOW", exit)

        self.style = Style(self)
        self.style.configure('TButton', padding=3)


        self.defaultFont = tkinter.font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Helvetica",
                                   size=19)

        # self.style.configure('TEntry', font=("Courrier", 25))

        self.title("Configuration Partie")
        self.minsize(700,500)
        
        self.menubar= Menu(self)
        self.menubar.add_command(label="Quitter", command=exit)

        self.config(menu=self.menubar)
        


        #spécialement pour le bouton "retour"
        self.liste_appels_foncions = [] 

        self.pseudoJoueur = ""
        self.modeFacile = False
        self.fichierJson = ""
        self.anciennePartie = False
        self.modeJeu = "JeuDeBase"
        self.adresseIP = ""
        self.heberger = False
        

        self.cadreContainer = Frame(self) #c'est le cadre qui contiendra TOUT
        self.cadreContainer.pack()


        self.demande_pseudo_joueur()


    def a_chaque_methode(self, methode_utilisee):
        # chaque fois qu'on change de scene faut memoriser la scene qui se detruit, faut suprrimer tous les widgets.. hmmm c'est bon

        self.liste_appels_foncions.append(methode_utilisee) #on ajoute à la liste la methode qui a appelée "a_chaque_methode"

        for widget in self.cadreContainer.winfo_children():
            widget.destroy()




    def demande_pseudo_joueur(self): # on demande le pseudo au joueur
        
        self.a_chaque_methode(self.demande_pseudo_joueur)




        labelBienvenue = Label(self.cadreContainer, text="Bienvenue sur le Jeu\nQui-Est-Ce?", font=("Courrier", 40 )) #faudra changer la taille hein
        labelBienvenue.grid(row=0, column=0, columnspan=2, pady=50)

        labelEntrezPseudo = Label(self.cadreContainer, text="Entrez votre pseudo", font=("Courrier", 15))
        labelEntrezPseudo.grid(row=1, column=0, columnspan=2, pady=15)


        self.strVarPseudo = StringVar() #je suis obligé...

        champSaisi = Entry(self.cadreContainer, textvariable=self.strVarPseudo)
        champSaisi.grid(row=2, column=0, padx=10)

        boutonValiderPseudo = self.creerBouton(self.cadreContainer, "OK", self.choixModeDeJeu)
        boutonValiderPseudo.grid(row=2, column=1, padx=20)


    def choixModeDeJeu(self):

        self.pseudoJoueur = self.strVarPseudo.get()   # on recup le pseudo entré

        if len(self.liste_appels_foncions) == 1:
            self.menubar.add_command(label="Retour", command=self.retour)

        self.a_chaque_methode(self.choixModeDeJeu)

        labelModeJeu = Label(self.cadreContainer, text = "Sélectionnez un mode de jeu")
        labelModeJeu.pack(pady=40)

        boutonJeuDeBase = Button(self.cadreContainer, text="Jeu de Base J1", command=lambda string="JeuDeBase" : self.setChoixModeJeu(string))
        boutonJeuDeBase.pack(pady=20)

        boutonReseau = Button(self.cadreContainer, text="Réseau", command=lambda string="Reseau" : self.setChoixModeJeu(string))
        boutonReseau.pack(pady=20)

        boutonBot = Button(self.cadreContainer, text="Contre le Bot", command=lambda string="Bot" : self.setChoixModeJeu(string))
        boutonBot.pack(pady=20)

        

    def setChoixModeJeu(self, chaineModeJeu):
        self.modeJeu = chaineModeJeu

        if chaineModeJeu == "Reseau":
            self.demandeServeurClient()
        else:
            self.choixPlateauJeu()
       



    def sauvegardeExiste(self): #faut tester si y a un fichier de sauvegarde à son nom (je le ferai)
        

        

        if os.path.exists('ressources/sauvegarde/jeu/' + self.pseudoJoueur + ".pickle"):
            self.chargerAnciennePartie()
        else:
            self.destroy()
             


    def chargerAnciennePartie(self): # on affiche un texte qui demande si on veut charger une ancienne partie ou en démarrer une nouvelle
        self.a_chaque_methode(self.chargerAnciennePartie)


        label_charger_partie = Label(self.cadreContainer, text="Il semblerait que vous n'ayez pas terminé une partie.\nVoulez vous la charger ou en relancer une nouvelle?"  ) 
        label_charger_partie.grid(row=0, column=0, columnspan=2, pady=40)

        boutonReprendre = self.creerBouton(self.cadreContainer, "Reprendre", self.chargerPartie) # bouton ReprendreNouvellePartie
        boutonReprendre.grid(row=1, column=0, pady=40, padx=30)

        boutonNouvellePartie = self.creerBouton(self.cadreContainer, "Nouvelle Partie", self.destroy ) # bouton NouvellePartie ,je pense ici que command=ChoixModeFacile
        boutonNouvellePartie.grid(row=1, column=1, pady=40, padx=30)




    def choixPlateauJeu(self): #on regarde quels plateaux de jeu sont disponibles dans /jeu/, et on les affiche sous forme de bouton
        self.a_chaque_methode(self.choixPlateauJeu)

        
        petitCadre = Frame(self.cadreContainer)
        petitCadre.pack()
        cadreScrollable = ScrollableFrame(petitCadre, False)
        cadreScrollable.pack(side="bottom")
        


        label_plateau=Label(petitCadre, text="Sur quel plateau voulez vous jouez?\n\n", font=("Courrier",20) ) 
        label_plateau.pack(side="top", pady=20)

        listePlateaux = []

        for strCheminFichier in os.listdir("ressources/JSON/"):
            if strCheminFichier.endswith(".json"):
                
                self.creerBouton(cadreScrollable.scrollable_frame,    strCheminFichier  , lambda variableJeSuppose=strCheminFichier : self.set_fichierJson( variableJeSuppose )  ).grid(padx=130, pady=20)


    def set_fichierJson(self, strCheminFichier): #on a cliqué sur un bouton qui désigne le fichier json
        self.fichierJson = strCheminFichier
        

        if self.modeJeu == "JeuDeBase":
            self.demandeChoixModeFacile()

        elif self.modeJeu == "Reseau":
            self.attendreConnexion()
            
        elif self.modeJeu == "Bot":
            self.sauvegardeExiste()
            
        else:
            print("probleme là")
            exit()



    def demandeServeurClient(self):
        self.a_chaque_methode(self.demandeServeurClient)

        labelServeur = Label(self.cadreContainer, text="Voulez-vous héberger la partie?\n(Vous devrez attendre qu'une personne se connecte)")
        labelServeur.pack(pady=30)

        boutonHebergerPartie = Button(self.cadreContainer, text="Héberger\nla partie", command=lambda oui=True : self.setHebergement(oui))
        boutonHebergerPartie.pack(pady=15)

        boutonSeConnecter = Button(self.cadreContainer, text="Rejoindre\nune partie", command=lambda non=False : self.setHebergement(non))
        boutonSeConnecter.pack(pady=15)


    def setHebergement(self, heberge):
        self.heberger = heberge
        if heberge:
            self.choixPlateauJeu()
        else:
            self.renseignerAdresseIp()




    def attendreConnexion(self):

        self.a_chaque_methode(self.attendreConnexion)

        

        labelAdresseIp = Label(self.cadreContainer, text="L'autre joueur devra se connecter à l'adresse IP :\n" + socket.gethostbyname(socket.gethostname()))
        labelAdresseIp.pack(pady=20)

        labelAttenteConnexion = Label(self.cadreContainer, text= "Fermez cette fenêtre pour démarrer le serveur", font=("Courier", 12))
        labelAttenteConnexion.pack(pady=30)

        self.protocol("WM_DELETE_WINDOW", self.destroy)





    def renseignerAdresseIp(self):
        self.a_chaque_methode(self.renseignerAdresseIp)

        labelRenseignerAdresseIP = Label(self.cadreContainer, text="Veuillez renseigner l'adresse IP\n de la machine hébergeant la partie")
        labelRenseignerAdresseIP.grid(row=0, column=0, columnspan=2, pady=20)

        self.entryAdresseIP = Entry(self.cadreContainer)
        self.entryAdresseIP.grid(row=1, column = 0, padx=15, pady=20)

        boutonValiderIP = Button(self.cadreContainer, text="Se connecter", command=self.getAdresseIP)
        boutonValiderIP.grid(row=1, column=1, padx=15, pady=20)

    def getAdresseIP(self):
        print(self.entryAdresseIP.get())
        self.adresseIP = self.entryAdresseIP.get()
        self.destroy()






    def demandeChoixModeFacile(self): #affiche 2 boutons "mode facile" et "mode normal" qui definissent
        self.a_chaque_methode(self.demandeChoixModeFacile)

        label_ModedeJeu=Label(self.cadreContainer, text="Choisissez votre Mode de Jeu", font=("Courrier", 20)   ) # affiche " QUELS MODES DE JEUX ?"
        label_ModedeJeu.grid(row=0, column=0, columnspan=2, pady=30)

        boutonModeFacile = self.creerBouton(self.cadreContainer, "Mode Facile", lambda: self.setChoixModeFacile(True) ) 
        boutonModeFacile.grid(row=1, column=0, pady=20, padx=30)

        boutonModeNormal= self.creerBouton(self.cadreContainer, "Mode Normal", lambda: self.setChoixModeFacile(False)) 
        boutonModeNormal.grid(row=1, column=1, pady=20, padx=30)

    def setChoixModeFacile(self, choixModeFacile):
        self.modeFacile = choixModeFacile

        self.sauvegardeExiste()




    def retour(self):

        del(self.liste_appels_foncions[-1]) #on supprime la derniere méthode prck c'est celle en cours
                                    
        if len(self.liste_appels_foncions) == 1: #on est dans la méthode "pseudo joueur" (au tout debut, y a pas de bouton retour)
            self.menubar.delete(2) #on supprime le menuButton "Retour"

        self.liste_appels_foncions[-1]() #on appelle l'avant derniere méthode qu'on a utilisée
        del(self.liste_appels_foncions[-1]) #vu qu'on a appelé la méthode à la ligne d'avant, ça a recré un élément dans liste qui sert à rien




    def chargerPartie(self):
        self.anciennePartie = True
        self.destroy()



    def creerBouton(self, container, nom, command):
        return Button(container, text=nom, command=command)
    
    


