from tkinter import Frame, Entry, Button
from tkinter.ttk import *



class ZoneDeTexte(Frame):

    fenetreAddAttribut = None
    

    def __init__(self, parent):

        Frame.__init__(self, parent)

        test = Style()
        test.configure("W.TButton", foreground="red", width=1)



        self.entry = Entry(self)
        boutonSuppr = Button(self,  text="x", command=self.appelSuppression, style = "W.TButton")

        self.entry.grid(row=0, column=0)
        boutonSuppr.grid(padx=10, row=0, column=1)


    def get(self):
        return self.entry.get()
    
    def appelSuppression(self):
        self.__class__.fenetreAddAttribut.supprimerAttr(self)
