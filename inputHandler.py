# -*- coding: cp1252 -*-
import pygame

class InputHandler():

    def __init__(self):
        self.direction = []
        self.escape = []
    
    def handle(self):
        self.decreaseFps = False
        self.increaseFps = False
        self.nextLevel = False
        self.pressC = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                self.escape = True
        

        # Détection évenement clavier
        keystate = pygame.key.get_pressed()
        
        # FPS
        if keystate[pygame.K_KP_MINUS] == 1:
            self.decreaseFps = True
        elif keystate[pygame.K_KP_PLUS] == 1:
            self.increaseFps = True
        elif keystate[pygame.K_KP_ENTER] == 1:
            self.nextLevel = True
        elif keystate[ord('c')] or keystate[ord('C')]:
            self.pressC = True

        # Direction
        self.direction = [keystate[pygame.K_RIGHT], keystate[pygame.K_UP], keystate[pygame.K_LEFT], keystate[pygame.K_DOWN]]
        return