# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time

class GameOverScene():

    def __init__(self, view, input, clock, score, Life ):
        self.input = input
        self.clock = clock
        self.score = score
        self.Life = Life
        self.view = view

    #-------------------------------------
    # Construction de la scene
    #-------------------------------------
    def Initialize(self):
        return
    
    #-------------------------------------
    # Démarrage de la scène
    #-------------------------------------
    def Start(self ):
        return

    def prepareGraphics(self):
        self.view.init()

    #-------------------------------------
    # DELTA T
    #-------------------------------------
    def tick(self):
        if self.input.pressC :
            self.terminate( 'CPressed' )
        self.clock.tick(10)

    def preDispatch(self):
        return

    def Stop(self):
        self.preDispatch()
        
    def draw(self):
        return
    
    def terminate(self, code ):
        self.stopEventName = code
        self.stopEvent = True
