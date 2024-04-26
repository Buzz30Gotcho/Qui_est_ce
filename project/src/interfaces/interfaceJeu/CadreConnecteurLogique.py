from tkinter import OptionMenu, StringVar, Menu
from tkinter.ttk import *

from project.src.interfaces.interfaceJeu.CadreQuestion import CadreQuestion
from project.src.interfaces.interfaceJeu.CadrePhrase import CadrePhrase
from project.src.interfaces.interfaceJeu.CadreAvantChoixQuestion import CadreAvantChoixQuestion

from project.src.jeu.And import And
from project.src.jeu.Or import Or
from project.src.jeu.Not import Not



class CadreConnecteurLogique(CadreQuestion):
    # vu que ça hérite de cadrequestion, peut être faudrait redéfinir des choses genre la hauteur ou quoi


    def __init__(self, parentFenetre, typeQuestion):

        
        #Cadre Qui contiendra une question, qui peut etre une phrase, un connecteur logique, on sait pas trop
        CadreQuestion.__init__(self, parentFenetre)
        

        self.boutonConnecteurLogique = Menubutton(self, width=4, text=typeQuestion)
        

        menuConnecteurLogique = Menu(self.boutonConnecteurLogique)
        for texte in self.__class__.listeQuestionsPossibles[1:4]:
            menuConnecteurLogique.add_command(label=texte, command=lambda string=texte : self.onchange_CL(string))

        self.boutonConnecteurLogique["menu"] = menuConnecteurLogique



        self.boutonConnecteurLogique.config(width=3)
        self.boutonConnecteurLogique.pack(side="left")

        self.boutonConnecteurLogique.bind("<Button-3>", self.pourSuppCL)

        #y a forcément une question pour un connecteur logique
        self.premiereQuestion = CadreAvantChoixQuestion(self)
        self.premiereQuestion.pack(side="top", anchor="w")
        self.deuxiemeQuestion = None

        #si le connecteur logique est OR ou AND on rajoute un cadre
        if typeQuestion != "NOT":
            self.deuxiemeQuestion = CadreAvantChoixQuestion(self)
            self.deuxiemeQuestion.pack(side="bottom", anchor="w")

        
        





    def onchange_CL(self, texteCL):
        self.boutonConnecteurLogique["text"]=texteCL
        if texteCL == "NOT" and self.deuxiemeQuestion != None: #on était sur un or ou un and et on check un "not"
            self.deuxiemeQuestion.destroy()
            self.deuxiemeQuestion = None
        
        elif texteCL != "NOT" and self.deuxiemeQuestion == None: #l'inverse (obligé de mettre un elif prck on peut passer d'un OR à un AND par exemple)
            self.deuxiemeQuestion = CadreAvantChoixQuestion(self)
            self.deuxiemeQuestion.pack(side="bottom", anchor="w")



    def creerQuestion(self, typeQuestion, cadreQuiVaSeDetruire):

        if (self.premiereQuestion == cadreQuiVaSeDetruire):
            self.premiereQuestion = self.typeQuestionAEnvoyer(typeQuestion)
            self.premiereQuestion.pack(side="top", anchor="w")
        else:
            self.deuxiemeQuestion = self.typeQuestionAEnvoyer(typeQuestion)
            self.deuxiemeQuestion.pack(side="bottom", anchor="w")
        cadreQuiVaSeDetruire.destroy()

            

    def typeQuestionAEnvoyer(self, typeQuestion):

        objetQuestion = None

        if(typeQuestion == "Phrase"):
            objetQuestion = CadrePhrase(self)

        else: #c'est un connecteurLogique
            objetQuestion = CadreConnecteurLogique(self, typeQuestion)

        return objetQuestion



    def supprimer_question(self, questionAsupprimer): #on supprimer la question qui a appelé cette methode
        if (self.premiereQuestion == questionAsupprimer):
            self.premiereQuestion = CadreAvantChoixQuestion(self)
            self.premiereQuestion.pack(side="top", anchor="w")
        else:
            self.deuxiemeQuestion = CadreAvantChoixQuestion(self)
            self.deuxiemeQuestion.pack(side="bottom", anchor="w")

        questionAsupprimer.destroy()
    

    def pourSuppCL(self, event): 
        menu = Menu(self, tearoff=0)
        menu.add_command(label= "supprimer", command= self.seSupprimer)

        try: 
            menu.tk_popup(event.x_root, event.y_root) 
        finally: 
            menu.grab_release()
    
    
    def seSupprimer(self):
        self.master.supprimer_question(self) #je suis obligé prck le menu peut pas prendre des arguments




    def transformationEnQuestion(self):
        typeQuestion = self.boutonConnecteurLogique["text"]
        questionARetourne = None

        if typeQuestion == "NOT":
            questionARetourne = Not()
            questionARetourne.add_question(self.premiereQuestion.transformationEnQuestion())
        elif typeQuestion == "OR":
            questionARetourne = Or()
            questionARetourne.add_question(self.premiereQuestion.transformationEnQuestion())
            questionARetourne.add_question(self.deuxiemeQuestion.transformationEnQuestion())
        else:
            questionARetourne = And()
            questionARetourne.add_question(self.premiereQuestion.transformationEnQuestion())
            questionARetourne.add_question(self.deuxiemeQuestion.transformationEnQuestion())

        return questionARetourne
