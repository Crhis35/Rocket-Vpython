from tkinter import ttk
from tkinter import *
from vpython import *
#from visual import *
#from visual.graph import *

class Datos:
    def __init__(self, Window):
        self.wind = Window
        self.wind.title('Crhis 2.0')

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
        
        #Metodos para tomar las variables de la ventana y usarlas en el modelo
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


if __name__ == '__main__':
    window = Tk()
    #window.geometry("250x250")
    aplicacion = Datos(window)
    window.mainloop() 
    n = int(input("Start Machine Crhis-Rocket: "))
    if(n==1):

        scene = canvas(title='Cohete Crhis',x=0, y=0, width=600, height=450, center=vector(5,0,0), background=color.black)

        #cohete = cylinder(pos=vector(0,0,0), color=color.blue, size=vector(0.5,0.1,0.1),velocidad = vector(0,0,0), masa= float(aplicacion.Masa()), gasolina_masa=float(aplicacion.Gas()),make_trail = True, axis=vector(0,1,0))
        
        partes_cohete = []
        height = 0.5
        partes_cohete.append(cylinder( pos=vector(0,0,0),color=color.red, size=vector(height,0.1,0.1), axis=vector(0,1,0),make_trail = True ))

        partes_cohete.append(cone(pos=partes_cohete[0].pos+partes_cohete[0].size.x*partes_cohete[0].axis*2, color=color.red,size=vector(partes_cohete[0].size.y,partes_cohete[0].size.y,partes_cohete[0].size.y),axis=vector(0,1,0)))

        partes_cohete.append(triangle( v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(1,0,0),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(1,0,0),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(1,2,0),color=color.red) ))

        partes_cohete.append(triangle( v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(-1,0,0),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(-1,0,0),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(-1,2,0),color=color.red)))

        partes_cohete.append(triangle( v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,0,1),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(0,0,1),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,2,1),color=color.red)))

        partes_cohete.append(triangle( v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,0,-1),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(0,0,-1),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,2,-1),color=color.red)))
                     
        cohete = compound(partes_cohete,pos=vector(0,0,0))
        cohete.masa = aplicacion.Masa()
        cohete.gasolina_masa = aplicacion.Gas()
        cohete.velocidad = vector(0,0,0)
       
        masa_inicial = cohete.masa + cohete.gasolina_masa
        masa_inicial_gas = cohete.gasolina_masa

        #graph=gdisplay(x=950,y=0,width=400,title = "Distancia vs Velocidad vs Masa",height=400,foreground=color.black, background=color.white)
        r_pos = gcurve(color=color.blue,label="Distancia")
        r_mas = gcurve(color=color.red,label='Masa')
        r_vel = gcurve(color=color.green,label='Velocidad')
        #label(display=graph, pos=(3,2))

        attach_trail(cohete)
        vec_velo = vector(0,-100,0)
        mdot = aplicacion.Velo()
        dt = 0.001
        t = 0


        while (cohete.gasolina_masa > 0):
            rate(500)
            dm = mdot*dt
            cohete.velocidad += dm/(cohete.masa+cohete.gasolina_masa)*(-vec_velo)
            cohete.pos += cohete.velocidad*dt
            cohete.gasolina_masa -=dm
            cohete.opacity = cohete.gasolina_masa/masa_inicial_gas
            t += dt
            r_pos.plot(pos=(t,cohete.pos.y))
            r_mas.plot(pos=(t,cohete.opacity))
            r_vel.plot(pos=(t,cohete.velocidad.y))
            scene.center = cohete.pos
            #print("Distancia -->",round(cohete.pos.y,2), "velo-->",round(cohete.velocidad.y,2),"Gaso-->",round(cohete.gasolina_masa,2),"Masa cohe-->",round(cohete.masa+cohete.gasolina_masa,2))
            
        #print(cohete.velocidad.y,mag(vec_velo)*log(masa_inicial/cohete.masa))