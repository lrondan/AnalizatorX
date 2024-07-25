from tkinter import *
from tkinter import messagebox as mBox
from tkinter import ttk, filedialog
import pandas as pd
import sqlite3

class ConectDB:
    def __init__(self, interfaz) -> None:
        self.gui_db = interfaz
        self.gui_db.geometry('500x500')
        self.gui_db.title('Conex_DB')
        self.gui_db.resizable(0,0)
        self.Labels()
        self.Entradas()
        self.Botones()


#Labels
    def Labels(self):
        Label(self.gui_db, text='Busca un archivo que contenga una base de datos.\nExtension: .db o .sqlite', justify=LEFT).place(x=0, y=10)
        Label(self.gui_db, text='Ecribe un comando SQL.', justify=LEFT).place(x=0, y=150)
        Label(self.gui_db, text='Convertido en top (10) DataFrame:', justify=LEFT).place(x=10,y=300-20)
#Entradas 
    def Entradas(self):
        self.table_name = StringVar()
        Entry(self.gui_db, textvariable=self.table_name, width=60, relief=SUNKEN, justify=LEFT, borderwidth=3).place(x=0, y=170)
#Botones
    def Botones(self):
        Button(self.gui_db, text='BUSCAR', justify=CENTER, command=self.Buscar).place(x=5, y=50)
        Button(self.gui_db, text='BUSCAR', justify=CENTER, command=self.Conexion).place(x=5, y=210)
        Button(self.gui_db, text='SALIR ', justify=CENTER, command=self.Salir).place(x=430, y=450)
#Funciones
    def Buscar(self):
        self.filename_db = StringVar()
        self.filename_db = filedialog.askopenfilename(filetypes=('archivos .sqlite', '* .db', '* .sqlite'))
        Label(self.gui_db, text=f' La ruta del archivo que se está usando es:\n {self.filename_db}', justify='left').place(x=20 ,y=100)

    def Conexion(self):
        conn = sqlite3.Connection(f'{self.filename_db}')

        cursor = conn.cursor()
        buffer = ''
        line_output = str(self.table_name.get())
        if line_output == '':
            mBox.showerror('Error', 'SQL invalido')
        else:
            buffer += line_output
            try:
                buffer = buffer.strip()
                vista1 = cursor.execute(buffer)

                if buffer.lstrip().upper().startswith('SELECT'):
                    vista1 = pd.DataFrame(data=vista1)

                    Label(self.gui_db, text=f'{vista1.head(10)}').place(x=10,y=320-20)
            except sqlite3.Error as e:
                mBox.showerror('Error', e.args[0])
        conn.close()

    def Salir(self):
        self.gui_db.quit()
        self.gui_db.destroy()


objeto_db = ConectDB(Tk())
objeto_db.gui_db.mainloop()