from tkinter import ttk
from tkinter import *
from vpython import *
import pandas as pd
from Datos import Datos
from graph import graph as grafica

window = Tk()
aplicacion = Datos(window)
window.mainloop() 

scene = canvas(title='<strong>Cohete<strong>',x=0, y=0, width=600, height=450, center=vector(5,0,0), background=color.black,align='left')
#Sitema de referencia
L=2
R=L/100
d=L-1
xaxis = cylinder(pos=vec(0,0,0), axis=vec(0,0,d), radius=R, color=color.white)
yaxis = cylinder(pos=vec(0,0,0), axis=vec(d,0,0), radius=R, color=color.white)
zaxis = cylinder(pos=vec(0,0,0), axis=vec(0,d,0), radius=R, color=color.white)
k = 1.02
h = 0.05*L
text(pos=xaxis.pos+k*xaxis.axis, text='x', height=h, align='center', billboard=True, emissive=True)
text(pos=yaxis.pos+k*yaxis.axis, text='y', height=h, align='center', billboard=True, emissive=True)
text(pos=zaxis.pos+k*zaxis.axis, text='z', height=h, align='center', billboard=True, emissive=True)

partes_cohete = []
altura = 0.5
partes_cohete.append(cylinder(pos=vector(0,0,0),color=color.white, size=vector(altura,0.1,0.1), axis=vector(0,1,0),make_trail = True))

partes_cohete.append(cone(pos=partes_cohete[0].pos+partes_cohete[0].size.x*partes_cohete[0].axis*2, color=color.yellow,size=vector(partes_cohete[0].size.y,partes_cohete[0].size.y,partes_cohete[0].size.y),axis=vector(0,1,0)))

partes_cohete.append(triangle(v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(1,0,0),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(1,0,0),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(1,2,0),color=color.red) ))

partes_cohete.append(triangle(v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(-1,0,0),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(-1,0,0),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(-1,2,0),color=color.red)))

partes_cohete.append(triangle(v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,0,1),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(0,0,1),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,2,1),color=color.red)))

partes_cohete.append(triangle(v0=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,0,-1),color=color.red),v1=vertex(pos=partes_cohete[0].pos+1.5*partes_cohete[0].size.y*vector(0,0,-1),color=color.red),v2=vertex(pos=partes_cohete[0].pos+0.5*partes_cohete[0].size.y*vector(0,2,-1),color=color.red)))
                
cohete = compound(partes_cohete,pos=vector(0,0,0))
cohete.masa = aplicacion.Masa()
cohete.gasolina_masa = aplicacion.Gas()
cohete.velocidad = vector(0,0,0)

masa_inicial = cohete.masa + cohete.gasolina_masa
masa_inicial_gas = cohete.gasolina_masa

graph(align='right',title='<strong>Grafica</strong>',xtitle='<strong>Tiempo (s)</strong>',ytitle='<strong>Distancia(m)</strong>')
r_pos = gcurve(color=color.blue,label="Distancia")
r_mas = gcurve(color=color.red,label='Masa')
r_vel = gcurve(color=color.green,label='Velocidad')

l = label(pos=cohete.pos,text=str(cohete.velocidad.y)+"/s", xoffset=20,yoffset=50, space=30,height=16, border=4,font='sans')

attach_trail(cohete) #humo del cohete
vec_velo = vector(0,-100,0)
mdot = aplicacion.Velo()
dt = 0.001
t = 0
# lista de datos 
t_ = []
v_ = []
d_ = []
m_ = []
i = 0
while (cohete.gasolina_masa > 0): #mientras haya gasolina continua la simulacion
    rate(500) #ajustamos los fps de la simulacion
    dm = mdot*dt #diferencial del ratio de masa
    cohete.velocidad += dm/(cohete.masa+cohete.gasolina_masa)*(-vec_velo) #calcular velocidad y asignar al cohet
    cohete.pos += cohete.velocidad*dt #suma velocidad a la distancia
    cohete.gasolina_masa -=dm #quitamos masa a medida que pasa el tiempo (diferecial de masa)
    cohete.opacity = cohete.gasolina_masa/masa_inicial_gas #opacidad del cohete
    t += dt #aumentamos el tiempo
    #Graficas
    r_pos.plot(pos=(t,cohete.pos.y)) 
    r_mas.plot(pos=(t,cohete.gasolina_masa))
    r_vel.plot(pos=(t,cohete.velocidad.y))
    scene.center = cohete.pos #Centrar camara en el cohete
    #Añadir datos para luego guardarlos
    t_.append(t)
    v_.append(cohete.velocidad.y)
    d_.append(cohete.pos.y)
    m_.append(cohete.gasolina_masa)
    l.pos=cohete.pos
    l.text=str(cohete.velocidad.y)

data = {
    "Tiempo": t_,"Distancia":d_ ,"Velocidad": v_,"Masa": m_
} 
grafica(data)
df = pd.DataFrame(data)
# convertir datos a archivo excel
df.to_csv("./data.csv",index=False)