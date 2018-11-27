

class Movement():
    '''
    mover movement gesture in the scene
    (position, orientation, sprite indice, obstacle)
    '''
    def __init__(self,scene,x,y,facing,moveIterate):
        # coordinates
        self.x = x
        self.y = y
        # Orientation
        self.facing = facing
        # Itération pour les images
        self.moveIterate = moveIterate
        # Indique si le mouvement est entravé
        self.obstacle = True
        self.scene = scene

    def move(self, direction):
        '''
        try to move
        '''
        movability = self.scene.testMovement( self.x, self.y, direction )
        if movability[0]:
            self.x = movability[1]
            self.y = movability[2]
            self.obstacle = False
        else:
            self.obstacle = True
        return self.obstacle

