# -*- coding: cp1252 -*-
import random

class BlindDirection():

    def getDirection( self, scene, x, y, facing, xTarget, yTarget ):
        return random.randint(0, 3)

class SceneAwareDirection():

    def getDirection( self, scene, x, y, facing, xTarget, yTarget ):
        return random.choice( scene.getAvailableDirections( x, y ) )

class SceneAwareFacingDirection():

    def getDirection( self, scene, x, y, facing, xTarget, yTarget ):
        m = scene.getAvailableDirections( x, y )
        m.extend([facing, facing, facing])
        return random.choice(m)

class SillyDirection():

    def getDirection( self, scene, x, y, facing, xTarget, yTarget ):
        return random.choice([0, 1, 2, 3, facing, facing])

class TargetDirection():

    def getDirection( self, scene, x, y, facing, xTarget, yTarget ):
        m = []
        if x - xTarget < 0: 
            m.append(0)
        elif x - xTarget > 0: 
            m.append(2)
        if y - yTarget < 0: 
            m.append(3)
        elif y - yTarget > 0: 
            m.append(1)
        direct = random.choice(m)
        return direct

class TargetRandomPathDirection():

    def getDirection( self, scene, x, y, facing, xTarget, yTarget ):
        m = []
        if x == xTarget:
            if y - yTarget < 0: 
                direct = 3
            elif y - yTarget > 0: 
                direct = 1
        elif y == yTarget:
            if x - xTarget < 0: 
                direct = 0
            elif x - xTarget > 0: 
                direct = 2
        else:
            m = scene.getAvailableDirections( x, y )
            m.extend([facing, facing, facing])
            direct = random.choice(m)
        return direct
