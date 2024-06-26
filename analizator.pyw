from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox as mBox
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import Menu


class Ventana:
    def __init__(self, interfaz) -> None:
        self.root = interfaz
        self.root.geometry("500x500")
        self.root.title("Analizator")
        self.root.resizable(0,0)
        self.Letras()
        self.Botones()
        self.Lista()
        self.Menuses()

    def Menuses(self):
        self.barramenu = Menu(self.root)
        self.root.config(menu=self.barramenu)

        self.opc1 = Menu(self.barramenu, tearoff=0)
        self.opc1.add_command(label='menu1')
        self.barramenu.add_cascade(label='archivo', menu=self.opc1)

    def Letras(self):
        Label(self.root, text='Paso1. Seleccione una fuente|extension de datos para cargar').place(x=0, y=400)

    def Botones(self):
        self.seleccion1 = Button(self.root, text='Seleccionar', command= self.ejecutar_seleccion, width=10).place(x=400, y=430)
        Button(self.root, text='Salir', command= self.Salida, width=10).place(x=400, y=460)
        
    def Lista(self):
        self.seleccio = StringVar()
        self.numero = Combobox(self.root, textvariable=self.seleccio, width=30, state='readonly', values=('.csv', '.json', '.xlsx','xml', 'sql-conect')).place(x=20, y= 430)
        

    def ejecutar_seleccion(self):
        if self.seleccio.get() == '.csv':
            try:
                import files.visor_csv
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrio algun problema al abrir el archivo')
          
        elif self.seleccio.get() == '.json':
            try:
                self.filename_json =filedialog.askopenfilename(filetypes=('archivos .json', '* .json'))
                print(self.filename_json)
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrio algun problema al abrir el archivo')

        elif self.seleccio.get() == '.xlsx':
            try:
                self.filename_xlsx =filedialog.askopenfilename(filetypes=('archivos .xlsx', '* .xlsx'))
                print(self.filename_xlsx)
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrio algun problema al abrir el archivo')

        elif self.seleccio.get() == '.xml':
            try:
                self.filename_xml =filedialog.askopenfilename(filetypes=('archivos .xml', '* .xml'))
                print(self.filename_xml)
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrio algun problema al abrir el archivo')

        elif self.seleccio.get() == 'sql-conect':
            print('funciona sql-conect')

    def Salida(self):
        self.root.quit()
        self.root.destroy()

objeto=Ventana(Tk())
objeto.root.mainloop()
