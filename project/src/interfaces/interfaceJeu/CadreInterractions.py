from project.src.interfaces.interfaceJeu.CadreQuestion import CadreQuestion
from project.src.interfaces.interfaceJeu.CadrePhrase import CadrePhrase
from project.src.interfaces.interfaceJeu.CadreAvantChoixQuestion import CadreAvantChoixQuestion
from project.src.interfaces.interfaceJeu.CadreConnecteurLogique import CadreConnecteurLogique


from tkinter import Frame, Button, Label
from tkinter.messagebox import *
from tkinter.ttk import *


class CadreInterractions(Frame):



    #ces attributs de classes seront modifiés dans la classe InterfaceJeu
    largeurCadre = 0
    
    
 
    def __init__(self, parentFenetre, jeu, fenetreJeu):

        


        #Ce sera le cadre principal, qui contiendra : le texte "choisissez une question", le bouton valider
        #et les questions
        Frame.__init__(self, parentFenetre, height=100, width=self.__class__.largeurCadre )

        self.fenetreJeu = fenetreJeu

        # le cadre qui contiendra les questions
        self.questionFinale = None


        self.jeu = jeu
        


        dico = self.jeu.calcule_MapAttibutsDomaine()
    


        CadrePhrase.dicoAttrVal = dico


        self.petitCadre = Frame(self)
        

        self.boutonQuestionComplexe = Button(self.petitCadre, text="Question Complexe", command=self.supprimer_question)

        #bouton qui servira à tester combien de personnes seront cochées SI jamais on validait la question
        self.boutonTester = None

        #Bouton qui permettra de valider la question correctement entrée
        self.boutonValider= Button(self.petitCadre, text="Valider", command=self.envoyerQuestion )

        
        
        
        self.creerQuestion("Phrase")

        self.boutonQuestionComplexe.pack(side="left")

        self.boutonValider.pack(side="right", padx=15)

        if  self.jeu.modeFacile:
            self.boutonTester = Button(self.petitCadre, text="Tester", command=self.testerQuestion)
            self.boutonTester.pack(side="right", padx=25)

        self.petitCadre.grid(row=1, pady=5, sticky="we")





    def supprimer_question(self, questionAsupprimer=None): #on supprimer la question qui a appelé cette methode
        
        
        self.questionFinale.destroy() # c'est implicitement la question qui a appelé cette fonction
        self.questionFinale = CadreAvantChoixQuestion(self)
        self.questionFinale.grid(row=0, pady=5, sticky="w")



    def creerQuestion(self, typeQuestion, cadreQuiVaSeDetruire=None):

        self.questionFinale = self.typeQuestionAEnvoyer(typeQuestion)
        self.questionFinale.grid(row=0, pady=5, sticky="w")
        if cadreQuiVaSeDetruire != None:
            cadreQuiVaSeDetruire.destroy()

            

    def typeQuestionAEnvoyer(self, typeQuestion):

        objetQuestion = None

        if(typeQuestion == "Phrase"):
            objetQuestion = CadrePhrase(self)

        else: #c'est un connecteurLogique
            objetQuestion = CadreConnecteurLogique(self, typeQuestion)

        return objetQuestion



    

    
    def envoyerQuestion(self): #clic sur bouton valider
        question = self.questionCorrecte()
        if question != None:
            reponse = (self.jeu.joueur).poser_question(question) #la réponse qu'on reçoit

            showinfo("réponse à la question", "la réponse à cette Question est : " + str(reponse))


            if self.jeu.modeFacile: #ça coche automatiquement si on est en mode facile
                self.fenetreJeu.cadreToutesLesPhotos.cocher(self.jeu.get_perso_invalide(question))
            


    def testerQuestion(self): #clic sur bouton tester

        if (question := self.questionCorrecte()) != None:
            listePersosDejaCoches = self.fenetreJeu.cadreToutesLesPhotos.get_liste_persos_coches()
            
            
            liste_personne_eliminee = self.jeu.get_perso_invalide(question)

            persosQuiSerontElimines = [x for x in liste_personne_eliminee if x not in listePersosDejaCoches]
            showinfo("Question ", "Cette Question éliminera "+ str(len(persosQuiSerontElimines)) +" personnages")
            
        
           

    #teste si la question est "bien formée" (s'il manque pas des valeurs à rentrer ou quoi)
    def questionCorrecte(self):
        question = None
        try:
            question = self.questionFinale.transformationEnQuestion() #c'est la question qui est envoyé de l'interface
            
        except Exception:
            showinfo("Question mal formée", "Votre question n'est pas bien formée")
            
                
        return question
        

        

