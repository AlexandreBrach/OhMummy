
import pygame
import pygame.image
from pygame.locals import *

class CatacombeView(pygame.sprite.Sprite):

    def __init__(self, screen, spriteSet, spriteAll ):
        SCREENRECT = Rect(0, 0, 768, 544)
        spritePlate = pygame.sprite.RenderUpdates()
        self.containers = spritePlate
        self.spritePlate = spritePlate
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.image = pygame.Surface((592, 384))
        background = pygame.Surface(SCREENRECT.size)
        self.background = background.convert()
        self.debugfont = pygame.font.Font( None, 16)
        self.spriteSet = spriteSet
        self.spriteAll = spriteAll

    def init(self, level, Life, Score, plate, debug, boxchoice ):
        '''
        initialization of the view
        '''
        l = str(level)

        self.background.fill((255,255,0))
        self.screen.blit( self.background, (0, 0))
        pygame.display.flip()

        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.left = 96
        self.rect.top = 94

        for i in range(1, 25):
            for j in range(1, 38):
                if plate[i][j] == 1:
                    self.image.blit(self.spriteSet['Trace']['None'], (16 * j - 16, 16 * i - 16))

        for i in range(4):
            for j in range(5):
                self.image.blit(self.spriteSet['Box']['NonTested'+l], (32 + 16 * 7 * j, 64 + 16 * 5 * i))
                if debug:
                    self.image.blit( self.debugfont.render( boxchoice[5*i+j], True, (255,255,255), (0,0,0) ), (32 + 16 * 7 * j, 64 + 16 * 5 * i))

        Life.render()
        Score.render()
        if debug:
            self.image.blit( self.debugfont.render( "Level " +str(level), True, (255,255,255), (0,0,0) ), (0,0))

    def remove( self, spriteContainer ):
        spriteContainer.sprite.kill()

    def render(self):
        '''
        scene rendering
        '''

        if( not( hasattr( self.Gargou, 'sprite' ) ) ):
             self.Gargou.sprite = GargouSprite( self.spriteAll,  self.spriteSet)
        for mum in self.Mummy:
            if( not( hasattr( mum, 'sprite' ) ) ):
                mum.sprite = MummySprite( self.spriteAll,  self.spriteSet)
        for guard in self.Guardian:
            if( not( hasattr( guard, 'sprite' ) ) ):
                guard.sprite = GuardianSprite( self.spriteAll,  self.spriteSet)

        self.Gargou.sprite.trace(self.Gargou.movement)
        if self.Gargou.movement.obstacle == False :
            self.addTrace( self.Gargou.movement )

        for mum in self.Mummy:
            mum.sprite.trace(mum.x, mum.y, mum.facing, mum.moveIterate)

        for guardian in self.Guardian:
            guardian.sprite.trace(guardian.x, guardian.y, guardian.iteration)

        pl = self.spritePlate.draw( self.screen )
        dirty = self.spriteAll.draw( self.screen )
        pygame.display.update(pl)
        pygame.display.update(dirty)

    def openBloc(self, box, x, y ):
        self.image.blit(self.spriteSet['Box'][box[y][x]], (32 + 112 * x, 64 + 80 * y))

    def eraseTrace(self, x, y):
        self.image.blit(self.spriteSet['Trace']['None'], (16 * x - 16, 16 * y - 16))
        self.image.blit(self.spriteSet['Trace']['None'], (16 * (x+1) - 16, 16 * y - 16))
        self.image.blit(self.spriteSet['Trace']['None'], (16 * x - 16, 16 * (y+1) - 16))
        self.image.blit(self.spriteSet['Trace']['None'], (16 * (x+1) - 16, 16 * (y+1) - 16))

    def addTrace(self, movement ):
        if movement.facing == 0:
            if movement.moveIterate == 0:
                self.image.blit(self.spriteSet['Trace']['DownRight'], (16 * movement.x - 32, 16 * movement.y - 16))
            else:
                self.image.blit(self.spriteSet['Trace']['UpRight'], (16 * movement.x - 32, 16 * movement.y - 16))

        elif movement.facing == 1:
            if movement.moveIterate == 0:
                self.image.blit(self.spriteSet['Trace']['LeftUp'], (16 * movement.x - 16, 16 * movement.y + 16))
            else:
                self.image.blit(self.spriteSet['Trace']['RightUp'], (16 * movement.x - 16, 16 * movement.y + 16))

        elif movement.facing == 2:
            if movement.moveIterate == 0:
                self.image.blit(self.spriteSet['Trace']['DownLeft'], (16 * movement.x + 16 , 16 * movement.y - 16))
            else:
                self.image.blit(self.spriteSet['Trace']['UpLeft'], (16 * movement.x + 16, 16 * movement.y - 16))

        elif movement.facing == 3:
            if movement.moveIterate == 0:
                self.image.blit(self.spriteSet['Trace']['LeftDown'], (16 * movement.x - 16, 16 * movement.y - 32))
            else:
                self.image.blit(self.spriteSet['Trace']['RightDown'], (16 * movement.x - 16 , 16 * movement.y - 32 ))

class GargouSprite(pygame.sprite.Sprite):

    def __init__(self,spriteAll, spriteSet ):
        self.containers = spriteAll
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spriteSet = spriteSet
        self.image = self.spriteSet['Gargou']['MoveDownRight']
        self.rect = self.image.get_rect()
        self.rect.left = 320
        self.rect.top = 94

    def trace(self, movement):
        self.image = self.spriteSet['Gargou']['Face'][2 * movement.facing + movement.moveIterate]
        self.rect.left = 80 + 16 * movement.x
        self.rect.top = 78 + 16 * movement.y

class MummySprite(pygame.sprite.Sprite):

    def __init__(self,spriteAll, spriteSet):
        self.containers = spriteAll
        self.spriteSet = spriteSet
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.spriteSet['Mummy']['MoveRight']
        self.rect = self.image.get_rect()

    def trace(self, x,y, facing, moveIterate):
        self.image = self.spriteSet['Mummy']['Face'][2 * facing + moveIterate]
        self.rect.left = 80 + 16 * x
        self.rect.top = 78 + 16 * y

class GuardianSprite(pygame.sprite.Sprite):

    def __init__(self,spriteAll, spriteSet):
        self.containers = spriteAll
        self.spriteSet = spriteSet
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.spriteSet['Mummy']['MoveRight']
        self.rect = self.image.get_rect()

    def trace(self, x,y, moveIterate):

        self.image = self.spriteSet['GuardianMummy'][moveIterate+1]
        self.rect = self.image.get_rect()
        self.rect.top = 110 + 16 * y - 2 * moveIterate
        self.rect.left = 80 + 16 * x
