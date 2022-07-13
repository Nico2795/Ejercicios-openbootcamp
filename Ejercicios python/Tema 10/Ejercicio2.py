import tkinter
from tkinter import *

lista= ["Hola", "Como estas", "Bien y tu"]

window=tkinter.Tk()

lista_items=tkinter.StringVar(value=lista)
listbox= tkinter.Listbox(window,listvariable=lista_items)
listbox.pack()

label = Label(text="Lista de saludos")
label.pack()

window.mainloop()

