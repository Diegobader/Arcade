import pygame
import math
import sys

#from Main import SCREEN_HEIGHT
#???

class Banana:
    
    def __init__(self, gorilas, indexGorilaIni, angle, power,
                 bananaSurface, windowSurface):
        self.gorilas=gorilas
        self.bananaSurface=bananaSurface
        self.x_imagen=bananaSurface.get_width()/2
        self.y_imagen=bananaSurface.get_height()/2
        self.windowSurface=windowSurface
        
        if indexGorilaIni==1:
            angle=180-angle
        self.x=gorilas[indexGorilaIni].x
        self.y=gorilas[indexGorilaIni].y - 40
        self.vx =  power * math.cos(math.radians(angle))
        self.vy = -power * math.sin(math.radians(angle))
        
    def frame(self):
        self.vy+=0.3   # gravedad
        # TODO: viento    self.vx+= ...
        
        self.x+=self.vx
        self.y+=self.vy
        
        #if self.y>SCREEN_HEIGHT:
        if self.y>600:
            return True # siguiente lanzamiento
        
        if get_dist(self,self.gorilas[0])<32 or get_dist(self,self.gorilas[1])<32:
            print("BUM!!!")
            pygame.quit()
            sys.exit()
        
        self.windowSurface.blit(self.bananaSurface, (self.x-self.x_imagen,self.y-self.y_imagen))
        
def get_dist(a,b):
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)