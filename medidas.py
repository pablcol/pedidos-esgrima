from tkinter import *

# Initialize tkinter and give it a page name
root = Tk()
root.title("Pedidos Grant Esgrima")

# Define functions
def medidas():
    return

# Create label texts
inicioLabel = Label(root, text="Medidas tirador/a")
alturaLabel = Label(root, text="Altura en cm:")
pechoLabel = Label(root, text="Tamaño pecho en cm:")
cinturaLabel = Label(root, text="Tamaño cintura en cm:")
caderaLabel = Label(root, text="Tamaño cadera en cm:")

# Define entries
alturaEntry = Entry(root, width=15)
pechoEntry = Entry(root, width=15)
cinturaEntry = Entry(root, width=15)
caderaEntry = Entry(root, width=15)

# Define buttons
buttonCalcular = Button(root, text="Calcular talla")

# Put elements on app
inicioLabel.grid(row=0, column=0, columnspan=2)

alturaLabel.grid(row=1, column=0, sticky=W)
alturaEntry.grid(row=1, column=1)

pechoLabel.grid(row=2, column=0, sticky=W)
pechoEntry.grid(row=2, column=1)

cinturaLabel.grid(row=3, column=0, sticky=W)
cinturaEntry.grid(row=3, column=1)

caderaLabel.grid(row=4, column=0, sticky=W)
caderaEntry.grid(row=4, column=1)

buttonCalcular.grid(row=5, column=1)

# Initialize main loop and app
root.mainloop()
