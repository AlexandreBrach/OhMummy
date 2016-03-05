# -*- coding: cp1252 -*-

#------------------------------------------------------------
# Classe ayant pour responsabilité le mouvement d'un "mover"
# Gère les restrictions de mouvement
#------------------------------------------------------------
class Movement():
    def __init__(self,scene,x,y,facing,moveIterate):
        # Coordonnées
        self.x = x
        self.y = y
        # Orientation
        self.facing = facing
        # Itération pour les images
        self.moveIterate = moveIterate
        # Indique si le mouvement est entravé
        self.entrave = True
        self.scene = scene

    #------------------------------------------------------------
    # Tente de déplacer le sujet dans la direction spécifiée 
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

