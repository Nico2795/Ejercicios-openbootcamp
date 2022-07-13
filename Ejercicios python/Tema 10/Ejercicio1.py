
import tkinter
from tkinter import Label, Variable, Widget, ttk
from tkinter import * 


window= tkinter.Tk()
window.columnconfigure(0 , weight=3)

def reset(event):
    print("adios")
    selected.set(None)
  

boton = tkinter.Button(window, text="Reset")
boton.grid(column=0, row=4 , sticky=tkinter.S)
boton.bind("<Button-1>",reset)



selected= tkinter.StringVar()
R1=ttk.Radiobutton(window, text="si", value ="1", variable=selected, )
R2=ttk.Radiobutton(window, text="no", value ="2", variable=selected)
R3=ttk.Radiobutton(window, text="quiza", value ="3", variable=selected,)


R1.grid(column=0, row=1, pady=5, padx=5)
R2.grid(column=0, row=2, pady=5, padx=5)
R3.grid(column=0, row=3, pady=5, padx=5)



window.mainloop()
