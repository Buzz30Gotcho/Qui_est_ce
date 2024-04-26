# Nous avons pris cette classe sur le site : 
# https://www.linuxtut.com/en/3ea14ffd7f17d8214961/
# Elle nous permet de crééer des cadres avec des barres de défilement intégrées
# (ce qui n'est pas présent de base dans tkinter)
import tkinter as tk
from tkinter.ttk import *



class ScrollableFrame(tk.Frame):
    def __init__(self, container, bar_x = True, bar_y = True):
        super().__init__(container)
        self.canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind( "<Configure>", lambda e: self.canvas.configure( scrollregion=self.canvas.bbox("all") ) )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        if bar_y:
            self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.scrollbar_y.pack(side=tk.RIGHT, fill="y")
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
            self.scrollbar_x.pack(side=tk.BOTTOM, fill="x")
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.pack(side=tk.LEFT, fill="both", expand=True)
