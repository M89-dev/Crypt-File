from importlib.resources import path
from tkinter import *
   
from tkinter import filedialog



def find_fichier():
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    path = filename
    

def affichage_cryptage():
    cryp = Tk()
    cryp.title("CRYPTAGE")
    cryp.geometry("450x450")

    label_file_explorer = Label(cryp,  text = "File Explorer using Tkinter", width = 100, height = 4,  fg = "blue").pack()

    extraire_fichier = Button(cryp, text="SÉLECTIONNER FICHIER", command=find_fichier).pack()

    label_file_explorer.conf



    mainloop()


affichage_cryptage()