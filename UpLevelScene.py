# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time

class UpLevelScene():

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
    def Start(self):
        if random.randint(0, 1) == 0 and self.Life.life < 9:
            self.bonus = 'Life+1'
        else:
            self.bonus = 'Score+200'
            
        if self.bonus == 'Life+1':
            self.Life.life += 1
        else:
            self.score.score += 200

        self.view.bonus = self.bonus
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
