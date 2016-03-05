# -*- coding: cp1252 -*-
import pygame
import random
import CatacombeScene
from movement import *

class Gargou():
    def __init__(self, scene ):
        self.scene = scene
        self.level = 1
        self.movement = Movement( scene, 15, 1, 0, 0 )

    def move(self, direction):
        try: direction = direction.index(1)
        except: return

        self.movement.facing = direction
        if self.movement.move( direction ) == True :
            return

        self.movement.moveIterate = (self.movement.moveIterate + 1) % 2
        
        if self.movement.entrave == False :                    
            if self.movement.facing == 0:
                self.scene.trace[self.movement.y][self.movement.x-1] = 1
                self.scene.trace[self.movement.y+1][self.movement.x-1] = 1
            elif self.movement.facing == 1:
                self.scene.trace[self.movement.y+2][self.movement.x] = 1
                self.scene.trace[self.movement.y+2][self.movement.x+1] = 1
            elif self.movement.facing == 2:
                self.scene.trace[self.movement.y][self.movement.x+2] = 1
                self.scene.trace[self.movement.y+1][self.movement.x+2] = 1            
            elif self.movement.facing == 3:
                self.scene.trace[self.movement.y-1][self.movement.x] = 1
                self.scene.trace[self.movement.y-1][self.movement.x+1] = 1
        
        # Passage de niveau ?
        if self.scene.Key and self.scene.RoyalMummy and self.movement.x == 15 and self.movement.y == 1:
            self.scene.terminate( 'UpLevel' )

class Mummy():
    def __init__(self, x, y, scene):
        self.scene = scene
        self.x = x
        self.y = y
        self.facing = 0
        self.moveIterate = 0
        self.movable = 0
        
    def move(self):
        self.movable = (self.movable + 1 ) % 3
        if self.movable == 0:        
            if self.scene.Gargou.level == 1: direct = random.randint(0, 3)
            elif self.scene.Gargou.level == 2: direct = random.choice([0, 1, 2, 3, self.facing, self.facing])
            elif self.scene.Gargou.level == 3: direct = random.choice(self.scene.getAvailableDirections( self.x, self.y ))
            elif self.scene.Gargou.level == 4:
                m = self.scene.getAvailableDirections( self.x, self.y )
                m.extend([self.facing, self.facing, self.facing])
                direct = random.choice(m)
            elif self.scene.Gargou.level == 5:
                m = []
                if self.x == self.scene.Gargou.x:
                    if self.y - self.scene.Gargou.y < 0: direct = 3
                    elif self.y - self.scene.Gargou.y > 0: direct = 1
                elif self.y == self.scene.Gargou.y:
                    if self.x - self.scene.Gargou.x < 0: direct = 0
                    elif self.x - self.scene.Gargou.x > 0: direct = 2
                else:
                    m = self.scene.getAvailableDirections( self.x, self.y )
                    m.extend([self.facing, self.facing, self.facing])
                    direct = random.choice(m)
            elif self.scene.Gargou.level >= 6:
                m = []
                if self.x - self.scene.Gargou.x < 0: m.append(0)
                elif self.x - self.scene.Gargou.x > 0: m.append(2)
                if self.y - self.scene.Gargou.y < 0: m.append(3)
                elif self.y - self.scene.Gargou.y > 0: m.append(1)
                direct = random.choice(m)

            self.facing = direct

            x = self.x; 
            y = self.y 
            if direct == 0: x = self.x + 1
            elif direct == 1: y = self.y - 1
            elif direct == 2: x = self.x - 1
            elif direct == 3: y = self.y + 1

            if self.scene.plate[y][x] == self.scene.plate[y][x+1] == self.scene.plate[y+1][x] == self.scene.plate[y+1][x+1] == 1:
                for mum in self.scene.Mummy:
                    if self != mum and abs(x-mum.x) <= 1 and abs(y -mum.y) <= 1:
                        return
                else:
                    self.x = x
                    self.y = y
            else: return
            self.moveIterate = (self.moveIterate + 1) % 2        

    def Restart(self, x, y):
        self.x = x
        self.y = y
        self.facing = 0
        self.moveIterate = 0
        self.movable = 0
    
class GuardianMummy():
    def __init__(self, scene, x, y):
        # x et y corresponde au num�ro de la bo�te sachant que 0<=x<=4 et 0<=y<=3
        self.iteration = 0
        
        ## D�finition de la position de naissance de la Momie        
        if scene.Gargou.movement.x < 3 + 7 * x: 
            self.x = 3 + 7 * x
        elif scene.Gargou.movement.x > 6 + 7 * x: 
            self.x = 6 + 7 * x
        else: 
            self.x = scene.Gargou.movement.x
        if scene.Gargou.movement.y < 5 + 5 * y: 
            self.y = 5 + 5 * y
        elif scene.Gargou.movement.y > 6 + 5 * y: 
            self.y = 6 + 5 * y
        else: 
            self.y = scene.Gargou.movement.y
        self.movable = 0 
        self.scene = scene

    def tick(self):
        self.movable = (self.movable + 1 ) % 6
