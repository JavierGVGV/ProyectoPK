# -*- coding: cp1252 -*-
#---- LIBRERIAS NECESARIAS ----
import random
import math
import time
import itertools
import profile

#---- DEFINICION DE LAS CARTAS ----
# Para saber el simbolo o numero de la carta con la colocacion actual
# solo sera necesario realizar la operacion modulo de 13

##Cartas={}
##Cartas[1]="As de Corazones"
##Cartas[2]="Dos de Corazones"
##Cartas[3]="Tres de Corazones"
##Cartas[4]="Cuatro de Corazones"
##Cartas[5]="Cinco de Corazones"
##Cartas[6]="Seis de Corazones"
##Cartas[7]="Siete de Corazones"
##Cartas[8]="Ocho de Corazones"
##Cartas[9]="Nueve de Corazones"
##Cartas[10]="Diez de Corazones"
##Cartas[11]="J de Corazones"
##Cartas[12]="Q de Corazones"
##Cartas[13]="K de Corazones"
## 
##Cartas[14]="As de Picas"
##Cartas[15]="Dos de Picas"
##Cartas[16]="Tres de Picas"
##Cartas[17]="Cuatro de Picas"
##Cartas[18]="Cinco de Picas"
##Cartas[19]="Seis de Picas"
##Cartas[20]="Siete de Picas"
##Cartas[21]="Ocho de Picas"
##Cartas[22]="Nueve de Picas"
##Cartas[23]="Diez de Picas"
##Cartas[24]="J de Picas"
##Cartas[25]="Q de Picas"
##Cartas[26]="K de Picas"
##
##Cartas[27]="As de Diamantes"
##Cartas[28]="Dos de Diamantes"
##Cartas[29]="Tres de Diamantes"
##Cartas[30]="Cuatro de Diamantes"
##Cartas[31]="Cinco de Diamantes"
##Cartas[32]="Seis de Diamantes"
##Cartas[33]="Siete de Diamantes"
##Cartas[34]="Ocho de Diamantes"
##Cartas[35]="Nueve de Diamantes"
##Cartas[36]="Diez de Diamantes"
##Cartas[37]="J de Diamantes"
##Cartas[38]="Q de Diamantes"
##Cartas[39]="K de Diamantes"
##
##Cartas[40]="As de Treboles"
##Cartas[41]="Dos de Treboles"
##Cartas[42]="Tres de Treboles"
##Cartas[43]="Cuatro de Treboles"
##Cartas[44]="Cinco de Treboles"
##Cartas[45]="Seis de Treboles"
##Cartas[46]="Siete de Treboles"
##Cartas[47]="Ocho de Treboles"
##Cartas[48]="Nueve de Treboles"
##Cartas[49]="Diez de Treboles"
##Cartas[50]="J de Treboles"
##Cartas[51]="Q de Treboles"
##Cartas[52]="K de Treboles"

def suma(lista1,lista2):
    return float(lista1)+float(lista2)

def divide(lista1,lista2):
    return float(lista1)/float(lista2)

# Preprocesado que combierte el 1 y el 0 AS y K en 14 y 13 para poder ser trabajados

def procesafigura(lista):
    a = (lista -1)% 13 + 1
    return a if a !=1 else 14

def procesapalo(lista):
    return (lista-1)/13

#---- DEFINICION DE METODOS DE SIMULACION ----
#carta1 y carta2 son arrays de cartas del tamano de la cantidad de jugadores
#numsim es el numero de simulaciones que queremos y nosotros siempre somos el indice 0 en el array
def simulacion(manos,numsim,jugadores,carta1p,carta2p,cartasmidrec):

    carta1 = []
    carta2 = []
    empates = []
    cartasmidrecproc = []
    resultados = []
    carta1.append(int(carta1p))
    carta2.append(int(carta2p))
    
    cartasmidrecproc = []

    # Generacion de un array para dividir y sacar la media
    #manosdiv = []
    manosdiv = [int(manos) for i in xrange(jugadores+1)]

    # Generacion de un array temporal para operar
    #resultadostemp2 = []
    resultadostemp2 = [int(0) for i in xrange(jugadores+1)]

    # Generacion de un array con todas las cartas excluyendo las nuestras
    #cartasrestantes = []
    cartasrestantes = [int(i+1) for i in xrange(52) if ((i+1) != int(carta1p)) & ((i+1) != int(carta2p))]

    # Indices restantes (no cartas restantes 0..49)
    restantes = 49

    # Procesado de cartas centrales
    for carta in cartasmidrec:

        if (cartasmidrec.count(carta) < 2):
            cartasmidrecproc.append(carta)
            cartasrestantes.remove(carta)
            restantes = restantes - 1

    restantesiniciales = restantes

    # Generacionde array temporal de cartas restantes para operar
    cartasrestantestemp = []
    cartasrestantestemp.extend(cartasrestantes)

    p = 1

    tiempo3 = float(time.time())
    while p<=manos:

        # Generacion de las manos de los jugadores
        i = 2
        while i<=jugadores:

            rand = random.randint(0,restantes)

            carta1.append(int(cartasrestantestemp[int(rand)]))
            
            cartasrestantestemp.remove(cartasrestantestemp[int(rand)])
            restantes = restantes - 1
     
            rand = random.randint(0,restantes)

            carta2.append(int(cartasrestantestemp[int(rand)]))
            
            cartasrestantestemp.remove(cartasrestantestemp[int(rand)])
            restantes = restantes - 1

            i = i + 1
        
##        numc = 0
        # Ganador es el indice del array de veces que gana cada persona
        # siendo el 1 nosotros mismos
        ganador = jugadores
##        maxganador = 0
##        i = 0
        # Almacena el valor de las jugadas para una simulacion
        valorjugadas = []
        # Almacena las veces que gana cada jugador en el numero de simulaciones establecidas
        vecesganadas = []
##
        vecesganadas = [0]*(jugadores+1)

        # Inicializacion de el array de veces ganadas y de la posicion de empates la siguiente al numero de jugadores
        #i = 1
        #while i <= jugadores+1:
        #    vecesganadas.append(0)
        #    i = i + 1

        cartasmid = []
        cartasmid.extend(cartasmidrecproc)
        numc = len(cartasmidrecproc)

##        cartasrestantestemp2 = []
##        cartasrestantestemp2.extend(cartasrestantestemp)
##        restantestemp = restantes
##        numsimtemp = numsim

##        while numsimtemp > 1:

            # Generacion random del resto de cartas desconocidas
        while numc < 5: 
            idcard = random.randint(0,restantes)

            # Comprobacion de que la carta generada no ha salido ya

            cartasmid.append(cartasrestantestemp[int(idcard)])
            numc = numc+1

            cartasrestantestemp.remove(cartasrestantestemp[int(idcard)])
            restantes = restantes - 1


        # Calculo del valor numerico de la jugada maxima de cada jugador

        valorjugadas = [tipojugada(cartasmid,carta1[i],carta2[i]) for i in xrange(0,jugadores)]

        # Busqueda del valor maximo y de su ganador(indice)
        # en caso de mas de uno se añade al final a empates
        maxganador = max(valorjugadas)
        cantidad = valorjugadas.count(maxganador)

        if cantidad > 1:
            ganador = jugadores
        else:
            ganador = valorjugadas.index(maxganador)

        temporal = vecesganadas[ganador]
        vecesganadas.pop(ganador)
        vecesganadas.insert(ganador, (temporal + 1))
        
        # Reinicializamos variables locales
##        ganador = jugadores
##        maxganador = 0
##        valorjugadas = []

        # Reinicializamos los valores para simular de nuevo
##        cartasmid = []
##        cartasmid.extend(cartasmidrecproc)
##        numc = len(cartasmidrecproc)
            
##        cartasrestantestemp2 = []
##        cartasrestantestemp2.extend(cartasrestantestemp)
##        restantestemp = restantes
##
##        numsimtemp = numsimtemp-1

##        resultadostemp = vecesganadas

##        numsimtemp = numsim 

        resultadostemp2 = map(suma,resultadostemp2,vecesganadas)

        cartasrestantestemp = []
        cartasrestantestemp.extend(cartasrestantes)
        restantes = restantesiniciales

        carta1 = []
        carta2 = []
        carta1.append(int(carta1p))
        carta2.append(int(carta2p))

        p = p + 1

    tiempo4 = time.time()
    print "TIEMPO BUCLE MANOS"
    print "%.8f" % (tiempo4-tiempo3)
    # Calcular la media

    resultados = map(divide,resultadostemp2,manosdiv)

    # Eliminar la ultima salida del array
    empate = resultados.pop(jugadores)

    temp = resultados.pop(0)
    resultados.insert(0,(temp+empate))

##    temp = 0
##    while temp < jugadores:
##        empates.append(float(empate/jugadores))
##        temp = temp + 1
##
##    resultados = map(suma,resultados,empates)

    return resultados
    
    

#La variable jugada guarda el tipo de jugada maxima con dichas cartas
#   1 -> Carta mas alta
#   2 -> Pareja
#   3 -> Doble Pareja
#   4 -> Trio
#   5 -> Escalera
#   6 -> Color (5 cartas del mismo palo)
#   7 -> Full (Trio y pareja)
#   8 -> Poker (4 Cartas iguales)
#   9 -> Escalera de Color (5 cartas consecutivas del mismo palo)
#   10 -> Escalera de Color Real (As,K,Q,J,10 del mismo palo)
#La variable valjugada guarda el valor mas alto de las cartas
#Siendo 1=AS el valor maximo y 13=K,12=Q...
#Las variables que almacenan la figura y el palo son operaciones matematicas de modulo y division con redondeo
#dejando que los palos son: 0->Corazones,1->Picas,2->Diamantes y 3->Treboles
def tipojugada(cartasmid,carta1,carta2):


    # El valor de la jugada para ser facilmente analizable se calcula son la siguiente formula
    # El tipo de jugada por 10.000 + la carta mas alta de la figura por 100 + la carta mas alta fuera de la figura
    # con lo que nos da el formato JJ/CC/FF = EJ:101203 -> 10/12/03

    # Juntar cartas centrales con las propias para analizar
    cartastotales = []
    cartastotales.extend(cartasmid)
    cartastotales.append(carta1)
    cartastotales.append(carta2)
    
    # Calcular las figuras y palos de las cartas proporcionadas
    cartasmidfig = []

    cartasmidfig = map(procesafigura,cartastotales)

    cartastotales.sort()
    cartasmidfig.sort()

    palo0 = 0
    palo1 = 0
    palo2 = 0
    palo3 = 0

    for carta in cartastotales:

        if carta < 14:
            palo0 = palo0 + 1
        elif carta < 27:
            palo1 = palo1 + 1
        elif carta < 40:
            palo2 = palo2 + 1
        else:
            palo3 = palo3 + 1

    cartaant = 0
    temp = 0
    valorpoker = 0
    valortrio = 0
    valorpareja1 = 0
    valorpareja2 = 0
    cartamaxima = 0
    numparejas = 0
    maxrelfig = 0
    recorridas = 0

    for carta in cartasmidfig:

        if cartaant == 0:
            cartaant = carta
            estado = 1
            temp = 1
        else:
            if (carta == cartaant) & (recorridas < 6):
                temp = temp + 1
            else:
                if (recorridas >= 6):
                    if (carta == cartaant):
                        temp = temp + 1
                if temp == 1:
                    cartamaxima = cartaant
                elif temp == 2:
                    if (numparejas%2) == 0:
                        valorpareja1 = cartaant
                    else:
                        valorpareja2 = cartaant
                    numparejas = numparejas + 1
                elif temp == 3:
                    valortrio = cartaant
                elif temp == 4:
                    valorpoker = cartaant

                if maxrelfig < temp:
                    maxrelfig = temp
                    
                temp = 1
                
        cartaant = carta
        recorridas = recorridas + 1

    # Buscar interrelacion entre las 7 cartas, centrales y de jugador
    
    # Array que almacena la cantidad de cartas iguales a cada carta central
    # El indice del array es cada carta central y las dos ultimas cartas de jugador
    # El bucle calcula dichas cifras siendo al menos el valor de 1 en cada casilla del array

    # Array que almacena la cantidad de cartas del mismo palo a acada carta central
    # El indice del array es cada carta central y las dos ultimas cartas de jugador
    # El bucle calcula dichas cifras siendo al menos el valor de 1 en cada casilla del array

    #relacionfig = [cartasmidfig.count(carta) for carta in cartasmidfig]

    # Calculo de la relacion maxima con los valores calculados
    # maxrelfig = max(relacionfig)
    maxrelpalo = max(palo0,palo1,palo2,palo3)

    # Analisis de los maximos resultantes
    # El maximo de coincidencias en figuras es de 4 al solo haber 4 palos
    # El maximo de coincidencias en palo es de 7 al poder ser 7 cartas del mismo palo
    # Con estos datos filtramos las posibles jugagas maximas en orden decreciencte del valor
    # de dichos maximos, obteniendo la mejor jugada posible con las cartas centrales y las de la mano
    # Si encontramos la mano mas alta esta variable se pone a 1
    finbusqueda = 0
    
    # Comprobar si tenemos Escalera de color O Escalera Real----------------------------------------------------------------------------------------
    if (finbusqueda == 0) & (maxrelfig < 4) & (maxrelpalo > 4):

        res1 = (cartastotales[1]-cartastotales[0])+(cartastotales[2]-cartastotales[1])+(cartastotales[3]-cartastotales[2])+(cartastotales[4]-cartastotales[3])
        res2 = (cartastotales[2]-cartastotales[1])+(cartastotales[3]-cartastotales[2])+(cartastotales[4]-cartastotales[3])+(cartastotales[5]-cartastotales[4])
        res3 = (cartastotales[3]-cartastotales[2])+(cartastotales[4]-cartastotales[3])+(cartastotales[5]-cartastotales[4])+(cartastotales[6]-cartastotales[5])
        res4 = (cartastotales[4]-cartastotales[0])+(cartastotales[2]-cartastotales[1])+(cartastotales[3]-cartastotales[2])+(cartastotales[4]-cartastotales[3])
        res5 = (cartastotales[5]-cartastotales[1])+(cartastotales[3]-cartastotales[2])+(cartastotales[4]-cartastotales[3])+(cartastotales[5]-cartastotales[4])
        res6 = (cartastotales[6]-cartastotales[2])+(cartastotales[4]-cartastotales[3])+(cartastotales[5]-cartastotales[4])+(cartastotales[6]-cartastotales[5])
        
        # Comprobar una posible escalera
        if (res1==4)|(res2==4)|(res3==4):

            jugada = 9
            finbusqueda = 1
            mejorcarta = 0
            mejorfuerajuego = 0

            # Comprobamos si es igual a 4 para saber si tenemos escalera normal
            # y comprobamos si es igual a 12 para saber si tenemos escalera con K y AS
            if (res1 == 4) | ((res4 == 15) & (res1 == 3)):
                if (procesafigura(cartastotales[0]) == 14) & ((res4 == 15) & (res1 == 3)):
                    mejorcarta = cartastotales[0]
                else:
                    mejorcarta = cartastotales[4]
                
                mejorfuerajuego = max(procesafigura(cartastotales[5]),procesafigura(cartastotales[6]))
                
            if (res2 == 4) | ((res5 == 15) & (res2 == 3)):
                if (procesafigura(cartastotales[1]) == 14) & ((res5 == 15) & (res2 == 3)):
                    mejorcarta = cartastotales[1]
                else:
                    mejorcarta = max(mejorcarta,cartastotales[5])
                    
                mejorfuerajuego = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[5]))
                
            if (res3 == 4) | ((res6 == 15) & (res3 == 3)):
                if (procesafigura(cartastotales[2]) == 14) & ((res6 == 15) & (res3 == 3)):
                    mejorcarta = cartastotales[2]
                else:
                    mejorcarta = max(mejorcarta,cartastotales[6])
                    
                mejorfuerajuego = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))

            mejorcarta = procesafigura(mejorcarta)

            if mejorcarta == 14:
                jugada = 10

            valjugada = (jugada*10000) + (mejorcarta*100) + mejorfuerajuego
        
    # Comprobar si tenemos Poker ----------------------------------------------------------------------------------------
    if (finbusqueda == 0) & (maxrelfig == 4):
        jugada = 8
        finbusqueda = 1

        valjugada = (jugada*10000) + (valorpoker*100) + cartamaxima
         
    # Comprobar si tenemos Full ----------------------------------------------------------------------------------------
    if (finbusqueda == 0) & (maxrelfig == 3) & (numparejas > 0):

        jugada = 7
        finbusqueda = 1

        valjugada = (jugada*10000) + (valortrio*100) + cartamaxima
            
    # Comprobar si tenemos Color ----------------------------------------------------------------------------------------
    if (finbusqueda == 0):

        if (palo0 > 4) | (palo1 > 4) | (palo2 > 4) | (palo3 > 4):

            jugada = 6
            finbusqueda = 1
            maximocolor = 0
            maximofueracolor = 0

            if (palo0 > 4):
                if procesafigura(cartastotales[0]) == 14:
                    maximocolor = 14
                else:
                    maximocolor = procesafigura(cartastotales[palo0-1])

                if palo0 == 5:
                    maximofueracolor = max(procesafigura(cartastotales[6]),procesafigura(cartastotales[5]))
                elif palo0 == 6:
                    maximofueracolor = procesafigura(cartastotales[6])
                else:
                    maximofueracolor = procesafigura(cartastotales[2])
                
            elif (palo1 > 4):
                if procesafigura(cartastotales[palo0]) == 14:
                    maximocolor = 14
                else:
                    maximocolor = procesafigura(cartastotales[palo0+palo1-1])
                    
                if (palo1 == 5) & (palo0 == 0):
                    maximofueracolor = max(procesafigura(cartastotales[6]),procesafigura(cartastotales[5]))
                elif (palo1 == 5) & (palo0 == 1):
                    maximofueracolor = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[6]))
                elif (palo1 == 5) & (palo0 == 2):
                    maximofueracolor = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))
                elif (palo1 == 6) & (palo0 == 0):
                    maximofueracolor = procesafigura(cartastotales[6])
                elif (palo1 == 6) & (palo0 == 1):
                    maximofueracolor = procesafigura(cartastotales[0])
                else:
                    maximofueracolor = procesafigura(cartastotales[2])
                
            elif (palo2 > 4):
                if procesafigura(cartastotales[palo0+palo1]) == 14:
                    maximocolor = 14
                else:
                    maximocolor = procesafigura(cartastotales[palo0+palo1+palo2-1])
                    
                if (palo2 == 5) & ((palo0+palo1) == 0):
                    maximofueracolor = max(procesafigura(cartastotales[6]),procesafigura(cartastotales[5]))
                elif (palo2 == 5) & ((palo0+palo1) == 1):
                    maximofueracolor = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[6]))
                elif (palo2 == 5) & ((palo0+palo1) == 2):
                    maximofueracolor = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))
                elif (palo2 == 6) & ((palo0+palo1) == 0):
                    maximofueracolor = procesafigura(cartastotales[6])
                elif (palo2 == 6) & ((palo0+palo1) == 1):
                    maximofueracolor = procesafigura(cartastotales[0])
                else:
                    maximofueracolor = procesafigura(cartastotales[2])
            else:
                if procesafigura(cartastotales[palo0+palo1+palo2]) == 14:
                    maximocolor = 14
                else:
                    maximocolor = procesafigura(cartastotales[palo0+palo1+palo2+palo3-1])
                    
                if (palo2 == 5) & ((palo0+palo1+palo2) == 0):
                    maximofueracolor = max(procesafigura(cartastotales[6]),procesafigura(cartastotales[5]))
                elif (palo2 == 5) & ((palo0+palo1+palo2) == 1):
                    maximofueracolor = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[6]))
                elif (palo2 == 5) & ((palo0+palo1+palo2) == 2):
                    maximofueracolor = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))
                elif (palo2 == 6) & ((palo0+palo1+palo2) == 0):
                    maximofueracolor = procesafigura(cartastotales[6])
                elif (palo2 == 6) & ((palo0+palo1+palo2) == 1):
                    maximofueracolor = procesafigura(cartastotales[0])
                else:
                    maximofueracolor = procesafigura(cartastotales[2])

            valjugada = (jugada*10000) + (maximocolor*100) + maximofueracolor
            
    # Comprobar si tenemos Escalera ----------------------------------------------------------------------------------------
    
    if (finbusqueda == 0) & (maxrelfig < 4):

        res1t = (cartasmidfig[1]-cartasmidfig[0])
        res2t = (cartasmidfig[2]-cartasmidfig[1])
        res3t = (cartasmidfig[3]-cartasmidfig[2])
        res4t = (cartasmidfig[4]-cartasmidfig[3])
        res5t = (cartasmidfig[5]-cartasmidfig[4])
        res6t = (cartasmidfig[6]-cartasmidfig[5])
        
        mejorcarta = 0
        mejorfuerajuego = 0

        # Comprobar una posible escalera
        if ((res1t+res2t+res3t+res4t)==4)|((res2t+res3t+res4t+res5t)==4)|((res3t+res4t+res5t+res6t)==4):

            # Comprobamos si es igual a 4 para saber si tenemos escalera normal
            # y comprobamos si es igual a 12 para saber si tenemos escalera con K y AS
            if (res3t == 1)&(res4t == 1)&(res5t == 1)&(res6t == 1):
                
                mejorcarta2 = cartastotales[6]
                    
                mejorfuerajuego = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))

                jugada = 5
                finbusqueda = 1

                mejorcarta2 = procesafigura(mejorcarta2)

                valjugada = (jugada*10000) + (mejorcarta2*100) + mejorfuerajuego

            elif (res3t == 1)&(res4t == 1)&(res5t == 1)&(res2t == 1):
               
                mejorcarta2 = cartastotales[5]
                    
                mejorfuerajuego = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))

                jugada = 5
                finbusqueda = 1

                mejorcarta2 = procesafigura(mejorcarta2)

                valjugada = (jugada*10000) + (mejorcarta2*100) + mejorfuerajuego
            
            elif (res1t == 1)&(res2t == 1)&(res3t == 1)&(res4t == 1):
                
                mejorcarta2 = cartastotales[4]
                
                mejorfuerajuego = max(procesafigura(cartastotales[0]),procesafigura(cartastotales[1]))

                jugada = 5
                finbusqueda = 1
                
                mejorcarta2 = procesafigura(mejorcarta2)

                valjugada = (jugada*10000) + (mejorcarta2*100) + mejorfuerajuego
            
    # Comprobar si tenemos Trio ----------------------------------------------------------------------------------------
    if (finbusqueda == 0) & (maxrelfig == 3):
        jugada = 4
        finbusqueda = 1
        
        valjugada = (jugada*10000) + (valortrio*100) + cartamaxima
        
    # Comprobar si tenemos Doble Pareja ----------------------------------------------------------------------------------------
    if (finbusqueda == 0) & (maxrelfig == 2) & (numparejas > 1):
        
        jugada = 3
        finbusqueda = 1
        valordobles = 0

        if (numparejas%2) == 1:
            valordobles = valorpareja1
        else:
            valordobles = valorpareja2
                
        valjugada = (jugada*10000) + (valordobles*100) + cartamaxima
                
    # Comprobar si tenemos Pareja ----------------------------------------------------------------------------------------
    if (finbusqueda == 0) & (maxrelfig == 2) & (numparejas == 1):
        
        jugada = 2
        finbusqueda = 1

        valjugada = (jugada*10000) + (valorpareja1*100) + cartamaxima

    # Asignar la carta mas alta en caso de no tener nada de lo anterior ------------------------------------------------------
    if finbusqueda == 0:

        valjugada = cartamaxima

    return valjugada

            
print "Cargado modulo estadisticas correctamente."

##profile.run("simulacion(100,100,2,1,2,[])")
##profile.run("tipojugada([43,12,32,4,8],1,2)")

