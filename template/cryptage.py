from importlib.resources import path
from tkinter import filedialog

# importing everything from tkinter
from tkinter import *
 
# creating the tkinter window
cryp = Tk()
cryp.title("CRYPTAGE")
cryp.geometry("450x450")
 

def affichage_cryptage():
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
     
    # configure
    label_file_explorer.config(text = "Hello")
 
label_file_explorer = Label(cryp,  text = "File Explorer using Tkinter", width = 100, height = 4,  fg = "blue")

extraire_fichier = Button(cryp, text="SÉLECTIONNER FICHIER", command = affichage_cryptage)
 
label_file_explorer.pack()
extraire_fichier.pack()
 
# Start the GUI
cryp.mainloop()