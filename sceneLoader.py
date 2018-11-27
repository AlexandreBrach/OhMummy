
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

    def run(self,Scene):
        '''
        run the scene
        '''
        Scene.stopEvent = False
        Scene.stopEventName = ''
        Scene.Start()
        Scene.prepareGraphics()

        fps = 16
        while Scene.stopEvent == False:
            self.input.handle()
            if self.input.escape:
                return False
            if self.input.increaseFps:
                fps=fps+1
            if self.input.decreaseFps:
                if fps>1 :
                    fps=fps-1

            Scene.tick()
            Scene.draw()
            self.clock.tick(fps)
        Scene.Stop()
        return True
