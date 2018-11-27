
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

from spriteInit import MummySprites

from gameConcepts import *

from CatacombeScene import CatacombeScene
from UpLevelScene import UpLevelScene
from GameOverScene import GameOverScene

from movers import Gargou,Mummy,GuardianMummy

from CatacombeView import *
from UpLevelView import *
from GameOverView import *

__version__ = (1, 0, 0)
__build__ = (0, 1)
__date__ = (2007, 4, 5)
__author__ = ('Guillaume', 'Duriaud')

def main():

    random.seed()
    screen = pygame.display.set_mode((768, 544))
    pygame.display.set_caption("Oh Mummy")
    clock = pygame.time.Clock()

    spriteAll = pygame.sprite.RenderUpdates()
    spriteEndgame = pygame.sprite.RenderUpdates()

    Score.containers = spriteAll
    Life.containers = spriteAll
    GuardianMummy.containers = spriteAll

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

    catacombeView = CatacombeView( screen, ImageOhMummy, spriteAll )
    GameScene = CatacombeScene( catacombeView, LIFE, clock, Input, SCORE )
    GameScene.Initialize()

    upLevelView = UpLevelView( screen, ImageOhMummy )
    NextLevelScene = UpLevelScene( upLevelView, Input, clock, SCORE, LIFE )
    NextLevelScene.Initialize()

    gameOverView = GameOverView( screen, ImageOhMummy )
    myGameOverScene = GameOverScene( gameOverView, Input, clock, SCORE, LIFE )
    SCORE.setScene( GameScene )

    sLoader = SceneLoader()
    sLoader.setInputHandler( Input )

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
