from tkinter import *
from tkinter import Tk

# Initialize tkinter and give it a page name
root = Tk()
root.title("Pedidos Grant Esgrima")
talla = 44

# Define frames
medidasFrame = LabelFrame(root, text="Medidas tirador/a:", padx=5, pady=5)
equipacionFrame = LabelFrame(root, text="Selección equipación:", padx=5, pady=5)


# Define functions
def medidas():
    talla = 1
    return talla


def equipcompleta(sexo):
    caretaLabel.grid(row=1, column=0)
    guanteLabel.grid(row=2, column=0)
    chaquetillaLabel.grid(row=3, column=0)
    espadalabel.grid(row=4, column=0)
    pasanteLabel.grid(row=5, column=0)
    if sexo == "fem":
        protectorLabel.grid(row=6, column=0)
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
alturaLabel = Label(medidasFrame, text="Altura en cm:")
pechoLabel = Label(medidasFrame, text="Tamaño pecho en cm:")
cinturaLabel = Label(medidasFrame, text="Tamaño cintura en cm:")
caderaLabel = Label(medidasFrame, text="Tamaño cadera en cm:")
tallaLabel = Label(medidasFrame, text="Talla: " + str(talla))

equipLabel = Label(equipacionFrame, text="Equipación completa")
caretaLabel = Label(equipacionFrame, text="Careta")
guanteLabel = Label(equipacionFrame, text="Guante")
chaquetillaLabel = Label(equipacionFrame, text="Chaquetilla")
espadalabel = Label(equipacionFrame, text="Espada")
pasanteLabel = Label(equipacionFrame, text="Pasante")
protectorLabel = Label(equipacionFrame, text="Protector femenino")

# Define entries
alturaEntry = Entry(medidasFrame, width=15)
pechoEntry = Entry(medidasFrame, width=15)
cinturaEntry = Entry(medidasFrame, width=15)
caderaEntry = Entry(medidasFrame, width=15)

# Define buttons
buttonCalcular = Button(medidasFrame, text="Calcular talla")

equipMButton = Button(equipacionFrame, text="Equipación completa Mas", command=lambda: equipcompleta("masc"))
equipFButton = Button(equipacionFrame, text="Equipación completa Fem", command=lambda: equipcompleta("fem"))
limpiarButton = Button(equipacionFrame, text="Limpiar", command=limpiar)

# Put elements on app

# Medidas
alturaLabel.grid(row=1, column=0, sticky=W)
alturaEntry.grid(row=1, column=2)

pechoLabel.grid(row=2, column=0, sticky=W)
pechoEntry.grid(row=2, column=2)

cinturaLabel.grid(row=3, column=0, sticky=W)
cinturaEntry.grid(row=3, column=2)

caderaLabel.grid(row=4, column=0, sticky=W)
caderaEntry.grid(row=4, column=2)

tallaLabel.grid(row=5, column=0, sticky=W)
buttonCalcular.grid(row=5, column=2)

# Equipaciones
equipMButton.grid(row=0, column=0)
equipFButton.grid(row=0, column=1)
limpiarButton.grid(row=7, column=0)

# Frames
medidasFrame.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
equipacionFrame.grid(row=0, column=1, sticky=W, padx=10, pady=10)

# Initialize main loop and app
root.mainloop()
