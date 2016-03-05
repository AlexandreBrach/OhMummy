# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time

from movers import Gargou,Mummy,GuardianMummy

from Views import *

class CatacombeScene():

    def __init__(self, sprites, life, clock, input, score, view ):
        self.spriteSet = sprites
        self.Life = life
        self.debug = True
        self.level = 1
        self.clock = clock
        self.input = input
        self.plate = []
        self.score = score
        self.view = view

    #-------------------------------------
    # Construction de la scene
    #-------------------------------------
    def Initialize(self):
        self.createGargou()
        self.createGuardianMummy() 
        self.createMummy()
        
    #-------------------------------------
    # Démarage de la scène
    #-------------------------------------
    def Start(self ):
        
        # Remplissage d'un tableau 39*26 avec des 0 ?
        self.plate = [39 * [0] for i in range(26)]
        self.trace = [39 * [0] for i in range(26)]
        # remplissage d'un tableau de 5*4 avec des 'NonTested' 
        self.box = [5 * ['NonTested'] for i in range(4)]
        l = str(self.level)
        # Permutation des blocs
        self.boxchoice = ['Treasure', 'Treasure', 'Treasure', 'Treasure', 'Treasure', 'Treasure', 'Treasure', 'Treasure', 'Treasure', 'Treasure',
                           'GuardianMummy'+l, 'Key', 'RoyalMummy', 'Scroll', 'Empty'+l, 'Empty'+l, 'Empty'+l, 'Empty'+l, 'Empty'+l, 'Empty'+l]
        random.shuffle(self.boxchoice)
        # Réinitialiation des variables de la scène
        self.Key = False
        self.Scroll = False
        self.RoyalMummy = False
        # Remlpissage des couloir de 1
        for i in range(3, 24, 5):
            for j in range(1, 38):
                self.plate[i][j] = 1
                self.plate[i+1][j] = 1
        for j in range(1, 37, 7):
            for i in range(3, 25):
                self.plate[i][j] = 1
                self.plate[i][j+1] = 1
        # ??
        self.plate[1][15] = 1
        self.plate[1][16] = 1
        self.plate[2][15] = 1
        self.plate[2][16] = 1
        # Ajout d'une momie supplémetaire
        self.Mummy.append(Mummy(1, 23, self, self.view))        
        # Réinitialisation emplacement momies
        i = 1
        for mum in self.Mummy:
            mum.Restart(1 + 2 * i, 23)
            i += 1

    def prepareGraphics(self):
        self.view.init( self.level, self.Life, self.score, self.plate, self.debug, self.boxchoice )

    #-------------------------------------
    # DELTA T
    #-------------------------------------
    def tick(self):

        if self.input.nextLevel :
            self.terminate( 'UpLevel' )

        # Joueur
        self.Gargou.tick()
        self.Gargou.move(self.input.direction)

        # Momies "gardiennes"
        for guardian in self.guardianMummy:
            guardian.tick()

        # Pour chaque momie
        for mum in self.Mummy:    
            mum.move()
            mum.tick()

    def preDispatch(self):
        
        if self.stopEventName == 'UpLevel' :
            self.level = max(1, (self.level + 1) % 6)
            # Tout les 6 niveau, self.Level revient à 1
            if self.level == 1:
                self.Gargou.level += 1               
                for mum in self.Mummy: mum.kill()
                MUMMY = []                
        elif self.stopEventName == 'GameOver' :
            return

    def Stop(self):
        self.preDispatch()
        for mum in self.guardianMummy: mum.kill()
        self.guardianMummy = []
        
    def draw(self,screen):
        self.view.render()

    #-------------------------------------
    # Détermine les direction possible selon
    # les coordonnées passées en paramètre
    #-------------------------------------    
    def getAvailableDirections(self, x, y ):
        res = []
        if self.plate[y][x+2] == 1 and self.plate[y+1][x+2] == 1: res.append(0)
        if self.plate[y-1][x] == 1 and self.plate[y-1][x+1] == 1: res.append(1)
        if self.plate[y][x-1] == 1 and self.plate[y+1][x-1] == 1: res.append(2)
        if self.plate[y+2][x] == 1 and self.plate[y+2][x+1] == 1: res.append(3)
        return res
    
    #-----------------------------------------------------------------------------------
    # Teste s'il est possible de se déplacer dans la direction <direction>
    # avec les coordonnées passées en paramètre
    # Renvoie un tableau contenant le boolean de réponse, et les nouvelles coordonnées
    #-----------------------------------------------------------------------------------
    def testMovement( self, oldX, oldY, direction ):
        x = oldX 
        y = oldY 
    
        if direction == 0: x = oldX + 1
        elif direction == 1: y = oldY - 1
        elif direction == 2: x = oldX - 1
        elif direction == 3: y = oldY + 1

        # Mouvement possible ?
        if self.plate[y][x] == self.plate[y][x+1] == self.plate[y+1][x] == self.plate[y+1][x+1] == 1:
            return ( True, x,y )
        else: 
            return ( False, oldX, oldY )

    #----------------------------------------------
    # Vérifie si le bloc présent en x,y doit être ouvert
    #----------------------------------------------
    def UpdateClose(self, x, y ):
        for i in range(3 + 5 * y, 10 + 5 * y):
            for j in range(1 + 7 * x, 10 + 7 * x):
                if self.plate[i][j] == 1 and self.trace[i][j] == 0: return False
        self.box[y][x] = self.boxchoice[5 * y + x]
        self.view.openBloc( self.box, x, y )
        #self.image.blit(self.spriteSet['Box'][self.box[y][x]], (32 + 112 * x, 64 + 80 * y))
        if self.box[y][x] == 'Treasure': self.score.score += 5
        elif self.box[y][x] == "RoyalMummy":
            self.score.score +=50
            self.RoyalMummy = True
        elif self.box[y][x] == "Scroll":
            self.Scroll = True
            self.score.render()
        elif self.box[y][x] == "Key":
            self.Key = True
        elif self.box[y][x] == "GuardianMummy"+str(self.level):
            self.guardianMummy.append(GuardianMummy(self, x, y ))
        self.score.render()

    def createGargou(self):
        self.Gargou = Gargou( self, self.view )
        self.Gargou.level = 1

    def createGuardianMummy(self):
        self.guardianMummy = []

    def createMummy(self):
        self.Mummy = []

    def terminate(self, code ):
        self.stopEventName = code
        self.stopEvent = True
