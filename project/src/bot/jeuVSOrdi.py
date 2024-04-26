from project.src.jeu.Jeu import Jeu
from project.src.bot.bot import Bot
from random import random

class JeuVSOrdi(Jeu):
    def __init__(self, metadonnees=None, modeFacile=False):
        # super(metadonnees, modeFacile)
        Jeu.__init__(self, metadonnees, modeFacile)
        # assert self.planche, "attribut n'existe pas"
        self.ordi = None
        print(f"{self.ordi=}")
        
    def __str__(self):
        return super().__str__() + "BOT = " + self.ordi.__str__()
    
    def set_un_bot(self):
        self.ordi = Bot(self)
        
    def reset(self):
        #choix d'un nouveau personnage mystere pour tout le joueur
        Jeu.reset(self)
        
        #choix d'un nouveau personnage mystere pour tout le bot
        
        del self.ordi

        self.set_un_bot()
        self.ordi.personnage_mystere = self.planche[int(random()*len(self.planche))]
        
        
