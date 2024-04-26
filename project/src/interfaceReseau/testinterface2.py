from tkinter import * 
from tkinter.ttk import *

import os
import signal


class fenetre(Tk):
    def __init__(self, objetTony):

        Tk.__init__(self)

        self.objet = objetTony

        self.style = Style(self)
        self.style.configure('TButton', font=('Helvetica', 16))
        self.style.configure('TEntry', font=('Helvetica', 16))
        self.style.configure('TLabel', font=('Helvetica', 16))
        self.title("host")


        self.labelState = Label(self, text = "state = (pas encore implémenter mdr)")
        self.labelState.grid(row=0, column=0 ,columnspan = 2,pady=30)

        self.entryJsp = Entry(self, width = 50)
        self.entryJsp.grid(row=1, column=0, pady=30, padx=30)



        self.boutonEnvoyer = Button(self, text="Envoyer", command=self.envoyerMsg)
        self.boutonEnvoyer.grid(row=1, column=1, pady=30, padx=30)

        pid = os.fork()
        
        if pid: #parent
            print("Je suis le parent", pid)
            self.mainloop()
            
            print(f"killing {pid}")
            os.kill(pid, signal.SIGKILL)
            # self.objet.envoyer_message("déconecté, fermez la fenêtre")
        else: #child
            print("Je suis l'enfant", pid)
            
            msg = "foo"
            while msg != "fin" or msg != "":
                msg = self.objet.recevoir_message()
                print(f">{msg}.")
            # self.objet.envoyer_message("fin")
            # self.destroy()
        


    def envoyerMsg(self):
        self.objet.envoyer_message(self.entryJsp.get())
        # print(f"{self.objet.recevoir_message()=}")

# test = fenetre(None)


