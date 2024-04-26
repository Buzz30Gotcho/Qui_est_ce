from tkinter import Frame, Button, OptionMenu, StringVar
from tkinter.ttk import *

class CadreQuestion(Frame):
    


    listeQuestionsPossibles=["Phrase","OR", "AND", "NOT"]
  

    def __init__(self, parentFenetre):

        
        #tous nos cadres questions seront bien des frames, donc autant le faire là
        Frame.__init__(self, parentFenetre, borderwidth=2, relief="groove" )

        
    

        
        


    