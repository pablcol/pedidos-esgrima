# import os
from tkinter import *
from tkinter import Tk
from tkinter import ttk


def main():

    # Initialize tkinter, give it a page name and a max size
    root = Tk()
    root.title("Pedidos Material Esgrima")
    root.geometry("800x620")
    '''img = PhotoImage(file='CEApng.xbm')
    root.tk.call('wm', 'iconphoto', root._w, img)
    if os.name == "nt":
        root.wm_iconbitmap(bitmap="CEApng.ico")
    else:
        root.wm_iconbitmap(bitmap="@CEApng.xbm")'''

    # Define main frames of the app, one for sizes, one for equipment, one for summary, one for gloves
    nombreframe = LabelFrame(root, text="Nombre tirador/a: ", padx=5, pady=5)
    medidasframe = LabelFrame(root, text="Medidas tirador/a: ", padx=5, pady=5)
    equipacionframe = LabelFrame(root, text="Selección equipación: ", padx=5, pady=5)
    summaryframe = LabelFrame(root, text="Resumen pedido: ", padx=5, pady=5)
    lateralidadframe = LabelFrame(root, text="Lateralidad: ", padx=5, pady=5)
    guantesframe = LabelFrame(root, text="Talla guante: ", padx=5, pady=5)

    # These functions are used for calculating the sizes, with distinction between female and male genders
    def medidasfemenino(altura, pecho):
        tl = Label(medidasframe, text="Talla:                  ")
        tl.grid(row=5, column=0, sticky=W)
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
        tl = Label(medidasframe, text="Talla: " + str(talla))
        tl.grid(row=5, column=0, sticky=W)
        return talla

    def medidasmasculino(altura, pecho):
        tl = Label(medidasframe, text="Talla:                  ")
        tl.grid(row=5, column=0, sticky=W)
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
        tl = Label(medidasframe, text="Talla: " + str(talla))
        tl.grid(row=5, column=0, sticky=W)
        return talla

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
    def summary(careta, guante, chaquetilla, espada, pasante, protector, diestro, zurdo, tallagua, tallacha):
        if careta:
            caretalabel.grid(row=2, column=0, sticky=W)
        if guante and diestro:
            if tallagua != "Seleccionar talla":
                guantelabel.grid(row=3, column=0, sticky=W)
                diestro1label.grid(row=3, column=2, sticky=W)
                guantetallalabel['text'] = tallagua
                guantetallalabel.grid(row=3, column=1, sticky=W)
        elif guante and zurdo:
            if tallagua != "Seleccionar talla":
                guantelabel.grid(row=3, column=0, sticky=W)
                zurdo1label.grid(row=3, column=2, sticky=W)
                guantetallalabel['text'] = tallagua
                guantetallalabel.grid(row=3, column=1, sticky=W)
        if chaquetilla and diestro:
            chaquetillalabel.grid(row=4, column=0, sticky=W)
            chaquetillatallalabel['text'] = tallacha
            chaquetillatallalabel.grid(row=4, column=1, sticky=W)
            diestro2label.grid(row=4, column=2, sticky=W)
        elif chaquetilla and zurdo:
            chaquetillalabel.grid(row=4, column=0, sticky=W)
            zurdo2label.grid(row=4, column=2, sticky=W)
        if espada and diestro:
            espadalabel.grid(row=5, column=0, sticky=W)
            diestro3label.grid(row=5, column=2, sticky=W)
        elif espada and zurdo:
            espadalabel.grid(row=5, column=0, sticky=W)
            combogloves.grid(row=5, column=2, sticky=W)
        if pasante:
            pasantelabel.grid(row=6, column=0, sticky=W)
        if protector:
            protectorlabel.grid(row=7, column=0, sticky=W)
        return

    # This function deletes the summary list
    def limpiarresumen():
        caretalabel.grid_forget()
        guantelabel.grid_forget()
        chaquetillalabel.grid_forget()
        espadalabel.grid_forget()
        pasantelabel.grid_forget()
        protectorlabel.grid_forget()
        diestro1label.grid_forget()
        diestro2label.grid_forget()
        diestro3label.grid_forget()
        zurdo1label.grid_forget()
        zurdo2label.grid_forget()
        combogloves.grid_forget()
        guantetallalabel.grid_forget()
        chaquetillatallalabel.grid_forget()
        return

    # This function copies the summary to the clipboard
    def copiarresumen(nombre, apellido, careta, guante, chaquetilla, espada, pasante, protector,
                      diestro, zurdo, tallagua, tallacha):
        summaryframe.clipboard_clear()
        output = " "
        if nombre:
            output += ("Nombre: " + nombre)
        if apellido:
            output += ("\nApellidos: " + apellido)
        if careta:
            output += "\nCareta"
        if guante and diestro:
            if tallagua != "Seleccionar talla":
                output += ("\nGuante diestro talla " + str(tallagua))
        if guante and zurdo:
            if tallagua != "Seleccionar talla":
                output += ("\nGuante zurdo talla " + str(tallagua))
        if chaquetilla and diestro:
            output += ("\nChaquetilla diestro talla " + tallacha)
        if chaquetilla and zurdo:
            output += ("\nChaquetilla zurdo talla " + tallacha)
        if espada and diestro:
            output += "\nEspada diestro"
        if espada and zurdo:
            output += "\nEspada zurdo"
        if pasante:
            output += "\nPasante"
        if protector:
            output += "\nProtector"
        summaryframe.clipboard_append(output)
        summaryframe.update()
        return

    # Create entry for name
    nombrelabel = Label(nombreframe, text="Nombre: ")
    nombreentry = Entry(nombreframe, width=30)
    apellidoslabel = Label(nombreframe, text="Apellidos: ")
    apellidosentry = Entry(nombreframe, width=30)

    # Create checkboxes for laterality
    diestrovar = BooleanVar()
    diestrocheck = Checkbutton(lateralidadframe, text="Diestro", variable=diestrovar)
    zurdovar = BooleanVar()
    zurdocheck = Checkbutton(lateralidadframe, text="Zurdo", variable=zurdovar)

    # Create drop down menu for glove sizes
    listaguantes = ["Seleccionar talla",
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
    combogloves = ttk.Combobox(guantesframe, textvariable=tallaguante, values=listaguantes)
    combogloves.current(0)
    combogloves['state'] = 'readonly'

    # Create checkboxes for equipment
    caretavar = BooleanVar()
    caretacheck = Checkbutton(equipacionframe, text="Careta", variable=caretavar)
    guantevar = BooleanVar()
    guantecheck = Checkbutton(equipacionframe, text="Guante", variable=guantevar)
    chaquetillavar = BooleanVar()
    chaquetillacheck = Checkbutton(equipacionframe, text="Chaquetilla", variable=chaquetillavar)
    espadavar = BooleanVar()
    espadacheck = Checkbutton(equipacionframe, text="Espada", variable=espadavar)
    pasantevar = BooleanVar()
    pasantecheck = Checkbutton(equipacionframe, text="Pasante", variable=pasantevar)
    protectorvar = BooleanVar()
    protectorcheck = Checkbutton(equipacionframe, text="Protector femenino", variable=protectorvar)

    # Create labels for mesurements
    alturalabel = Label(medidasframe, text="Altura en cm:")
    pecholabel = Label(medidasframe, text="Tamaño pecho en cm:")
    cinturalabel = Label(medidasframe, text="Tamaño cintura en cm:")
    caderalabel = Label(medidasframe, text="Tamaño cadera en cm:")

    # Create labels for summary
    summaryequiplabel = Label(summaryframe, text="Equipación |")
    summarytallalabel = Label(summaryframe, text="Talla |")
    summarylatelabel = Label(summaryframe, text="Lateralidad")
    caretalabel = Label(summaryframe, text="Careta")
    guantelabel = Label(summaryframe, text="Guante")
    chaquetillalabel = Label(summaryframe, text="Chaquetilla")
    espadalabel = Label(summaryframe, text="Espada")
    pasantelabel = Label(summaryframe, text="Pasante")
    protectorlabel = Label(summaryframe, text="Protector")
    diestro1label = Label(summaryframe, text="Diestro")
    diestro2label = Label(summaryframe, text="Diestro")
    diestro3label = Label(summaryframe, text="Diestro")
    zurdo1label = Label(summaryframe, text="Zurdo")
    zurdo2label = Label(summaryframe, text="Zurdo")
    combogloves = Label(summaryframe, text="Zurdo")
    guantetallalabel = Label(summaryframe, text=" ")
    chaquetillatallalabel = Label(summaryframe, text=" ")

    # Define entries for the sizes, in cm
    alturaentry = Entry(medidasframe, width=15)
    pechoentry = Entry(medidasframe, width=15)
    cinturaentry = Entry(medidasframe, width=15)
    caderaentry = Entry(medidasframe, width=15)

    # Create entries for size
    tallalabel = Label(summaryframe, text="Introduce talla: ")
    tallaentry = Entry(summaryframe, width=5)

    # Define buttons
    buttoncalcularmasc = Button(medidasframe, text="Calcular talla masculina",
                                width=20, command=lambda: medidasmasculino(
                                                          int(alturaentry.get()),
                                                          int(pechoentry.get()),
                                                          ))
    buttoncalcularfem = Button(medidasframe, text="Calcular talla femenina", width=20, command=lambda: medidasfemenino(
                                                                                                int(alturaentry.get()),
                                                                                                int(pechoentry.get()),
                                                                                                ))
    equipmbutton = Button(equipacionframe, text="Equipación completa Mas", width=20, command=lambda: equipcompleta(
                                                                                                     "masc"))
    equipfbutton = Button(equipacionframe, text="Equipación completa Fem", width=20, command=lambda: equipcompleta(
                                                                                                     "fem"))
    limpiarequipbutton = Button(equipacionframe, text="Limpiar", width=20, command=limpiarequip)
    resumenbutton = Button(equipacionframe, text="Resumen equipación", width=20, command=lambda: summary(
                                                                                                 caretavar.get(),
                                                                                                 guantevar.get(),
                                                                                                 chaquetillavar.get(),
                                                                                                 espadavar.get(),
                                                                                                 pasantevar.get(),
                                                                                                 protectorvar.get(),
                                                                                                 diestrovar.get(),
                                                                                                 zurdovar.get(),
                                                                                                 combogloves.get(),
                                                                                                 tallaentry.get()
                                                                                                ))
    limpiarresumenbutton = Button(summaryframe, text="Limpiar pedido", width=16, command=limpiarresumen)
    copiarresumenbutton = Button(summaryframe, text="Copiar a portapapeles", width=16, command=lambda: copiarresumen(
                                                                                                nombreentry.get(),
                                                                                                apellidosentry.get(),
                                                                                                caretavar.get(),
                                                                                                guantevar.get(),
                                                                                                chaquetillavar.get(),
                                                                                                espadavar.get(),
                                                                                                pasantevar.get(),
                                                                                                protectorvar.get(),
                                                                                                diestrovar.get(),
                                                                                                zurdovar.get(),
                                                                                                combogloves.get(),
                                                                                                tallaentry.get()
                                                                                                ))
    cerrar = Button(root, text="Cerrar", width=10, command=root.quit)

    # Put elements on app
    # Frist the name bar
    nombrelabel.grid(row=0, column=0, sticky=NW)
    nombreentry.grid(row=0, column=1, sticky=W)
    apellidoslabel.grid(row=1, column=0, sticky=NW)
    apellidosentry.grid(row=1, column=1, sticky=W)

    # then the checkboxes for laterality
    diestrocheck.grid(row=0, column=0, sticky=W)
    zurdocheck.grid(row=1, column=0, sticky=W)

    # then the glove menu
    combogloves.grid(row=0, column=0, sticky=NW)

    # then the sizes
    alturalabel.grid(row=1, column=0, sticky=W)
    alturaentry.grid(row=1, column=2)

    pecholabel.grid(row=2, column=0, sticky=W)
    pechoentry.grid(row=2, column=2)

    cinturalabel.grid(row=3, column=0, sticky=W)
    cinturaentry.grid(row=3, column=2)

    caderalabel.grid(row=4, column=0, sticky=W)
    caderaentry.grid(row=4, column=2)

    buttoncalcularmasc.grid(row=5, column=2)
    buttoncalcularfem.grid(row=6, column=2)

    # then the equipment
    equipmbutton.grid(row=0, column=0)
    equipfbutton.grid(row=0, column=1)
    limpiarequipbutton.grid(row=7, column=0)
    resumenbutton.grid(row=7, column=1)

    # then the summary text and button
    tallalabel.grid(row=0, column=0, sticky=NW)
    tallaentry.grid(row=0, column=1, sticky=W)
    summaryequiplabel.grid(row=1, column=0, sticky=W)
    summarytallalabel.grid(row=1, column=1, sticky=W)
    summarylatelabel.grid(row=1, column=2, sticky=W)
    copiarresumenbutton.grid(row=8, column=2)
    limpiarresumenbutton.grid(row=9, column=2)

    # then the checkboxes for the equipment
    caretacheck.grid(row=1, column=0, sticky=W)
    guantecheck.grid(row=2, column=0, sticky=W)
    chaquetillacheck.grid(row=3, column=0, sticky=W)
    espadacheck.grid(row=4, column=0, sticky=W)
    pasantecheck.grid(row=5, column=0, sticky=W)
    protectorcheck.grid(row=6, column=0, sticky=W)

    # then initialize and put the frames up
    nombreframe.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
    lateralidadframe.grid(row=0, column=1, sticky=NW, padx=10, pady=10)
    medidasframe.grid(row=1, column=0, sticky=NW, padx=10, pady=10)
    guantesframe.grid(row=1, column=1, sticky=NW, padx=10, pady=10)
    equipacionframe.grid(row=2, column=0, sticky=NW, padx=10, pady=10)
    summaryframe.grid(row=2, column=1, sticky=NW, padx=10, pady=10)
    cerrar.grid(row=3, column=1, sticky=E)

    # Initialize main loop and run app
    root.mainloop()


if __name__ == '__main__':
    main()
