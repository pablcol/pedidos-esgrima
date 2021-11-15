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
def medidas(altura, pecho, cintura, cadera):
    tallaLabel = Label(medidasFrame, text="Talla:                  ")
    tallaLabel.grid(row=5, column=0, sticky=W)
    if 164 <= altura <= 170 and 82 <= pecho <= 88 and 70 <= cintura <= 74 and 88 <= cadera <= 92:
        talla = 44
    elif 164 <= altura <= 170 and 89 <= pecho <= 92 and 75 <= cintura <= 78 and 93 <= cadera <= 96:
        talla = 46
    elif 171 <= altura <= 176 and 93 <= pecho <= 96 and 79 <= cintura <= 82 and 97 <= cadera <= 100:
        talla = 48
    elif 171 <= altura <= 176 and 97 <= pecho <= 100 and 83 <= cintura <= 86 and 101 <= cadera <= 104:
        talla = 50
    elif 177 <= altura <= 182 and 101 <= pecho <= 104 and 87 <= cintura <= 90 and 105 <= cadera <= 108:
        talla = 52
    elif 177 <= altura <= 182 and 105 <= pecho <= 108 and 91 <= cintura <= 94 and 109 <= cadera <= 112:
        talla = 54
    elif 183 <= altura <= 188 and 109 <= pecho <= 112 and 95 <= cintura <= 98 and 113 <= cadera <= 116:
        talla = 56
    elif 183 <= altura <= 188 and 113 <= pecho <= 116 and 99 <= cintura <= 102 and 117 <= cadera <= 120:
        talla = 58
    elif 183 <= altura <= 188 and 117 <= pecho <= 120 and 103 <= cintura <= 106 and 121 <= cadera <= 124:
        talla = 60
    elif 189 <= altura <= 194 and 121 <= pecho <= 124 and 107 <= cintura <= 110 and 125 <= cadera <= 128:
        talla = 62
    elif 195 <= altura <= 200 and 125 <= pecho <= 128 and 111 <= cintura <= 114 and 129 <= cadera <= 132:
        talla = 64
    else: 
        talla = "Especial"
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
buttonCalcular = Button(medidasFrame, text="Calcular talla", command=lambda: medidas(int(alturaEntry.get()), int(pechoEntry.get()), int(cinturaEntry.get()), int(caderaEntry.get())))
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
