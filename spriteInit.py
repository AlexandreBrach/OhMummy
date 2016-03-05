# -*- coding: cp1252 -*-
import pygame
import pygame.image

class MummySprites():
    
    def getSprites(self):

        ImageOhMummy = {}
        ImageOhMummy['Gargou'] = {}
        ImageOhMummy['Gargou']['Left'] = pygame.image.load("./Image/GargouLeft.png")
        ImageOhMummy['Gargou']['MoveLeft'] = pygame.image.load("./Image/GargouMoveLeft.png")
        ImageOhMummy['Gargou']['Right'] = pygame.image.load("./Image/GargouRight.png")
        ImageOhMummy['Gargou']['MoveRight'] = pygame.image.load("./Image/GargouMoveRight.png")
        ImageOhMummy['Gargou']['MoveDownLeft'] = pygame.image.load("./Image/GargouMoveDownLeft.png")
        ImageOhMummy['Gargou']['MoveDownRight'] = pygame.image.load("./Image/GargouMoveDownRight.png")
        ImageOhMummy['Gargou']['MoveUpLeft'] = pygame.image.load("./Image/GargouMoveUpLeft.png")
        ImageOhMummy['Gargou']['MoveUpRight'] = pygame.image.load("./Image/GargouMoveUpRight.png")
        i = ImageOhMummy['Gargou']
        ImageOhMummy['Gargou']['Face'] = [i['Right'], i['MoveRight'], i['MoveUpLeft'], i['MoveUpRight'],
                                          i['Left'], i['MoveLeft'], i['MoveDownLeft'], i['MoveDownRight']]
        ImageOhMummy['Mummy'] = {}
        ImageOhMummy['Mummy']['Left'] = pygame.image.load("./Image/MummyLeft.png")
        ImageOhMummy['Mummy']['MoveLeft'] = pygame.image.load("./Image/MummyMoveLeft.png")
        ImageOhMummy['Mummy']['Right'] = pygame.image.load("./Image/MummyRight.png")
        ImageOhMummy['Mummy']['MoveRight'] = pygame.image.load("./Image/MummyMoveRight.png")
        ImageOhMummy['Mummy']['MoveDownLeft'] = pygame.image.load("./Image/MummyMoveDownLeft.png")
        ImageOhMummy['Mummy']['MoveDownRight'] = pygame.image.load("./Image/MummyMoveDownRight.png")
        ImageOhMummy['Mummy']['MoveUpLeft'] = pygame.image.load("./Image/MummyMoveUpLeft.png")
        ImageOhMummy['Mummy']['MoveUpRight'] = pygame.image.load("./Image/MummyMoveUpRight.png")
        i = ImageOhMummy['Mummy']
        ImageOhMummy['Mummy']['Face'] = [i['Right'], i['MoveRight'], i['MoveUpLeft'], i['MoveUpRight'],
                                          i['Left'], i['MoveLeft'], i['MoveDownLeft'], i['MoveDownRight']]
        
        ImageOhMummy['GuardianMummy'] = {}
        for i in range(1, 17):
            ImageOhMummy['GuardianMummy'][i] = pygame.image.load("./Image/GuardianMummy"+str(i)+".png")
        
        ImageOhMummy['Trace'] = {}
        ImageOhMummy['Trace']['None'] = pygame.image.load("./Image/TraceNone.png")
        ImageOhMummy['Trace']['LeftDown'] = pygame.image.load("./Image/TraceLeftDown.png")
        ImageOhMummy['Trace']['LeftUp'] = pygame.image.load("./Image/TraceLeftUp.png")
        ImageOhMummy['Trace']['RightDown'] = pygame.image.load("./Image/TraceRightDown.png")
        ImageOhMummy['Trace']['RightUp'] = pygame.image.load("./Image/TraceRightUp.png")
        ImageOhMummy['Trace']['DownLeft'] = pygame.image.load("./Image/TraceDownLeft.png")
        ImageOhMummy['Trace']['DownRight'] = pygame.image.load("./Image/TraceDownRight.png")
        ImageOhMummy['Trace']['UpLeft'] = pygame.image.load("./Image/TraceUpLeft.png")
        ImageOhMummy['Trace']['UpRight'] = pygame.image.load("./Image/TraceUpRight.png")
        
        ImageOhMummy['Box'] = {}
        ImageOhMummy['Box']['RoyalMummy'] = pygame.image.load("./Image/RoyalMummy.png")
        ImageOhMummy['Box']['Scroll'] = pygame.image.load("./Image/Scroll.png")
        ImageOhMummy['Box']['Key'] = pygame.image.load("./Image/Key.png")
        ImageOhMummy['Box']['Treasure'] = pygame.image.load("./Image/Treasure.png")
        for i in range(1, 6):
            ImageOhMummy['Box']['Empty'+str(i)] = pygame.image.load("./Image/Empty"+str(i)+".png")
            ImageOhMummy['Box']['NonTested'+str(i)] = pygame.image.load("./Image/NonTested"+str(i)+".png")
            ImageOhMummy['Box']['GuardianMummy'+str(i)] = pygame.image.load("./Image/Empty"+str(i)+".png")
        ImageOhMummy['Chiffre'] = {}
        ImageOhMummy['ChiffreScroll'] = {}
        ImageOhMummy['Lettre'] = {}
        ImageOhMummy['Score'] = pygame.image.load("./Image/Score.png")
        ImageOhMummy['Men'] = pygame.image.load("./Image/Men.png")
        
        
        ImageOhMummy['EndLife'] = pygame.image.load("./Image/EndLife.png")
        ImageOhMummy['End200'] = pygame.image.load("./Image/End200.png")
        ImageOhMummy['GameOver'] = pygame.image.load("./Image/GameOver.png")
        
        
        for i in range(10):
            ImageOhMummy['Chiffre'][i] = pygame.image.load('./Image/Chiffre'+str(i)+".png")
            ImageOhMummy['ChiffreScroll'][i] = pygame.image.load('./Image/ChiffreScroll'+str(i)+".png")
            
        return ImageOhMummy