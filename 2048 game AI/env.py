import random
class Game:
    def reset(self):
        self.grid = [[0 for _ in range(4)] for _ in range(4) ]
        self.placeSquare()
    
    def placeSquare(self):
        posX = random.randint(0,3)
        posY = random.randint(0,3)

        if self.grid[posY][posX] != 0:
            self.placeSquare()
        else:
            # 95% 2 et 5% 4
            r = random.random()
            if r < 0.05:
                self.grid[posY][posX] = 4
            else:
                self.grid[posY][posX] = 2
    
    def play_step(self, action):
        # action = 0-up 1-rigth 2-down 3-left
        match action:
            case 0:
                for y in range(3,0,-1): # 3,2,1   0 = out
                    for x in range(4): # 0,1,2,3
                        newPosY = y - 1

                        if self.grid[newPosY][x] == 0:
                            self.grid[newPosY][x] = self.grid[y][x]
                            self.grid[y][x] = 0
                            continue
                        elif self.grid[newPosY][x] == self.grid[y][x]:
                            self.grid[newPosY][x] **= 2
                            self.grid[y][x] = 0
                            continue
                        else:
                            continue
            case 1:
                for y in range(4): # 3,2,1,0
                    for x in range(3): # 0,1,2  3 = out
                        newPosX = x + 1

                        if self.grid[y][newPosX] == 0:
                            self.grid[y][newPosX] = self.grid[y][x]
                            self.grid[y][x] = 0
                            continue
                        elif self.grid[y][newPosX] == self.grid[y][x]:
                            self.grid[y][newPosX] **= 2
                            self.grid[y][x] = 0
                            continue
                        else:
                            continue
            case 2:
                for y in range(3): # 2,1,0  3 = out
                    for x in range(4): # 0,1,2,3
                        newPosY = y - 1

                        if self.grid[newPosY][x] == 0:
                            self.grid[newPosY][x] = self.grid[y][x]
                            self.grid[y][x] = 0
                            continue
                        elif self.grid[newPosY][x] == self.grid[y][x]:
                            self.grid[newPosY][x] **= 2
                            self.grid[y][x] = 0
                            continue
                        else:
                            continue
            case 3:
                for y in range(4): # 3,2,1,0
                    for x in range(3,0,-1): # 1,2,3  0 = out
                        newPosX = x - 1

                        if self.grid[y][newPosX] == 0:
                            self.grid[y][newPosX] = self.grid[y][x]
                            self.grid[y][x] = 0
                            continue
                        elif self.grid[y][newPosX] == self.grid[y][x]:
                            self.grid[y][newPosX] *= 2
                            self.grid[y][x] = 0
                            continue
                        else:
                            continue
        done = True
        for y in self.grid:
            for x in y:
                if x == 0:
                    done = False
        if not done:
            self.placeSquare()
        return done