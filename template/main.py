from tkinter import *

from setuptools import Command
import pygame as py
from cryptage import *


app = Tk()
app.title("H-TEC")
app.geometry("407x314")


def open_cryp():
    affichage_cryptage()
    

# récupérer l'image dans une variable
pic =PhotoImage(file="C:\\Users\\Rémi\\Desktop\\Crypt-File\\template\\lock2.png")
# affiche l'image
a_pic = Label(app, image=pic,).grid(row=0, column=1)
# Titre
H_Tec = Label(app, text="H-TEC", font=("Arial", 30)).grid(row=1, column=1)

# bouton pour page cryptage 
bt_c = Button(app, text="CRYPTAGE", font=("Arial",12), command=affichage_cryptage).grid(row=3, column=0)

# bouton pour page gestionnaire de mdp
bt_mdp = Button(app, text="GÉRER MDP", font=("Arial",12), command=affichage_cryptage).grid(row=3, column=1)

# bouton page décryptage 
bt_decryp = Button(app, text="DÉCRYPTAGE", font=("Arial",12), command=open_cryp).grid(row=3, column=2)

# bouton page profil 
bt_pt = Button(app, text="PROFIL", font=("Arial",12), command=open_cryp).grid(row=4, column=1)



app.mainloop()

