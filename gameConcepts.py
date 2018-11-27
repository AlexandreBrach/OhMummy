
import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self,sprites):
        self.sprites = sprites
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.score = 0
        self.image = pygame.Surface((176, 16))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.top = 78
        self.rect.left = 96
        self.image.blit(self.sprites['Score'], (0, 0))
        for i in range(5):
            self.image.blit(self.sprites['Chiffre'][0], (96 + 16* i, 0))

    def setScene(self, scene):
        self.scene = scene

    def render(self):
        scorestr = str(self.score).zfill(5)
        b = 0
        for i in scorestr:
            if self.scene.Scroll: self.image.blit(self.sprites['ChiffreScroll'][int(i)], (96+16 * b, 0))
            else: self.image.blit(self.sprites['Chiffre'][int(i)], (96+16 * b, 0))
            b += 1


class Life(pygame.sprite.Sprite):
    def __init__(self, sprites):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.sprites = sprites
        self.life = 5
        self.image = pygame.Surface((320, 32))
        self.rect = self.image.get_rect()
        self.rect.top = 78
        self.rect.left = 416

    def render(self):
        self.image.fill((255, 255, 0))
        self.image.blit(self.sprites['Men'], (0, 0))
        for i in range(0, self.life, 2):
            self.image.blit(self.sprites['Gargou']['MoveRight'], (64 + 32* i, 0))
        for i in range(1, self.life, 2):
            self.image.blit(self.sprites['Gargou']['Right'], (64 + 32* i, 0))
