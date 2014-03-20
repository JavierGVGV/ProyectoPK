# -*- coding: cp1252 -*-
try:
    from Tkinter import *
except ImportError:
    raise ImportError,"Se requiere el modulo Tkinter"

try:
    import time
except ImportError:
    raise ImportError,"Se requiere el modulo Time"

import Inteligencia, time
import PIL.ImageTk
import tkFont
import string
import math
import Estadisticas
import threading

# ----- Ventana principal -----

inicio = Tk()
inicio.title("Bot Poker Texas Hold`em")
inicio.maxsize(195,150)
inicio.minsize(195,150)

# ----- Constantes Importantes -----

app_init = [0,0]
estado = 0
valor = StringVar()

# ----- Subventanas -----

resultados = Toplevel(inicio)
resultados.maxsize(620,360)
resultados.minsize(620,360)
resultados.title("Resultados")
resultados.state(newstate='withdraw')

# ----- Funciones -----

def convertirpalo(letra):
    salida = -1
    if letra in "Cc":
        salida = 0
    elif letra in "Pp":
        salida = 13
    elif letra in "Dd":
        salida = 26
    elif letra in "Tt":
        salida = 39
    else:
        salida = -1

    return salida
        

def funsalir():
    resultados.state(newstate='withdraw')

def funreconocer():
    print "Bien Reconocer"

def funcalibrar():
    time.sleep(10)
    app_init[0] = Inteligencia.calibrar()[0]
    app_init[1] = Inteligencia.calibrar()[1]
    print "Bien Calibrar"

def funmanual():

    # ----- Creacion de la ventana -----
    
    manual = Toplevel(inicio)
    manual.title("Bot Poker Texas Hold`em")
    manual.geometry("800x600")
    manual.maxsize(800,630)
    manual.minsize(800,630)

    # ----- Etiquetas -----
    
    et1 = Label(manual,text="Cartas Centrales",font=("Helvetica",14),justify=LEFT)
    #et2 = Label(manual,text="Simulaciones",font=("Helvetica",14),justify=LEFT)
    et3 = Label(manual,text="Jugadores",font=("Helvetica",14),justify=LEFT)
    et4 = Label(manual,text="Cartas Propias",font=("Helvetica",14),justify=LEFT)
    et8 = Label(manual,text="Carta 1:",font=("Helvetica",10),justify=LEFT)
    et9 = Label(manual,text="Carta 2:",font=("Helvetica",10),justify=LEFT)
    et10 = Label(manual,text="Manos",font=("Helvetica",14),justify=CENTER)

    # ----- Campos de texto -----

    #in1 = Entry(manual,justify=RIGHT)
    in2 = Text(manual,width=20,height=10)
    in5 = Entry(manual,justify=RIGHT,width=120)
    in6 = Entry(manual,justify=LEFT)
    in7 = Entry(manual,justify=LEFT)
    in8 = Entry(manual,justify=RIGHT)
    lista1 = Text(manual,width=20,height=10)

    # ----- Elemento panel de cartas -----

    foto = PIL.Image.open("mesa.jpg")
    global imgtablero
    imgtablero = PIL.ImageTk.PhotoImage(foto)
    tablero = Canvas(manual, width = 800, height = 600)
    mesa = tablero.create_image(100,0,image=imgtablero, anchor = NW)
    fuente = tkFont.Font(family='Helvetica',size='12',weight='bold')
    mres1 = tablero.create_text(400,25,fill='red',text="Tu: 0%",font=fuente)
    mres2 = tablero.create_text(250,25,fill='white',text="Jugador 2: 0%",font=fuente)
    mres3 = tablero.create_text(550,25,fill='white',text="Jugador 3: 0%",font=fuente)
    mres4 = tablero.create_text(250,280,fill='white',text="Jugador 4: 0%",font=fuente)
    mres5 = tablero.create_text(400,280,fill='white',text="Jugador 5: 0%",font=fuente)
    mres6 = tablero.create_text(550,280,fill='white',text="Jugador 6: 0%",font=fuente)
    mres7 = tablero.create_text(200,100,fill='white',text="Jugador 7: 0%",font=fuente)
    mres8 = tablero.create_text(200,200,fill='white',text="Jugador 8: 0%",font=fuente)
    mres9 = tablero.create_text(600,100,fill='white',text="Jugador 9: 0%",font=fuente)
    mres10 = tablero.create_text(600,200,fill='white',text="Jugador 10: 0%",font=fuente)
    
    # ----- Funciones Propias -----

    def funcancelar():
        manual.destroy()
        print "Bien Cancelar"

    def funaceptar():
    
        try:
            #simulaciones = int(Entry.get(in1))
            manos = int(Entry.get(in8))
            simulaciones = 1
            jugadores = in2.get(1.0,END)
            longitud = len(jugadores)

            cartasmidrec = []
            fallo = 0

            numjug=-1
            if (longitud != 56) & (jugadores.find(',')==-1):
                numjug = 1
            elif (jugadores.find(',')!=-1):
                numjug = len(jugadores.split(','))
                if numjug > 10:
                    numjug = 10
            else:
                numjug = -1


            centrales = lista1.get(1.0,END)

            if (len(centrales) < 2):
                cartasmidrec = []
                
            elif (len(centrales) < 25):
        
                centrales = centrales.replace(centrales[-1],"")
                cartasmidstring = centrales.split(",")
                cartasmidrec = []
                
                y = 0
                while y < len(cartasmidstring):
                    carta = cartasmidstring[y]
                    carta2 = carta.replace(carta[-1],"")

                    if(int(carta2)>13) | (int(carta2)<1):
                        fallo = 1

                    cartasmidrec.append(int(int(carta2)+convertirpalo(carta[-1])))
                    y = y + 1

            carta1s = Entry.get(in6)
            carta2s = Entry.get(in7)

            carta1f = convertirpalo(carta1s[-1])
            carta2f = convertirpalo(carta2s[-1])

            if (carta1f < 0) | (carta2f < 0):
                in5.delete(0,END)
                in5.insert(0,"Formato incorrecto al introducir las cartas.")

            else:
                carta1s = carta1s.replace(carta1s[-1],"")
                carta2s = carta2s.replace(carta2s[-1],"")

                if (int(carta1s)>13) | (int(carta1s)<1) | (int(carta2s)>13) | (int(carta2s)<1):

                    # Provocamos excepcion
                    carta1 = 1000
                    carta2 = 1001

                else:

                    carta1 = int(carta1s)+carta1f
                    carta2 = int(carta2s)+carta2f

            if len(cartasmidrec)>5:
                in5.delete(0,END)
                in5.insert(0,"No introducir mas de cinco cartas centrales.")

            elif (carta1 in cartasmidrec) | (carta2 in cartasmidrec):
                in5.delete(0,END)
                in5.insert(0,"Las cartas centrales no pueden repetir las cartas propias.")
                
            elif carta1 == carta2:
                in5.delete(0,END)
                in5.insert(0,"Introduce dos cartas propias que sean diferentes.")

            elif carta1 == 1000:
                in5.delete(0,END)
                in5.insert(0,"El numero de la carta debe estar entre 1 y 13.")

            elif fallo == 1:
                in5.delete(0,END)
                in5.insert(0,"El numero de las cartas centrales debe estar entre 1 y 13.")
            
            elif numjug != -1:
                in5.delete(0,END)
                numjug = numjug + 1

                resultados = Estadisticas.simulacion(manos,simulaciones,numjug,carta1,carta2,cartasmidrec)
                nomjugs = jugadores.split(',')

                i = 0
                result = []
                
                while i<len(resultados): #-1 por el numero de empates ya quitado
                    result.append(float(resultados[i])*100)
                    i = i + 1
            
                contador = 1

                if contador==1:
                    texto = "Tu %.2f" % result[contador-1] , '%'
                    tablero.itemconfigure(mres1,text=texto)
                
                for jug in nomjugs:
                    texto = jug + "%.2f" % result[contador] , '%'

                    if contador==1:
                        tablero.itemconfigure(mres2,text=texto)
                    elif contador==2:
                        tablero.itemconfigure(mres3,text=texto)
                    elif contador==3:
                        tablero.itemconfigure(mres4,text=texto)
                    elif contador==4:
                        tablero.itemconfigure(mres5,text=texto)
                    elif contador==5:
                        tablero.itemconfigure(mres6,text=texto)
                    elif contador==6:
                        tablero.itemconfigure(mres7,text=texto)
                    elif contador==7:
                        tablero.itemconfigure(mres8,text=texto)
                    elif contador==8:
                        tablero.itemconfigure(mres9,text=texto)
                    elif contador==9:
                        tablero.itemconfigure(mres10,text=texto)

                    contador = contador + 1

                texto = ""

                while contador < 10:

                    if contador==1:
                        tablero.itemconfigure(mres2,text=texto)
                    elif contador==2:
                        tablero.itemconfigure(mres3,text=texto)
                    elif contador==3:
                        tablero.itemconfigure(mres4,text=texto)
                    elif contador==4:
                        tablero.itemconfigure(mres5,text=texto)
                    elif contador==5:
                        tablero.itemconfigure(mres6,text=texto)
                    elif contador==6:
                        tablero.itemconfigure(mres7,text=texto)
                    elif contador==7:
                        tablero.itemconfigure(mres8,text=texto)
                    elif contador==8:
                        tablero.itemconfigure(mres9,text=texto)
                    elif contador==9:
                        tablero.itemconfigure(mres10,text=texto)

                    contador = contador + 1
                    
            else:
                in5.delete(0,END)
                in5.insert(0,"Introduzca el nombre de los jugadores separados por comas.")

        except:
            in5.delete(0,END)
            in5.insert(0,"Formato de simulaciones o cartas incorrecto(Simulaciones=Numeros Enteros,NP=NumeroPalo).")
  

        print "Bien Aceptar"


    # ----- Botones -----

    boton1 = Button(manual, text="Aceptar", command=funaceptar)
    boton2 = Button(manual, text="Cancelar", command=funcancelar)
    #boton3 = Button(manual, text="Reconocer Jugadores", command=funreconocer)

    # ----- Conbinacion de los elementos -----

    et1.grid(row=1,column=1,padx=10,pady=10)
    lista1.grid(row=2,column=1,rowspan=10,padx=0,pady=0)
    #et2.grid(row=12,column=1,padx=5,pady=5)
    #in1.grid(row=13,column=1,padx=0,pady=0)
    in8.grid(row=13,column=2,padx=0,pady=0)
    et3.grid(row=1,column=2,padx=10,pady=10)
    in2.grid(row=2,column=2,rowspan=10,padx=0,pady=0)
    et4.grid(row=1,column=3,columnspan=2,padx=10,pady=10)
    boton1.grid(row=12,column=3,rowspan=3,padx=0,pady=0)
    boton2.grid(row=12,column=4,rowspan=3,padx=0,pady=0)
    #boton3.grid(row=12,column=2,padx=10,pady=10)
    et10.grid(row=12,column=2,padx=0,pady=0)
    in5.grid(row=14,column=1,columnspan=4,padx=10,pady=10)
    in6.grid(row=2,column=4,padx=10,pady=10)
    in7.grid(row=3,column=4)
    et8.grid(row=2,column=3)
    et9.grid(row=3,column=3)
    tablero.grid(row=15,column=1,columnspan=4,padx=5,pady=5)

    
    #in1.insert(0,"100")
    in8.insert(0,"100")
    in2.insert(INSERT,"Introduce el nombre de tus rivales divididos por comas.")
    lista1.insert(INSERT,"Introduce las cartas centrales o nada.  Formato = NP        N = Figura/Numero   P = Palo(C,T,P,D)   Separadas por comas.")
    in6.insert(0,"1C")
    in7.insert(0,"2C")
    
    print "Bien Manual"

def funauto():
    
    global estado
    global valor

    if estado == 0:
        lista = ('Cliente','Poker Stars','888 Poker')
        valor.set(lista[0])
        tipo = OptionMenu(inicio,valor,*lista)
        inicio.maxsize(300,150)
        inicio.minsize(300,150)
        tipo.grid(row=2,column=2)
        
    elif estado == 1:
        if valor.get().find('Poker Stars') == 0:
            print 'Bien Poker'
            #Inteligencia.posicionlanzadorPS()
            # Crear hilo independiente
            t = threading.Thread(Inteligencia.juegoautomatico())
            t.start()
            print salida
            
        elif valor.get().find('888 Poker') == 0:
            print 'Bien 888'
            Inteligencia.posicionlanzador888()
            
    cambio = 0
    
    if (estado == 0) & (cambio == 0):
        estado = 1
        cambio = 1
    if (estado == 1) & (cambio == 0):
        inicio.maxsize(195,150)
        inicio.minsize(195,150)
        estado = 0
        cambio = 1
        
    print "Bien Automatico"

def funfinal():
    inicio.destroy()
    Inteligencia.salir = 1
    print "Bien Final"
    
# ----- Etiquetas -----

et5 = Label(resultados,text="Estadisticas",font=("Helvetica",14),justify=CENTER)
et6 = Label(resultados,text="Consejo",font=("Helvetica",14),justify=CENTER)
et7 = Label(resultados,text="Apuesta recomendada",font=("Helvetica",14),justify=CENTER)

# ------ Graficas -----

gr1 = Canvas(resultados)
coord = 20, 60, 220, 260
arc1 = gr1.create_arc(coord,start=0,extent=300,fill="red")

# ----- Botones -----


boton4 = Button(resultados, text="Salir", command=funsalir,width=15)
boton5 = Button(inicio, text="Calibrar", command=funcalibrar,width=25)
boton6 = Button(inicio, text="Manual", command=funmanual,width=25)
boton7 = Button(inicio, text="Automatico", command=funauto,width=25)
boton8 = Button(inicio, text="Salir", command=funfinal, width=25)

# ----- Campos de Texto -----


in3 = Text(resultados,width=20,height=10)
in4 = Entry(resultados,justify=RIGHT,width=30)

# ----- Desplegables -----

lista2 = Listbox(resultados)

for item in ["Pedro","Luis","Jose"]:
    lista2.insert(END,item) 

# ----- Combinacion de los elementos subventana 1 -----

boton4.grid(row=5,column=3,padx=5,pady=5)
et6.grid(row=1,column=1,padx=10,pady=5)
et7.grid(row=3,column=1,padx=10,pady=5)
in4.grid(row=4,column=1,padx=10,pady=5)
in3.grid(row=2,column=1,padx=10,pady=5)
lista2.grid(row=2,column=2,columnspan=1,rowspan=1,padx=5,pady=5)
et5.grid(row=1,column=2,padx=5,pady=5)
gr1.grid(row=1,column=3,padx=5,pady=5,rowspan=3)

# ----- Combiacion de los elementos de la ventana de inicio -----

boton6.grid(row=1,column=1,padx=5,pady=5)
boton7.grid(row=2,column=1,padx=5,pady=5)
boton8.grid(row=4,column=1,padx=5,pady=5)
boton5.grid(row=3,column=1,padx=5,pady=5)

def iniciar():
    inicio.mainloop()

print "Cargado modulo interfaz correctamente."

iniciar()


print app_init
