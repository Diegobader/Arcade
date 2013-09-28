import pygame

class Gorila:
    
    def __init__(self, posIni, gorilaSurface, windowSurface):
        self.gorilaSurface=gorilaSurface
        self.x_imagen=gorilaSurface.get_width()/2
        self.y_imagen=gorilaSurface.get_height()/2
        self.windowSurface=windowSurface
        
        self.x = posIni[0]
        self.y = posIni[1] - gorilaSurface.get_height()/2 -1
        
    def blit(self):
        self.windowSurface.blit(self.gorilaSurface, (self.x-self.x_imagen, self.y-self.y_imagen))