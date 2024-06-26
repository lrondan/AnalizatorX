import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mBox
import csv
import pandas as pd

class Ventana2:
    def __init__(self, interfaz) -> None:
        self.roott = interfaz
        self.roott.title('csv files')
        self.roott.geometry('350x350')
        self.roott.resizable(0,0)
        self.Labels()
        self.Botones()



    def Labels(self):
        Label(self.roott,text='Paso1. Elegir archivo con extension .csv').place(x=0, y=0)
        Label(self.roott,text='Paso2. Crear un DataFrame por columnas a partir de los datos').place(x=0, y=100)
        Label(self.roott, text='Paso3. Procesar datos').place(x=0, y=160)
        Label(self.roott, text='Metodo').place(x=0, y=180)
        Label(self.roott, text='Grafico').place(x=200, y=180)

        

    def Botones(self):
        Button(self.roott, text='Buscar', command=self.Cargar).place(x=0, y=25)
        Button(self.roott,text='Crear', command=self.Crear).place(x=0, y=120)
        Button(self.roott,text='Binning', command=self.Binns).place(x=0, y=200)
        Button(self.roott,text='Plot Bins', command=self.Binns).place(x=200, y=200)


    def Cargar(self):
        self.filename_csv = StringVar()
        self.filename_csv = filedialog.askopenfilename(filetypes=('archivos .csv', '* .csv'))
        Label(self.roott, text=f' La direccion del archivo que se esta usando es:\n {self.filename_csv}', justify='left', state='disabled').place(x=0 ,y=50)
        with open(f'{self.filename_csv}', 'r')as file:
            self.path = file.read()
            self.df = pd.read_csv(self.path)    

    def Crear(self):
        self.url = self.filename_csv
        self.df1 = pd.read_csv(self.url, header=None)
        raiz = Tk()
        raiz.title('DataFrame')
        raiz.resizable(0,0)
        Label(raiz, text=f'{self.df1}', justify='left').pack()
        raiz.mainloop()

    def Binns(self):
        pass


objeto = Ventana2(Tk())
objeto.roott.mainloop()
