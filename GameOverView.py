# -*- coding: cp1252 -*-
import pygame
import pygame.image
from pygame.locals import *

class GameOverView():

    def __init__(self, screen, sprites): 
        SCREENRECT = Rect(0, 0, 768, 544)
        self.spriteSet = sprites
        self.screen = screen
        background = pygame.Surface(SCREENRECT.size)
        self.background = background.convert()

    def init(self):
        self.screen.blit(self.spriteSet['GameOver'], (208, 238))
        pygame.display.flip()

    def draw(self):
        return
