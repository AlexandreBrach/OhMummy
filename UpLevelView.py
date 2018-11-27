
import pygame
import pygame.image
from pygame.locals import *

class UpLevelView():

    def __init__(self, screen, sprites):
        SCREENRECT = Rect(0, 0, 768, 544)
        self.spriteSet = sprites
        self.screen = screen
        background = pygame.Surface(SCREENRECT.size)
        self.background = background.convert()

    def init(self):
        if self.bonus == 'Life+1':
            self.background.blit(self.spriteSet['EndLife'], (0, 0))
        else:
            self.background.blit(self.spriteSet['End200'], (0, 0))
        self.screen.blit( self.background, (0, 0))
        pygame.display.flip()

    def draw(self):
        return
