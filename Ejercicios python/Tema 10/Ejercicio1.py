import tkinter
from tkinter import ttk
from tkinter import *


window= tkinter.Tk()
label1 = Label(window)
label1.pack()
window.columnconfigure(0 , weight=3)



def seleccionar():
    label1.config(text="{}".format(selected.get()))

def reset():
    print("Clear")
    label1.config(text="")
    selected.set(None)





boton = tkinter.Button(window, text="Reset", command=reset)
boton.pack(side="bottom")

selected= tkinter.StringVar(None)
R1=ttk.Radiobutton(window, text="Volver al futuro", value ="Volver al futuro", variable=selected, command=seleccionar).pack(anchor=W)
R2=ttk.Radiobutton(window, text="Batman", value ="Batman", variable=selected, command=seleccionar).pack(anchor=W)
R3=ttk.Radiobutton(window, text="Cloud Atlas", value ="Cloud Atlas", variable=selected, command=seleccionar).pack(anchor=W)


window.mainloop()
