import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mBox
import matplotlib.pyplot as mpl
import pandas as pd

class Ventana4:
    def __init__(self, interfaz) -> None:
        self.root4 = interfaz
        self.root4.title('xml files')
        self.root4.geometry('350x350')
        self.root4.resizable(0,0)
        self.Labels()
        self.Botones()
        self.Entradas()

    def Labels(self):
        Label(self.root4,text='Paso1. Elegir archivo con extensión .xml').place(x=0, y=0)
        Label(self.root4,text='Paso2. Crear un DataFrame por columnas a partir de los datos').place(x=0, y=100)
        Label(self.root4, text='Paso3. Visualizar').place(x=0, y=160)

    def Botones(self):
        Button(self.root4, text='Buscar', command=self.Cargar4, width=10).place(x=0, y=25)
        Button(self.root4, text='Salir', command=self.Salir4, width=10).place(x=250, y=305)

    def Entradas(self):
        pass

    def Cargar4(self):
        self.filename_xml = StringVar()
        self.filename_xml = filedialog.askopenfilename(filetypes=('archivos .xml', '* .xml'))
        Label(self.root4, text=f' La ruta del archivo que se está usando es:\n {self.filename_xml}', justify='left', state='disabled').place(x=0 ,y=50)
        
    def Salir4(self):
        self.root4.quit()
        self.root4.destroy()


objeto4 = Ventana4(Tk())
objeto4.root4.mainloop()
