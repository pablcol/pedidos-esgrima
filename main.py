from tkinter import *
from tkinter import Tk

# Initialize tkinter and give it a page name
root = Tk()
root.title("Pedidos Grant Esgrima")
# root.iconbitmap("CEApng.ico")

# Define frames
medidasFrame = LabelFrame(root, text="Medidas tirador/a:", padx=5, pady=5)
equipacionFrame = LabelFrame(root, text="Selección equipación:", padx=5, pady=5)


# Define functions
def medidasmasculino(altura, pecho, cintura, cadera):
    tallalabel = Label(medidasFrame, text="Talla:                  ")
    tallalabel.grid(row=5, column=0, sticky=W)
    if 164 <= altura <= 170: # and 82 <= pecho <= 88:
        talla = 44
    elif 164 <= altura <= 170: # and 89 <= pecho <= 92:
        talla = 46
    elif 171 <= altura <= 176: # and 93 <= pecho <= 96:
        talla = 48
    elif 171 <= altura <= 176: # and 97 <= pecho <= 100:
        talla = 50
    elif 177 <= altura <= 182: # and 101 <= pecho <= 104:
        talla = 52
    elif 177 <= altura <= 182: # and 105 <= pecho <= 108:
        talla = 54
    elif 183 <= altura <= 188: # and 109 <= pecho <= 112:
        talla = 56
    elif 183 <= altura <= 188: # and 113 <= pecho <= 116:
        talla = 58
    elif 183 <= altura <= 188: # and 117 <= pecho <= 120:
        talla = 60
    elif 189 <= altura <= 194 and 121 <= pecho <= 124:
        talla = 62
    elif 195 <= altura <= 200 and 125 <= pecho <= 128:
        talla = 64
    else: 
        talla = "Especial"
    tallalabel = Label(medidasFrame, text="Talla: " + str(talla))
    tallalabel.grid(row=5, column=0, sticky=W)
    return


def equipcompleta(sexo):
    caretacheck.select()
    guantecheck.select()
    chaquetillacheck.select()
    espadacheck.select()
    pasantecheck.select()
    if sexo == "fem":
        protectorcheck.select()
    return


def limpiarequip():
    caretacheck.deselect()
    guantecheck.deselect()
    chaquetillacheck.deselect()
    espadacheck.deselect()
    pasantecheck.deselect()
    protectorcheck.deselect()
    return


# Create checkboxes
caretavar = BooleanVar()
caretacheck = Checkbutton(equipacionFrame, text="Careta", variable=caretavar)
guantevar = BooleanVar()
guantecheck = Checkbutton(equipacionFrame, text="Guante", variable=guantevar)
chaquetillavar = BooleanVar()
chaquetillacheck = Checkbutton(equipacionFrame, text="Chaquetilla", variable=chaquetillavar)
espadavar = BooleanVar()
espadacheck = Checkbutton(equipacionFrame, text="Espada", variable=espadavar)
pasantevar = BooleanVar()
pasantecheck = Checkbutton(equipacionFrame, text="Pasante", variable=pasantevar)
protectorvar = BooleanVar()
protectorcheck = Checkbutton(equipacionFrame, text="Protector femenino", variable=protectorvar)


# Create label texts
alturaLabel = Label(medidasFrame, text="Altura en cm:")
pechoLabel = Label(medidasFrame, text="Tamaño pecho en cm:")
cinturaLabel = Label(medidasFrame, text="Tamaño cintura en cm:")
caderaLabel = Label(medidasFrame, text="Tamaño cadera en cm:")

caretacheck.grid(row=1, column=0, sticky=W)
guantecheck.grid(row=2, column=0, sticky=W)
chaquetillacheck.grid(row=3, column=0, sticky=W)
espadacheck.grid(row=4, column=0, sticky=W)
pasantecheck.grid(row=5, column=0, sticky=W)
protectorcheck.grid(row=6, column=0, sticky=W)

# Define entries
alturaEntry = Entry(medidasFrame, width=15)
pechoEntry = Entry(medidasFrame, width=15)
cinturaEntry = Entry(medidasFrame, width=15)
caderaEntry = Entry(medidasFrame, width=15)

# Define buttons
buttonCalcular = Button(medidasFrame, text="Calcular talla", command=lambda: medidasmasculino(int(alturaEntry.get()),
                                                                                              int(pechoEntry.get()),
                                                                                              int(cinturaEntry.get()),
                                                                                              int(caderaEntry.get())))
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

# Buttons
Button(root, text="Cerrar", command=root.quit).grid(row=3, column=3)

# Initialize main loop and app
root.mainloop()
