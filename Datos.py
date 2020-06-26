from tkinter import ttk
from tkinter import *

class Datos:
    def __init__(self, Window):
        self.wind = Window
        self.wind.title('Cohete')

        #CREAR CONTENEDOR FRAME
        frame = LabelFrame(self.wind, text='Datos del cohete')
        frame.grid(row = 0, column = 0, columnspan = 6, pady = 20)

        #variables
        self.a = DoubleVar()
        self.a.set(100.0)
        self.b = DoubleVar()
        self.b.set(10.0)
        self.c = DoubleVar()
        self.c.set(1.0)

        #ENTRADA DE DATOS
        Label(frame, text = 'Masa: ').grid(row= 1, column = 0)
        self.masa = Entry(frame, textvariable=self.a)
        self.masa.focus()
        self.masa.grid(row = 1, column = 1)

        Label(frame, text = 'Gasolina: ').grid(row= 2, column = 0)
        self.gasolina = Entry(frame, textvariable=self.b)
        self.gasolina.focus()
        self.gasolina.grid(row = 2, column = 1)

        Label(frame, text = 'Velo-Gaso: ').grid(row= 3, column = 0)
        self.velo = Entry(frame, textvariable=self.c)
        self.velo.focus()
        self.velo.grid(row = 3, column = 1)
        
        #BOTON
        Button(frame, text='Enviar',command= self.datos).grid(row = 5, columnspan = 2, sticky = W + E)
        
        #Funciones para tomar las variables y usarlas en el modelo
    def Masa(self):
        self.masa = self.a_val
        return self.masa
    def Velo(self):
        self.velocidad = self.c_val
        return self.velocidad
    def Gas(self):
        self.gasolina = self.b_val
        return self.gasolina
    def datos(self):
        self.a_val = self.a.get()
        self.b_val = self.b.get()   
        self.c_val = self.c.get()
        self.Masa()
        self.Velo()
        self.Gas()