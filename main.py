from tkinter import *
from tkinter import Tk

# Initialize tkinter and give it a page name
root = Tk()
root.title("Pedidos Grant Esgrima")
# root.iconbitmap("CEApng.ico")
talla = 0

# Define frames
medidasFrame = LabelFrame(root, text="Medidas tirador/a:", padx=5, pady=5)
equipacionFrame = LabelFrame(root, text="Selección equipación:", padx=5, pady=5)


# Define functions
def medidas(pecho, altura):
    if 82 <= pecho <= 86 and 164 <= altura <= 170:
        talla = 44
    else:
        talla = 0
    tallaLabel = Label(medidasFrame, text="Talla: " + str(talla))
    tallaLabel.grid(row=5, column=0, sticky=W)
    return    


def equipcompleta(sexo):
    caretaLabel.grid(row=1, column=0, sticky=W)
    guanteLabel.grid(row=2, column=0, sticky=W)
    chaquetillaLabel.grid(row=3, column=0, sticky=W)
    espadalabel.grid(row=4, column=0, sticky=W)
    pasanteLabel.grid(row=5, column=0, sticky=W)
    if sexo == "fem":
        protectorLabel.grid(row=6, column=0, sticky=W)
    return


def limpiarequip():
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
buttonCalcular = Button(medidasFrame, text="Calcular talla", command=lambda: medidas(int(pechoEntry.get()), int(alturaEntry.get())))
equipMButton = Button(equipacionFrame, text="Equipación completa Mas", command=lambda: equipcompleta("masc"))
equipFButton = Button(equipacionFrame, text="Equipación completa Fem", command=lambda: equipcompleta("fem"))
limpiarEquipButton = Button(equipacionFrame, text="Limpiar", command=limpiarequip)

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

# tallaLabel.grid(row=5, column=0, sticky=W)
buttonCalcular.grid(row=5, column=2)

# Equipaciones
equipMButton.grid(row=0, column=0)
equipFButton.grid(row=0, column=1)
limpiarEquipButton.grid(row=7, column=0)

# Frames
medidasFrame.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
equipacionFrame.grid(row=0, column=1, sticky=W, padx=10, pady=10)

# Initialize main loop and app
root.mainloop()
