# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time
from inputHandler import *
from pygame.locals import *

class SceneLoader():

    def __init__(self):
        self.clock = pygame.time.Clock()

    def setInputHandler(self, Input):
        self.input = Input
        
    def setScreen(self, screen):
        self.screen = screen

    # ------------------------------------------------
    # Lance la scene
    # Renvoie false si une interruption de programme est 
    # détecté : idéalement, le programme est arrêté
    # True dans tout les autres cas
    # ------------------------------------------------
    def run(self,Scene):
        Scene.stopEvent = False
        Scene.stopEventName = ''
        Scene.Start()
        Scene.prepareGraphics()

        fps = 16
        while Scene.stopEvent == False:
            self.input.handle()
            # Trigger de sortie
            if self.input.escape:
                return False
            # Altération FPS
            if self.input.increaseFps:
                fps=fps+1
            if self.input.decreaseFps:
                if fps>1 :
                    fps=fps-1
             
            # ------ BOUCLE DU JEU ------
            Scene.tick()
            Scene.draw( self.screen )
            self.clock.tick(fps)
        Scene.Stop()
        return True