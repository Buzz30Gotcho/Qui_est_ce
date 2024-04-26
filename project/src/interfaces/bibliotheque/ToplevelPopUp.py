from tkinter import Toplevel


class ToplevelPopUp(Toplevel):

    generateur = None
    fenetreGen = None

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
    

    
    def popupFenetre(self, fenetreQuiPop):

        # self.attributes("-disabled", True)
        fenetreQuiPop.grab_set()
        self.wait_window(fenetreQuiPop)
        del fenetreQuiPop
        # self.attributes("-disabled", False)
        self.lift()


    @classmethod
    def getAttributFromNom(cls, nom):
        for attribut in cls.generateur.all_attributs:
            if attribut.nom == nom:
                return attribut


        