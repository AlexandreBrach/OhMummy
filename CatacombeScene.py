# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time

# Direction algorithme
from DirectionAlgo import *

from movers import Gargou,Mummy,GuardianMummy

from Views import *

class CatacombeScene():

    def __init__(self, view, life, clock, input, score ):
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
        self.Mummy = []
        self.guardianMummy = []
        self.Gargou = Gargou( self )
        self.Gargou.level = 1
        self.view.Mummy = self.Mummy
        self.view.Guardian = self.guardianMummy
        self.view.Gargou = self.Gargou

        # Algorithme orederer with level
        self.directionAlgo = [
            BlindDirection(),
            SillyDirection(),
            TargetRandomPathDirection(),
            SceneAwareDirection(),
            SceneAwareFacingDirection(),
            TargetDirection()
        ];
        
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
        self.Mummy.append(Mummy(1, 23, self, self.directionAlgo[self.Gargou.level-1] ))
        # Réinitialisation emplacement momies
        i = 1
        for mum in self.Mummy:
            mum.Restart(1 + 2 * i, 23)
            i += 1

    def prepareGraphics(self):
        self.view.init( self.level, self.Life, self.score, self.plate, self.debug, self.boxchoice)

    #-------------------------------------
    # DELTA T
    #-------------------------------------
    def tick(self):

        if self.input.nextLevel :
            self.terminate( 'UpLevel' )

        # Joueur
        self.Gargou.move(self.input.direction)

        # Si il y a eu mouvement (non entravé)
        if self.Gargou.movement.entrave == False :                    
            # Ouverture de blocs ?
            if self.Gargou.movement.y>2:
                xx1 = min(4, max(0, (self.Gargou.movement.x - 3) // 7))
                yy1 = min(3, max(0, (self.Gargou.movement.y - 5) // 5))
                xx2 = min(4, (self.Gargou.movement.x - 1 )// 7)
                yy2 = min(3, (self.Gargou.movement.y - 3) // 5)
                # 4 possibilités
                if self.box[yy1][xx1] == 'NonTested': 
                    self.UpdateClose(xx1, yy1)
                if self.box[yy1][xx2] == 'NonTested': 
                    self.UpdateClose(xx2, yy1)
                if self.box[yy2][xx1] == 'NonTested': 
                    self.UpdateClose(xx1, yy2)
                if self.box[yy2][xx2] == 'NonTested': 
                    self.UpdateClose(xx2, yy2)

        # Momies "gardiennes"
        for guardian in self.guardianMummy:
            guardian.tick()
            if guardian.movable == 0:
                guardian.iteration += 1
                
                if guardian.iteration == 16:
                    self.Mummy.append(Mummy(guardian.x, guardian.y, self, self.directionAlgo[self.Gargou.level-1] ))
                    self.plate[guardian.y][guardian.x] = 1
                    self.plate[guardian.y+1][guardian.x] = 1
                    self.plate[guardian.y][guardian.x+1] = 1
                    self.plate[guardian.y+1][guardian.x+1] = 1
                    self.view.eraseTrace( guardian.x, guardian.y )
                    self.guardianMummy.remove(guardian)
                    self.view.remove(guardian)

        # Pour chaque momie
        for mum in self.Mummy:    
            mum.move()

            # Collision Momie/Joueur ?
            if abs(mum.x - self.Gargou.movement.x) <= 1 and abs(mum.y - self.Gargou.movement.y) <= 1:
                # Incidence uniquement si le joueur ne détient pas le parchemin
                if not self.Scroll:
                    # Perte d'une vie
                    self.Life.life -= 1
                    self.Life.render()
                    if self.Life.life == 0:
                        self.terminate( 'GameOver' )
                # Le joueur a un parchemin
                else:
                    # Perte du parchemin
                    self.Scroll = False
                    # Mise à jour du score
                    self.score.render()
                # La momie est "bouffée" par le joueur
                # mum.sprite.kill()
                self.Mummy.remove(mum)
                self.view.remove(mum)

    def preDispatch(self):
        
        if self.stopEventName == 'UpLevel' :
            self.level = max(1, (self.level + 1) % 6)
            # Tout les 6 niveau, self.Level revient à 1
            if self.level == 1:
                self.Gargou.level += 1               
                for mum in self.Mummy: 
                    self.Mummy.remove(mum)
                    self.view.remove(mum)
                MUMMY = []                
        elif self.stopEventName == 'GameOver' :
            return

    def Stop(self):
        self.preDispatch()
        for guardian in self.guardianMummy: 
            self.guardianMummy.remove(guardian)
            self.view.remove(guardian)
        
    def draw(self):
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

    def terminate(self, code ):
        self.stopEventName = code
        self.stopEvent = True
