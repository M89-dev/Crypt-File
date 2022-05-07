from tkinter import *

from setuptools import Command
import background as bk
import pygame as py

app = Tk()
app.title("H-TEC")
app.geometry("407x314")


def open_1():
    #bk.run()
    pass

# récupérer l'image dans une variable
pic =PhotoImage(file="C:\\Users\\berry\\OneDrive\\Documents\\NSI\\Crypt-File\\template\\lock2.png")
# affiche l'image
a_pic = Label(app, image=pic,).grid(row=0, column=1)
# Titre
H_Tec = Label(app, text="H-TEC", font=("Arial", 30)).grid(row=1, column=1)

# bouton pour page cryptage 
bt_c = Button(app, text="CRYPTAGE", font=("Arial",12), command=open_1).grid(row=3, column=0)

# bouton pour page gestionnaire de mdp
bt_mdp = Button(app, text="GÉRER MDP", font=("Arial",12), command=open_1).grid(row=3, column=1)

# bouton page décryptage 
bt_decryp = Button(app, text="DÉCRYPTAGE", font=("Arial",12), command=open_1).grid(row=3, column=2)

# bouton page profil 
bt_pt = Button(app, text="PROFIL", font=("Arial",12), command=open_1).grid(row=4, column=1)



app.mainloop()

