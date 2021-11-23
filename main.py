from tkinter import *
from tkinter import Tk
from tkinter import ttk

# Initialize tkinter and give it a page name
root = Tk()
root.title("Pedidos Grant Esgrima")
# root.iconbitmap("CEApng.ico")

# Define main frames of the app, one for sizes, one for equipment, one for summary, one for gloves
medidasFrame = LabelFrame(root, text="Medidas tirador/a:", padx=5, pady=5)
equipacionFrame = LabelFrame(root, text="Selección equipación:", padx=5, pady=5)
summaryFrame = LabelFrame(root, text="Resumen pedido:", padx=5, pady=5)
guantesFrame = LabelFrame(root, text="Guantes:", padx=5, pady=5)


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
def summary(careta, guante, chaquetilla, espada, pasante, protector):
    if careta:
        caretaLabel.grid(row=1, column=0, sticky=W)
    if guante:
        guanteLabel.grid(row=2, column=0, sticky=W)
    if chaquetilla:
        chaquetillaLabel.grid(row=3, column=0, sticky=W)
    if espada:
        espadaLabel.grid(row=4, column=0, sticky=W)
    if pasante:
        pasanteLabel.grid(row=5, column=0, sticky=W)
    if protector:
        protectorLabel.grid(row=6, column=0, sticky=W)
    return


# This function outputs the laterality of the equipment
def lateralidad(late):
    latelabel1 = " "
    latelabel2 = " "
    latelabel3 = " "
    if late == "zurdo":
        latelabel1 = Label(summaryFrame, text="Zurdo")
        latelabel2 = Label(summaryFrame, text="Zurdo")
        latelabel3 = Label(summaryFrame, text="Zurdo")
    elif late == 'diestro':
        latelabel1 = Label(summaryFrame, text="Diestro")
        latelabel2 = Label(summaryFrame, text="Diestro")
        latelabel3 = Label(summaryFrame, text="Diestro")
    latelabel1.grid(row=2, column=2)
    latelabel2.grid(row=3, column=2)
    latelabel3.grid(row=4, column=2)
    return


# This function deletes the summary list
def limpiarresumen():
    caretaLabel.grid_forget()
    guanteLabel.grid_forget()
    chaquetillaLabel.grid_forget()
    espadaLabel.grid_forget()
    pasanteLabel.grid_forget()
    protectorLabel.grid_forget()
    return


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
summaryEquipLabel = Label(summaryFrame, text="Equipación | ")
summaryTallaLabel = Label(summaryFrame, text="Talla | ")
summaryLateLabel = Label(summaryFrame, text="Lateralidad")
caretaLabel = Label(summaryFrame, text="Careta")
guanteLabel = Label(summaryFrame, text="Guante")
chaquetillaLabel = Label(summaryFrame, text="Chaquetilla")
espadaLabel = Label(summaryFrame, text="Espada")
pasanteLabel = Label(summaryFrame, text="Pasante")
protectorLabel = Label(summaryFrame, text="Protector")

caretacheck.grid(row=1, column=0, sticky=W)
guantecheck.grid(row=2, column=0, sticky=W)
chaquetillacheck.grid(row=3, column=0, sticky=W)
espadacheck.grid(row=4, column=0, sticky=W)
pasantecheck.grid(row=5, column=0, sticky=W)
protectorcheck.grid(row=6, column=0, sticky=W)

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
                                                                                            protectorvar.get()
                                                                                            ))
limpiarResumenButton = Button(root, text="Limpiar pedido", command=limpiarresumen)
lateButton = Button(root, text="Lateralidad", command=lambda: lateralidad("zurdo"))
cerrar = Button(root, text="Cerrar", width=15, command=root.quit)

# Put elements on app
# first the sizes
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

# then the summary text
summaryEquipLabel.grid(row=0, column=0)
summaryTallaLabel.grid(row=0, column=1)
summaryLateLabel.grid(row=0, column=2)

# then initialize and put the frames up
medidasFrame.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
equipacionFrame.grid(row=0, column=1, sticky=W, padx=10, pady=10)
summaryFrame.grid(row=1, column=0, sticky=W, padx=10, pady=10)
lateButton.grid(row=1, column=3)
limpiarResumenButton.grid(row=3, column=1)
cerrar.grid(row=3, column=2, sticky=E)

# Initialize main loop and run app
root.mainloop()
