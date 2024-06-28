from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox as mBox
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import Menu
from tkinter import PhotoImage


class Ventana:
    def __init__(self, interfaz) -> None:
        self.root = interfaz
        self.root.geometry("500x515")
        self.root.title("AnalizatorX")
        self.root.resizable(0,0)
        self.root.iconbitmap('roadmap0.ico')
        self.Letras()
        self.Botones()
        self.Lista()
        self.Menuses()

    def Menuses(self):
        self.barramenu = Menu(self.root)
        self.root.config(menu=self.barramenu)

        self.opc1 = Menu(self.barramenu, tearoff=0)
        self.opc1.add_command(label='Manual de uso', command=self.Menux)

        self.opc2 = Menu(self.barramenu, tearoff=0)
        self.opc2.add_command(label='Actualización', command= self.Menu2)
        self.opc2.add_separator()
        self.opc2.add_command(label='Contacto', command= self.Contactos)

        self.barramenu.add_cascade(label='Ayuda', menu=self.opc1)
        self.barramenu.add_cascade(label='Soporte',menu=self.opc2)

    def Letras(self):
        Label(self.root, text='Paso1. Seleccione una fuente|extensión de datos para cargar').place(x=0, y=400)
        Label(self.root, text='Este programa pretende ser una guía de estudio para integrar el análisis de datos\n a la creación de GUI con librerias tkinter y pandas', justify='left').place(x=5, y=20)
        self.imagen = PhotoImage(file="images/roadmap0.png")
        Label(self.root, image=self.imagen, bd=12).place(x=50 ,y=60)

    def Botones(self):
        self.seleccion1 = Button(self.root, text='Seleccionar', command= self.ejecutar_seleccion, width=10, background='lightgreen').place(x=250, y=428)
        Button(self.root, text='Salir', command= self.Salida, width=10, background='lightblue').place(x=400, y=460)
        
    def Lista(self):
        self.seleccio = StringVar()
        self.numero = Combobox(self.root, textvariable=self.seleccio, width=30, state='readonly', values=('.csv', '.json', 'sql-conect')).place(x=20, y= 430)

        

    def ejecutar_seleccion(self):
        if self.seleccio.get() == '.csv':
            try:
                import files.visor_csv
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrió algun problema al abrir el archivo')
          
        elif self.seleccio.get() == '.json':
            try:
                import files.visor_json
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrió algun problema al abrir el archivo')

        elif self.seleccio.get() == 'sql-conect':
            try:
                import conector.conector_sql_python
            except IOError:
                mBox.showerror('Error!!!', 'Ocurrió algun problema al abrir el archivo')

    def Menux(self):
        import menu.working

    def Menu2(self):
        import menu.menu2

    def Contactos(self):
        import menu.contact

    def Salida(self):
        self.root.quit()
        self.root.destroy()

objeto=Ventana(Tk())
objeto.root.mainloop()
