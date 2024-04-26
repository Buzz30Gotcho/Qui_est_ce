from tkinter import * 
from tkinter.ttk import *

import os
import signal
import threading


class fenetre(Tk):
    def __init__(self, objetTony, nom_fenetre):

        Tk.__init__(self)

        self.objet = objetTony

        self.style = Style(self)
        self.style.configure('TButton', font=('Helvetica', 16))
        self.style.configure('TEntry', font=('Helvetica', 16))
        self.style.configure('TLabel', font=('Helvetica', 16))
        self.title(nom_fenetre)


        self.labelState = Label(self, text = "state = (pas encore implémenter mdr)")
        self.labelState.grid(row=0, column=0 ,columnspan = 2,pady=30)

        self.entryJsp = Entry(self, width = 50)
        self.entryJsp.grid(row=1, column=0, pady=30, padx=30)



        self.boutonEnvoyer = Button(self, text="Envoyer", command=self.envoyerMsg)
        self.boutonEnvoyer.grid(row=1, column=1, pady=30, padx=30)


        
        
    def launch(self):
        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()
        
        self.mainloop()
            
        # le mec ferme la fenetre
        print("The system> Envoie du  signal pour terminer la discussion")
        self.objet.envoyer_message("Goodbye!")
        
            
    def receive(self):
        msg = "foo"
        while True:
            try: 
                msg = self.objet.recevoir_message()
                print(f"The other guy said> {msg}.")
                    
                if msg == "Goodbye!":
                    print(f"The system> Veuillez fermer la fenêtre.")
                    
                    self.objet.envoyer_message("Goodbye!") # signal pour que l'autre s'arrête correctement
                     
                    break # fin du thread
            except:
                print("arret de la reception message")
                self.objet.co.close()
                break # fin du thread
                


    def envoyerMsg(self):
        print(f"You say> {self.entryJsp.get()}")
        self.objet.envoyer_message(self.entryJsp.get())

# test = fenetre(None)


