import numpy as np
import random

class Game:
    def reset(self): # state
        self.grid = np.zeros((4,4), dtype=int)
        self.placeSquare()
    
    def placeSquare(self):
        posX = random.randint(0,3)
        posY = random.randint(0,3)
        if self.grid[posY, posX] != 0:
            self.grid[posY, posX] = 2
        else:
            self.placeSquare()