from tkinter import *
from tkinter import ttk

# Initialize tkinter and give it a page name
root = Tk()
root.title("")

listavalores = ['1', '2', '3']

combo = ttk.Combobox(root, values=listavalores).grid(row=1, column=1)
print(combo)

root.mainloop()
