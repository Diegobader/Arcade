# -*- coding: utf8 -*-

# Gorillas, python edition
# (copia de Gorillas, tarea 1 de IIC1103, 2012-1, secci�n 1)

import sys
import pygame
from pygame.locals import *
from random import randint
from Tools import *
from Gorila import *
from Banana import *

# constantes
SCREEN_WIDTH    = 800
SCREEN_HEIGHT   = 600

# variables globales
windowSurface=None
font=None
blackColor=None

def write(texto):
    msgSurface=font.render(texto, False, blackColor)
    msgRect=msgSurface.get_rect(center=(SCREEN_WIDTH/2, 20))
    windowSurface.blit(msgSurface, msgRect)
    
    

def main():
    pygame.init()
    fpsClock=pygame.time.Clock()

    global windowSurface
    windowSurface=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    pygame.display.set_caption("Gorillas, python edition")
    
    global font,blackColor
    font=pygame.font.SysFont("Verdana", 16)
    blackColor=pygame.Color(0,0,0)

    fill_gradient(windowSurface, pygame.Color(47,83,123), pygame.Color(118,169,212))
    posIniGorilas=crearEdificios()
    fondoSurface=windowSurface.copy()
    
    gorilaSurface=pygame.image.load("img/gorilla.png")
    bananaSurface=pygame.image.load("img/banana.png")
    
    gorilas=[]
    gorilas.append( Gorila(posIniGorilas[0], gorilaSurface, windowSurface) )
    gorilas.append( Gorila(posIniGorilas[1], gorilaSurface, windowSurface) )

    angle=0
    power=0
    banana=None
    
    n_jugador=0
    esperaInput=True
    texto="Pulse [ENTER] para que el jugador 1 lance"
    
    # loop principal
    while True:
        windowSurface.blit(fondoSurface,(0,0))  # borrar todo
        
        write(texto)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type==KEYDOWN:
                if event.key==K_RETURN and esperaInput:
                    esperaInput=False
                    texto=""
                    
                    windowSurface.blit(fondoSurface,(0,0))  # borrar todo
                    pygame.display.update()
                    
                    # TODO: pedir datos con alguna interfaz gráfica
                    
                    # block
                    angle=int(raw_input("Angle >"))
                    power=int(raw_input("Power >"))
                    
                    banana=Banana(gorilas, n_jugador, angle, power,
                                  bananaSurface, windowSurface)
                    
        gorilas[0].blit()
        gorilas[1].blit()
        
        if not esperaInput:
            r=banana.frame()
            if r:
                del banana
                esperaInput=True
                n_jugador+=1
                if n_jugador==2:
                    n_jugador=0
                texto="Pulse [ENTER] para que el jugador " + str(n_jugador+1) + " lance"
                print("")

        pygame.display.update()
        fpsClock.tick(30)



def crearEdificios():
    COLORES_EDIFICIO=[
        pygame.Color(168, 0 , 0 ),
        pygame.Color( 0 ,168,168),
        pygame.Color(168,168,168) ]
    
    COLOR_VENTANA_ENCENDIDA = pygame.Color(252,252, 84)
    COLOR_VENTANA_APAGADA   = pygame.Color( 75, 75, 75)
    
    # int[,] posIniGorilas=new int[2,2];
    posIniGorilas=[]
    posIniGorilas.append([])
    posIniGorilas.append([])
    posIniGorilas[0]=[] # gorila1: x,y
    posIniGorilas[0].append(None)
    posIniGorilas[0].append(None)
    posIniGorilas[1]=[] # gorila2: x,y
    posIniGorilas[1].append(None)
    posIniGorilas[1].append(None)
    
    n_edificio=0
    
    x_1antes=0
    x_2antes=0
    y_1antes=0
    y_2antes=0

    x=4     # 4 pixeles sin edificio
    while x<SCREEN_WIDTH:
        ventanasAncho=randint(3,4)
        ventanasAlto =randint(3,10)
        altura= 8 + ventanasAlto*(18+16)-16 +8
        color=COLORES_EDIFICIO[ randint(0,len(COLORES_EDIFICIO)-1) ]
        # para 3 ventanas:
        # ....____________............____________............____________....
        #   4      12          12          12          12          12       4
        ancho= 4*2 + (ventanasAncho*2 -1)*12
        pygame.draw.rect(windowSurface, color, (x, SCREEN_HEIGHT-altura, ancho, altura))
        
        if n_edificio==1:
            posIniGorilas[0][0] = x + ancho/2
            posIniGorilas[0][1] = SCREEN_HEIGHT-altura
        else:
            x_2antes=x_1antes
            x_1antes = x + ancho/2
            y_2antes=y_1antes
            y_1antes = SCREEN_HEIGHT-altura

        # ventanas hacia abajo
        # ........__________________................___ _  _   _    (visto en vertical)
        #    8            18               16          ...
        for i in range(ventanasAncho):
            for j in range(SCREEN_HEIGHT-altura+8, SCREEN_HEIGHT, 18+16):

                if randint(1,100)>30:
                    color=COLOR_VENTANA_ENCENDIDA
                else:
                    color=COLOR_VENTANA_APAGADA

                pygame.draw.rect(windowSurface, color, (x+4 + i*(12+12), j, 12, 18))

        x += ancho+4
        n_edificio+=1

    posIniGorilas[1][0]=x_2antes
    posIniGorilas[1][1]=y_2antes
    return posIniGorilas




main()
