# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time

class UpLevelScene():

    def __init__(self, screen, sprites, input, clock, background, score, Life ):
        self.spriteSet = sprites
        self.input = input
        self.clock = clock
        self.background = background
        self.score = score
        self.Life = Life
        self.screen = screen

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
        return

    def prepareGraphics(self):
        if self.bonus == 'Life+1':
            self.background.blit(self.spriteSet['EndLife'], (0, 0))
        else:
            self.background.blit(self.spriteSet['End200'], (0, 0))
        self.screen.blit( self.background, (0, 0))
        pygame.display.flip()

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
        
    def draw(self,screen):
        return
    
    def terminate(self, code ):
        self.stopEventName = code
        self.stopEvent = True
