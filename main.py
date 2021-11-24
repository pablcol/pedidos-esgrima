import os
from tkinter import *
from tkinter import Tk
from tkinter import ttk

# Initialize tkinter, give it a page name and a max size
root = Tk()
root.title("Pedidos Material Esgrima")
root.geometry("1000x600")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="CEApng.ico")
else:
    root.wm_iconbitmap(bitmap="@CEApng.xbm")

# Define main frames of the app, one for sizes, one for equipment, one for summary, one for gloves
nombreFrame = LabelFrame(root, text="Nombre tirador/a: ", padx=5, pady=5)
medidasFrame = LabelFrame(root, text="Medidas tirador/a: ", padx=5, pady=5)
equipacionFrame = LabelFrame(root, text="Selección equipación: ", padx=5, pady=5)
summaryFrame = LabelFrame(root, text="Resumen pedido: ", padx=5, pady=5)
lateralidadFrame = LabelFrame(root, text="Lateralidad: ", padx=5, pady=5)
guantesFrame = LabelFrame(root, text="Talla guante: ", padx=5, pady=5)


# These functions are used for calculating the sizes, with distinction between female and male genders
def medidasfemenino(altura, pecho):
    tallalabel = Label(medidasFrame, text="Talla:                  ")
    tallalabel.grid(row=5, column=0, sticky=W)
    if 158 <= altura <= 164 and 82 <= pecho <= 86:
        talla = 36
    elif 158 <= altura <= 164 and 87 <= pecho <= 90:
        talla = 38
    elif 165 <= altura <= 170 and 91 <= pecho <= 94:
        talla = 40
    elif 165 <= altura <= 170 and 95 <= pecho <= 98:
        talla = 42
    elif 171 <= altura <= 176 and 99 <= pecho <= 102:
        talla = 44
    elif 171 <= altura <= 176 and 103 <= pecho <= 106:
        talla = 46
    elif 177 <= altura <= 182 and 107 <= pecho <= 110:
        talla = 46
    else:
        talla = "Especial"
    tallalabel = Label(medidasFrame, text="Talla: " + str(talla))
    tallalabel.grid(row=5, column=0, sticky=W)
    return


def medidasmasculino(altura, pecho):
    tallalabel = Label(medidasFrame, text="Talla:                  ")
    tallalabel.grid(row=5, column=0, sticky=W)
    if 164 <= altura <= 170 and 82 <= pecho <= 88:
        talla = 44
    elif 164 <= altura <= 170 and 89 <= pecho <= 92:
        talla = 46
    elif 171 <= altura <= 176 and 93 <= pecho <= 96:
        talla = 48
    elif 171 <= altura <= 176 and 97 <= pecho <= 100:
        talla = 50
    elif 177 <= altura <= 182 and 101 <= pecho <= 104:
        talla = 52
    elif 177 <= altura <= 182 and 105 <= pecho <= 108:
        talla = 54
    elif 183 <= altura <= 188 and 109 <= pecho <= 112:
        talla = 56
    elif 183 <= altura <= 188 and 113 <= pecho <= 116:
        talla = 58
    elif 183 <= altura <= 188 and 117 <= pecho <= 120:
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


# These functions are used to automatically check and/or uncheck the equipment
def equipcompleta(sexo):
    caretacheck.select()
    guantecheck.select()
    chaquetillacheck.select()
    espadacheck.select()
    pasantecheck.select()
    if sexo == "fem":
        protectorcheck.select()
    else:
        protectorcheck.deselect()
    return


def limpiarequip():
    caretacheck.deselect()
    guantecheck.deselect()
    chaquetillacheck.deselect()
    espadacheck.deselect()
    pasantecheck.deselect()
    protectorcheck.deselect()
    return


# This function checks the state of the checkbox and outputs a summary text
def summary(careta, guante, chaquetilla, espada, pasante, protector, diestro, zurdo, tallagua):
    if careta:
        caretaLabel.grid(row=1, column=0, sticky=W)
    if guante and diestro:
        guanteLabel.grid(row=2, column=0, sticky=W)
        diestro1Label.grid(row=2, column=2, sticky=W)
        guantetallaLabel['text'] = tallagua
        guantetallaLabel.grid(row=2, column=1, sticky=W)
    elif guante and zurdo:
        guanteLabel.grid(row=2, column=0, sticky=W)
        zurdo1Label.grid(row=2, column=2, sticky=W)
        guantetallaLabel['text'] = tallagua
        guantetallaLabel.grid(row=2, column=1, sticky=W)
    if chaquetilla and diestro:
        chaquetillaLabel.grid(row=3, column=0, sticky=W)
        diestro2Label.grid(row=3, column=2, sticky=W)
    elif chaquetilla and zurdo:
        chaquetillaLabel.grid(row=3, column=0, sticky=W)
        zurdo2Label.grid(row=3, column=2, sticky=W)
    if espada and diestro:
        espadaLabel.grid(row=4, column=0, sticky=W)
        diestro3Label.grid(row=4, column=2, sticky=W)
    elif espada and zurdo:
        espadaLabel.grid(row=4, column=0, sticky=W)
        zurdo3Label.grid(row=4, column=2, sticky=W)
    if pasante:
        pasanteLabel.grid(row=5, column=0, sticky=W)
    if protector:
        protectorLabel.grid(row=6, column=0, sticky=W)


# This function deletes the summary list
def limpiarresumen():
    caretaLabel.grid_forget()
    guanteLabel.grid_forget()
    chaquetillaLabel.grid_forget()
    espadaLabel.grid_forget()
    pasanteLabel.grid_forget()
    protectorLabel.grid_forget()
    diestro1Label.grid_forget()
    diestro2Label.grid_forget()
    diestro3Label.grid_forget()
    zurdo1Label.grid_forget()
    zurdo2Label.grid_forget()
    zurdo3Label.grid_forget()
    guantetallaLabel.grid_forget()
    return


# Create entry for name
nombreLabel = Label(nombreFrame, text="Nombre: ")
nombreEntry = Entry(nombreFrame, width=30)
apellidosLabel = Label(nombreFrame, text="Apellidos: ")
apellidosEntry = Entry(nombreFrame, width=30)

# Create checkboxes for laterality
diestrovar = BooleanVar()
diestrocheck = Checkbutton(lateralidadFrame, text="Diestro", variable=diestrovar)
zurdovar = BooleanVar()
zurdocheck = Checkbutton(lateralidadFrame, text="Zurdo", variable=zurdovar)

# Create drop down menu for glove sizes
listaGuantes = ["Seleccionar talla",
                "6",
                "6.5",
                "7",
                "7.5",
                "8",
                "8.5",
                "9",
                "9.5",
                "10"]
tallaguante = StringVar()
comboGloves = ttk.Combobox(guantesFrame, textvariable=tallaguante, values=listaGuantes)
comboGloves.current(0)
comboGloves['state'] = 'readonly'

# Create checkboxes for equipment
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

# Create labels for mesurements
alturaLabel = Label(medidasFrame, text="Altura en cm:")
pechoLabel = Label(medidasFrame, text="Tamaño pecho en cm:")
cinturaLabel = Label(medidasFrame, text="Tamaño cintura en cm:")
caderaLabel = Label(medidasFrame, text="Tamaño cadera en cm:")

# Create labels for summary
summaryEquipLabel = Label(summaryFrame, text="Equipación |")
summaryTallaLabel = Label(summaryFrame, text="Talla |")
summaryLateLabel = Label(summaryFrame, text="Lateralidad")
caretaLabel = Label(summaryFrame, text="Careta")
guanteLabel = Label(summaryFrame, text="Guante")
chaquetillaLabel = Label(summaryFrame, text="Chaquetilla")
espadaLabel = Label(summaryFrame, text="Espada")
pasanteLabel = Label(summaryFrame, text="Pasante")
protectorLabel = Label(summaryFrame, text="Protector")
diestro1Label = Label(summaryFrame, text="Diestro")
diestro2Label = Label(summaryFrame, text="Diestro")
diestro3Label = Label(summaryFrame, text="Diestro")
zurdo1Label = Label(summaryFrame, text="Zurdo")
zurdo2Label = Label(summaryFrame, text="Zurdo")
zurdo3Label = Label(summaryFrame, text="Zurdo")
guantetallaLabel = Label(summaryFrame, text=" ")

# Define entries for the sizes, in cm
alturaEntry = Entry(medidasFrame, width=15)
pechoEntry = Entry(medidasFrame, width=15)
cinturaEntry = Entry(medidasFrame, width=15)
caderaEntry = Entry(medidasFrame, width=15)

# Define buttons
buttonCalcularMasc = Button(medidasFrame, text="Calcular talla masculina", width=20, command=lambda: medidasmasculino(
                                                                                            int(alturaEntry.get()),
                                                                                            int(pechoEntry.get()),
                                                                                            # int(cinturaEntry.get()),
                                                                                            # int(caderaEntry.get())
                                                                                            ))
buttonCalcularFem = Button(medidasFrame, text="Calcular talla femenina", width=20, command=lambda: medidasfemenino(
                                                                                            int(alturaEntry.get()),
                                                                                            int(pechoEntry.get()),
                                                                                            # int(cinturaEntry.get()),
                                                                                            # int(caderaEntry.get())
                                                                                            ))
equipMButton = Button(equipacionFrame, text="Equipación completa Mas", width=20, command=lambda: equipcompleta("masc"))
equipFButton = Button(equipacionFrame, text="Equipación completa Fem", width=20, command=lambda: equipcompleta("fem"))
limpiarEquipButton = Button(equipacionFrame, text="Limpiar", width=20, command=limpiarequip)
resumenButton = Button(equipacionFrame, text="Resumen equipación", width=20, command=lambda: summary(
                                                                                            caretavar.get(),
                                                                                            guantevar.get(),
                                                                                            chaquetillavar.get(),
                                                                                            espadavar.get(),
                                                                                            pasantevar.get(),
                                                                                            protectorvar.get(),
                                                                                            diestrovar.get(),
                                                                                            zurdovar.get(),
                                                                                            comboGloves.get()
                                                                                            ))
limpiarResumenButton = Button(summaryFrame, text="Limpiar pedido", command=limpiarresumen)
cerrar = Button(root, text="Cerrar", width=15, command=root.quit)

# Put elements on app
# Frist the name bar
nombreLabel.grid(row=0, column=0, sticky=NW)
nombreEntry.grid(row=0, column=1, sticky=W)
apellidosLabel.grid(row=1, column=0, sticky=NW)
apellidosEntry.grid(row=1, column=1, sticky=W)

# then the checkboxes for laterality
diestrocheck.grid(row=0, column=0, sticky=W)
zurdocheck.grid(row=1, column=0, sticky=W)

# then the glove menu
comboGloves.grid(row=0, column=0, sticky=NW)

# then the sizes
alturaLabel.grid(row=1, column=0, sticky=W)
alturaEntry.grid(row=1, column=2)

pechoLabel.grid(row=2, column=0, sticky=W)
pechoEntry.grid(row=2, column=2)

cinturaLabel.grid(row=3, column=0, sticky=W)
cinturaEntry.grid(row=3, column=2)

caderaLabel.grid(row=4, column=0, sticky=W)
caderaEntry.grid(row=4, column=2)

buttonCalcularMasc.grid(row=5, column=2)
buttonCalcularFem.grid(row=6, column=2)

# then the equipment
equipMButton.grid(row=0, column=0)
equipFButton.grid(row=0, column=1)
limpiarEquipButton.grid(row=7, column=0)
resumenButton.grid(row=7, column=1)

# then the summary text and button
summaryEquipLabel.grid(row=0, column=0, sticky=W)
summaryTallaLabel.grid(row=0, column=1, sticky=W)
summaryLateLabel.grid(row=0, column=2, sticky=W)
limpiarResumenButton.grid(row=7, column=3)

# then the checkboxes for the equipment
caretacheck.grid(row=1, column=0, sticky=W)
guantecheck.grid(row=2, column=0, sticky=W)
chaquetillacheck.grid(row=3, column=0, sticky=W)
espadacheck.grid(row=4, column=0, sticky=W)
pasantecheck.grid(row=5, column=0, sticky=W)
protectorcheck.grid(row=6, column=0, sticky=W)

# then initialize and put the frames up
nombreFrame.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
lateralidadFrame.grid(row=0, column=1, sticky=NW, padx=10, pady=10)
medidasFrame.grid(row=1, column=0, sticky=NW, padx=10, pady=10)
guantesFrame.grid(row=1, column=1, sticky=NW, padx=10, pady=10)
equipacionFrame.grid(row=2, column=0, sticky=NW, padx=10, pady=10)
summaryFrame.grid(row=2, column=1, sticky=NW, padx=10, pady=10)
cerrar.grid(row=3, column=2, sticky=E)

# Initialize main loop and run app
root.mainloop()
