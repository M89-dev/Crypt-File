from tkinter import *
import tkinter

gui = Tk()
gui.geometry("500x200")

Label(gui, text="Firstname").grid(row=0, column=2)
Label(gui, text="Lastname").grid(row=1, column=3)

e1 = Entry(gui)
e2 = Entry(gui)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

gui.mainloop()