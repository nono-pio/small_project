import random
class Pipe:

    spaceBetweenPipeUpDown = 50
    width = 50
    velocityPipe = 1

    def __init__(self, x, HEIGHT) -> None: 
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = random.randint(50, HEIGHT - 50)   # y = distance beetween the top and the top of the up pipe    50 is the minimal space between top or bottum of the pipe and screen
        self.y2 = HEIGHT - self.y - self.spaceBetweenPipeUpDown
    
    def update(self):
        self.x -= self.velocityPipe
    
    def collision(self, pos:tuple): # pos = (x, y, w, h)
        # collision pos x
        if pos[0] < self.x + self.width and pos[0] + pos[2] > self.x:
            # collision y with pipe up
            if pos[1] < self.y and pos[3] + pos[1] > 0:
                return True
            # collision y with pipe down
            elif pos[1] < self.HEIGHT and pos[3] + pos[1] > self.y2:
                return True
        return False