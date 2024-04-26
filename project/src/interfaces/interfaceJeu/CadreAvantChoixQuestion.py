from tkinter import Frame, OptionMenu, StringVar, Menu
from tkinter.ttk import *



class CadreAvantChoixQuestion(Frame):
    


    listeQuestionsPossibles=["Phrase","OR", "AND", "NOT"]

    #il me faut même la liste des attributs et des valeurs (je la recupererait de metadonnees)

    def __init__(self, parentFenetre):

        

        #Cadre Qui contiendra une question, qui peut etre une phrase, un connecteur logique, on sait pas trop
        Frame.__init__(self, parentFenetre)

        self.style = Style(self)
        self.style.configure('TOptionMenu', font=('Helvetica', 15))
        
        self.boutonTypeQuestion = Menubutton(self, width=7, text="Type Q°")
        

        menuTypeQuestion = Menu(self.boutonTypeQuestion)
        for texte in self.__class__.listeQuestionsPossibles:
            menuTypeQuestion.add_command(label=texte, command=lambda string=texte : self.onchange_TQ(string))

        self.boutonTypeQuestion["menu"] = menuTypeQuestion

        self.boutonTypeQuestion.config(width=3)
        self.boutonTypeQuestion.pack(side="left")
        # c'est la liste déroulante qui va vérifier si la question sera une phrase ou un connecteur logique
        
        
        
        

    def onchange_TQ(self, texte): #je crois que "jsp" c'est une valeur envoyée par option menu au changement
        
        self.master.creerQuestion(texte, self)





    