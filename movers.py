
import pygame
import random
from movement import *

class Gargou():
    def __init__(self, scene ):
        self.scene = scene
        self.level = 1
        self.movement = Movement( scene, 15, 1, 0, 0 )

    def move(self, direction):
        try:
            direction = direction.index(1)
        except: return

        self.movement.facing = direction
        if self.movement.move( direction ) == True :
            return

        self.movement.moveIterate = (self.movement.moveIterate + 1) % 2

        if self.movement.obstacle == False :
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

        # Next Level ?
        if self.scene.Key and self.scene.RoyalMummy and self.movement.x == 15 and self.movement.y == 1:
            self.scene.terminate( 'UpLevel' )

class Mummy():
    def __init__(self, x, y, scene, directionAlgo):
        self.scene = scene
        self.x = x
        self.y = y
        self.facing = 0
        self.moveIterate = 0
        self.movable = 0
        self.directionAlgo = directionAlgo

    def tick(self):
        self.movable = (self.movable + 1 ) % 3
        if self.movable == 0:
            direct = self.directionAlgo.getDirection( self.scene, self.x, self.y, self.facing, self.scene.Gargou.movement.x, self.scene.Gargou.movement.y )

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
        # x et y : position of the bloc hosting the guardian
        self.iteration = 0

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
        if self.movable == 0:
            self.iteration += 1
