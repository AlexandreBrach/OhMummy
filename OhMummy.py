# -*- coding: cp1252 -*-
import pygame
import pygame.image
import random
import time
from inputHandler import *
from sceneLoader import *

from pygame.locals import *
from sceneLoader import SceneLoader
pygame.init()
pygame.font.init()

# Importation des images sous la forme de variable globale "ImageOhMummy" (tableau)
from spriteInit import MummySprites

# Importation des concepts du jeu (score, vie, etc)
from gameConcepts import *

# Importation des scenes
from CatacombeScene import CatacombeScene
from UpLevelScene import UpLevelScene
from GameOverScene import GameOverScene

# Importations des éléments mobiles du jeu
from movers import Gargou,Mummy,GuardianMummy

from Views import *

# Initialisation

__version__ = (1, 0, 0)
__build__ = (0, 1)
__date__ = (2007, 4, 5)
__author__ = ('Guillaume', 'Duriaud')

def main():

    # Initialisation de l'application
    random.seed()   
    screen = pygame.display.set_mode((768, 544))
    pygame.display.set_caption("Oh Mummy")
    clock = pygame.time.Clock()
    
    spriteAll = pygame.sprite.RenderUpdates()
    spriteEndgame = pygame.sprite.RenderUpdates()
    
    #CatacombeScene.containers = spritePlate
    Score.containers = spriteAll
    #Gargou.containers = spriteAll
    Life.containers = spriteAll
    #Mummy.containers = spriteAll
    GuardianMummy.containers = spriteAll

    # Instantiation des élements du jeu
    
    global GameScene
    global NextLevelScene
    global SCORE
    global LIFE
    global Input
    global sceneView
    
    spriteLoader = MummySprites()
    ImageOhMummy = spriteLoader.getSprites()
    
    LIFE = Life( ImageOhMummy )
    Input = InputHandler()
    SCORE = Score( ImageOhMummy )
    
    GameScene = CatacombeScene( screen, ImageOhMummy, spriteAll,LIFE, clock, Input, SCORE )
    # NextLevelScene = UpLevelScene( screen, ImageOhMummy, Input, clock, background, SCORE, LIFE )
    # myGameOverScene = GameOverScene( screen, ImageOhMummy, Input, clock, background, SCORE, LIFE )
    SCORE.setScene( GameScene )
    
    # Le jeu proprement dit
    GameScene.Initialize()
    # NextLevelScene.Initialize()
    # myGameOverScene.Initialize()

    sLoader = SceneLoader() 
    sLoader.setInputHandler( Input )
    sLoader.setScreen( screen )
    goon = True
    while goon :
        runResult = sLoader.run( GameScene ) 
        if runResult == False :
            goon = False
        if GameScene.stopEventName == 'GameOver' :
            sLoader.run( myGameOverScene )
            goon = False
        elif GameScene.stopEventName == 'UpLevel' :
            if GameScene.level == 1 :
                runResult = sLoader.run( NextLevelScene ) 
                if runResult == False :
                    goon = False

main()
