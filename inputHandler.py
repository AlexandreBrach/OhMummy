
import pygame

class InputHandler():

    def __init__(self):
        self.direction = []
        self.escape = []
        self.oldState = 0

    def calcDirection(self, keystate):
        newState = keystate[pygame.K_RIGHT] + ( keystate[pygame.K_UP] << 1 ) + ( keystate[pygame.K_LEFT] << 2 ) + ( keystate[pygame.K_DOWN] << 3 )
        newKeyPressed = newState & self.oldState
        self.oldState = newState
        if( newKeyPressed ):
            if newKeyPressed & 1:
                return [1,0,0,0]
            if newKeyPressed & 2:
                return [0,1,0,0]
            if newKeyPressed & 4:
                return [0,0,1,0]
            if newKeyPressed & 8:
                return [0,0,0,1]
        if( newState ):
            if newState & 1:
                return [1,0,0,0]
            if newState & 2:
                return [0,1,0,0]
            if newState & 4:
                return [0,0,1,0]
            if newState & 8:
                return [0,0,0,1]

    def handle(self):
        self.decreaseFps = False
        self.increaseFps = False
        self.nextLevel = False
        self.pressC = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.escape = True


        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_KP_MINUS] == 1:
            self.decreaseFps = True
        elif keystate[pygame.K_KP_PLUS] == 1:
            self.increaseFps = True
        elif keystate[pygame.K_KP_ENTER] == 1:
            self.nextLevel = True
        elif keystate[ord('c')] or keystate[ord('C')]:
            self.pressC = True

        self.direction = self.calcDirection( keystate )
        return
