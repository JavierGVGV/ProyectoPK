import Estadisticas, ControlJugadas, math, random, ctypes, time, PIL, PIL.Image, Image

#Variables globales imporatantes
#Posiciones de juego de la interfaz para busqueda de sitio

posxbus = [283,528,680,721,629,405,175,79,126]
posybus = [116,116,170,291,406,443,405,287,171]

#Posiciones de juego de la interfaz para reconocimiento de cartas

posxcar = [236,473,629,672,581,355,129,37,80]
posycar = [59,59,115,228,343,386,343,228,115]

#Posiciones de juego de la interfaz para el reconocimiento de las cartas centrales

posxcent = [272,326,380,434,488]
posycent = [220,220,220,220,220]

#Pixeles de carta a carta
saltocarta = 49
saltocarta2 = 48

#Fin del hilo
salir = 0

#Metodo que simula mas acotadamente las probabilidades de ganar, en
#funcion de las estadisticas de los adversarios y de las cartas ya en juego
#def simulacionacotada(numsim,jugadores,carta1p,carta2p):

#Metodo que calcula las coordenadas maximas y minimas de la situacion
#del lanzador de la aplicacion
#Nota: lanzador de dimensiones constantes 1010x750 y sale centrado
def posicionlanzador888():
    resolucion, restrabajo = ControlJugadas.resolucion()
    posicion_x = (resolucion[0]-1010)/2
    posicion_y = (resolucion[1]-750)/2
    posicion = [posicion_x,posicion_y]
    ControlJugadas.click_izq(posicion_x,posicion_y)
    return posicion

#Metodo de que en caso de no funcionar bien el modo automatico calcula
#manualmente la posicion del lanzador
def calibrar():
    posicion = ControlJugadas.posicion_actual()
    return posicion

def posicionlanzadorPS():
    resolucion, restrabajo = ControlJugadas.resolucion()
    posicion_x = (resolucion[0])/2
    posicion_y = (resolucion[1])/2
    posicion = [posicion_x,posicion_y]
    ControlJugadas.click_izq(posicion_x,posicion_y)
    ControlJugadas.maximizar()
    return posicion

#Retorna el porcentage de parecido entre las dos imagenes
def comparadorimagenes(imagen1,imagen2):
    
    resx = min(imagen1.size[0],imagen1.size[0])
    resy = min(imagen1.size[1],imagen1.size[1])
    maxpixval = (resx*resy)*(math.sqrt((255*255)+(255*255)+(255*255)))
    actpixval = 0
    j = 0
    while j<resx:
        k = 0
        while k<resy:
            pixel1 = ControlJugadas.valorpixel(imagen1,j,k)
            pixel2 = ControlJugadas.valorpixel(imagen2,j,k)
            r = pixel1[0] - pixel2[0]
            g = pixel1[1] - pixel2[1]
            b = pixel1[2] - pixel2[2]
            dif = math.sqrt((r*r)+(g*g)+(b*b))
            actpixval = actpixval + dif
            k = k + 1
        j = j + 1

    pctgsim = ((maxpixval-actpixval)/maxpixval)*100

    return pctgsim

def buscasitio():
    global posxbus
    global posybus
    global salir
    cont = 0
    buscando = 1
    while buscando:
        ControlJugadas.click_izq(posxbus[cont],posybus[cont])
        # Espera para ver si hemos conseguido sitio
        time.sleep(3)
        cap = ControlJugadas.abririmagen("imgops/confinicio.jpg")
        # Capturamos la pantalla y recortamos el trozo de imagen que nos dice si estamos dentro
        # Al poner el modo a 1 hace otra captura y la procesa
        capconf = ControlJugadas.recorta(65,65,237,123,1,"ninguna.jpg","res1.jpg")

        if comparadorimagenes(cap,capconf) > 90:
            buscando = 0
        else:
            cont = cont + 1
            cont = cont % 9

        if salir == 1:
            buscando = 0

    #Pulsar el boton ok para aceptar el sitio
    ControlJugadas.click_izq(350,375)

    return cont

#Metodo que permite saber cuando es nuestro turno de jugar
def turno():
    coorx = 430
    coory = 535
    salida = 0
    capconf = ControlJugadas.recorta(25,50,coorx,coory,1,"ninguna.jpg","res2.jpg")
    fold = ControlJugadas.abririmagen("imgops/fold.jpg")
    if comparadorimagenes(fold,capconf) > 90:
        salida = 1

    return salida

#Metodo que permite en caso de que sea nuestro turno realizar un fold
def fold():
    coorfoldx = 430
    coorfoldy = 535
    salida = 0
    capconf = ControlJugadas.recorta(25,50,coorfoldx,coorfoldy,1,"ninguna.jpg","res2.jpg")
    fold = ControlJugadas.abririmagen("imgops/fold.jpg")
    if comparadorimagenes(fold,capconf) > 90:
        ControlJugadas.click_izq(coorfoldx,coorfoldy)
        salida = 1

    return salida

#Metodo que permite en caso de que sea nuestro turno realizar un check
def check():
    coorcheckx = 560 
    coorchecky = 535
    salida = 0
    capconf = ControlJugadas.recorta(25,60,coorcheckx,coorchecky,1,"ninguna.jpg","res2.jpg")
    check = ControlJugadas.abririmagen("imgops/check.jpg")
    if comparadorimagenes(check,capconf) > 90:
        ControlJugadas.click_izq(coorcheckx,coorchecky)
        salida = 1

    return salida

#Metodo que permite en caso de que sea nuestro turno realizar un call
def call():
    coorcallx = 570
    coorcally = 525
    salida = 0
    capconf = ControlJugadas.recorta(25,40,coorcallx,coorcally,1,"ninguna.jpg","res2.jpg")
    call = ControlJugadas.abririmagen("imgops/call.jpg")
    if comparadorimagenes(call,capconf) > 90:
        ControlJugadas.click_izq(coorcallx,coorcally)
        salida = 1

    return salida

def call2():
    coorcallx = 705
    coorcally = 525
    salida = 0
    capconf = ControlJugadas.recorta(25,45,coorcallx,coorcally,1,"ninguna.jpg","res2.jpg")
    call = ControlJugadas.abririmagen("imgops/call2.jpg")
    if comparadorimagenes(call,capconf) > 90:
        ControlJugadas.click_izq(coorcallx,coorcally)
        salida = 1

    return salida

#Metodo que permite en caso de que sea nuestro turno realizar un bet
def bet():
    coorbetx = 685
    coorbety = 525
    salida = 0
    capconf = ControlJugadas.recorta(25,85,coorbetx,coorbety,1,"ninguna.jpg","res2.jpg")
    bet = ControlJugadas.abririmagen("imgops/bet.jpg")
    if comparadorimagenes(bet,capconf) > 90:
        ControlJugadas.click_izq(coorbetx,coorbety)
        salida = 1

    return salida

#Metodo que permite en caso de que sea nuestro turno realizar un raise
def rase():
    coorrasex = 685
    coorrasey = 525
    salida = 0
    capconf = ControlJugadas.recorta(25,85,coorrasex,coorrasey,1,"ninguna.jpg","res2.jpg")
    rase = ControlJugadas.abririmagen("imgops/raise.jpg")
    if comparadorimagenes(rase,capconf) > 90:
        ControlJugadas.click_izq(coorrasex,coorrasey)
        salida = 1

    return salida

def cartasmano(puesto):
    global posxcar
    global posycar
    global saltocarta2
    signo1 = 0
    signo2 = 0
    #Evaluacion de cartas de nuestra mano
    carta1 = ControlJugadas.recorta(35,15,posxcar[puesto],posycar[puesto],1,"ninguna.jpg","res3.jpg")
    carta2 = ControlJugadas.recorta(35,15,posxcar[puesto]+saltocarta2,posycar[puesto],1,"ninguna.jpg","res4.jpg")
    i=1
    porcentajemax1 = 0
    porcentajemax2 = 0
    while i<14:
        text1 = "cartas/"+str(i)+"c.jpg"
        text2 = "cartas/"+str(i)+"p.jpg"
        text3 = "cartas/"+str(i)+"d.jpg"
        text4 = "cartas/"+str(i)+"t.jpg"

        im1 = ControlJugadas.abririmagen(text1)
        im2 = ControlJugadas.abririmagen(text2)
        im3 = ControlJugadas.abririmagen(text3)
        im4 = ControlJugadas.abririmagen(text4)

        val1 = comparadorimagenes(im1,carta1)
        val2 = comparadorimagenes(im2,carta1)
        val3 = comparadorimagenes(im3,carta1)
        val4 = comparadorimagenes(im4,carta1)
        val5 = comparadorimagenes(im1,carta2)
        val6 = comparadorimagenes(im2,carta2)
        val7 = comparadorimagenes(im3,carta2)
        val8 = comparadorimagenes(im4,carta2)

        res1 = max(val1,val2,val3,val4)
        res2 = max(val5,val6,val7,val8)

        if res1 > porcentajemax1:
            porcentajemax1 = res1
            
            #Suma de desplazamiento en funcion del signo
            if res1 == val1:
                signo1 = i+0
            elif res1 == val2:
                signo1 = i+13
            elif res1 == val3:
                signo1 = i+26
            else:
                signo1 = i+39

        if res2 > porcentajemax2:
            porcentajemax2 = res2

            #Suma de desplazamiento en funcion del signo
            if res2 == val5:
                signo2 = i+0
            elif res2 == val6:
                signo2 = i+13
            elif res2 == val7:
                signo2 = i+26
            else:
                signo2 = i+39
        i = i + 1

    #print "Porcentaje max 1: %d" %porcentajemax1
    #print "Porcentaje max 2: %d" %porcentajemax2
    
    # Comprobar que esta cogiendo cartas y no otra cosa
    if (porcentajemax1 < 80) | (porcentajemax2 < 80):
        signo1 = 0
        signo2 = 0

    return signo1, signo2

#Metodo que comprueba si existen nuevas cartas centrales en funcion de la fase de juego en la que estemos
def cartasmesa(fase):

    salida = 1
    
    if fase == 0:
        posxcartamid1 = 272
        posycartamid1 = 220
        recorte = ControlJugadas.recorta(35,15,posxcartamid1,posycartamid1,1,"ninguna.jpg","res31.jpg")
        comp = ControlJugadas.abririmagen("imgops/mesa1.jpg")
        if comparadorimagenes(recorte,comp) > 90:
            salida = 0
        
        
    elif fase == 1:
        posxcartamid4 = 434
        posycartamid4 = 220
        recorte = ControlJugadas.recorta(35,15,posxcartamid4,posycartamid4,1,"ninguna.jpg","res32.jpg")
        comp = ControlJugadas.abririmagen("imgops/mesa4.jpg")
        if comparadorimagenes(recorte,comp) > 90:
            salida = 0

    elif fase == 2:
        posxcartamid5 = 488
        posycartamid5 = 220
        recorte = ControlJugadas.recorta(35,15,posxcartamid5,posycartamid5,1,"ninguna.jpg","res33.jpg")
        comp = ControlJugadas.abririmagen("imgops/mesa5.jpg")
        if comparadorimagenes(recorte,comp) > 90:
            salida = 0

    return salida

#Metodo que permite saber el valor de las cartas actuales del medio
def cartasmesavalor(posicion):
    global posxcent
    global posycent

    signo1 = 0
    
    #Evaluacion de cartas de nuestra mano
    carta = ControlJugadas.recorta(35,15,posxcent[posicion],posycent[posicion],1,"ninguna.jpg","res35.jpg")
    
    i=1
    porcentajemax1 = 0

    while i<14:
        text1 = "cartas/"+str(i)+"c.jpg"
        text2 = "cartas/"+str(i)+"p.jpg"
        text3 = "cartas/"+str(i)+"d.jpg"
        text4 = "cartas/"+str(i)+"t.jpg"

        im1 = ControlJugadas.abririmagen(text1)
        im2 = ControlJugadas.abririmagen(text2)
        im3 = ControlJugadas.abririmagen(text3)
        im4 = ControlJugadas.abririmagen(text4)

        val1 = comparadorimagenes(im1,carta)
        val2 = comparadorimagenes(im2,carta)
        val3 = comparadorimagenes(im3,carta)
        val4 = comparadorimagenes(im4,carta)

        res1 = max(val1,val2,val3,val4)

        if res1 > porcentajemax1:
            porcentajemax1 = res1
            
            #Suma de desplazamiento en funcion del signo
            if res1 == val1:
                signo1 = i+0
            elif res1 == val2:
                signo1 = i+13
            elif res1 == val3:
                signo1 = i+26
            else:
                signo1 = i+36

        i = i + 1

    return signo1

# Metodo que calcula el numero de jugadores restantes
def numerojugadores():
    global posycar
    global posycar
    posicion = 0
    contador = 0
    while posicion < 9:
        carta = ControlJugadas.recorta(25,15,posxcar[posicion],(posycar[posicion])+10,1,"ninguna.jpg","res8.jpg")
        comp = ControlJugadas.abririmagen("imgops/cartacontrol.jpg")
        if comparadorimagenes(carta,comp) > 90:
            contador = contador + 1
        posicion = posicion + 1

    return contador
        
    
def cartaall(carta):
    salida = 0
    cartaproc = carta%13
    if (cartaproc > 9) | (cartaproc == 1) | (cartaproc == 0):
        salida = 1

    return salida

#Maquina de estados que determina el comportamiento del juego en funcion de calculos estadisticos
#en tiempo real
# RETOCAR PORCENTAGES Y ESTRATEGIAS DE JUEGO EN FUNCION DE LAS VALORES ESTADISTICOS
def juegoautomatico():
    global salir
    puesto = buscasitio()
    prob = 0
    print "Puesto: %d" %puesto
    cartasmidrec = []
    fase = 0
    salir = 0
    carta1 = 0
    carta2 = 0
    numjug = 9 #Modificar para conteo real

    while salir == 0:
        
        #Pre-Flop, ciegas 10% con 9 jugadores para estar seguros de que tenemos una buena mano
        if fase == 0:

            salida = 0
            while salida == 0:
                salida = turno()

            print "----- Detecto mi turno -----"

            verifcambiofase = cartasmesa(2)

            if verifcambiofase == 1:

                fase = 3
                cartasmidrec = []
                cartasmidrec.extend(cartasmidrectemp3)

            else:

                print "----- Reinicio contadores de cartas -----"
                carta1 = 0
                carta2 = 0

                cartasmidrec = []

                # Esperar a que salgan las nuevas cartas
                # time.sleep(3)

                # Comprobar el cambio de mano y si estamos con cartas actuales en mano
                while (carta1 == carta2):
                    carta1, carta2 = cartasmano(puesto)

                print "Carta 1: %d" %carta1
                print "Carta 2: %d" %carta2

                # Calcular los jugadores restantes
                numjug = numerojugadores()
                
                if numjug == 0:
                    numjug = 1
                    
                print "Jugadores restantes: %d" % numjug

                
                porcentajecorte = (100/(numjug+1)) + (20/(numjug+1))
                porcentajecorteall = porcentajecorte + (20/(numjug+1))

                print "Porcentaje corte: %d" %porcentajecorte
                print "PORCENTAJE ALL: %d" %porcentajecorteall
                
                prob = Estadisticas.simulacion(60000,200,numjug+1,carta1,carta2,cartasmidrec)
                print "Fase 0: Porcentaje: %d" %(prob[0]*100)

                salida = 0
                while salida == 0:
                    
                    salida = turno()

                    if salida == 1:
                        if (prob[0]*100) > porcentajecorte:
                            
                            callok = call()
                            
                            if callok == 0:
                                checkok = check()
                                if checkok == 0:

                                    if ((prob[0]*100) > porcentajecorteall) & (cartaall(carta1) == 1) & (cartaall(carta2) == 1):
                                        callok2 = call2()

                                        if callok2 == 0:
                                            foldok = fold()
                                            if foldok == 1:
                                                fase = 0
                                        else:
                                            fase = 1
                                    else:
                                        foldok = fold()
                                        if foldok == 1:
                                            fase = 0
                                else:
                                    fase = 1
                            else:
                                fase = 1  
                        else:
                            checkok = check()
                            if checkok == 0:
                                foldok = fold()
                                if foldok == 1:
                                    fase = 0
                            else:
                                fase = 1
                    
        #Flop, tres cartas descubiertas
        elif fase == 1:

            finrivales = 0
            while finrivales == 0:
                finrivales = turno()
            
            verifcambiofase = cartasmesa(0)

            if verifcambiofase == 1:

                cartasmidrec = []
                
                cartasmidrec.append(cartasmesavalor(0))
                cartasmidrec.append(cartasmesavalor(1))
                cartasmidrec.append(cartasmesavalor(2))

                print "Carta Mid 1: %d" %cartasmidrec[0]
                print "Carta Mid 2: %d" %cartasmidrec[1]
                print "Carta Mid 3: %d" %cartasmidrec[2]

                # Calcular los jugadores restantes
                numjug = numerojugadores()

                if numjug == 0:
                    numjug = 1
                    
                print "Jugadores restantes: %d" % numjug

                
                porcentajecorte = (100/(numjug+1))+(30/(numjug+1))
                porcentajecorteall = porcentajecorte +(30/(numjug+1))

                print "Porcentaje corte: %d" %porcentajecorte
                print "PORCENTAJE ALL: %d" %porcentajecorteall
                
                prob = Estadisticas.simulacion(60000,200,numjug+1,carta1,carta2,cartasmidrec)
                print "Fase 1: Porcentaje: %d" %(prob[0]*100)

                salida = 0
                while salida == 0:
                    salida = turno()

                    if salida == 1:
                        if (prob[0]*100) > porcentajecorte:
                            
                            callok = call()
                            
                            if callok == 0:
                                checkok = check()
                                
                                if checkok == 0:

                                    if (prob[0]*100) > porcentajecorteall:
                                        callok2 = call2()

                                        if callok2 == 0:
                                            foldok = fold()
                                            if foldok == 1:
                                                fase = 0
                                        else:
                                            fase = 2
                                    else:
                                        foldok = fold()
                                        if foldok == 1:
                                            fase = 0
                                else:
                                    fase = 2
                            else:
                                fase = 2  
                        else:
                            checkok = check()
                            if checkok == 0:
                                foldok = fold()
                                if foldok == 1:
                                    fase = 0
                            else:
                                fase = 2
            else:
                fase = 0


        #Turn, una carta mas descubierta
        elif fase == 2:

            finrivales = 0
            while finrivales == 0:
                finrivales = turno()
            
            verifcambiofase = cartasmesa(1)

            if verifcambiofase == 1:

                cartasmidrectemp2 = []
                cartasmidrectemp2.extend(cartasmidrec)
                
                cartasmidrec.append(cartasmesavalor(3))
                print "Carta Mid 4: %d" %cartasmidrec[3]

                # Calcular los jugadores restantes
                numjug = numerojugadores()

                if numjug == 0:
                    numjug = 1
                
                print "Jugadores restantes: %d" % numjug

                porcentajecorte = (100/(numjug+1))+(30/(numjug+1))
                porcentajecorteall = porcentajecorte + (30/(numjug+1))

                print "Porcentaje corte: %d" %porcentajecorte
                print "PORCENTAJE ALL: %d" %porcentajecorteall
            
                prob = Estadisticas.simulacion(60000,200,numjug+1,carta1,carta2,cartasmidrec)
                print "Fase 2: Porcentaje: %d" %(prob[0]*100)

                salida = 0
                while salida == 0:
                    salida = turno()

                    if salida == 1:
                        if (prob[0]*100) > porcentajecorte:
                            
                            callok = call()
                            
                            if callok == 0:
                                checkok = check()
                                if checkok == 0:

                                    if (prob[0]*100) > porcentajecorteall:
                                        callok2 = call2()

                                        if callok2 == 0:
                                    
                                            foldok = fold()
                                            if foldok == 1:
                                                fase = 0
                                        else:
                                            fase = 3
                                    else:
                                        foldok = fold()
                                        if foldok == 1:
                                            fase = 0
                                else:
                                    fase = 3
                            else:
                                fase = 3  
                        else:
                            checkok = check()
                            if checkok == 0:
                                foldok = fold()
                                if foldok == 1:
                                    fase = 0
                            else:
                                fase = 3
            else:
                fase = 1
                
        #River, una carta mas descubierta
        elif fase == 3:

            finrivales = 0
            while finrivales == 0:
                finrivales = turno()
            
            verifcambiofase = cartasmesa(2)

            if verifcambiofase == 1:

                cartasmidrectemp3 = []
                cartasmidrectemp3.extend(cartasmidrec)
                
                cartasmidrec.append(cartasmesavalor(4))
                print "Carta Mid 5: %d" %cartasmidrec[4]

                # Calcular los jugadores restantes
                numjug = numerojugadores()

                if numjug == 0:
                    numjug = 1
                    
                print "Jugadores restantes: %d" % numjug

                porcentajecorte = (100/(numjug+1))+(40/(numjug+1))
                porcentajecorteall = porcentajecorte + (30/(numjug+1))

                print "Porcentaje corte: %d" %porcentajecorte
                print "PORCENTAJE ALL: %d" %porcentajecorteall
            
                prob = Estadisticas.simulacion(60000,200,numjug+1,carta1,carta2,cartasmidrec)
                print "Fase 3: Porcentaje: %d" %(prob[0]*100)

                salida = 0
                while salida == 0:
                    salida = turno()

                    if salida == 1:
                        if (prob[0]*100) > porcentajecorte:
                            
                            callok = call()
                            
                            if callok == 0:
                                
                                checkok = check()
                                if checkok == 0:

                                    if (prob[0]*100) > porcentajecorteall:
                                        callok2 = call2()

                                        if callok2 == 0:
                                    
                                            foldok = fold()
                                            if foldok == 1:
                                                fase = 0

                                        else:
                                            fase = 0
                                    else:
                                        foldok = fold()
                                        if foldok == 1:
                                            fase = 0
                                else:
                                    fase = 0
                            else:
                                fase = 0  
                        else:
                            checkok = check()
                            if checkok == 0:
                                foldok = fold()
                                if foldok == 1:
                                    fase = 0
                            else:
                                fase = 0
            else:
                fase = 2
                cartasmidrec = []
                cartasmidrec.extend(cartasmidrectemp2)
                
        #Resto de apuestas tras la primera apuesta del river
        else:
            
            fase = 0
        
    
    return 1
        
#def sistemaautomatico():

#def obtencioncartaspropias():

#def obtencionjugadores():

#def obtencioncartasneutrales():

#def calculoapuesta():

#simulacionciega(1000,5,1,13)
