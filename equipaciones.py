from tkinter import *

# Initialize tkinter and give it a page name
root = Tk()
root.title("Pedidos Grant Esgrima: Equipaciones")

# Define functions
def equipCompletaM():
    caretaLabel.grid(row=1, column=0)
    guanteLabel.grid(row=2, column=0)
    chaquetillaLabel.grid(row=3, column=0)
    espadalabel.grid(row=4, column=0)
    pasanteLabel.grid(row=5, column=0)
    return

def equipCompletaF():
    caretaLabel.grid(row=1, column=1)
    guanteLabel.grid(row=2, column=1)
    chaquetillaLabel.grid(row=3, column=1)
    espadalabel.grid(row=4, column=1)
    pasanteLabel.grid(row=5, column=1)
    protectorLabel.grid(row=6, column=1)
    return

def limpiar():
    caretaLabel.grid_remove()
    guanteLabel.grid_remove()
    chaquetillaLabel.grid_remove()
    espadalabel.grid_remove()
    pasanteLabel.grid_remove()
    protectorLabel.grid_remove()
    return

# Create label texts
equipLabel = Label(root, text="Equipación completa")
caretaLabel = Label(root, text="Careta")
guanteLabel = Label(root, text="Guante")
chaquetillaLabel = Label(root, text="Chaquetilla")
espadalabel = Label(root, text="Espada")
pasanteLabel = Label(root, text="Pasante")
protectorLabel = Label(root, text="Protector femenino")

# Define entries

# Define buttons
equipMButton = Button(root, text="Equipación completa Mas", command=equipCompletaM)
equipFButton = Button(root, text="Equipación completa Fem", command=equipCompletaF)
limpiarButton = Button(root, text="Limpiar", command=limpiar)

# Put elements on app
equipMButton.grid(row=0, column=0)
equipFButton.grid(row=0, column=1)
limpiarButton.grid(row=7, column=0, columnspan=2)

# Initialize main loop and app
root.mainloop()
