import numpy as np
import random

'''

actions:
0) None
1) turn right
2) turn left

'''

class Game:

    def __init__(self, colmns, rows, recompense={'col_snake':-200,'apple':30,'out':-500,'none':0}) -> None:
        self.col = colmns
        self.row = rows
        self.recompense = recompense

    def reset(self):
        self.grid = np.zeros((self.col, self.row), dtype=int)
        self.score = 0

        snakex = self.col // 2
        snakey = self.row // 2
        self.grid[snakex, snakey] = 1
        self.snake = [(snakex, snakey)]
        self.dir = 0

        self.placeApple()

        #return self.get_state()
        return self.get_stateV2()
    
    def get_state(self):
        applePosX, applePosY = self.posApple
        headPosX, headPosY = self.snake[0]
        
        state = []

        if applePosX == headPosX:
            state.append(0)
        elif applePosX > headPosX:
            state.append(1)
        else:
            state.append(2)
        
        if applePosY == headPosY:
            state.append(0)
        elif applePosY > headPosY:
            state.append(1)
        else:
            state.append(2)
        
        state.append(self.dir)

        isDanger = [
            1 if headPosY == 0  else 1 if self.grid[headPosY-1, headPosX] == 1 else 0,
            1 if headPosX+1 == self.col  else 1 if self.grid[headPosX+1, headPosY] == 1 else 0,
            1 if headPosY+1 == self.row  else 1 if self.grid[headPosY+1, headPosX] == 1 else 0,
            1 if headPosX == 0  else 1 if self.grid[headPosX-1, headPosY] == 1 else 0,
        ]

        state += [isDanger[(-1 + self.dir + i)%4] for i in range(3)]

        return tuple(state)
    
    def get_stateV2(self):
        applePosX, applePosY = self.posApple
        headPosX, headPosY = self.snake[0]
        
        state = []

        if applePosX == headPosX:
            state.append(0)
        elif applePosX > headPosX:
            state.append(1)
        else:
            state.append(2)
        
        if applePosY == headPosY:
            state.append(0)
        elif applePosY > headPosY:
            state.append(1)
        else:
            state.append(2)
        
        state.append(self.dir)

        isDanger = [
            1 if headPosY == 0  else 1 if self.grid[headPosY-1, headPosX] == 1 else 0,
            1 if headPosX+1 == self.col  else 1 if self.grid[headPosY, headPosX+1] == 1 else 0,
            1 if headPosY+1 == self.row  else 1 if self.grid[headPosY+1, headPosX] == 1 else 0,
            1 if headPosX == 0  else 1 if self.grid[headPosY, headPosX-1] == 1 else 0,
        ]

        state += [isDanger[(-1 + self.dir + i)%4] for i in range(3)]

        return tuple(state)

    def play_step(self, action): # new_state, reward, done
        reward = 0
        done = False

        #new direction
        if action == 0: pass
        elif action == 1: self.dir = (self.dir + 1)%4
        elif action == 2: self.dir = (self.dir - 1)%4

        headPosX, headPosY = self.snake[0]

        #new head position
        if self.dir == 0:
            newPosX, newPosY = headPosX, headPosY-1
        elif self.dir == 1:
            newPosX, newPosY = headPosX+1, headPosY
        elif self.dir == 2:
            newPosX, newPosY = headPosX, headPosY+1
        else:
            newPosX, newPosY = headPosX-1, headPosY
        
        #collision
        if newPosX == -1 or newPosX == self.col:
            reward, done = self.recompense['out'], True
        
        if newPosY == -1 or newPosY == self.row:
            reward, done = self.recompense['out'], True
        
        #on Apple or on snake
        if not done:
            if self.grid[newPosX, newPosY] == 2:
                reward = self.recompense['apple']
                self.score += 10
                self.placeApple()
            elif self.grid[newPosX, newPosY] == 1:
                reward, done = self.recompense['col_snake'], True
            else:
                self.grid[self.snake[-1][0], self.snake[-1][1]] = 0
                self.snake.pop(-1)
            self.snake.insert(0,(newPosX,newPosY))
            self.grid[newPosX, newPosY] = 1
        
        return self.get_state(), reward if reward != 0 else self.recompense['none'], done

    def placeApple(self):
        posx = random.randint(0, self.col - 1)
        posy = random.randint(0, self.row - 1)
        if self.grid[posx, posy] == 1:
            self.placeApple()
        else:
            self.grid[posx, posy] = 2
            self.posApple = (posx, posy)