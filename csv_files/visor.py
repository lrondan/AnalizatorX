import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mBox
import matplotlib.pyplot as mpl
import pandas as pd

class Ventana2:
    def __init__(self, interfaz) -> None:
        self.roott = interfaz
        self.roott.title('csv files')
        self.roott.geometry('350x350')
        self.roott.resizable(0,0)
        self.Labels()
        self.Botones()
        self.Entradas()



    def Labels(self):
        Label(self.roott,text='Paso1. Elegir archivo con extension .csv').place(x=0, y=0)
        Label(self.roott,text='Paso2. Crear un DataFrame por columnas a partir de los datos').place(x=0, y=100)
        Label(self.roott, text='Paso3. Visualizar').place(x=0, y=160)
        Label(self.roott, text='Metodo').place(x=0, y=180)
        Label(self.roott, text='Grafico').place(x=150, y=180)
        Label(self.roott, text='X=').place(x=210, y=200)
        Label(self.roott, text='Y=').place(x=210, y=230)
        

        

    def Botones(self):
        Button(self.roott, text='Buscar', command=self.Cargar).place(x=0, y=25)
        Button(self.roott,text='Crear', command=self.Crear).place(x=0, y=120)
        Button(self.roott,text='Agrupar', command=self.Binns).place(x=0, y=200)
        Button(self.roott,text='Plot', command=self.PlotBinns).place(x=150, y=200)
        Button(self.roott, text='Salir', command=self.Salir).place(x=300, y=305)

    def Entradas(self):
        self.col1 = IntVar()
        self.col2 = IntVar()
        Entry(self.roott, textvariable=self.col1, width=15).place(x=230, y=200)
        Entry(self.roott, textvariable=self.col2, width=15).place(x=230, y=230)

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
        self.columnas1 = self.col1.get()
        self.columnas2 = self.col2.get()
        self.ejex = self.df1.iloc[2:, self.columnas1]
        self.ejey = self.df1.iloc[2:, self.columnas2]
        mBox.showinfo('Nuevo Set', f'{self.ejex, self.ejey}')
        print(self.ejex, self.ejey)

    def PlotBinns(self):
        self.ejex.astype('int64')
        mpl.plot(self.ejex, self.ejey)
        mpl.show()

    def Salir(self):
        self.roott.quit()
        self.roott.destroy()

objeto = Ventana2(Tk())
objeto.roott.mainloop()
