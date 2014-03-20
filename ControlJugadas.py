# -*- coding: cp1252 -*-
import win32api, win32con, os, ctypes, PIL.ImageGrab, PIL.ImageOps
import PIL.ImageTk, PIL.Image, PIL.ImageMath


#Click izquierdo automatico en la posicion indicada
def click_izq(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#Click derecho automatico en la posicion indicada
def click_der(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

#Retorna en forma de array la posicion actual del cursor
def posicion_actual():
    return win32api.GetCursorPos()

#Metodo que permite ejecutar comandos del sistema
def ejecutar(prog):
    os.system(prog)

#Metodo que simula la ejecucion de una combinacion de teclas
def maximizar():
    win32api.keybd_event(win32con.VK_MENU,0,0,0)
    win32api.keybd_event(win32con.VK_MENU,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(32,0,0,0)
    win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(88,0,0,0)
    win32api.keybd_event(88,0,win32con.KEYEVENTF_KEYUP,0)

#Metodo que permite cambiar de pestaña
def cambioventana():
    win32api.keybd_event(win32con.VK_MENU,0,0,0)
    win32api.keybd_event(win32con.VK_TAB,0,0,0)
    win32api.keybd_event(win32con.VK_TAB,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(win32con.VK_MENU,0,win32con.KEYEVENTF_KEYUP,0)

#Metodo que obtiene la resolucion de pantalla
def resolucion():
    i = 0
    while i < 100:
        try:
            mondata = win32api.GetMonitorInfo(i)
            i = 100
        except:
            #print "Controlador %d no es el controlador de pantalla" %i
            hola = 1

        i = i + 1

    res_x = mondata["Monitor"][2]
    res_y= mondata["Monitor"][3]
    restrabajo_x = mondata["Work"][2]
    restrabajo_y = mondata["Work"][3]

    resolucion = [res_x, res_y]
    restrabajo = [restrabajo_x, restrabajo_y]

    return resolucion, restrabajo

#Metodo que captura la pantalla
def captura():
    im = PIL.ImageGrab.grab()
    im.save("captura.jpg")
    return im

#Metodo que recorta un rectangulo de las dimensiones espacificadas
# empezando en dicha coordenada
def recorta(alto,ancho,x,y,modo,imagenorigin,imagenfin):
    res,rest = resolucion()
    limitexinf = 0
    limiteyinf = 0
    limitexsup = res[0]
    limiteysup = res[1]
    if (alto>limitexinf) & (ancho>limiteyinf) & ((x+ancho)<limitexsup) & ((y+alto)<limiteysup):
        if modo == 0:
            im = PIL.Image.open(imagenorigin)
        else:
            im = captura()
        cortesup = x
        corteizq = y
        corteinf = x+ancho
        corteder = y+alto
        #print cortesup,corteizq,corteder,corteinf
        improc = im.crop((cortesup,corteizq,corteinf,corteder))
        improc.save(imagenfin)
        return improc

#Metodo que abre una imagen de fichero
def abririmagen(imagen):
    im = PIL.Image.open(imagen)
    return im

#Metodo que retorna el valor en RGB de un determinado pixel
def valorpixel(imagen,x,y):
    improc = imagen.getpixel((x,y))
    return improc

print "Cargado modulo control de jugadas correctamente."


