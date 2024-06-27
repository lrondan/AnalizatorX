import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mBox
import matplotlib.pyplot as mpl
import pandas as pd
import json

class Ventana3:
    def __init__(self, interfaz3) -> None:
        self.roottt = interfaz3
        self.roottt.title('json files')
        self.roottt.geometry('350x350')
        self.roottt.resizable(0,0)
        self.Labels3()
        self.Botones3()
        self.Entradas3()

    def Labels3(self):
        Label(self.roottt,text='Paso1. Elegir archivo con extensión .json').place(x=0, y=0)
        Label(self.roottt,text='Paso2. Consultar los datos contenidos dentro del dicionario, se introduce una clave y se obtiene un valor', justify='left').place(x=0, y=85)
        Label(self.roottt, text='Paso3. Visualizar').place(x=0, y=160)
        Label(self.roottt, text='Clave: ').place(x=130, y=125)
        
    def Botones3(self):
        Button(self.roottt, text='Buscar', command=self.Cargar3, width=10).place(x=0, y=25)
        Button(self.roottt,text='Consultar', command=self.Crear3, width=10).place(x=0, y=120)
        Button(self.roottt, text='Salir', command=self.Salir3, width=10).place(x=250, y=305)

    def Entradas3(self):
        self.col1 = IntVar()
        self.seleccion1 = StringVar()
        Entry(self.roottt, textvariable=self.seleccion1, width=25).place(x=170, y=125)

    def Cargar3(self):
        self.filename_json = StringVar()
        self.filename_json = filedialog.askopenfilename(filetypes=('archivos .json', '* .json'))
        Label(self.roottt, text=f' La ruta del archivo que se está usando es:\n {self.filename_json}', justify='left', state='disabled').place(x=0 ,y=50)
        
    def Crear3(self):
        with open(f'{self.filename_json}', 'r')as json_file:
            self.info = json.load(json_file)
            self.xyz1=self.seleccion1.get()
            self.valor1 = self.info[self.xyz1]
            Label(self.roottt, text=f'valor :{self.valor1}', justify='left', font='BOLD').place(x=10, y=200)
        
    def Salir3(self):
        self.roottt.quit()
        self.roottt.destroy()

objeto3 = Ventana3(Tk())

objeto3.roottt.mainloop()