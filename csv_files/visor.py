import tkinter as tk
from tkinter import *
from tkinter import filedialog
import csv
import pandas as pd

class Ventana:
    def __init__(self, interfaz) -> None:
        self.root = interfaz
        self.root.title('csv files')
        self.root.geometry('350x350')
        self.root.resizable(0,0)
        self.Labels()
        self.Botones()


    def Labels(self):
        Label(self.root,text='Paso1. Elegir archivo con extension .csv').place(x=0, y=0)
        Label(self.root,text='Paso2. Crear un DataFrame a partir de los datos').place(x=0, y=0)
        

    def Botones(self):
        Button(text='Buscar', command=self.Cargar).place(x=0, y=25)

    def Cargar(self):
        self.filename_csv = StringVar()
        self.filename_csv = filedialog.askopenfilename(filetypes=('archivos .csv', '* .csv'))
        Label(self.root, text=f' La direccion del archivo que se esta usando es:\n {self.filename_csv}', justify='left', state='disabled').place(x=0 ,y=50)
        with open(f'{self.filename_csv}', 'r')as file:
            self.path = file.read()
            self.df = pd.read_csv(self.path)
            print(self.df)
        
        

        
        
        

objeto = Ventana(Tk())
objeto.root.mainloop()
