import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox as mBox
from tkinter import ttk
import webbrowser

class Windows:
    def __init__(self, visual) -> None:
        self.rt = visual
        self.rt.geometry('500x100')
        self.rt.title('Scraping')
        self.rt.resizable(0,0)
        self.rt.iconbitmap('roadmap0.ico')
        self.Lab()
        self.Ent()
        self.Bot()

    def Lab(self):
        Label(self.rt, text='Paso1. Copiar el URL de la pagina objetivo', justify='left').place(x=5, y=5)
        Label(self.rt, text='URL= ', justify='left').place(x=5, y=30)

    def Ent(self):
        self.dirr = StringVar()
        Entry(self.rt, textvariable=self.dirr, justify='left', width=70).place(x=45, y=30)

    def Bot(self):
        Button(self.rt, text='Acceder', command=self.Req, width=10).place(x=100, y=60)
        Button(self.rt, text='Abrir Local', command=self.Abri, width=10).place(x=200, y=60)
        Button(self.rt, text='Salir', command=self.Sal, width=10).place(x=300, y=60)

    def Req(self):
        urlx = str(self.dirr.get())
        print(urlx)
        pagina = requests.get(f'{urlx}').text
        soup = BeautifulSoup(pagina, 'html.parser')
#pull all instance of <table> tag
        plan = soup.find_all('table')
        results = []
        mBox.showinfo('Scraping','HTML obtenido')

        for x in plan:
            results.append(str(x))

#write an file.html
        with open('scraping/index.html', 'w') as filew:
            for line in results:
                filew.write(line)

    def Abri(self):
        webbrowser.open('scraping\index.html')

    def Sal(self):
        self.rt.quit()
        self.rt.destroy()


obj = Windows(Tk())
obj.rt.mainloop()
