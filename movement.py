# -*- coding: cp1252 -*-

#------------------------------------------------------------
# Classe ayant pour responsabilit� le mouvement d'un "mover"
# G�re les restrictions de mouvement
#------------------------------------------------------------
class Movement():
    def __init__(self,scene,x,y,facing,moveIterate):
        # Coordonn�es
        self.x = x
        self.y = y
        # Orientation
        self.facing = facing
        # It�ration pour les images
        self.moveIterate = moveIterate
        # Indique si le mouvement est entrav�
        self.entrave = True
        self.scene = scene

    #------------------------------------------------------------
    # Tente de d�placer le sujet dans la direction sp�cifi�e 
    # Renvoie True si Ok, False sinon
    #------------------------------------------------------------    
    def move(self, direction):
        movability = self.scene.testMovement( self.x, self.y, direction )
        if movability[0]:
            self.x = movability[1]
            self.y = movability[2]            
            self.entrave = False
        else:
            self.entrave = True
        return self.entrave

