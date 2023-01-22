class Board:
    grid = [[" " for _ in range(3)] for _ in range(3)]

    def update(self, pos, playeur):
        self.grid[pos[0]][pos[1]] = playeur.value
    
    def draw(self):
        print("_"*30,"\n")
        print("_"*30,"\n")
        for i in range(3):
            print("       |       |       ")
            print(f"   {self.grid[i][0]}   |   {self.grid[i][1]}   |   {self.grid[i][2]}   ")
            print("       |       |       ")
            if i != 2: print("-"*23)
    
    def winner(self):
        #horizontalement
        for x in range(3):
            if self.grid[x][0] == self.grid[x][1] == self.grid[x][2] != " ":
                return self.grid[x][0]
        
        #verticalement
        for y in range(3):
            if self.grid[0][y] == self.grid[1][y] == self.grid[2][y] != " ":
                return self.grid[0][y]
        
        #diagonalement
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[1][1]
        
        #rien
        return None